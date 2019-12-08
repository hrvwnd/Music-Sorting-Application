""" Project imports """
from flask import render_template, redirect, url_for, request, flash
from application import app, db, bcrypt
from application.models import Artists, Tracks, Genres
from application.forms import DirectoryForm, GenreForm, SortForm, UpdateArtistsForm, \
    DeleteASong
from flask_login import login_user,current_user, logout_user, login_required
from application.py.file_interactions import create_single_folder, identify_mp3_lx, \
    mp3_id3_read, folder_identify_lx, double_backslash_lx, strip_eyed3,move_files_lx 


"""  ~~~PROJECT ROUTES~~~   """
@app.route("/")
@app.route('/sort', methods = ['GET','POST'])
def sort():
    directory = "/home/harveyawendon/harvey/music" #testing store (only works on hosted vm)
    directory = "/opt/flask-app/music"
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

        return redirect(url_for('sort'))
    return render_template("sort.html",title="Sort", form=form, mp3s=mp3s)


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


@app.route('/update_artist_genre', methods = ['GET','POST'])
def update_artist_genre():
    form = UpdateArtistsForm()
    if form.validate_on_submit():
        dbartist = Artists.query.filter_by(name = artist_name).first()
        dbartist.default_genre = form.new_default_genre.data
        db.session.commit()
        return redirect(url_for('update_artist_genre'))
    return render_template("update_artist_genre.html",title="Update Artist Genre", form=form)
        

@app.route('/delete', methods = ['GET','POST'])
def delete():
    form = DeleteASong()
    if form.validate_on_submit():
        Tracks.query.filter_by(title = form.song_title.data).delete()
        return redirect(url_for('delete'))
    return render_template("delete.html",title="Delete a song", form=form)

