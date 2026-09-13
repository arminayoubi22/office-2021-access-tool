# build ac9ac42a03
# (auto) f683e6
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'ok'
