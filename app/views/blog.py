from . import views as views_blueprint

@views_blueprint.route('/')
def index():
    return 'hello flask'