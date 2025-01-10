from flask import Flask, render_template, request, redirect
from models import db, StudentModel
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create tables explicitly
with app.app_context():
    db.create_all()

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    
    if request.method == 'POST':
        # Extract data from the form
        fullname = request.form['fullname']
        FatherName = request.form['FatherName']
        MotherName = request.form['MotherName']
        SchoolName = request.form['SchoolName']
        Medium = request.form['Medium']
        Gender = request.form['Gender']
        PhoneNumber = request.form['PhoneNumber']
        Fee = request.form['Fee']

        # Create a new StudentModel instance
        students = StudentModel(
            fullname=fullname,
            FatherName=FatherName,
            MotherName=MotherName,
            SchoolName=SchoolName,
            Medium=Medium,
            Gender=Gender,
            PhoneNumber=PhoneNumber,
            Fee=Fee
        )

        # Add the new student to the session and commit to the database
        db.session.add(students)
        db.session.commit()
        # Redirect to a success page
        return redirect('/')
    
@app.route('/home')
def home():
    return render_template('home.html')
    
@app.route('/', methods=['GET'])
def RetrieveList():
    students = StudentModel.query.all()
    return render_template('index.html',students=students)




@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def update(id):
    student = StudentModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if student:
             db.session.delete(student)
             db.session.commit()
             fullname = request.form['fullname']
             FatherName = request.form['FatherName']
             MotherName = request.form['MotherName']
             SchoolName = request.form['SchoolName']
             Medium = request.form['Medium']
             Gender = request.form['Gender']
             PhoneNumber = request.form['PhoneNumber']
             Fee = request.form['Fee']

             student = StudentModel(
             fullname=fullname,
             FatherName=FatherName,
             MotherName=MotherName,
             SchoolName=SchoolName,
             Medium=Medium,
             Gender=Gender,
             PhoneNumber=PhoneNumber,
             Fee=Fee
        )

        # Add the new student to the session and commit to the database
        db.session.add(student)
        db.session.commit()
        # Redirect to a success page
        return redirect('/')
        return f"Student with id = {id} Does not exist"
    return render_template('update.html', student=student)




@app.route('/<int:id>/delete', methods=['GET','POST'])

def delete(id):
    students = StudentModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if students:
            db.session.delete(students)
            db.session.commit()
            return redirect('/')
            abort(404)
    return render_template('delete.html')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)