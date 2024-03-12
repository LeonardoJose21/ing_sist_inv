from flask import Blueprint, redirect,request,url_for
from src.database.db_connection import db
from src.models.students import Students
from src.models.evaluators import Evaluators

main = Blueprint('sign_up_validation_blueprint', __name__)

@main.route('/sig_up_validation', methods=['GET','POST'])
def sign_up_validation():
    role= request.args.get('choosen_role')
    if request.method == 'POST':

        password = request.form['pass']
        confirm_password = request.form['confirm_password']
        
        if(role.split('-')[0] =='estudiante'):
            student_names = request.form['student_names']
            student_lastnames = request.form['student_surnames']
            student_code = request.form['student_code']
            student_email = request.form['student_email']

            if password != confirm_password:
                return redirect(url_for('sign_up_blueprint.sign_up', choosen_role=role.split('-')[0]+'-pass_no_equal')) #modificar esto
            else:
                try:
                    user_already_signed = Students.query.filter_by(student_cod = student_code).first()

                    if(user_already_signed and user_already_signed.password_hash != None):
                        return redirect(url_for('sign_up_blueprint.sign_up', choosen_role=role.split('-')[0]+'-already_signed_up'))
                    
                    if(user_already_signed and user_already_signed.password_hash == None):
                        user_already_signed.set_password(password)
                        user_already_signed.names = student_names
                        user_already_signed.lastnames = student_lastnames
                        user_already_signed.student_cod = student_code
                        user_already_signed.email = student_email
                        db.session.commit()
                        return redirect(url_for('student_blueprint.student', student_id=student_code))

                    # Add the student's data to the database
                    new_student = Students(names=student_names, lastnames=student_lastnames, student_cod =student_code, email=student_email)
                    new_student.set_password(password)
                    db.session.add(new_student)
                    db.session.commit()

                    new_student_id = new_student.student_cod

                    # Redirect to the student route after successful sign up
                    return redirect(url_for('student_blueprint.student', student_id=new_student_id))
                except Exception as e:
                    # Redirect to an error page or return an error message
                    return f"An error occurred while signing up:" + str(e)
        else:

            type_of_doc = request.form['evaluator_id_type']
            evaluator_id = request.form['evaluator_id']
            evaluator_name = request.form['evaluator_name']
            evaluator_lastname = request.form['evaluator_lastname']
            evaluator_title = request.form['evaluator_grade']
            evaluator_email = request.form['evaluator_email']
            if password != confirm_password:
               return redirect(url_for('sign_up_blueprint.sign_up', choosen_role=role.split('-')[0]+'-pass_no_equal')) #modifica
            else:
                try:
                    user_already_signed = Evaluators.query.filter_by(doc_id_number = evaluator_id).count() > 0
                    if(user_already_signed):
                        return redirect(url_for('sign_up_blueprint.sign_up', choosen_role=role.split('-')[0]+'-already_signed_up'))
                    # Add the student's data to the database
                    new_evaluator = Evaluators(type_of_id=type_of_doc, doc_id_number=evaluator_id, names = evaluator_name, lastnames  = evaluator_lastname, title= evaluator_title, email = evaluator_email)
                    new_evaluator.set_password(password)
                    db.session.add(new_evaluator)
                    db.session.commit()

                    # new_student_id = new_student.student_cod

                    # Redirect to the student route after successful sign up
                    return redirect(url_for('evaluator_blueprint.evaluator'))
                except Exception as e:
                    # Redirect to an error page or return an error message
                    return f"An error occurred while signing up: {request.form}" + str(e)