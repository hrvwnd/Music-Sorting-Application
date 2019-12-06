from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Posts, Users
from application.forms import PostForm, RegistrationForm, LoginForm, UpdateAccountForm
from flask_login import login_user,current_user, logout_user, login_required
""" Project imports """
from flask import render_template, redirect, url_for, request, flash
from application import app, db, bcrypt
from application.models import Artists, Tracks, Genres
from application.forms import DirectoryForm, GenreForm 
from flask_login import login_user,current_user, logout_user, login_required
from application.py.file_interactions import create_single_folder

@app.route('/')
@app.route('/home')
def home():
    postData = Posts.query.all() 
    return render_template('home.html', title='Home', posts=postData)
    

@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/post', methods=['GET','POST'])
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        postData = Posts(
                title = form.title.data,
                content = form.content.data,
                author = current_user
        )
        db.session.add(postData)
        db.session.commit()
    
        return redirect(url_for('home'))
    else:
        print(form.errors)
    
    return render_template('post.html', title='Post', form=form)


@app.route('/register',methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data)
        user = Users(
            first_name=form.first_name.data,
            last_name = form.last_name.data,
            email=form.email.data,
            password=hashed_pw
            )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('post'))
    return render_template('register.html',title='Register',form=form)
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('home'))


@app.route("/login", methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        
        if user and bcrypt.check_password_hash(user.password,
         form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else: 
            
                return redirect(url_for('home'))
    
    return render_template('login.html', title='login',form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/account', methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)


"""  ~~~PROJECT ROUTESs~~~   """
@app.route('/sort', methods = ['GET','POST'])
def sort():
    pass

@app.route('/amend_directory', methods = ['GET','POST'])
def amend_directory():
    form = GenreForm()
    if form.validate_on_submit():
        new_genre = Genres(
            name = form.genre_name.data,
            folder_path = form.folder_path.data+form.genre_name.data
        )
        db.session.add(new_genre)
        db.session.commit()

        return redirect(url_for('amend_directory'))
    check_if_created = create_single_folder(form.genre_name.data,form.folder_path.data)
    if check_if_created:
        flash ("Directory created")
    else:
        flash ("Directory already exists")

    return render_template("amend_directory.html",title="Amend Stuff", form=form)

    
@app.route('/manual_sort', methods = ['GET','POST'])
def manual_sot():
    pass

