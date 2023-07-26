from flask import Flask, jsonify, render_template
from test import some_method

app = Flask(__name__)

MYJSON = [
    {
        "id": "12",
        "name": "Thanga anantha Kumar",
        "age": "23",
    },
    {
        "id": "13",
        "name": "Aasha loosu",
        "age": "20",
    },
    {
        "id": "13",
        "name": "AK__A",
        "age": "20",
    }
]

@app.route("/")
def hello_world():
    some_method()
    return render_template("home.html", jobs=MYJSON)

@app.route("/api/getdetails")
def get_Details():
  
    return jsonify(MYJSON)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
