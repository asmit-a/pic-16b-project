'''
At the command line: 
conda activate PIC16B
export FLASK_ENV=development; flask run

'''

from flask import Flask, render_template, g, request

app = Flask(__name__)

#Show base page with links to submit and view
@app.route("/")
def main():
    return render_template("basic.html")

#Establish submit page
@app.route("/submit", methods=['POST', 'GET'])
def submit():
    if request.method == 'GET' :
        return render_template("submit.html")
    else:
        tab = gather_data(request)
        return render_template("submit.html", done = True)

#Function inserts the message into the table
def gather_data(request):
    #Get inputs from form
    table = request.form['table']

    return table

#Establish view page
@app.route("/view")
def view():
    return render_template('view.html')