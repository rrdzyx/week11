from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#SETUP app to use a sqlachmey database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sampledb.db'

db = SQLAlchemy(app)

class Visitor(db.Model):
    username = db.Column(db.String(100), primary_key=True)
    numVisits = db.Column(db.Integer, default=1)

    def __repr__(self):
        return f"{self.username} - {self.numVisits}"
    
#create tables in Database
with app.app_context():
    db.create_all()

#function to read in details for page
# Make a homepage   
@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/hello/<name>')
def hello(name):
    listOfNames = [name, "Chums", "Chester"]
    return render_template('name.html', name=name, nameList=listOfNames)

@app.route('/visitor>')
def wat(name):
    return render_template('visitors.html')

@app.route('/form', methods=['GET', 'POST'])
def formDemo(name=None):
    if request.method == 'POST':
        name=request.form['name']
    return render_template('form.html', name=name)

# Add the option to run this file directly
if __name__ == "__main__":
    app.run(debug=True)