from requests import get


def weather_parser(city, token):
    request = get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric')
    response = request.json()

    if response == {'cod': '404', 'message': 'city not found'}:
        return 'Error'

    return response


def json_parser(weather_data):
    place = weather_data['main']

    return f"""Weather in {weather_data['name'].capitalize()} today:\ntemperature is {round(place['temp'], 1)}° """\
           f"""but feels like {round(place['feels_like'], 1)}°\nhumidity is {place['humidity']}%\nspeed of wind is """\
           f"""{round(weather_data['wind']['speed'], 1)}m/s\n\nconclusion: {weather_data['weather'][0]['description'].lower()}"""
