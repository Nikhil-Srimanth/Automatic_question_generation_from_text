from flask import Flask,render_template,redirect,url_for

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")
@app.route('/Ques')
def Ques():
    a = 
if __name__ == "__main__":
    app.run(debug=True)