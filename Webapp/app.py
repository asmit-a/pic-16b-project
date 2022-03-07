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
        states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 
            'Colorado', 'Delaware', 'District of Columbia', 'Connecticut', 
            'Florida', 'Georgia', 'Idaho', 'Hawaii', 'Illinois', 'Indiana', 
            'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 
            'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 
            'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 
            'New Jersey', 'New Mexico', 'New York', 'North Carolina', 
            'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 
            'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 
            'Texas', 'Vermont', 'Utah', 'Virginia', 'Washington', 
            'West Virginia', 'Wisconsin', 'Wyoming', 'Puerto Rico']
        return render_template("submit.html", states = states)
    else:
        table = request.form["table"]
        state = request.form["state"]
        if (table == "marriage"):
            make_marriage_table(state)
            return render_template("marriage.html")
        elif (table == "household"):
            make_household_table(state)
            return render_template("household.html")
        elif (table == "divorce"):
            make_divorce_table(state)
            return render_template("divorce.html")

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

def make_marriage_table(state):
    marriage = get_tables(['B12007_001E', 'B12007_002E'], 
        ['Male age', 'Female age'], [2009, 2014, 2019])
    mar_state = marriage[marriage['State'] == state]
    fig = px.scatter(data_frame = mar_state, 
                x = "Year", 
                y = ["Male age", "Female age"],
                title = "Median Age of First Marriage (" + state + ")",
                trendline = "ols", # ordinary least squares regression trendline
                width = 800,
                height = 600)
    write_html(fig, "templates/marriage.html")

def make_household_table(state): 
    household_type = get_tables(['B11001_001E', 'B11001_002E','B11001_003E','B11001_004E','B11001_007E','B11001_008E','B11001_009E'], 
                                ['Total', 'Total Family','Married-couple Family', 'Single Householder, no spouse','Total Nonfamily','Nonfamily Living Alone','Nonfamily Not Alone'], 
                                [2009, 2014, 2019])
    household = household_type[household_type['State']==state]
    mc_percentage = household['Married-couple Family'] / household['Total']
    sh_percentage = household['Single Householder, no spouse'] / household['Total']
    nla_percentage = household['Nonfamily Living Alone'] / household['Total']
    nna_percentage = household['Nonfamily Not Alone'] / household['Total']
    year = household['Year']

    household_percentage = pd.DataFrame({
        'Married-couple Family': mc_percentage,
        'Single Householder': sh_percentage, 
        'Nonfamily Living Alone': nla_percentage, 
        'Nonfamily Not Alone': nna_percentage,
        'Year': year
    })

    household_percentage = household_percentage.round(decimals = 4)
    fig = px.bar(household_percentage,
             x="Year", 
             y=["Married-couple Family","Single Householder", "Nonfamily Living Alone","Nonfamily Not Alone"],  
             title="Household Types (" + state + ")", 
             width = 800, 
             height = 600)

    write_html(fig, "templates/household.html")

def make_divorce_table(state): 
    divorces = get_tables(['B12503_001E','B12503_003E','B12503_005E','B12503_006E','B12503_008E','B12503_010E','B12503_011E'],
                          ['Total','Male Never Married', 'Male Married; Divorced Last Year', 'Male Married; Not Divorced Last Year','Female Never Married','Female Married; Divorced Last Year','Female Married; Not Divorced Last Year'],
                          [2012, 2019])

    divorces = divorces[divorces['State']==state]
    never_married_total = divorces["Male Never Married"] + divorces["Female Never Married"]
    div_last_year = divorces["Male Married; Divorced Last Year"] + divorces["Female Married; Divorced Last Year"]
    married_not_div = divorces["Male Married; Not Divorced Last Year"] + divorces["Female Married; Not Divorced Last Year"]
    total = divorces["Total"]
    year = divorces["Year"]

    divorces_totals = pd.DataFrame({
        'Total': total,
        'Never Married Total': never_married_total,
        'Ever Married; Divorced Last Year': div_last_year, 
        'Ever Married; Did Not Divorce Last Year': married_not_div, 
        'Year': year
    })

    never_married_per = divorces_totals["Never Married Total"] / divorces_totals["Total"]
    married_div_per = divorces_totals["Ever Married; Divorced Last Year"] / divorces_totals["Total"]
    married_not_div_per = divorces_totals["Ever Married; Did Not Divorce Last Year"] / divorces_totals["Total"]

    divorces_percentages = pd.DataFrame({
        'Never Married': never_married_per,
        'Ever Married; Divorced Last Year': married_div_per, 
        'Ever Married; Did Not Divorce Last Year': married_not_div_per, 
        'Year': year
    })

    divorces_percentages = divorces_percentages.round(decimals = 4)
    fig = px.scatter(divorces_percentages, 
                x = "Year", 
                y = ["Never Married", "Ever Married; Divorced Last Year", "Ever Married; Did Not Divorce Last Year"],
                title = "Divorces in the Past Year in " + state,
                trendline = "ols", # ordinary least squares regression trendline
                width = 800,
                height = 600)
    write_html(fig, "templates/divorce.html")


    


    




#Establish view page
@app.route("/view")
def view():
    make_marriage_table("California")
    return render_template('marriage.html')



#Establish find page
@app.route("/find", methods=['POST', 'GET'])
def find():
    if request.method == 'GET' :
        return render_template('find.html')
    else:
        topic = request.form["topic"]
        year = 2019#request.form["state"]
        names = see_tables(year, topic)
        return render_template('find.html', names = names)


def see_tables(year, keyword):
    tables = censusdata.search('acs5', year,'concept', keyword)
    names = list(set([row[1] for row in tables[:len(tables)] if len(row[1]) < 500]))
    names.sort()
    return names
