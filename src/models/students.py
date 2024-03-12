from src.database.db_connection import db, bcrypt

class Students(db.Model):
    student_cod = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.String(100), nullable=False)
    lastnames = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=True)  # Assuming hashed passwords are stored

    def __repr__(self):
        return f"<Student {self.names} {self.lastnames}>"
    
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password)
