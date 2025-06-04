import streamlit as st
import pandas as pd
import httpx
import plotly.express as px
import os


API_URL = "http://localhost:8080/predict"

st.set_page_config(page_title="Game Forecast", layout="wide")

st.title("Game Player Forecasting Dashboard")

with st.sidebar:
    st.header("Prediction Input")
    game = st.selectbox("Select Game", ["cs2", "dota2", "pubg"])
    months = st.slider("Months to Forecast", 1, 12, 3)
    patch_count = st.number_input("Patch Count", min_value=0, value=3)
    google_trend = st.number_input("Google Trends Index", min_value=0, value=85)
    submit = st.button("Run Forecast")

if submit:
    payload = {
        "game": game,
        "months": months,
        "Patch_Count": patch_count,
        "Google_Trends_Index": google_trend
    }

    with st.spinner("Fetching prediction from model..."):
        try:
            response = httpx.post(API_URL, json=payload)
            response.raise_for_status()
            results = response.json()
            df = pd.DataFrame(results)
            df["ds"] = pd.to_datetime(df["ds"])
            st.success("Forecast loaded successfully!")

            fig = px.line(df, x="ds", y="yhat", title=f"{game.upper()} Player Forecast")
            st.plotly_chart(fig, use_container_width=True)
            st.dataframe(df)

        except Exception as e:
            st.error(f" Failed to fetch prediction: {str(e)}")
