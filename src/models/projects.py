from src.database.db_connection import db
from sqlalchemy import Enum
class Projects(db.Model):
    project_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    area_of_study = db.Column(db.String(100), nullable=False)
    director_id = db.Column(db.Integer)
    director_full_name  = db.Column(db.String(100))
    project_advisor_id = db.Column(db.Integer)
    project_advisor_full_name = db.Column(db.String(100))
    author_1_id = db.Column(db.Integer, nullable=False)
    author_2_id = db.Column(db.Integer)
    author_3_id = db.Column(db.Integer)
    evaluator_id = db.Column(db.Integer)
    comment = db.Column(db.Text)
    state = db.Column(Enum('Sin evaluador', 'Con evaluador', 'Revisado', name='project_status'), default='Sin evaluador')
    file_path = db.Column(db.String(200), nullable=False)  # Assuming file path won't exceed 200 characters

    def __repr__(self):
        return '<Project %r>' % self.title
