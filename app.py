import os
from src.database.db_connection import app
from flask_session import Session
from src import init_app
from dotenv import load_dotenv

load_dotenv() 

sess = Session()

# def create_tables():
#     with app.app_context():
#         db.create_all()

# # Call the function to create tables
# create_tables()


if __name__ == '__main__':
    init_app()
    app.secret_key = os.getenv('SECRET_KEY')
    app.config['SESSION_TYPE'] = os.getenv('SESSION_TYPE')
    sess.init_app(app)
    app.run(debug=True)