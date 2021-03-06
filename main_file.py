from flask import Flask, render_template, request,json,session,redirect,flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_mail import Mail
from datetime import datetime
import os
import math

with open("templates/config.json", 'r') as c:
    params = json.load(c)['params']

app = Flask(__name__)

app.secret_key='susvni23ndnlcnioejviwenv'

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password']
)

mail=Mail(app)

app.config['UPLOAD_FOLDER']=params['upload_location']
app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
db = SQLAlchemy(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(20), nullable=False)

class posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    img_file = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(120), nullable=False)

@app.route("/")
def home():
    post=posts.query.filter_by().all()
    last=math.ceil(len(post)/int(params['no_of_posts']))
    page=request.args.get('page')
    if(not str(page).isnumeric()):
        page=1
    page=int(page)
    post=post[(page-1)*int(params['no_of_posts']):(page-1)*int(params['no_of_posts'])+int(params['no_of_posts'])]
    if(page==1):
        prev="#"
        next="/?page="+str(page+1)
    elif(page==last):
        prev="/?page="+str(page-1)
        next = "#"
    else:

        prev="/?page=" + str(page-1)
        next ="/?page=" + str(page + 1)
    return render_template('index.html',page=page,params=params,posts=post,prev=prev,next=next)

@app.route("/about")
def about():
    return render_template('about.html',params=params)

@app.route("/uploader",methods=['GET',"POST"])
def uploadingFunc():
    if ('user' in session and session['user'] == params['admin_user']):
        if (request.method == "POST"):
            f=request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename))) # os.path.join joined 2 paths
            return "Upload successfully"
    return "Upload Error"

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashboard')

@app.route('/delete/<string:sno>',methods=['GET','POST'])
def delete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        post=posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')

@app.route("/edit/<string:sno>",methods=["GET","POST"])
def edit(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if(request.method=="POST"):
            box_title=request.form.get('title')
            slug=request.form.get('slug')
            content=request.form.get('content')
            img_file=request.form.get('img_file')
            Date=datetime.now()
            if (sno=='0'):
                post=posts(title=box_title,slug=slug,content=content,img_file=img_file,date=Date)
                db.session.add(post)
                db.session.commit()
            else:
                post=posts.query.filter_by(sno=sno).first()
                post.title=box_title
                post.slug=slug
                post.content=content
                post.img_file=img_file
                post.date=Date
                db.session.commit()
                return redirect('/edit/'+sno)
        postVar=posts.query.filter_by(sno=sno).first()
        return render_template('edit.html',params=params,post=postVar,sno=sno)
    return 'Please Login First by going to "/dashboard"'

@app.route("/dashboard",methods=['GET',"POST"])
def dashboard():
    if ('user' in session and session['user']==params['admin_user'] ):
        postVar=posts.query.filter_by().all()
        return render_template('dashboard.html',params=params,posts=postVar)
    if request.method=='POST':
        username=request.form.get('uname')
        userpass = request.form.get('pass')
        if(username==params['admin_user'] and userpass==params['admin_password']):
                session['user']=username
                postVar=posts.query.filter_by().all()
                return  render_template('dashboard.html',params=params,posts=postVar)
    return render_template('login.html')

@app.route("/post/<string:post_slug>",methods=['GET'])
def post_route(post_slug):
    post=posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html',params=params,post=post)

@app.route("/postdata",methods=['GET'])
def pd():
    a=request.args.get('bar')
    return a

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        name = request.form.get('name')
        emailVar = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name=name, phone_num = phone, msg = message,email = emailVar )
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from ' + name,
                          sender='kaushikshah74@yahoo.com.in',
                          recipients=[params['gmail-user'],'kaushikshah74@yahoo.co.in'],
                          body=message + "\n" + phone
                          )
        flash("Congrats,You Have Successfully Submitted the form !", "success")
    else:
        flash("Fill the form & we'll get back to u soon :)", "danger")
    return render_template('contact.html',params=params)

app.run(debug=True)