import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)
url = os.getenv("CONNECTION_STRING")
connection = psycopg2.connect(url)


@app.get('/')
def hello_world():
    return 'Hello, World!'


