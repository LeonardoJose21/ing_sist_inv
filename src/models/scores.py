from src.database.db_connection import db

class Scores(db.Model):

    score_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Scores for different aspects
    tematica_score = db.Column(db.Integer, nullable=False)
    coherencia_score = db.Column(db.Integer, nullable=False)
    planteamiento_problema_score = db.Column(db.Integer, nullable=False)
    justificacion_score = db.Column(db.Integer, nullable=False)
    objetivos_score = db.Column(db.Integer, nullable=False)
    metodologia_score = db.Column(db.Integer, nullable=False)
    resultados_score = db.Column(db.Integer)
    principales_conclusiones_score = db.Column(db.Integer, nullable=False)
    # Comments for different aspects
    tematica_comment = db.Column(db.String(255))
    coherencia_comment = db.Column(db.String(255))
    planteamiento_problema_comment = db.Column(db.String(255))
    justificacion_comment = db.Column(db.String(255))
    objetivos_comment = db.Column(db.String(255))
    metodologia_comment = db.Column(db.String(255))
    resultados_comment = db.Column(db.String(255))
    principales_conclusiones_comment = db.Column(db.String(255))
    # General observations
    general_observations = db.Column(db.String(300))
    # Foreign key
    project_id = db.Column(db.Integer)

    def __repr__(self):
        return f"Score(score_id={self.score_id}, project_id={self.project_id})"
