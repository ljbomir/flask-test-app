from flask import Flask
import os
import requests
import time
#r = requests.get("https://i506493hi.cfapps.sap.hana.ondemand.com/")


app = Flask(__name__)
# Port number is required to fetch from env variable
# http://docs.cloudfoundry.org/devguide/deploy-apps/environment-variable.html#PORT


cf_port = os.getenv("PORT")

# Only get method by default
@app.route('/')
def hello():
        return 'Hello World'
@app.route("/bomba")
def get_data():
    count = 1
    url = 'https://lyubo.info'
    while (count < 20):
        resp = requests.get(url).content
        print(resp)
        count +=1
        time.sleep(0.5)

    a = "'%s' was called %d times" %(url,count)   
    return a

if __name__ == '__main__':
	if cf_port is None:
		app.run(host='0.0.0.0', port=5000, debug=True)
	else:
		app.run(host='0.0.0.0', port=int(cf_port), debug=True)

