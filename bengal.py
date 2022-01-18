from flask import Flask, render_template
#from flask_ngrok import run_with_ngrok
#import webbrowser
app = Flask(__name__)
#run_with_ngrok(app)

@app.route('/')
def ab():
    return render_template("index.html")
    
@app.route('/chinangle')
def ch():
    return render_template("Chinangle.html")
    
@app.route('/japanangle')
def ja():
    return render_template("Japanangle.html")
    
@app.route('/urisha')
def ur():
    return render_template("Urisha.html")
    
@app.route('/bf')
def bf():
    return render_template("Ba.html")
    
@app.route('/bengol')
def be():
    return render_template("bengol.html")
    
app.run(debug=True, host="0.0.0.0")    