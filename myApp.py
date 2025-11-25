from flask import Flask

app= Flask(__name__)

@app.route("/")
def index():
    return {
        "status": "SUCCESS",
        "data":{
            "regno": 18472074,
            "name": "SOUMILI",
            "email":"soumili@msds.christuniversity.in"
        }
    }

if __name__ == "__main__":
    app.run(debug=True)