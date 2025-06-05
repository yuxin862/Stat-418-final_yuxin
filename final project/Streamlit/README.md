### Streamlit app

First as usual you will need to sync your repo to pull the new files. To run this API, change your directory to the docker folder and run, Since I using dockercompose file for both flask and Streamlit, I run the the code in the directory 'final project', not flask and streamlit:

docker compose up -d

Then you can just go to the directory where streamlit_app.py exist and run the streamlit_app.py in your terminal:

streamlit run streamlit_app.py

Then it will open the streamlit app website automatically. You can select games(cs2,dota2 and pubg2), month(from 1 to 12)- starting from 2025/6/1, patch count and google index trend to forecast. In the right side, it will plot the predicted average player counts starting from 2025/6/1 and show the exact number below.

After that I created a image, tag it and docker push to the repositary kanelo123/streamlit-plot from dockerhub. Finally, I deploy it on the google cloud run and get the url: https://streamlit-plot-860094761515.us-west1.run.app

#### Test
Since there is something wrong with my flask api prediction deployment on the google cloud run, I can not get the forecast result from the streamlit using cloudrun.
