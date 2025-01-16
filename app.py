from flask import Flask, render_template
import json

app = Flask(__name__, template_folder="frontend/templates")

@app.route("/")
def home():
    with open("all_champions_stats.json", encoding="utf-8") as f:
        champions = json.load(f)
    return render_template("index.html", champions=champions)

if __name__ == "__main__":
    app.run(debug=True)
