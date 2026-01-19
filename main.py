from flask import Flask, request, render_template
from weather import Parameters

app = Flask(__name__)

@app.route('/city', methods=["GET", "POST"])
def home():
    temp = None
    error = None
    if request.method == "POST":
        city = request.form["city"]
        try:
            weather = Parameters(city)
            temp = weather.getTemp()
        except Exception as e:
            error = str(e)

    return render_template("index.html", temp=temp, error=error)

if __name__ == "__main__":
    app.run(debug=True)