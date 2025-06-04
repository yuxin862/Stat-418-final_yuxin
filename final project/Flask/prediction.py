import pandas as pd
from prophet import Prophet

EXTERNAL_REGRESSORS = ["Patch_Count", "Google_Trends_Index"]
_model_cache = {}
_df_cache = {}

def load_and_train(csv_file):
    df = pd.read_csv(csv_file)

    # Rename and preprocess
    df.rename(columns={"Month": "ds", "Avg. Players": "y"}, inplace=True)
    df["ds"] = pd.to_datetime(df["ds"])
    df = df.sort_values("ds")
    df = df[df["ds"] >= "2021-01-01"]
    df = df.dropna()

    # Avoid regressors with zero variance
    for reg in EXTERNAL_REGRESSORS:
        if df[reg].std() == 0:
            df[reg] += 0.001

    model = Prophet(
        changepoint_prior_scale=0.1,
        changepoint_range=0.9,
        n_changepoints=20
    )
    for reg in EXTERNAL_REGRESSORS:
        model.add_regressor(reg)

    try:
        model.fit(df)  # Use default optimization
    except Exception as e:
        print("Model fitting failed:", str(e))
        raise e

    return model, df

def get_model_and_data(game):
    if game in _model_cache:
        return _model_cache[game], _df_cache[game]

    filename = f"{game}_with_patch_trend.csv"
    model, df = load_and_train(filename)
    _model_cache[game] = model
    _df_cache[game] = df
    return model, df

def predict(game, months, patch_count=None, google_trend=None):
    if game not in ["cs2", "dota2", "pubg"]:
        raise ValueError("Invalid game name")

    model, df = get_model_and_data(game)
    last_date = df["ds"].max()

    future_dates = pd.date_range(start=last_date + pd.DateOffset(months=1), periods=months, freq='MS')
    future_df = pd.DataFrame({"ds": future_dates})

    # Fill in the regressors
    future_df["Patch_Count"] = patch_count if patch_count is not None else df["Patch_Count"].mean()
    future_df["Google_Trends_Index"] = google_trend if google_trend is not None else df["Google_Trends_Index"].mean()

    try:
        forecast = model.predict(future_df)
        return forecast[["ds", "yhat"]].to_dict(orient="records")
    except Exception as e:
        print("Prediction failed:", str(e))
        return [{"ds": None, "yhat": f"Prediction failed: {e}"}]








