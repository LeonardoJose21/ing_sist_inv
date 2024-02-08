from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:leopas23@localhost/database"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
 
 
#our model
class todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable = False)
    completd = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.datetime.now())
 
 
    def __repr__(self):
        return '<Task %r>' % self.id
 

@app.route('/',  methods = ['POST', 'GET'])
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)