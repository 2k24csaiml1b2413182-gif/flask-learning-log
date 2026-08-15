from flask import Flask
app = Flask(__name__)

# ---------------- HOME PAGE ---------------------------
@app.route("/")
def home():
    return "<h1> Home Page </h1><ul>About<br>Contact<br>Orders<ul>My Purchases</ul><br></ul>"

# ---------------- ABOUT ---------------------------
@app.route("/about")
def about():
    return "<h1>About Page</h1>"

# ---------------- CONTACT ---------------------------
@app.route("/contact")
def contact():
    return "<h1>Contact Details</h1><p>Email : huda.fatimag1442@gmail.com <br> Phone: +91 8707492723</p>"

# ---------------- ORDERS ---------------------------
@app.route("/orders")
def order():
    return "<H1> Orders</h1><br> <h2>Your orders will appear here</h2>"

# ---------------- PURCHASES ---------------------------
@app.route("/orders/purchases/")
@app.route("/orders/purchases/<username>")
def purchase(username="Huda"):
    return f"<h1>{username}'s Purchases :</h1>"

# ---------------- POINTS ---------------------------
@app.route("/orders/purchases/points/")
@app.route("/orders/purchases/points/<username>/")
@app.route("/orders/purchases/points/<username>/<user_id>/")
@app.route("/orders/purchases/points/<username>/<int:user_id>/<int:user_points>")
def points(username="Huda", user_id=0 , user_points=0):
    return f"<H1>{username}'s POINT CHART</H1> <br><h2> User ID :  {user_id}<br> Your points are: {user_points}</h2>"

# ---------------- CONNECT ---------------------------
@app.route("/contact/connectwithus")
def connect():
    return "<h1>FOLLOW US HERE!!</h1>"

# ---------------- PLAIN ---------------------------
@app.route("/plain")
def plain():
    return "Just plain text"

# ---------------- STYLED ---------------------------
@app.route("/styled")
def styled():
    return "<H1> This is HTML</H1><h4> Flask renders this as markup</h4>"

# ---------------- GREET ---------------------------
@app.route("/greet/")
@app.route("/greet/<name>")
def greeting(name="Huda"):
    return f"<H1> Greetings {name}! How may we help you today.</h1>"

if __name__ == "__main__":     
    app.run(debug=True)

