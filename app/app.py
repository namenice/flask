#coding: utf-8
import docker
import logging
import json

from flask import Flask, render_template, jsonify, request, stream_with_context, Response

app = Flask(__name__)


@app.route("/test")
def hello():
    app.logger.info(dir(client.api))

    return "ok na ja"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
