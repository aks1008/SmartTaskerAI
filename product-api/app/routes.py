from app.app_routes.student import student_bp

def register_blueprints(app):
    app.register_blueprint(student_bp, url_prefix='/api')