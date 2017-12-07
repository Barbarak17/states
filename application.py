from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required, apology
import re


# Configure web application
app = Flask(__name__)


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///states.db")


@app.route("/")
@login_required
def index():
    """Handle requests for / via GET (and POST)"""

    # Route to the home page
    return render_template("index.html")


@app.route("/state", methods=['GET','POST'])
@login_required
def state():
    """Get to each state's html"""
    # if routed via POST
    if request.method == "POST":
        # select from the index each state's id and render to the appropriate template.
        state = request.form.get('state')
        if state == "id1":
            return render_template("ak.html")
        elif state == "id2":
            return render_template("al.html")
        elif state == "id3":
            return render_template("ar.html")
        elif state == "id4":
            return render_template("az.html")
        elif state == "id5":
            return render_template("ca.html")
        elif state == "id6":
            return render_template("co.html")
        elif state == "id7":
            return render_template("ct.html")
        elif state == "id8":
            return render_template("de.html")
        elif state == "id9":
            return render_template("fl.html")
        elif state == "id10":
            return render_template("ga.html")
        elif state == "id11":
            return render_template("hi.html")
        elif state == "id12":
            return render_template("ia.html")
        elif state == "id13":
            return render_template("id.html")
        elif state == "id14":
            return render_template("il.html")
        elif state == "id15":
            return render_template("in.html")
        elif state == "id16":
            return render_template("ks.html")
        elif state == "id17":
            return render_template("ky.html")
        elif state == "id18":
            return render_template("la.html")
        elif state == "id19":
            return render_template("ma.html")
        elif state == "id20":
            return render_template("md.html")
        elif state == "id21":
            return render_template("me.html")
        elif state == "id22":
            return render_template("mi.html")
        elif state == "id23":
            return render_template("mn.html")
        elif state == "id24":
            return render_template("mo.html")
        elif state == "id25":
            return render_template("ms.html")
        elif state == "id26":
            return render_template("mt.html")
        elif state == "id27":
            return render_template("nc.html")
        elif state == "id28":
            return render_template("nd.html")
        elif state == "id29":
            return render_template("ne.html")
        elif state == "id30":
            return render_template("nh.html")
        elif state == "id31":
            return render_template("nj.html")
        elif state == "id32":
            return render_template("nm.html")
        elif state == "id33":
            return render_template("nv.html")
        elif state == "id34":
            return render_template("ny.html")
        elif state == "id35":
            return render_template("oh.html")
        elif state == "id36":
            return render_template("ok.html")
        elif state == "id37":
            return render_template("or.html")
        elif state == "id38":
            return render_template("pa.html")
        elif state == "id39":
            return render_template("ri.html")
        elif state == "id40":
            return render_template("sc.html")
        elif state == "id41":
            return render_template("sd.html")
        elif state == "id42":
            return render_template("tn.html")
        elif state == "id43":
            return render_template("tx.html")
        elif state == "id44":
            return render_template("ut.html")
        elif state == "id45":
            return render_template("va.html")
        elif state == "id46":
            return render_template("vt.html")
        elif state == "id47":
            return render_template("wa.html")
        elif state == "id48":
            return render_template("wi.html")
        elif state == "id49":
            return render_template("wv.html")
        elif state == "id50":
            return render_template("wy.html")
        return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/back")
def back():
    """go back to index"""

    # Redirect user to the home page
    return redirect(url_for("index"))


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        password = request.form.get("password")

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Require certain length, uppercase, and alphanumerical passwords
        elif re.search('[0-9]', password) is None:
            return apology("password must contain a number", 403)

        elif re.search('[A-Z]', password) is None:
            return apology("password must contain an uppercase letter", 403)

        elif len(password) < 6:
            return apology("password must contain minimum 6 characters", 403)

        # Ensure password confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must re-enter password", 403)

        # Ensure passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords don't match", 403)

        # Insert registered users into users with passwords stored as hash values
        result = db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)",
                            username=request.form.get("username"), hash=generate_password_hash(request.form.get("password")))
        if not result:
            return apology("username taken", 403)

        # remember user session
        user_id = db.execute("SELECT id FROM users WHERE username IS :username",
                             username=request.form.get("username"))
        session["user_id"] = user_id[0]['id']

        # redirect user to home page
        return redirect(url_for("index"))

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)

# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
