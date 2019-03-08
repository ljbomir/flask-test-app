from flask import Flask
import requests
from time import sleep
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"



@app.route("/bomba")
def get_data():
    count = 1
    url = 'https://lyubo.info'
    while (count < 5):
            resp = requests.get(url).content
            print(resp)
            count +=1
            sleep(1)
    a = f"'{url}' was called {count} times"   
    return a

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=555, debug=True)
