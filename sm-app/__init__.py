from flask import Flask 

app = Flask(__name__)

from v1.views import api_v1_blueprint