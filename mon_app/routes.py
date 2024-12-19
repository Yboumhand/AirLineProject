from flask import render_template, url_for, flash, redirect
from mon_app.forms import RegistrationForm, LoginForm
from mon_app.models import User, Post
from mon_app import app


posts = [
    {
        'author': 'Ahmed Sefrioui',
        'title': 'Boite à Merveilles',  
        'classification': 'Roman Autobiographique',
        'origin': 'Maroc',
        'city': 'Fès',
        'date_posted': '2010'
    },
    {
        'author': 'Victor Hugo',
        'title': 'Les Miserables',
        'classification': 'Nouvelle',
        'origin': 'France',
        'city': 'Paris',
        'date_posted': '2009'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts= posts)

@app.route("/about")
def about():    
    return render_template('about.html', title='About')

@app.route("/register", methods = ['GET', 'POST'])
def register(): 
    form = RegistrationForm() #() pour créer une instance
    if form.validate_on_submit(): 
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))  #redirecting to the Home Page (home function ) -- above
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods = ['GET', 'POST'])
def login(): 
    form = LoginForm() #() pour créer une instance
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unseccussful. Please check username and password', 'danger')
            # 'danger' it's a class belong to bootstrap Library 
    return render_template('login.html', title='Login', form=form)
