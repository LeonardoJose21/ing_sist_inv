from src.database.db_connection import db, bcrypt

class Evaluators(db.Model):
    evaluator_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_of_id = db.Column(db.String(100), nullable=False)
    doc_id_number = db.Column(db.Integer, unique=True, nullable=False)
    names = db.Column(db.String(100), nullable=False)
    lastnames = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"<Evaluator {self.names} {self.lastnames}>"
    
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password)