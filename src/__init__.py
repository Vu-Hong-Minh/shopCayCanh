from flask import Flask
import os
from dotenv import load_dotenv
from src.controllers.handle_category import categories
from src.controllers.handle_customer import customers
from src.controllers.handle_receiver import receivers
from src.controllers.handle_employee import employees
from src.controllers.handle_receipt import receipt
from src.controllers.handle_order import orders
from src.controllers.handle_product import products
from src.controllers.handle_customer import customers

load_dotenv()
SECRET_KEY = os.environ.get("KEY")

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    #đăng ký Blueprint với app
    app.register_blueprint(products)
    app.register_blueprint(categories)
    app.register_blueprint(customers)
    app.register_blueprint(receivers)
    app.register_blueprint(employees)
    app.register_blueprint(receipt)
    app.register_blueprint(orders)
    app.register_blueprint(products)
    app.register_blueprint(customers)
    return app