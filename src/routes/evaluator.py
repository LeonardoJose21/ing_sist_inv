from flask import Blueprint, redirect, render_template, request, url_for
from src.models.projects import Projects
from src.models.scores import Scores
from src.database.db_connection import db
# from src.models.students import Students
# from src.models.evaluators import Evaluators
# from src.database.db_connection import db
main = Blueprint('evaluator_blueprint', __name__, template_folder='templates', url_prefix='/evaluator')
review = Blueprint('review', __name__, template_folder='templates')
send_scores = Blueprint('send_scores', __name__)

main.register_blueprint(review)
main.register_blueprint(send_scores)


@main.route('/')
def evaluator():
    evaluator_id = request.args.get('evaluator_id')
    projects = Projects.query.filter(Projects.evaluator_id == evaluator_id, Projects.state != 'Revisado').all()
    return render_template('evaluator.html', projects = projects, message='')

@review.route('/review')
def evaluator_review():
    project_id = request.args.get('project')
    project = Projects.query.filter(Projects.project_id ==project_id).first()
    return render_template('evaluator_review.html', project = project) 

@send_scores.route('/send_scores', methods=['GET', 'POST'])
def send_scores():
    project_id = request.args.get('project_id')
    form_data = {'project_id': project_id}
    try:
    # Iterate over form fields and extract key-value pairs
        for field, value in request.form.items():
            # Store the key-value pair in the dictionary
            form_data[field] = value

        # Create a Score object using the form data
        scores = Scores(**form_data)

        # Add the Score object to the database session and commit changes
        db.session.add(scores)
        db.session.commit()

        project = Projects.query.get(project_id)
        evaluator = project.evaluator_id
        if(project):
            project.state = 'Revisado'
            db.session.add(project)
            # Commit the changes
            db.session.commit()

        return redirect(url_for('evaluator_blueprint.evaluator', message = 'successfully_reviewed_project', evaluator_id = evaluator))
    except Exception as e:
        return f"Ha ocurrido un error. Intente de nuevo {e}"

    