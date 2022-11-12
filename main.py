from flask import Flask, render_template

app = Flask(__name__, template_folder="./resources/html", static_url_path="/resources/static")

@app.route("/")
def hello_world():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)