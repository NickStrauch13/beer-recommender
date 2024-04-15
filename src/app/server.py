from flask import Flask, request, jsonify, render_template
from utils import get_recommendations_for_user, get_users

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('recommendation.html')

@app.route('/get_users', methods=['GET'])
def get_users_api():
    users = get_users()
    return jsonify(users)

@app.route('/recommend_beers', methods=['POST'])
def recommend_beers():
    data = request.json
    username = data['username']
    model = data['model']
    n = int(data['n'])
    recommended_beers = get_recommendations_for_user(username, model, n) 
    return jsonify(recommended_beers)

if __name__ == '__main__':
    app.run(debug=True)
