from . import views as views_blueprint

@views_blueprint.route('/login', method=['GET', 'POST'])
def login():
    pass

@views_blueprint.route('logout', method=['GET', 'POST'])
def logout():
    pass