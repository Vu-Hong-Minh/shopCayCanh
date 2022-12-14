from flask import Flask
import os
from dotenv import load_dotenv
from src.controllers.handle_product import product

load_dotenv()
SECRET_KEY = os.environ.get("KEY")

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    #đăng ký Blueprint với app
    app.register_blueprint(product)
    return app