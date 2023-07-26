from flask import Blueprint, render_template, redirect, request
from app import db
from models.order import Order
from models.user import User


orders_blueprint = Blueprint('orders', __name__)


@orders_blueprint.route('/orders')
def orders():
    orders = Order.query.all()
    users = User.query.all()
    return render_template('index.jinja', orders=orders, users=users)

@orders_blueprint.route('/orders/add', methods=["POST"])
def add_order():
    user_id = request.form['user_id']
    payment_method = request.form['payment_method']
    order_date = request.form['date']
    order = Order(user_id = user_id, payment_method = payment_method, date = order_date)
    db.session.add(order)
    db.session.commit()
    return redirect('/orders')

@orders_blueprint.route('/orders/<id>')
def show_order(id):
    order = Order.query.get(id)
    user = User.query.get(order.user_id)
    return render_template('order.jinja', order=order, user=user)

@orders_blueprint.route('/orders/<id>/update')
def update_order(id):
    order = Order.query.get(id)
    users = User.query.all()
    return render_template('update.jinja', order=order, users=users)

@orders_blueprint.route('/orders/<id>/update', methods=["POST"])
def apply_update(id):
    user_id = request.form['user_id']
    payment_method = request.form['payment_method']
    order_date = request.form['date']
    order = Order.query.get(id)
    order.payment_method = payment_method
    order.date = order_date
    order.user_id = user_id
    db.session.commit()
    return redirect(f'/orders/{order.id}')
    
@orders_blueprint.route('/orders/<id>/delete', methods=["POST"])
def delete_order(id):
    order = Order.query.get(id)
    db.session.delete(order)
    db.session.commit()
    return redirect('/orders')

@orders_blueprint.route('/orders/add/user', methods=['POST'])
def add_new_user():
    user_name = request.form['username']
    age = request.form['age']
    user = User(username = user_name, age = age)
    db.session.add(user)
    db.session.commit()
    return redirect('/orders')
