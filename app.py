from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/contact'
db = SQLAlchemy(app)
mail = Mail(app)

'''class Contacts(db.Model):
    name = db.column(db.String(60), nullable = False)
    email = db.column(db.String(60), nullable = False)
    subject = db.column(db.String(100), nullable = False)
    message = db.column(db.String(250), nullable = False)
    date = db.column(db.String(50), nullable=True)'''

app.config['SECRET_KEY'] = 'contact form'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'amitnitt015@gmail.com'
app.config['MAIL_PASSWORD'] = 'amit1999'
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

class Contacts(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    '''Phone_Number = db.Column(db.String(10), unique=True, nullable=False)'''
    subject = db.Column(db.String(80), unique=False, nullable=False)
    message = db.Column(db.String(200), unique=False, nullable=False)
    date = db.Column(db.String(12), unique=True, nullable=True)

@app.route("/")
def index():
    return render_template("contact.html")

@app.route("/result", methods=['POST', 'GET'])
def result():
    if request.method == "POST":
        Name = request.form.get("Name")
        email = request.form.get("email")
        subject = request.form.get("Subject")
        message = request.form.get("message")

        entry = Contacts(name= Name, email=email, subject=subject, message=message, date=datetime.now()  )
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message', 
                           sender= email, 
                           recipients = ['ak2383977@gmail.com'],
                           body = Name + "\n" + email + "\n" + subject + "\n" + message)
        flash('Form submitted')
    '''return redirect(url_for('contact'))'''
    return render_template("contact.html", result="Sucess!")
    
    
if __name__ == '__main__':
    app.run(debug=True)


