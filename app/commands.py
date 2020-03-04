import click
from app.models import db

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