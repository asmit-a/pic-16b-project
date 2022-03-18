# U. S. Census Project

by Eva Mars and Asmita Majumder

In our project, we aimed to explore how family structures have been changing in the U.S. over time, and to display this data in a webapp that a casual user could easily navigate and understand.

All files relevant to this project can be found at [this Github respository](https://github.com/asmit-a/pic-16b-project). 


## Accessing the Web App

*Downloading censusdata (pip install?) and flask? ADD THAT IN*

First, download the folder titled "Webapp" from the Github repository linked above. Open up your Command Prompt window and navigate into the Webapp folder that should now be present on your local machine. In your Command Prompt, type `export FLASK_ENV=development` (replace `export` with `set` if you are on a Windows device), and then type `flask run`. This should provide you with a URL that will take you to a version of the web app that is now being run locally on your machine. Copy-paste this URL into a web browser.

## How It Works

Our webapp has three main pages: *I FORGOT THE NAMES FILL THIS IN*. 

### **PAGE ONE TITLE WHOSE NAME I FORGOT**

This page is simple, displaying a `Plotly` graph that shows how the median age of first marriage in California has changed over time. This page offers little functionality beyond the user being able to interact with the plot, and is primarily present for purpose of showing users what kinds of _isualizations the user can expect from our next page.

### Request A Visualization

This page allows the user to see how different aspects of family structure in certain states has changed over time. The user is first asked to select a table whose data they would like to ac_ess, as well as a state. Upon clicking the "Submit" button, they will then be redirected to a `Plotly` plot that displays how data from their chosen data has changed over the previous years. 

### Download Tables

This page allows the user to sear_h for tables of interest and then download them as CSV files. First, the user is prompted to search for a topic of interest. Possible topics include "household", "marriage", and "di_orce". They are then presented with a list of possible tables that concern their topic of interest. Upon choosing one of these tables, the user is taken to a page that contains a link they can press in order to download the relevant data and outlines the way this data is organized in their downloaded table. 



