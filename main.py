from flask import Flask, jsonify, render_template

app = Flask(__name__)

MYJSON = [
    {
        "id": "12",
        "name": "Thanga anantha Kumar",
        "age": "23",
    },
    {
        "id": "13",
        "name": "Akila",
        "age": "23",
    }
]

@app.route("/")
def hello_world():
    return render_template("home.html", jobs=MYJSON)

@app.route("/api/getdetails")
def get_Details():
    return jsonify(MYJSON)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
