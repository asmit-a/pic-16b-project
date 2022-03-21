'''
At the command line: 
conda activate PIC16B
export FLASK_ENV=development; flask run

'''

from flask import Flask, render_template, g, request, url_for, redirect, session, send_file

import pandas as pd
import censusdata
import itertools

import plotly.io as pio
from plotly import express as px
from plotly.io import write_html

app = Flask(__name__)
app.secret_key = "info"
#searched = ""

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
        elif (table == "multigen"):
            make_multigen_table(state)
            return render_template("multigen.html")
        elif (table == "children"):
            make_children_table(state)
            return render_template("children.html")

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

def make_multigen_table(state):
    multigen = get_tables(['B11017_001E','B11017_002E','B11017_003E'],
                                   ['Total','Multigenerational','Other'],
                                   [2012,2019])

    multigen = multigen[multigen['State']==state]

    mg_percentage = multigen['Multigenerational'] / multigen['Total']
    other_percentage = multigen['Other'] / multigen['Total']
    year = multigen['Year']

    multigen_percentages = pd.DataFrame({
        'Multigenerational': mg_percentage,
        'Other': other_percentage, 
        'Year': year
    })

    multigen_percentages = multigen_percentages.round(decimals = 4)

    fig = px.scatter(multigen_percentages, 
                x = "Year", 
                y = ["Multigenerational", "Other"],
                title = "Multigenerational Households in " + state,
                trendline = "ols", # ordinary least squares regression trendline
                width = 800,
                height = 600)
    write_html(fig, "templates/multigen.html")

def make_children_table(state):
    children = get_tables(['B09002_001E','B09002_002E', 'B09002_009E','B09002_015E'], 
                          ['Total','In Married-couple Households','In Single Male Households', 'In Single Female Households'], 
                          [2009, 2014, 2019])

    children = children[children["State"]==state]

    fig = px.scatter(children, 
                    x = "Year", 
                    y = ["Total", "In Married-couple Households", "In Single Male Households", "In Single Female Households"],
                    title = "Own Children Under 18 in CA",
                    trendline = "ols", # ordinary least squares regression trendline
                    width = 800,
                    height = 600)
    write_html(fig, "templates/children.html")


    


#Establish view page
@app.route("/view")
def view():
    make_marriage_table("California")
    return render_template('marriage.html')



#Establish find page
@app.route("/find", methods=['POST', 'GET'])
def find():
    if request.method == 'GET' :
        #Open the page and include available years
        session['all_years'] = list(range(2009, 2020))
        return render_template('find.html', years = session['all_years'])
    else:
        #Get inputs from the form
        searched = request.form["topic"]
        year = request.form["year"]

        #Lookup the tables
        session['names'] = see_tables(year, searched)

        #Add variable to session for use in new page
        session['searched'] = searched
        session['year'] = int(year)

        #Open next page to choose table
        return redirect(url_for('choose'))


def see_tables(year, keyword):
    #Lookup the tables matching the keyword
    tables = censusdata.search('acs5', year,'concept', keyword)

    #Get all the unique names excluding an unusually long one
    names = list(set([row[1] for row in tables[:len(tables)] if len(row[1]) < 500]))
    names.sort()
    return names

#Establish choose page
@app.route("/choose", methods=['POST', 'GET'])
def choose():
    if request.method == 'GET':
        #Prepare choose page
        empty = (len(session['names']) == 0)
        return render_template('choose.html', names = session['names'], empty = empty, searched = session['searched'], year = session['year'])
    else:
        session['name'] = request.form["name"]

        #Get the info about the selected table
        codes, variables, session['display'], session['even'] = get_code(session["searched"], session['name'], session['year'])

        #Use that to get the actual table
        table = get_tables(codes, variables, [session['year']])
        table.to_csv("table.csv") #download

        #Go to final page
        return redirect(url_for('table'))
        
        
def get_code(topic, full_name, year):
    #list of tables
    tables = censusdata.search('acs5', year,'concept', topic)
    
    #We will return the following lists
    codes = []
    variables = []

    #And make a display with unordered lists 
    display = "<ul>"
    indents = []

    #We will also make an unordered list displaying the full variable names
    even = "<ul>"
    even += "<li>State</li>" #First column is state
    
    #For each item of table variable
    for item in tables:
        #We'll check if it's the one we want
        if item[1] == full_name:
            #The code is the first element
            codes.append(item[0])
            
            #We'll remove colons and split up the variable name in to levels
            var = item[2].replace(':', '')
            parts = var.split('!!')

            #All variables have the same first two parts
            indent = len(parts)-2
            
            #If it has no further parts it's the total
            if indent == 0:
                #Set to last part (typically Total)
                variable = parts[-1]
                
            #For all other variables
            else:
                #We'll separate the levels by dashes
                variable = " - ".join(parts[2:])

            #Now we want to make a display with html tags for nesting lists
            #We'll get the previous indent
            previous = 0
            if len(indents):
                previous = indents[-1]

            #Close out any lists
            while indent < previous:
                display += "</li></ul>"
                previous = previous - 1
            
            #If we need to indent more
            if indent > previous:
                #If there are no items already, we'll start one
                if len(indents) == 0:
                    display += "<li>"

                #Make another list and add the item
                display += f"<ul><li>{parts[-1]}"

            #If we are at the same indentation level
            elif indent == previous:
                #If there are items, we'll close out the previous one
                if len(indents):
                    display += "</li>"
                #And add the next item
                display += f"<li>{parts[-1]}"
                
            #We'll add the variable as a list item to our simple display
            even += f"<li>{variable}</li>"

            #Add indent
            indents.append(indent)
            
            #In order to avoid errors when the first character is a dollar sign
            if variable[0] == "$":
                #This will make the table title print better
                variable = "\\" + variable
            variables.append(variable) 

    #If are items
    if len(indents):
        #Get the current indentation
        previous = indents[-1]

        #While it is indented
        while previous >= 0:
            #Close out lists
            display += "</li></ul>"
            previous = previous - 1
    
    even += "<li>Year</li>" #Last column is the year
    even += "</ul>" #Close the even list

    return codes, variables, display, even

@app.route('/table')
def table():
    #Will show structure of the table
    return render_template('table.html', display = session['display'], even = session['even'], name = session['name'])

@app.route('/getCSV/<file_name>')
def getCSV(file_name):
    #Will allow user to click on link to download csv
    return send_file(file_name,
                     mimetype='text/csv',
                     attachment_filename=file_name,
                     as_attachment=True)

@app.route("/choropleths", methods=['POST', 'GET'])
def choose_choropleth():
    if request.method == 'GET' :
        choropleth_options = ['Median Age of Marriage (Male)', 'Median Age of Marriage (Female)',
                   'Percentage of Married-Couple Households',
                   'Percentage of Population Divorced in Last Year', 'Percentage of Population Never Married',
                   'Percentage of Population in Multigenerational Households',
                   'Percentage of Children in Married-Couple Households','Percentage of Children in Single-Male Households', 'Percentage of Children in Single-Female Households']
        return render_template("choropleths.html", choropleth_options = choropleth_options)
    else:
        chosen_choropleth = request.form["choropleth_options"]
        if (chosen_choropleth == 'Median Age of Marriage (Male)'):
            return render_template("median_age_male_choro.html")
        elif (chosen_choropleth == 'Median Age of Marriage (Female)'):
            return render_template("median_age_female_choro.html")
        elif (chosen_choropleth == 'Percentage of Married-Couple Households'):
            return render_template("married_couple_choro.html")
        elif (chosen_choropleth == 'Percentage of Population Divorced in Last Year'):
            return render_template("divorces_choro.html")
        elif (chosen_choropleth == 'Percentage of Population Never Married'):
            return render_template("never_married_choro.html")
        elif (chosen_choropleth == 'Percentage of Population in Multigenerational Households'):
            return render_template("multigen_choro.html")
        elif (chosen_choropleth == 'Percentage of Children in Married-Couple Households'):
            return render_template("married_household_children_choro.html")
        elif (chosen_choropleth == 'Percentage of Children in Single-Male Households'):
            return render_template("male_household_children_choro.html")
        elif (chosen_choropleth == 'Percentage of Children in Single-Female Households'):
            return render_template("female_household_children_choro.html")
        
        
        
@app.route('/other')
def other():
    #Get the grouping variables
    g = other_years(session["searched"], session["name"])
    return render_template('other.html', groups = g)

def format_years(years):
    #If there is only one year, no and is required
    if len(years) == 1:
        return str(years[0])
    
    #If there are two years, there's no oxford comma
    elif len(years) == 2:
        return str(years[0]) + " and " + str(years[1])

    #Otherwise we'll add each year followed by a comma until the last 
    text = ""
    for i in range(len(years) - 1):
        text += str(years[i]) + ", "
    
    #When we include the and
    return text + "and " + str(years[-1])

def other_years(topic, full_name):
    #Stores the tuples of all years that have the table
    valid = []
    
    #Look in all years and gather info
    for y in session['all_years']:
        tup = get_code(topic, full_name, y)
        
        #If the table is present, add it to valid with year
        if tup[0] != []:
            valid.append((tup, y))
    
    #Group the tables that are identical
    an_iterator = itertools.groupby(valid, lambda x:x[0])

    #Stores each group
    groups = []

    #For each group
    for key, group in an_iterator:
        #Get the years include it
        years = [g[1] for g in list(group)]

        table = get_tables(key[0], key[1], years)
        num = len(groups) + 1
        file_name = "table_g" + str(num) + ".csv"
        table.to_csv(file_name) #download
        
        #Add the display and nicely formatted years
        groups.append([key[2], format_years(years), num, file_name])
    return groups