from flask import Blueprint, request, jsonify, abort
from app.models import db
from sqlalchemy import desc, text

shoppinglistuser_bp = Blueprint('shoppinglistuser', __name__)

# CREATE a new shoppinglist_user entry
@shoppinglistuser_bp.route('/shoppinglistuser', methods=['POST'])
def create_shoppinglistuser():
    data = request.get_json()
    required = ['user_id', 'item_id', 'purchased_date', 'quantity', 'purchase_mode']
    if not data or not all(k in data for k in required):
        abort(400, 'user_id, item_id, purchased_date, quantity, and purchase_mode are required.')
    from app.models import User, ShoppingList
    user = User.query.get(data['user_id'])
    item = ShoppingList.query.get(data['item_id'])
    if not user or not item:
        abort(404, 'User or Item not found.')
    sql = '''INSERT INTO shoppinglist_user (user_id, item_id, purchased_date, quantity, purchase_mode) VALUES (?, ?, ?, ?, ?)'''
    db.session.execute(text(sql), (data['user_id'], data['item_id'], data['purchased_date'], data['quantity'], data['purchase_mode']))
    db.session.commit()
    return jsonify({'message': 'ShoppingListUser entry created successfully.'}), 201

# READ all shoppinglist_user entries (with user and item names)
@shoppinglistuser_bp.route('/shoppinglistuser', methods=['GET'])
def get_all_shoppinglistuser():
    sql = '''SELECT slu.id, u.name as user_name, i.itemname as product_name, i.price as item_price, \
                    slu.purchased_date, slu.quantity, slu.purchase_mode, \
                    (i.price * slu.quantity) as total_purchase_amount
             FROM shoppinglist_user slu
             JOIN users u ON slu.user_id = u.id
             JOIN shoppinglist i ON slu.item_id = i.id
             ORDER BY slu.id DESC'''
    result = db.session.execute(text(sql))
    rows = [dict(row) for row in result.mappings()]
    return jsonify(rows)

# READ a single shoppinglist_user entry by id
@shoppinglistuser_bp.route('/shoppinglistuser/<int:id>', methods=['GET'])
def get_shoppinglistuser(id):
    sql = '''SELECT slu.id, u.name as user_name, i.itemname as product_name, i.price as item_price, \
                    slu.purchased_date, slu.quantity, slu.purchase_mode, \
                    (i.price * slu.quantity) as total_purchase_amount
             FROM shoppinglist_user slu
             JOIN users u ON slu.user_id = u.id
             JOIN shoppinglist i ON slu.item_id = i.id
             WHERE slu.id = ?'''
    result = db.session.execute(text(sql), (id,)).fetchone()
    if not result:
        abort(404, 'Entry not found.')
    return jsonify(dict(result._mapping))

# UPDATE a shoppinglist_user entry
@shoppinglistuser_bp.route('/shoppinglistuser/<int:id>', methods=['PUT'])
def update_shoppinglistuser(id):
    data = request.get_json()
    fields = ['user_id', 'item_id', 'purchased_date', 'quantity', 'purchase_mode']
    updates = {k: data[k] for k in fields if k in data}
    if not updates:
        abort(400, 'No valid fields to update.')
    set_clause = ', '.join([f"{k} = :{k}" for k in updates])
    updates['id'] = id
    sql = f'''UPDATE shoppinglist_user SET {set_clause} WHERE id = :id'''
    db.session.execute(text(sql), updates)
    db.session.commit()
    return jsonify({'message': 'Entry updated successfully.'})

# DELETE a shoppinglist_user entry
@shoppinglistuser_bp.route('/shoppinglistuser/<int:id>', methods=['DELETE'])
def delete_shoppinglistuser(id):
    sql = '''DELETE FROM shoppinglist_user WHERE id = ?'''
    db.session.execute(text(sql), (id,))
    db.session.commit()
    return jsonify({'message': 'Entry deleted successfully.'})
