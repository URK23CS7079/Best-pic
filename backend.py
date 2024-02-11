from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual API key
TMDB_API_KEY = 'YOUR_API_KEY'
TMDB_API_URL = 'https://api.themoviedb.org/3/search/movie'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.form.get('movie_input')
    
    # Fetch movie data from TMDB API
    params = {'api_key': TMDB_API_KEY, 'query': user_input}
    response = requests.get(TMDB_API_URL, params=params)
    movie_data = response.json()['results']

    # Process and filter the movie data (you may implement recommendation logic here)

    # Return recommended movies to the front end
    return render_template('recommendations.html', recommendations=movie_data)

if __name__ == '__main__':
    app.run(debug=True)
