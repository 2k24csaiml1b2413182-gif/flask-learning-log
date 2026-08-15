from flask import Flask, render_template,request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('homepage.html')

@app.route("/details")
def details():
    username= request.args.get('username','').strip()
    if not username:
        return render_template("homepage.html")
    languages=['Python','Javascript','HTML','CSS']
    return render_template('details.html',username=username,repo_count=31,is_active =True, languages= languages)



if __name__ == '__main__':
    app.run(debug=True)