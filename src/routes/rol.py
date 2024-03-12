from flask import Blueprint, render_template, session,request

main = Blueprint('rol_blueprint', __name__, template_folder='templates')


@main.route('/rol')
def rol():
    action = request.args.get('action')
    session['action'] = action
    return render_template('rol.html')
