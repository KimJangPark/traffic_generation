import jetson.inference
import jetson.utils

import argparse
import sys
import requests

from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def main():
    input_URI = request.args.get('input_URI')
    print(input_URI)

    # create video sources & outputs
    response = requests.get(input_URI)
    file = open("downloads/video_tmp", "wb")
    file.write(response.content)
    file.close()


    # HTTP response 
    return Config.current_node


export FLASK_APP=imagenet_link  #[without .py]
flask run --host=0.0.0.0