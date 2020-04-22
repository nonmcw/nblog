from . import views as views_blueprint
from flask import render_template
from app.models import Post

@views_blueprint.route('/')
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('blog/index.html', posts=posts)

@views_blueprint.route('/about')
def about():
    return render_template('blog/about.html')

@views_blueprint.route('/category/<int:category_id>')
def show_category(category_id):
    return render_template('blog/category.html')

@views_blueprint.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    return render_template('blog/post.html')