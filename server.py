from flask import Flask, render_template, request
from Weather import get_weather
from waitress import serve

app =Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')

@app.route('/Weather')
def get_weather_():
    try: 
        city = request.args.get('city')
        weather_data = get_weather(city)
        if weather_data['cod'] == '404' or city == '':
            return render_template('city-not-found.html')
        else: 
            return render_template(
                'weather.html',
                    city = city,
                    m_weather = weather_data["weather"][0]["main"],
                    weather_desc = weather_data["weather"][0]["description"],
                    temp = round(weather_data["main"]["temp"]),
                    feels_like = round(weather_data["main"]["feels_like"])
                )
    except:
        return render_template('not_found.html')


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)