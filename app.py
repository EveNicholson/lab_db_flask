from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://davidbujok@localhost:5432/orders_app"
db = SQLAlchemy(app)
migrate = Migrate(app,db)

from controllers.order_controllers import orders_blueprint
app.register_blueprint(orders_blueprint)