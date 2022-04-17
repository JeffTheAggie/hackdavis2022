from flask import Flask, Response, request, render_template, session
from flask_restful import Api, Resource, fields, marshal_with, reqparse 
from flask_sqlalchemy import SQLAlchemy
import json 

app = Flask(__name__)
api = Api(app)
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

class Webhook(Resource): 
    def get(): 
        return "Hooks are recived here"

    def post():

        payload = request.json
        event_id = payload["event_id"]
        form_response = payload["form_response"]
        form_id = form_response["form_id"]
        answers = form_response["answers"]

        return {"Message": "Success"}

api.add_resource(Webhook, "/hook")

@app.route("/")
def index(): 
    return "Hello world"

if __name__ == "__main__": 
    app.run()