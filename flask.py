from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    # Get a random cat image from the internet
    url = "https://api.thecatapi.com/v1/images/random"
    response = requests.get(url)
    if response.status_code == 200:
        image = response.json()["url"]
    else:
        image = None

    # Render the template with the cat image
    return render_template("index.html", image=image)

if __name__ == "__main__":
    app.run(debug=True)
