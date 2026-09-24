#task 2 
import requests
import pandas as pd

temp = pd.DataFrame()
for i in range(1,130):
    url = "https://api.themoviedb.org/3/tv/top_rated?api_id=90e7897dbc8aa8d21ec6ee3d14a6389e&language=en-US&page=129"

    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5MGU3ODk3ZGJjOGFhOGQyMWVjNmVlM2QxNGE2Mzg5ZSIsIm5iZiI6MTc5MDE4MDEyMi42OTkwMDAxLCJzdWIiOiI2YWIzZmIxYWRiZDMxODA4NjRkNTA0YWQiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.RPBMmFmejtj8hmlEFltVH39xKbDUP0B8P6So43cBPME"
    }
    response = requests.get(url, headers=headers)
    df = pd.DataFrame(response.json()['results'])
    df = df[['id','genre_ids','name','vote_count','origin_country','original_language','first_air_date','adult','softcore','popularity']]
    temp = pd.concat([temp,df],ignore_index=False)
    
temp.to_csv('uff.csv')
print(df.shape)


