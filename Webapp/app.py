'''
At the command line: 
conda activate PIC16B
export FLASK_ENV=development; flask run

'''

from flask import Flask, render_template, g, request

import pandas as pd
import censusdata

import plotly.io as pio
from plotly import express as px
from plotly.io import write_html

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

def get_tables(codes, names, years):
    tables = []
    for year in years:
        #Get table
        df = censusdata.download('acs5', year,
                   censusdata.censusgeo([('state', '*')]),
                    codes)
        
        #Rename columns
        name_dict = dict(zip(codes, names))
        name_dict['index'] = 'State'
        df = df.reset_index() #Turns row names into row
        df = df.rename(columns = name_dict)
        
        #Shorten states column to state name
        df = df.astype({'State':'str'})
        df['State'] = df['State'].str.split(':').str.get(0) 
        
        #Add column for year
        df['Year'] = year
        
        tables.append(df)
    return pd.concat(tables)

def make_marriage_table():
    marriage = get_tables(['B12007_001E', 'B12007_002E'], 
        ['Male age', 'Female age'], [2009, 2014, 2019])
    mar_cal = marriage[marriage['State'] == "California"]
    fig = px.scatter(data_frame = mar_cal, 
                x = "Year", 
                y = ["Male age", "Female age"],
                title = "Median Age of First Marriage (CA)",
                trendline = "ols", # ordinary least squares regression trendline
                width = 800,
                height = 600)
    write_html(fig, "templates/plot.html")



#Establish view page
@app.route("/view")
def view():
    make_marriage_table()
    return render_template('plot.html')