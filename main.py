from flask import Flask, jsonify, request
import pandas as pd

movies_data = pd.read_csv("final.csv")
app=Flask(__name__)
all_movies=movies_data[["original_title","poster_link","release_date","runtime","weighted_rating"]]

liked_movie=[]
not_liked_movies=[]
did_not_watch=[]


def assign_val():
    m_data={
        "original_title":all_movies.iloc[0,0],
        "poster_link":all_movies.iloc[0,1],
        "release_date":all_movies.iloc[0,2] or "N/A"
        "duration":all_movies.iloc[0,3],
        "rating":all_movies.iloc[0,4]/2
    }
    return m_data

@app.route("/movies")

def get_movie():
    movies_data=assign_val()
    return jsonify({
        "data":movies_data,
        "status":"sucess"
    })

@app.route("/like")

def liked_movie():
    global all_movies
    movies_data=assign_val()
    liked_movies.append(movies_data)
    all_movies.drop([0],inplace = True)
    all_movies=all_movies.reset_index(drop=True)
    return jsonify({
        "status":"sucess"
    })



@app.route("/dislike")

def unliked_movie():
    global all_movies
    movies_data=assign_val()
    not_liked_movieliked_movies.append(movies_data)
    all_movies.drop([0],inplace = True)
    all_movies=all_movies.reset_index(drop=True)
    return jsonify({
        "status":"sucess"
    })


@app.route("/did_not_watch")

def did_not_watch_view():
    global all_movies
    movies_data=assign_val()
    did_not_watch.append(movies_data)
    all_movies.drop([0],inplace = True)
    all_movies=all_movies.reset_index(drop=True)
    return jsonify({
        "status":"sucess"
    })

if __name__ == "__main__":
    app.run()