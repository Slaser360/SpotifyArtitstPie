from flask import Flask, redirect, request, session, url_for, send_from_directory, jsonify
from spotipy.oauth2 import SpotifyOAuth
import spotipy
import matplotlib.pyplot as plt
import openai
import os
from flask import render_template
from PIL import Image
from io import BytesIO
import requests

app = Flask(__name__)
app.secret_key = 'nuts'

SPOTIFY_CLIENT_ID = 'INSERT YOURS'
SPOTIFY_CLIENT_SECRET = 'INSERT YOURS'
SPOTIFY_REDIRECT_URI = 'INSERT YOURS'

scope = 'user-top-read'

sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope=scope
)

# Setup your OpenAI API Key here
openai.api_key = 'INSERT YOURS'

@app.route('/')
def login():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session['token_info'] = token_info
    return redirect(url_for('get_top_artists'))

@app.route('/get_top_artists')
def get_top_artists():
    token_info = session.get('token_info', None)
    if not token_info:
        return redirect(url_for('login'))
    
    sp = spotipy.Spotify(auth=token_info['access_token'])
    top_artists = sp.current_user_top_artists(time_range='short_term', limit=10)
    
    # For pie chart
    artist_names = [artist['name'] for artist in top_artists['items']]
    artist_popularity = [artist['popularity'] for artist in top_artists['items']]
    
    # For OpenAI description
    artist_genres = []
    for artist in top_artists['items']:
        artist_genres.extend(artist['genres'])
    unique_genres = list(set(artist_genres))
    genre_description = ', '.join(unique_genres)
    
    prompt = f"Create a 2 sentence or 30 word creative pie description that includes elements of the following music genres: {genre_description}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=100
    )
    
    # Assuming correct access to the text
    # Make sure to access the response appropriately according to the API documentation
    creative_description = response["choices"][0]["message"]["content"]

    # Generating and Saving a Pie Chart
    plt.figure(figsize=(10, 7))
    plt.pie(artist_popularity, labels=artist_names, autopct='%1.1f%%', startangle=140)
    plt.title('Top 10 Artists in the Last Month')
    plt.axis('equal')

    # Ensure 'static' folder exists. If not, create it.
    static_folder_path = os.path.join(app.root_path, 'static')
    if not os.path.exists(static_folder_path):
        os.makedirs(static_folder_path)

    # Save the chart in the 'static' folder using an absolute path
    chart_path = os.path.join(static_folder_path, 'top_artists_pie_chart.png')
    plt.savefig(chart_path)

    def generate_image(description):
        #Generate an image based on the given description using the OpenAI API.
        response = openai.Image.create(
            model="dall-e-3",
            prompt = f"Create an artistic, creative image of a pie that visually represents the following description: {creative_description}. The image should be a pie chart or a realistic pie illustration, not just text or random imagery.",
            size="1024x1024",
            quality="standard",
            n=1,
        )

        # Get the image URL from the response
        image_url = response['data'][0]['url']

        # Download the image data
        image_data = BytesIO(requests.get(image_url).content)

        # Open the image data using PIL
        image = Image.open(image_data)

        return image

    generated_image = generate_image(creative_description)

    image_path = os.path.join(static_folder_path, 'generated_image.png')
    generated_image.save(image_path)
    
    return render_template(
        'artist_analysis.html',
        pie_chart_path=url_for('static', filename='top_artists_pie_chart.png'),
        generated_image_path=url_for('static', filename='generated_image.png'),
        creative_description=creative_description
    )


if __name__ == '__main__':
    app.run(debug=True, port=3000)