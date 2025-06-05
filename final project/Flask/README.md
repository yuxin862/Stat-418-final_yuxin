## Flask API
This is a an actual prophet model deployed locally through a Flask API. The environment again is created through a docker-compose command, that again references the corresponding Dockerfile and requirements.txt file.

Since I using dockercompose file for both flask and Streamlit, I run the the code in the directory 'final project', not flask and streamlit:

docker compose up -d

If it has created the localhost server correctly you will not get your prompt back. You will need to open a new terminal (be in the same directory) and run the following curl command to get a response

curl http://localhost:8080/

Finally, let's test out some predictions. If you open the prediction.py script you can see that the inputs into the model are "game", "months", "Patch_Count", "Google_Trend_Index". We will pass these through a json formatted input through a curl POST request to the API. This is done as

curl -X POST http://localhost:8080/predict -H "Content-Type: application/json" -d '{
  "game": "dota2",
  "months": 6,
  "Patch_Count": 3,
  "Google_Trends_Index": 90
}'

You can change some of the values to see the prediction change. Both of the curl commands can be found in the file curl_test.sh. As usual, check to see if you have any docker containers running using docker container ls and stop them through docker componse down -v

The predicted result to test it locally should be: [{"ds":"Sun, 01 Jun 2025 00:00:00 GMT","yhat":764938.1111784144},{"ds":"Tue, 01 Jul 2025 00:00:00 GMT","yhat":763882.9457529178},{"ds":"Fri, 01 Aug 2025 00:00:00 GMT","yhat":754973.0122922461},{"ds":"Mon, 01 Sep 2025 00:00:00 GMT","yhat":737951.2902569534},{"ds":"Wed, 01 Oct 2025 00:00:00 GMT","yhat":726046.6879563394},{"ds":"Sat, 01 Nov 2025 00:00:00 GMT","yhat":782779.5736652678}]

### google cloud deployment:
I created the docker image and tag it, and then pushed it on the repositary kanelo123/flask-api-player from dockerhub. Finally, I deploy the flask api prediction on the google cloud:

https://flask-api-player-860094761515.us-central1.run.app

But the test result shows: {"error":"Error during optimization! Command '/usr/local/lib/python3.10/site-packages/prophet/stan_model/prophet_model.bin random seed=87886 data file=/tmp/tmpv8igqb63/ml66mjw_.json init=/tmp/tmpv8igqb63/ba_rp8xj.json output file=/tmp/tmpv8igqb63/prophet_model3s741thf/prophet_model-20250605002727.csv method=optimize algorithm=newton iter=10000' failed: "}

I tried to get bigger memory, but it does not work. I think it is the prophet optimizer that is fragile on the cloud environment. Even I change the optimizer, I still have the same error.
