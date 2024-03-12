from flask import Blueprint, redirect, request, render_template, url_for, flash
from src.models.students import Students
from src.models.evaluators import Evaluators
from src.database.db_connection import bcrypt
main = Blueprint('log_in_blueprint', __name__, template_folder='templates')
validate_log_in = Blueprint('validate_log_in', __name__)
main.register_blueprint(validate_log_in)



@main.route('/log-in/<choosen_role>')
def log_in(choosen_role):
    current_path = request.path
    if current_path not in ['/log-in/estudiante', '/log-in/evaluador', '/log-in/estudiante-error', '/log-in/evaluador-error',
                            '/log-in/estudiante-no_signed_up', '/log-in/evaluador-no_signed_up']:
        return "Invalid role"
    return render_template('log-in.html', choosen_role =  choosen_role)

@validate_log_in.route('/validate_data', methods=['GET', 'POST'])
def validate_data():

    role = request.args.get('choosen_role')

    if request.method == 'POST':
        password = request.form['password']
        if role.split('-')[0] == 'estudiante':
            student_cod = request.form['student_cod']

            student_is_registered = Students.query.filter_by(student_cod=student_cod).first()
            if (student_is_registered):
                valid_hash = student_is_registered.password_hash
                if (valid_hash == None):
                    return redirect(url_for('sign_up_blueprint.sign_up', choosen_role = 'estudiante'))
                password_is_valid = bcrypt.check_password_hash(valid_hash, password) 

                if(password_is_valid):
                    return redirect(url_for('student_blueprint.student', student_id = student_is_registered.student_cod))
                else:
                    return redirect(url_for('log_in_blueprint.log_in', choosen_role = role.split('-')[0] + '-error'))
            else:
                return redirect(url_for('log_in_blueprint.log_in', choosen_role = role.split('-')[0] + '-no_signed_up'))
        else:
            evaluator_number_id = request.form['doc_id_number']
            evaluator_is_registered = Evaluators.query.filter_by(doc_id_number=evaluator_number_id).first()
            
            if (evaluator_is_registered):
                valid_hash = evaluator_is_registered.password_hash
                if (valid_hash == None):
                    return redirect(url_for('sign_up_blueprint.sign_up', choosen_role = 'evaluador'))
                password_is_valid = bcrypt.check_password_hash(valid_hash, password) 

                if(password_is_valid):
                    return redirect(url_for('evaluator_blueprint.evaluator', evaluator_id = evaluator_is_registered.evaluator_id))
                else:
                    return redirect(url_for('log_in_blueprint.log_in', choosen_role = role.split('-')[0] + '-error'))
            else:
                return redirect(url_for('log_in_blueprint.log_in', choosen_role = role.split('-')[0] + '-no_signed_up'))

        
        
