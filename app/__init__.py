import os
import click

from flask import Flask, render_template
from config import config
from app.views import views as views_blueprint
from app.extensions import bootstrap, mail, moment, db, ckeditor

def create_app(config_name=None):
    if config_name == None:
        config_name = os.getenv('NBLOG_CONFIG', 'default')
    
    app = Flask('app')
    app.config.from_object(config[config_name])
    app.register_blueprint(views_blueprint)

    register_logging(app)
    register_blueprints(app)
    register_extensions(app)
    register_shell_context(app)
    register_template_context(app)
    register_errors(app)
    register_commands(app)

    return app

def register_logging(app):
    pass

def register_blueprints(app):
    app.register_blueprint(views_blueprint)

def register_extensions(app):
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    ckeditor.init_app(app)
    
def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db)
    
def register_template_context(app):
    pass

def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400
    
def register_commands(app):
    pass