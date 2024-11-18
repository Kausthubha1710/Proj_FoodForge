from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_key = '6afea73bde7d4e2e8f838b0ed17e966d'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    ingredients = request.form['ingredients']
    diet = request.form['diet']

    url = f'https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&diet={diet}&number=5&apiKey={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        recipes = response.json()
        return render_template('results.html', recipes=recipes)
    else:
        return f"Failed to fetch data: {response.status_code}"

if __name__ == '__main__':
    app.run(debug=True)
