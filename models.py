from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class StudentModel(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String())
    FatherName = db.Column(db.String())
    MotherName = db.Column(db.String())
    SchoolName = db.Column(db.String())
    Medium = db.Column(db.String())
    Gender = db.Column(db.String())
    PhoneNumber = db.Column(db.String())
    Fee = db.Column(db.Integer)  # Fixed capitalization of Integer

    def __init__(self, fullname, FatherName, MotherName, SchoolName, Medium, Gender, PhoneNumber, Fee):
        self.fullname = fullname
        self.FatherName = FatherName
        self.MotherName = MotherName
        self.SchoolName = SchoolName
        self.Medium = Medium
        self.Gender = Gender
        self.PhoneNumber = PhoneNumber
        self.Fee = Fee

    def __repr__(self):
        return f"{self.fullname}:{self.FatherName}:{self.MotherName}"  # Fixed attribute names and indentation
