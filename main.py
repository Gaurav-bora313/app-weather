from flask import Flask, request, render_template
from weather import Parameters

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    temp = None
    error = None
    min_temp = None
    max_temp = None
    feel_temp = None
    humidity = None
    status = None
    if request.method == "POST":
        city = request.form["city"]
        try:
            weather = Parameters(city)
            temp = weather.Temp()
            min_temp = weather.minTemp()
            max_temp = weather.maxTemp()
            feel_temp = weather.TempFeel()
            humidity = weather.humidity()
            status = weather.weatherStatus().capitalize()
        except Exception as e:
            error = str(e)

    return render_template("index.html", temp=temp, error=error, min_temp=min_temp, 
                           max_temp=max_temp, feel_temp=feel_temp, humidity=humidity,
                           status=status)

if __name__ == "__main__":
    app.run(debug=True)