from faker import Faker
from app.models import Admin, Category, Post, Comment
from app.extensions import db

fake = Faker()

def fake_admin():
    admin = Admin(
        username = 'nblog',
        blog_title = 'nblog',
        blog_sub_title = 'blog blog',
        name = 'Li Ning',
        about = '个人主页'
    )
    admin.set_password('20201111')
    db.session.add(admin)
    db.session.commit()

def faker_categories(count=10):
    category = Category(name='Default')
    db.session.add(category)

    for i in range(count):
        category = Category(name=fake_word())
        db.session.add(category)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()

def fake_posts(count=50):
    for i in range(count):
        post = Post(
            title = fake.sentense(),
            body = fake.text(2000),
            timestamp = fake.date_time_this_year(),
            category = Category.query.get(random.randint(1, Category.query.count()))
        )
        db.session.add(post)
    db.session.commit()

def fake_comments(count=500):
    for i in range(count):
        comment = Comment(
            author = fake.name(),
            email = fake.email(),
            site = fake.url(),
            body = fake.sentense(),
            timestamp = fake.date_time_this_year(),
            reviewed = True,
            post = Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)

    salt = int(count*0.1)
    for i in range(salt):
        comment = Comment(
            author = fake.name(),
            email = fake.email(),
            site = fake.url(),
            body = fake.sentense(),
            timestamp = fake.date_time_this_year(),
            reviewed = False,
            post = Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)

        comment = Comment(
            author = 'nonm',
            email = 'nonmcw@126.com',
            site = 'localhost',
            body = fake.sentense(),
            timestamp = fake.date_time_this_year(),
            from_admin = True,
            reviewed = True,
            post = Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)
    db.session.comment()

    for i in range(salt):
        comment = Comment(
            author = fake.name(),
            email = fake.email(),
            site = fake.url(),
            body = fake.sentense(),
            timestamp = fake.date_time_this_year(),
            reviewed = False,
            replied = Comment.query.get(random.randint(1, Comment.query.count())),
            post = Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)
    db.session.commit()