from flask import Flask, jsonify, request, render_template
import pymongo
import re

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/v1/past")
def past():
    conn = "mongodb://localhost:27017"
    
    org = request.args.get("org")
    rocket = request.args.get("rocket")
    success = request.args.get("success")
    my_list = []
    query = {}
    
    if org != None:
        query["Organization"] = re.compile(org, re.IGNORECASE)
    if rocket != None:
        query["Rocket"] = re.compile(rocket, re.IGNORECASE)
    if success != None:
        query["Success"] = True if success.lower() == "true" else False
    
    with pymongo.MongoClient(conn) as client:
        db = client.spaceship
        for row in db.past.find(query):
            my_list.append({"Organization":row["Organization"], "Rocket":row["Rocket"], "Mission":row["Mission"], "Time":row["Time"], "Location":row["Location"], "Success":row["Success"]})
    
    return jsonify(my_list)

@app.route("/api/v1/upcoming")
def upcoming():
    conn = "mongodb://localhost:27017"
    
    org = request.args.get("org")
    rocket = request.args.get("rocket")
    my_list = []
    query = {}
    
    if org != None:
        query["Organization"] = re.compile(org, re.IGNORECASE)
    if rocket != None:
        query["Rocket"] = re.compile(rocket, re.IGNORECASE)
    
    with pymongo.MongoClient(conn) as client:
        db = client.spaceship
        for row in db.upcoming.find(query):
            my_list.append({"Organization":row["Organization"], "Rocket":row["Rocket"], "Mission":row["Mission"], "Time":row["Time"], "Location":row["Location"]})
    
    return jsonify(my_list)

@app.route("/api/v1/rocket")
def rocket():
    conn = "mongodb://localhost:27017"
    
    mfr = request.args.get("mfr")
    rocket = request.args.get("rocket")
    status = request.args.get("status")
    my_list = []
    query = {}
    
    if mfr != None:
        query["Manufacturer"] = re.compile(mfr, re.IGNORECASE)
    if rocket != None:
        query["Name"] = re.compile(rocket, re.IGNORECASE)
    if status != None:
        query["Status"] = re.compile(status, re.IGNORECASE)
    
    with pymongo.MongoClient(conn) as client:
        db = client.spaceship
        for row in db.rocket.find(query):
            my_list.append({"Name":row["Name"], "Manufacturer":row["Manufacturer"], "Status":row["Status"]})
    
    return jsonify(my_list)


if __name__ == "__main__":
    app.run(debug=True)
