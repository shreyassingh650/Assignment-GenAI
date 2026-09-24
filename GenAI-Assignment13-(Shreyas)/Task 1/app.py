import requests
import pandas as pd
url = "https://api.themoviedb.org/3/genre/movie/list?api_id=90e7897dbc8aa8d21ec6ee3d14a6389e?language=en"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5MGU3ODk3ZGJjOGFhOGQyMWVjNmVlM2QxNGE2Mzg5ZSIsIm5iZiI6MTc5MDE4MDEyMi42OTkwMDAxLCJzdWIiOiI2YWIzZmIxYWRiZDMxODA4NjRkNTA0YWQiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.RPBMmFmejtj8hmlEFltVH39xKbDUP0B8P6So43cBPME"
}

response = requests.get(url, headers=headers)

df = pd.DataFrame(data=response.json()['genres'])
print(df)