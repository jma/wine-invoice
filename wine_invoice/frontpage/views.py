from flask import Blueprint, render_template

blueprint = Blueprint('frontpage', __name__, template_folder='templates', static_folder='static')

@blueprint.route('/')
def frontpage():
    return render_template('frontpage/frontpage.html')