from flask import Flask, render_template, request, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime
from flask_mail import Mail
import os
import math
from werkzeug.utils import secure_filename

with open("templates/config.json", 'r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)
app.secret_key = 'Each Flask web application contains a secret key which is used to sign session cookies for protection against cookie data tampering. This is a must if we are implementing session system or we get error'
app.config['UPLOAD_FOLDER'] = params['upload_location']
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password'],
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)
mail = Mail(app)
if params['local_server']:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
db = SQLAlchemy(app)


class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)


class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    img_file = db.Column(db.String(21), nullable=True)
    date = db.Column(db.String(12), nullable=True)


@app.route('/')
def home():
    post = Posts.query.filter_by().all()
    last = math.ceil(len(post) / int(params['no_of_posts']))
    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    post = post[(page - 1) * int(params['no_of_posts']):(page - 1) * int(params['no_of_posts']) + int(params['no_of_posts'])]
    if (page == 1):
        prev = "#"
        next = "/?page=" + str(page + 1)
    elif (page == last):
        prev = "/?page=" + str(page - 1)
        next = "#"
    else:
        prev = "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)
    return render_template('index.html', page=page, params=params, posts=post, prev=prev, next=next, last=last)


@app.route('/about')
def about():
    return render_template('about.html', params=params)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name=name, phone_num=phone, msg=message, date=datetime.now(), email=email)
        db.session.add(entry)
        db.session.commit()
        mail.send_message('Notification about BlogPage',
                          sender=email,
                          recipients=[params['gmail-user']],
                          body= "New User Signed Up:" + name + '\nemail:' + email +'\nmessage:' + message + '\nphone:' + phone)
    #     We have to turn on Allow less secure app setting to allow smtp server to send emails.
    #     Its link is https://myaccount.google.com/lesssecureapps
        flash("Congrats,You Have Successfully Submitted the form !", "success")
    # else:
        # flash("Fill the form & we'll get back to u soon :)", "danger")
    return render_template('contact.html', params=params)


@app.route('/post/<string:post_slug>', methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)


@app.route('/login', methods=['GET', 'POST'])
def dashboard():
    loginfail = False
    if 'user' in session and session['user'] == params['admin_user']:
        posts = Posts.query.all()
        return render_template('dashboard.html', params=params, posts=posts)
    elif request.method == 'POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if username == params['admin_user'] and userpass == params['admin_password']:
            session['user'] = username
            posts = Posts.query.all()
            return render_template('dashboard.html', params=params, posts=posts)
        else:
            loginfail = "Credentials Don't Match"
            return render_template('login.html', params=params, loginfail=loginfail)
    else:
        return render_template('login.html', params=params)


@app.route("/edit/<string:sno>", methods=['GET', 'POST'])
def edit(sno):
    if "user" in session and session['user'] == params['admin_user']:
        if sno == '0':
            message = "Add"
        else:
            message = "Edit"

        # This Post request below is from edit.html to submit an edited or a new post. The above lines and the lines below the if request.method=="POST" are responsible to bring us to the edit.html where we can add or edit a post.
        if request.method == "POST":
            box_title = request.form.get('title')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            date = datetime.now()

            if sno == '0':
                post = Posts(title=box_title, slug=slug, content=content, img_file=img_file, date=date)
                db.session.add(post)
                db.session.commit()

            else:
                post = Posts.query.filter_by(sno=sno).first()   #find that exact post in database and commit changes there
                post.title = box_title
                post.slug = slug
                post.content = content
                post.img_file = img_file
                post.date = date
                db.session.commit()
            return redirect('/login')

        post = Posts.query.filter_by(sno=sno).first()
        return render_template('edit.html', params=params, post=post, sno=sno, message=message)
    return redirect('/login')


@app.route('/uploader', methods=['GET','POST'])
def uploader():
    if 'user' in session and session['user'] == params['admin_user']:
        if request.method == 'POST':
            f = request.files['file1']
            f.save(os.path.join(params['upload_location'], secure_filename(f.filename)))
            posts = Posts.query.all()
            return render_template('dashboard.html', params=params, posts=posts, uploadMessage="File Uploaded Successfully")
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/login')


@app.route('/delete/<string:sno>', methods=['GET','POST'])
def delete(sno):
    if 'user' in session and session['user'] == params['admin_user']:
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/login')

# API to get a list of all available Images
@app.route('/AvailableImageFiles', methods=['GET','POST'])
def availImages():
    astring = ''
    firstiteration = 0
    a = os.listdir(params['upload_location'])
    for i in a:
        if firstiteration == 0:
            astring += i
            firstiteration += 1
        else:
            astring += ', '+i
    return astring

app.run(debug=True)
