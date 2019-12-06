from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Posts, Users
from application.forms import PostForm, RegistrationForm, LoginForm, UpdateAccountForm
from flask_login import login_user,current_user, logout_user, login_required
""" Project imports """
from flask import render_template, redirect, url_for, request, flash
from application import app, db, bcrypt
from application.models import Artists, Tracks, Genres
from application.forms import DirectoryForm, GenreForm, SortForm
from flask_login import login_user,current_user, logout_user, login_required
from application.py.file_interactions import create_single_folder, identify_mp3_lx, \
    mp3_id3_read, folder_identify_lx, double_backslash_lx, strip_eyed3

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


"""  ~~~PROJECT ROUTES~~~   """
@app.route('/sort', methods = ['GET','POST'])
def sort():
    directory = "/home/harveyawendon/harvey/music/hiphop" #testing store
    mp3s = identify_mp3_lx(directory)
    form = SortForm()
    print (str(mp3s))
    if form.is_submitted():
        for mp3 in mp3s:
            track_id3_tags = mp3_id3_read(directory,mp3) # returns id3 tags of track
            id3_artist = track_id3_tags[2] #selects artist (title, album, artist, genre)
            id3_artist = id3_artist.lower()
            artist_in_db = bool(Artists.query.filter_by(name=id3_artist).first())
            print (id3_artist)
            print (artist_in_db)

            if artist_in_db:
                artist_has_no_default_genre = bool(Artists.query.filter_by(default_genre="").first())
                print ("no default genre: " + str(artist_has_no_default_genre))
                if artist_has_no_default_genre:
                    flash ("Artist has no default genre")
                    print ("Artist has not default genre")
                    #return redirect(url_for("sort"))
                
                elif artist_has_no_default_genre == False:
                    artist_dbrecord = Artists.query.filter_by(name=id3_artist).first()
                    print (artist_dbrecord.default_genre)
                    artist_default_genre = artist_dbrecord.default_genre #checks if master folder exists
                    existing_master_folder = folder_identify_lx(directory,"") # checks if sub folder exists
                    existing_sub_folder = folder_identify_lx(directory,artist_default_genre)
                    if existing_master_folder and existing_sub_folder:
                        master_folder_path = double_backslash_lx(directory,mp3)
                        sub_folder_path = double_backslash_lx(directory,artist_default_genre) # adds genre folder to end of path
                        sub_folder_path = double_backslash_lx(sub_folder_path,mp3) # adds mp3 name to path
                        #moving mp3 files
                        move_files_lx(master_folder_path, sub_folder_path)
                        if folder_identify_lx(sub_folder_path,""):
                            succ_or_fail = True
                        else:
                            succ_or_fail = False


                    #if existing_folder:
                     #   oldpath = double_backslash_lx(directory,CHANGEME)
                      #  move_files_lx()

        #return redirect(url_for('sort'))
    return render_template("sort.html",title="Sort", form=form, mp3s=mp3s, succ_or_fail = succ_or_fail)


@app.route('/amend_directory', methods = ['GET','POST'])
def amend_directory():
    form = GenreForm()
    if form.validate_on_submit():
        check_if_created = create_single_folder(str(form.folder_path.data),str(form.genre_name.data))
        if check_if_created:
            new_genre = Genres(
                name = form.genre_name.data,
                folder_path = form.folder_path.data+form.genre_name.data
            )
            db.session.add(new_genre)
            db.session.commit()
            flash ("Genre Folder Created")
        else:
            flash ("Genre Folder Already Exists")       
        return redirect(url_for('amend_directory'))
    return render_template("amend_directory.html",title="Amend Stuff", form=form)

    
@app.route('/manual_sort', methods = ['GET','POST'])
def manual_sot():
    pass

