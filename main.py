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
    file = open("downloads/image.jpg", "wb")
    file.write(response.content)
    file.close()

    net = jetson.inference.imageNet("googlenet")
    input = jetson.utils.videoSource("downloads/image.jpg", argv=sys.argv)
    font = jetson.utils.cudaFont()
    img = input.Capture()

    # classify image 
    class_id, confidence = net.Classify(img)

    # find the object description
    class_desc = net.GetClassDesc(class_id)

                # HTTP response 
    return {"label": class_desc, "confidence": (confidence)}


export FLASK_APP=imagenet_link  #[without .py]
flask run --host=0.0.0.0