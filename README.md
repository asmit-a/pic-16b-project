# U. S. Census Project

by Eva Mars and Asmita Majumder

In our project, we aimed to explore how family structures have been changing in the U.S. over time, and to display this data in a webapp that a casual user could easily navigate and understand.

All files relevant to this project can be found at [this Github respository](https://github.com/asmit-a/pic-16b-project). 


## Accessing the Web App

*Downloading censusdata (pip install?) and flask? ADD THAT IN*
You may need to install a couple packages to run our site. 
You will likely need to install the censusdata package to run our site. To do so, you can run the command `python3 -m pip install censusdata` in the terminal.

To run the app, first download the github repository linked above, or just the "Webapp" folder. Open up your Command Prompt window and navigate into the Webapp folder that should now be present on your local machine. In your Command Prompt, type `export FLASK_ENV=development` (replace `export` with `set` if you are on a Windows device), and then type `flask run`. This should provide you with a URL that will take you to a version of the web app that is now being run locally on your machine. Copy-paste this URL into a web browser and you'll be able to use our site!

## How It Works

Our webapp has four pages the user can navigate directly to:

### Request a Choropleth

This page allows the use to choose from five variables in a drop down menu. Once they make their selection and submit, they will be taken to a `Plotly` choropleth plot that shows that variable in each state in a colored map.

### View California Marriage Visualization**

This page is simple, displaying a `Plotly` graph that shows how the median age of first marriage in California has changed over time. This page offers little functionality beyond the user being able to interact with the plot, and is primarily present for purpose of showing users what kinds of visualizations the user can expect from our next page.

### Request A Visualization

This page allows the user to see how different aspects of family structure in certain states has changed over time. The user is first asked to select a table whose data they would like to access, as well as a state. Upon clicking the "Submit" button, they will then be redirected to a `Plotly` plot that displays how data from their chosen data has changed over the previous years. 

### Request a Table to Download

This page allows the user to search for tables of interest and then download them as CSV files. First, the user is prompted to search for a topic of interest. Possible topics include "household", "marriage", and "divorce". They are then presented with another form containing a list of tables related to their topic of interest. Upon choosing one of these tables, the user is taken to a page that contains a link to download the table formatted into a CSV and below outlines the way the variables in the table are organized. 



