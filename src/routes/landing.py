from flask import Blueprint, render_template

main = Blueprint('landing_blueprint', __name__)

@main.route('/')
def landing():
    return render_template('landing.html')