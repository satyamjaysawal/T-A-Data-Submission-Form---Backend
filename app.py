from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb+srv://todo:todo@todo.ji1xifd.mongodb.net/tandaDB")
mongo = PyMongo(app)
db = mongo.db

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    db.submissions.insert_one(data)
    return jsonify({"message": "Data submitted successfully"}), 201

@app.route('/submissions', methods=['GET'])
def get_submissions():
    submissions = list(db.submissions.find({}, {'_id': 0}))  
    return jsonify(submissions), 200

# Add a route to check if the server is running
@app.route('/')
def index():
    return "Server is running!"

# Only needed for local testing; Vercel doesn't use __main__
if __name__ == '__main__':
    app.run(debug=True)
