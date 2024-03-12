from src.database.db_connection import db
from src.models.projects import Projects
from src.models.evaluators import Evaluators
from sqlalchemy import join
from flask import Blueprint, redirect, render_template, request, url_for
from flask import send_file
from src.models.evaluators import Evaluators


main = Blueprint('admin_blueprint', __name__,  template_folder='templates', url_prefix='/admin')
log_in = Blueprint('log_in', __name__)
all_projects = Blueprint('all_projects', __name__, template_folder='templates')
assign_evaluator = Blueprint('assign_evaluator', __name__, template_folder='templates')
add_evaluator = Blueprint('add_evaluator', __name__, template_folder='templates')
download_file = Blueprint('download_file', __name__, template_folder='templates')
associate_evaluator = Blueprint('associate_evaluator', __name__, template_folder='templates')
filter_and_group = Blueprint('filter_and_group', __name__, template_folder='templates')
admin_config = Blueprint('admin_config', __name__, template_folder='templates')

main.register_blueprint(all_projects)
main.register_blueprint(log_in)
main.register_blueprint(assign_evaluator)
main.register_blueprint(add_evaluator)
main.register_blueprint(download_file)
main.register_blueprint(associate_evaluator)
main.register_blueprint(filter_and_group)
main.register_blueprint(admin_config)

@main.route('/log_in')
def admin_log_in():
    return render_template('admin_log_in.html')

@log_in.route('/validate_data', methods=['GET', 'POST'])
def log_in():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']

        if user == 'admin' and password == '123':
            return redirect(url_for('admin_blueprint.all_projects.admin_all_projects'))
        else:
            return render_template('admin_log_in.html', error ='incorrect_credentials')
    else:
        return f"Something went wrong: {request.form}"

@all_projects.route('/all_projects')
def admin_all_projects():
    projects = Projects.query.with_entities(Projects.title, Projects.area_of_study, Projects.state).all() 
    total_projects = len(projects)
    return render_template('admin_all_projects.html', page='admin_all_projects', projects = projects, total = total_projects, count = 0)

@assign_evaluator.route('/assign_evaluator')
def admin_assign_evaluator():
    projects = Projects.query.with_entities(Projects.project_id, Projects.title, Projects.area_of_study).filter(Projects.state == 'Sin evaluador').all()
    return render_template('admin_assign_evaluator.html', page='admin_assign_evaluator', projects = projects)

@add_evaluator.route('/add_evaluator', methods=['GET', 'POST'])
def add_evaluator():
    message = request.args.get('message')
    project_id = request.args.get('project_id')
    project = Projects.query.filter(Projects.project_id == project_id).first()
    evaluators = Evaluators.query.all()
    return render_template('admin_add_evaluator.html',page='admin_assign_evaluator', project_information = project, evaluators = evaluators, message = message)
    
@download_file.route('/download_file', methods=['GET'])
def download_file():
    file_name = request.args.get('file_path').split('\\')[-1]
    file_path = '../../static/uploads/'+file_name
    return send_file(file_path, as_attachment=True)

@associate_evaluator.route('/associate_evaluator', methods=['GET', 'POST'])
def associate_evaluator():
    project_id = request.args.get('project_id')
    evaluator = request.form['evaluator']
    state = 'Con evaluador'
    project = Projects.query.filter(Projects.project_id == project_id).first()
    try:
        project.evaluator_id = evaluator
        project.state = state
        db.session.commit()
        
        return redirect(url_for('admin_blueprint.add_evaluator.add_evaluator', message = 'asignado_correctamente', project_id = project_id))
    except Exception as e:
        return f"Ha ocurrido un erro: {e}"

@filter_and_group.route('/filter_and_group')
def admin_filter_and_group():
    projects = db.session.query(Projects, Evaluators).select_from(join(Projects, Evaluators, Projects.evaluator_id == Evaluators.evaluator_id)).add_columns(Projects.project_id, Projects.title, Projects.area_of_study, Projects.state, Evaluators.names, Evaluators.lastnames).all()
    return render_template('admin_filter_and_group.html', page='admin_filter_and_group', projects= projects)
