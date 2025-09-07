from flask import Flask , Blueprint , render_template , redirect , url_for , request , flash , session

auth_bp = Blueprint('auth' , __name__)

creditcredentials = {
    "admin" : "1234"   # username=admin, password=1234
}

@auth_bp.route("/", methods =["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in creditcredentials and creditcredentials[username] == password:
            session['user'] = username
            flash(f'{username} successfully logged in' , 'success')
            return redirect(url_for('home.home'))   # ye chalega jab home_bp register hoga
        else:
            flash('invalid username or password', 'error')
            return redirect(url_for('auth.login'))

    return render_template('login.html')

@auth_bp.route("/signup", methods =["GET","POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username not in creditcredentials:
            creditcredentials[username] = password
            flash(f'successfully {username} added' , 'success')
            return redirect(url_for('auth.login'))
        else:
            flash("username already exists", "error")
    return render_template('signup.html')

@auth_bp.route("/logout", methods =["GET","POST"])
def logout():
    session.pop('user', None)
    flash('logout successfully' , 'info')
    return redirect(url_for("auth.login"))
