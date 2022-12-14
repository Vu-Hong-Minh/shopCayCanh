from flask import Flask
import os
from dotenv import load_dotenv
from src.controllers.handle_Product import product
from src.controllers.handle_Category import categories
from src.controllers.handle_Customer import customers
from src.controllers.handle_Receiver import receivers
from src.controllers.handle_Employee import employees
from src.controllers.handle_Receipt import receipt
from src.controllers.handle_Order import orders




load_dotenv()
SECRET_KEY = os.environ.get("KEY")

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    #đăng ký Blueprint với app
    app.register_blueprint(product)
    app.register_blueprint(categories)
    app.register_blueprint(customers)
    app.register_blueprint(receivers)
    app.register_blueprint(employees)
    app.register_blueprint(receipt)
    app.register_blueprint(orders)
    return app