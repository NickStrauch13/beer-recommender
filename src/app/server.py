from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('recommendation.html')

@app.route('/recommend_beers', methods=['POST'])
def recommend_beers():
    data = request.json
    username = data['username']
    # Dummy logic to fetch recommendations
    # TODO: Replace with actual recommendation logic
    recommended_beers = ["Beer 1", "Beer 2", "Beer 3"]  
    return jsonify(recommended_beers)

if __name__ == '__main__':
    app.run(debug=True)
