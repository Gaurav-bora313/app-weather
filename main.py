from flask import Flask, request, render_template
from weather import Parameters

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('home.html')

@app.route('/city', methods=["GET", "POST"])
def city():
    data = None
    error = None

    if request.method == "POST":
        city = request.form["city"].strip()
        try:
            weather = Parameters(city)
            data = {
                "temp" : weather.Temp(),
                "feel_like" : weather.TempFeel(),
                "max_temp" : weather.maxTemp(),
                "min_temp" : weather.minTemp(),
                "humidity" : weather.humidity(),
                "status" : weather.weatherStatus(),
            }
        except Exception as e:
            error = str(e)

    return render_template("city.html", data=data, error=error)

if __name__ == "__main__":
    app.run(debug=True)