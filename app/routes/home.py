from flask import Flask , Blueprint , render_template , redirect , url_for , request , flash , session
from app.models import post
from app import db
home_bp = Blueprint('home' , __name__)

@home_bp.route("/home", methods =["GET","POST"])
def home():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    posts = post.query.all()
    return render_template('home.html', posts=posts)
@home_bp.route("/createpost", methods =["GET","POST"])
def createpost():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    title = request.form.get('title')
    discription = request.form.get('discription')
    username = session.get('user')
    if title:
        new_post = post(title=title , discription=discription , username=username)
        db.session.add(new_post)
        db.session.commit()
        flash('post created successfully','success')
        return redirect(url_for('home.home'))
    return render_template('createpost.html')
@home_bp.route("/update/<int:post_id>", methods =["GET","POST"])
def update(post_id):
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    username = session.get('user')
    postss = post.query.get(post_id)

    # Author check
    if username != postss.username:
        flash("You are not allowed to edit this post", "danger")
        return redirect(url_for('home.home'))

    if request.method == "POST":
        postss.title = request.form.get("title")
        postss.discription = request.form.get("discription")
        db.session.commit()
        flash("Post updated successfully!", "success")
        return redirect(url_for('home.home'))

    # GET request → show edit form
    return render_template("update.html", post=postss)
@home_bp.route("/delete/<int:post_id>", methods =["GET","POST"])
def delete(post_id):
    postss = post.query.get(post_id)
    db.session.delete(postss)
    db.session.commit()
    flash('post deleted' , 'success')
    return redirect(url_for('home.home'))

        


    

