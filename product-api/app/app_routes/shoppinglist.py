from flask import Blueprint, request, jsonify, abort
from app.models import db, ShoppingList

shoppinglist_bp = Blueprint('shoppinglist', __name__)

# CREATE a new shopping list item
@shoppinglist_bp.route('/shoppinglist', methods=['POST'])
def create_item():
    data = request.get_json()
    if not data or not data.get('itemname') or not data.get('price') or not data.get('category'):
        abort(400, 'itemname, price, and category are required.')
    item = ShoppingList(itemname=data['itemname'], price=data['price'], category=data['category'])
    db.session.add(item)
    db.session.commit()
    return jsonify({'id': item.id, 'itemname': item.itemname, 'price': item.price, 'category': item.category}), 201

# READ all shopping list items
@shoppinglist_bp.route('/shoppinglist', methods=['GET'])
def get_items():
    items = ShoppingList.query.all()
    return jsonify([
        {'id': item.id, 'itemname': item.itemname, 'price': item.price, 'category': item.category}
        for item in items
    ])

# READ a single item by id
@shoppinglist_bp.route('/shoppinglist/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = ShoppingList.query.get_or_404(item_id)
    return jsonify({'id': item.id, 'itemname': item.itemname, 'price': item.price, 'category': item.category})

# UPDATE an item by id
@shoppinglist_bp.route('/shoppinglist/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = ShoppingList.query.get_or_404(item_id)
    data = request.get_json()
    if not data:
        abort(400, 'No input data provided')
    item.itemname = data.get('itemname', item.itemname)
    item.price = data.get('price', item.price)
    item.category = data.get('category', item.category)
    db.session.commit()
    return jsonify({'id': item.id, 'itemname': item.itemname, 'price': item.price, 'category': item.category})

# DELETE an item by id
@shoppinglist_bp.route('/shoppinglist/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = ShoppingList.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': f'Item {item_id} deleted'})
