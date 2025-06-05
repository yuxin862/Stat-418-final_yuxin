curl -X POST http://localhost:8080/predict \
-H "Content-Type: application/json" \
-d '{
  "game": "dota2",
  "months": 6,
  "Patch_Count": 3,
  "Google_Trends_Index": 90
}'
