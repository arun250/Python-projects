from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()
def get_current_movie(movie = "Iron man"):
    requests_url = f"https://api.themoviedb.org/3/search/movie?query={movie}"
    headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MTA2YWUxNjlmYzQ4M2Y4ZDljMWE0ODIxN2QwYmYzOSIsIm5iZiI6MTczMjE5OTA1NC42MTk5MTY0LCJzdWIiOiI2NzNmNDEyMDRkZWMxZjk4YjI5YmVlMGMiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.yHqbFvp4MlW0sJNyw7969ZZ2imVTQlRxLNehkBNT-b8','Accept': 'application/json'}
    movie_data = requests.get(requests_url, headers= headers).json()
    return movie_data



if __name__ == "__main__":
    
    movie = input("Please enter a movie name")
    movie_data = get_current_movie(movie)
    
    pprint(movie_data)

    
