from flask import Flask, request, redirect, render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configure the SQLAlchemy part
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///survey.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define your database model
class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feedback = db.Column(db.String(250), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Serve the survey form
@app.route('/')
def survey():
    form_html = '''
    <form action="/submit" method="post">
        <label for="feedback">Your feedback:</label><br>
        <input type="text" id="feedback" name="feedback"><br>
        <input type="submit" value="Submit">
    </form> 
    '''
    return render_template_string(form_html)

# Handle form submission
@app.route('/submit', methods=['POST'])
def submit_survey():
    feedback = request.form['feedback']
    new_survey = Survey(feedback=feedback)
    db.session.add(new_survey)
    db.session.commit()
    return redirect('/count')

# Count and display the number of surveys
@app.route('/count')
def count_surveys():
    total_surveys = Survey.query.count()
    return f'Total number of surveys submitted: {total_surveys}'