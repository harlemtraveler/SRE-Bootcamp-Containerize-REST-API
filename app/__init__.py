from flask import Flask
from .db import db
from .routes.students import students_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    app.register_blueprint(students_bp, url_prefix='/api/v1/students')

    @app.route('/healthcheck')
    def healthcheck():
        return {'status': 'healthy'}, 200

    return app