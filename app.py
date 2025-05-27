from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Get a random cat fact
    fact_res = requests.get('https://catfact.ninja/fact')
    cat_fact = fact_res.json().get('fact')

    # Get a random cat image
    img_res = requests.get('https://api.thecatapi.com/v1/images/search')
    cat_img = img_res.json()[0]['url']

    return render_template('index.html', cat_fact=cat_fact, cat_img=cat_img)

if __name__ == '__main__':
    app.run(debug=True)
