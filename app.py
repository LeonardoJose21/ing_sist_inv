from flask import Flask, render_template, request, redirect, send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sys
from time import sleep


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:leopas23@localhost/database"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
 
 
#our model
class todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
 
 
    def __repr__(self):
        return '<Task %r>' % self.id
# Function to create tables within application context
def create_tables():
    with app.app_context():
        db.create_all()

# Call the function to create tables
create_tables()
list = ['Registro de proyectos',
        'Seguimiento del progreso', 
        'Gestión de recursos',
        'Colaboración entre investigadores',
        'Generación de informes']
# @app.route('/',  methods = ['POST', 'GET'])
# def index():
#      if request.method == 'POST':
#         task_content = request.form['content']
#         new_task = todo(content=task_content)
#         try:
#             db.session.add(new_task)
#             db.session.commit()
#             return redirect('/')
#         except:
#             return 'There was an issue adding your task'

#      else:
#         tasks = todo.query.order_by(todo.date_created).all()
#         return render_template('index.html', tasks=tasks)

@app.route('/')
def landing():
    return render_template('landing.html', list=list)


@app.route('/sign-up')
def sign_up():
    return render_template('sign-up.html')

@app.route('/log-in')
def log_in():
    return render_template('log-in.html')

@app.route('/student')
def student():
     return render_template('student_start.html', page='student')

@app.route('/student/register_proposal', methods=['GET', 'POST'])
def register_proposal():
     return render_template('student_register_proposal.html', page='register_proposal')

@app.route('/student/download_guide')
def download_guide():
    file_path = 'static/files/'
    # Specify the filename that the browser will use when downloading the file
    filename = 'hero.jpg'
    # Send the file for download
    try:
        return send_file('static/files/hero.jpg', as_attachment=True)
    except Exception as e:
        return str(e)
    
if __name__ == '__main__':
    app.run(debug=True)