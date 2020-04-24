import os
import click

from flask import Flask, render_template
from config import config
from app.views import views as views_blueprint
from app.extensions import bootstrap, mail, moment, db, ckeditor
from app.models import Admin, Category

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
    app.register_blueprint(views_blueprint, url_perfix='/views')

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
    @app.context_processor
    def make_template_context():
        admin = Admin.query.frist()
        categories = Category.query.order_by(Category.name).all()
        return dict(admin=admin, categories=categories)

def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400
    
def register_commands(app):
    @app.cli.command()
    @click.option('--category', default=10, help='Quantity of categoies, default it is 10.')
    @click.option('--post', default=10, help='Quantity of posts, default it is 50.')
    @click.option('--comment', default=500, help='Quantity of comments, default it is 500.')
    def forge(category, post, comment):
        """Generates the fake the categories, posts and comments."""
        from app.fakes import fake_admin, fake_categories, fake_posts, fake_comments
        db.drop_all()
        db.create_all()
        click.echo('Generating the administrator...')
        fake_admin()

        click.echo('Generating %d of categoies... ' % category)
        fake_categories(category)

        click.echo('Generating %d of posts... ' % post)
        fake_posts(post)

        click.echo('Generating %d of comments... ' % comment)
        fake_comments(comment)

        click.echo('Done')