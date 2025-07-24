from app.app_routes.user import user_bp
from app.app_routes.shoppinglist import shoppinglist_bp
from app.app_routes.shoppinglistuser import shoppinglistuser_bp

def register_blueprints(app):
    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(shoppinglist_bp, url_prefix='/api')
    app.register_blueprint(shoppinglistuser_bp, url_prefix='/api')