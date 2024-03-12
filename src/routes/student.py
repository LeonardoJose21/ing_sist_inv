import os
from src.database.db_connection import app,db
from src.models.projects import Projects
from flask import Blueprint, flash, redirect, render_template, request, send_file, url_for
from sqlalchemy import not_, or_
from src.models.scores import Scores
from src.models.students import Students
from werkzeug.utils import secure_filename

main = Blueprint('student_blueprint', __name__,  template_folder='templates', url_prefix='/student/<int:student_id>')
register_proposal = Blueprint('student_register_proposal', __name__, template_folder='templates')
send_proposal = Blueprint('student_send_proposal', __name__, template_folder='templates')
see_score = Blueprint('see_score', __name__, template_folder='templates')

main.register_blueprint(register_proposal)
main.register_blueprint(send_proposal)
main.register_blueprint(see_score)

app.config['UPLOAD_FOLDER'] = 'static\\uploads'  # Folder where files will be uploaded
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'doc', 'docx'} 

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

has_uploaded_proposal = False
proposal_is_assigned = False
proposal_is_reviewed = False

@main.route('/')
def student(student_id):
    global has_uploaded_proposal
    global proposal_is_assigned
    global proposal_is_reviewed
    
    # Query the database to retrieve the student by their ID
    student = Students.query.filter_by(student_cod=student_id).first()
    student_email = student.email
    verify_proposal = Projects.query.filter(
    (Projects.author_1_id == student_id) |
    (Projects.author_2_id == student_id) |
    (Projects.author_3_id == student_id)).first()

    verify_if_proposal_is_assigned = Projects.query.filter(
    or_(
        Projects.author_1_id == student_id,
        Projects.author_2_id == student_id,
        Projects.author_3_id == student_id
    ),
    not_(Projects.state == 'Sin evaluador')).first()

    verify_if_proposal_is_reviewed = Projects.query.filter(
    or_(
        Projects.author_1_id == student_id,
        Projects.author_2_id == student_id,
        Projects.author_3_id == student_id
    ),
    Projects.state == 'Revisado').first()
    
    if verify_proposal:
        has_uploaded_proposal = True

    if verify_if_proposal_is_assigned:
        proposal_is_assigned = True

    if verify_if_proposal_is_reviewed:
        proposal_is_reviewed = True


    return render_template('student_start.html', page='student', student_email=student_email, student_id = student_id, has_uploaded_proposal = has_uploaded_proposal, proposal_is_assigned = proposal_is_assigned, proposal_is_reviewed = proposal_is_reviewed)

@register_proposal.route('/register_proposal')
def register_proposal(student_id):
    student = Students.query.filter_by(student_cod=student_id).first()
    student_email = student.email
    verify_proposal = Projects.query.filter(
    (Projects.author_1_id == student_id) |
    (Projects.author_2_id == student_id) |
    (Projects.author_3_id == student_id)).count() > 0
    if(verify_proposal):
        has_uploaded_proposal = True
    else:
        has_uploaded_proposal = False
    return render_template('student_register_proposal.html', page='register_proposal',student_email=student_email, student_id = student_id, has_uploaded_proposal = has_uploaded_proposal)

@send_proposal.route('/send_proposal', methods=['GET', 'POST'])
def send_proposal(student_id):
    if request.method == 'POST':
        title = request.form['title']
        area_of_study = request.form['area_of_study']
        director_id = request.form['director_id'] or None
        director_name = request.form['director_name'] 
        advisor_id = request.form['advisor_id'] or None
        advisor_name = request.form['advisor_name']
        author_1_cod = request.form['author_1_id']
        author_2_cod = request.form['author_2_id'] or None
        author_2_name = request.form['author_2_name']
        author_2_names = ' '.join(author_2_name.strip(' ')[:-2])
        author_2_lastnames = ' '.join(author_2_name.strip(' ')[-2:])
        author_2_email = request.form['author_2_email']
        author_3_cod = request.form['author_3_id'] or None
        author_3_name = request.form['author_3_name']
        author_3_names = ' '.join(author_3_name.split(' ')[:-2])
        author_3_lastnames = ' '.join(author_3_name.split(' ')[-2:])
        author_3_email = request.form['author_3_email']
        comment = request.form['comment']

        if(author_2_cod != None):
            student_exists = Students.query.filter(Students.student_cod == author_2_cod).first()
            if(not student_exists):
                new_student = Students(names= author_2_names, lastnames=author_2_lastnames, student_cod =author_2_cod, email=author_2_email)
                db.session.add(new_student)
                db.session.commit()
            else:
                pass

        if(author_3_cod != None):
            student_exists = Students.query.filter(Students.student_cod == author_3_cod).first()
            if(not student_exists):
                new_student = Students(names= author_3_names, lastnames=author_3_lastnames, student_cod =author_3_cod, email=author_3_email)
                db.session.add(new_student)
                db.session.commit()
            else:
                pass

        try:
            if 'file' not in request.files:
                flash('No file part')
                # return redirect(request.url)
            
            file = request.files['file']
            if file.filename == '':
                flash('No selected file')
                # return redirect(request.url)

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)

                new_project = Projects(title=title, area_of_study=area_of_study, director_id = director_id,
                                    director_full_name = director_name, project_advisor_id = advisor_id,
                                    project_advisor_full_name = advisor_name, author_1_id = author_1_cod,
                                    author_2_id = author_2_cod, author_3_id = author_3_cod, comment = comment,
                                    file_path=file_path )
                db.session.add(new_project)
                db.session.commit()

            # Redirect or render a response here
                # has_uploaded_proposal = True
                return redirect(url_for('student_blueprint.student', student_id=student_id, has_uploaded_proposal = has_uploaded_proposal))
        except Exception as e:
            return str(e)

@see_score.route('/see_score')
def see_score(student_id):
    project = Projects.query.filter(
    (Projects.author_1_id == student_id) |
    (Projects.author_2_id == student_id) |
    (Projects.author_3_id == student_id)).first()

    student = Students.query.filter(Students.student_cod==student_id).first()
    student_email = student.email
    scores = Scores.query.filter_by(project_id = project.project_id).first()

    return render_template('student_see_score.html', student_id = student_id, page = 'student', scores = scores, student_email = student_email)