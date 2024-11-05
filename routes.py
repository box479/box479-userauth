import os
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
from app import app, db
from models import User
from forms import LoginForm, RegisterForm, EditProfileForm

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('profile'))
        flash('Invalid email or password', 'danger')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            first_name=form.first_name.data,
            last_initial=form.last_initial.data,
            phone_number=form.phone_number.data,
            role=form.role.data
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_initial = form.last_initial.data
        current_user.phone_number = form.phone_number.data
        
        if form.profile_picture.data:
            file = form.profile_picture.data
            if file and allowed_file(file.filename):
                filename = secure_filename(f"user_{current_user.id}_{file.filename}")
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                current_user.profile_picture = filename
        
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile'))
    
    form.first_name.data = current_user.first_name
    form.last_initial.data = current_user.last_initial
    form.phone_number.data = current_user.phone_number
    return render_template('edit_profile.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
