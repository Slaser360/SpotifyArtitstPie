# Spotify Artist Analysis

This project is a web application that allows users to analyze their top artists on Spotify using the Spotify API, OpenAI API, and data visualization. The application generates a pie chart displaying the user's top 10 artists in the last month, along with a creative description generated by OpenAI's language model. Additionally, the application creates an image representing the creative description using OpenAI's image generation capabilities.

![alt text][(http://url/to/img.png](https://github.com/Slaser360/SpotifyArtitstPie/blob/main/ExamplePie.PNG?raw=true))
## Features

- **Spotify Authentication**: Users can authenticate with their Spotify accounts to access their listening data.
- **Top Artists Analysis**: The application retrieves the user's top 10 artists in the last month using the Spotify API.
- **Pie Chart Visualization**: A pie chart is generated to visually represent the user's top artists and their popularity.
- **Creative Description Generation**: OpenAI's language model is used to generate a creative description based on the genres of the user's top artists.
- **Image Generation**: An image representing the creative description is generated using OpenAI's image generation capabilities.

## Technologies Used

- **Python**: The backend of the application is built using Python.
- **Flask**: The web framework used for building the application.
- **Spotipy**: A Python library for interacting with the Spotify Web API.
- **OpenAI API**: Used for generating creative descriptions and images based on the user's top artist data.
- **Matplotlib**: A Python plotting library used for generating the pie chart visualization.
- **HTML/CSS**: Used for structuring and styling the web pages.

## Installation

1. Clone the repository: git clone https://github.com/Slaser360/SpotifyArtitstPie.git
2. Install the required dependencies: pip install -r requirements.txt


Copy code

3. Set up your Spotify and OpenAI API credentials in the `app.py` file.

4. Run the Flask application:
python app.py


Copy code

5. Open your web browser and navigate to `http://localhost:3000` to access the application.

## Usage

1. Click the "Login with Spotify" button to authenticate with your Spotify account.
2. After successful authentication, the application will retrieve your top 10 artists in the last month.
3. A pie chart displaying your top artists and their popularity will be generated.
4. A creative description based on the genres of your top artists will be generated using OpenAI's language model.
5. An image representing the creative description will be generated using OpenAI's image generation capabilities.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
- [OpenAI API](https://openai.com/api/)
- [Spotipy](https://spotipy.readthedocs.io/)
- [Matplotlib](https://matplotlib.org/)
