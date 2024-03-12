from flask import Blueprint, render_template,request

main = Blueprint('sign_up_blueprint', __name__, template_folder='templates')


@main.route('/sign-up/<choosen_role>')
def sign_up(choosen_role):
    current_path = request.path
    if current_path not in ['/sign-up/estudiante', '/sign-up/evaluador', '/sign-up/estudiante-pass_no_equal', '/sign-up/evaluador-pass_no_equal',
                            '/sign-up/estudiante-already_signed_up', '/sign-up/evaluador-already_signed_up']:
        return "Invalid role"
    return render_template('sign-up.html', choosen_role =  choosen_role)