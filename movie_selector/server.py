from flask import Flask, render_template, request
from movie import get_current_movie

from waitress import serve


app = Flask(__name__)


@app.route("/")


@app.route("/movie")

def get_movie():
    movie = request.args.get("movie")
    movie_data = get_current_movie(movie)
       
    return render_template(
        "movie.html",
        title = movie_data["results"][1]["title"],
        overview = movie_data["results"][1]["overview"]
    
        )
    
if __name__ == "__main__":
    serve(app, host="0.0.0.0", port = 5560)


    
    
    






