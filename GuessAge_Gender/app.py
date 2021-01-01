from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/<name>')
def home(name):
    # guess the gender based on name from the api
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    # guess the age based on name from the api
    age_api_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_api_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("index.html", person_name=name, gender=gender, age=age)


if __name__ == '__main__':
    app.run()
