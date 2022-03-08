# Aca-coder's Project

by Eva Mars and Asmita Majumder

## Pre-submission Notes

### What We Have So Far

A lot of the files in our repository consists of scratch work that we used to try and figure our project out. The only real "clean" file in our main repository is the file "censusdata presentation.ipynb", which contains the Jupyter Notebook we used for our first project update presentation. This Notebook demonstrates use of the census API, and contains visualizations of trends that can be observed in certain pieces of census data over a decade or so. 

The main feature of our project is the web app, which can be found in the folder titled "Webapp". We still haven't been able to set it up online, but it can be run on locally by downloading the "Webapp" folder, changing the directory to this folder's location, and then running the usual flask commands (i.e. "set FLASK_ENV=development" followed by "flask run").

This web app contains, at the moment, three pages: 

1. Request a Visualization

This allows the user to select one of 5 tables which they wish to observe, as well as a U.S. state. Once they have made their selections and clicked "Submit", they are taken to a plot showing how the data in their chosen table has changed over time in the selected state. 

2. View California Marriage Visualization

This page simply displays a graph that shows how the median age of first marriage in CA has changed between 2009 and 2019.  

3. Request a Table to Download

This page allows users to search for a topic, look through a list of relevant tables, and then examine and download a table of their choosing.

### What We Are Working On

We plan to add some CSS to our web app and make it more visually appealing. 

We were also considering delving into modeling; we've seen some interesting trends in the data, and it would be cool to be able to translate these trends from the past into a projection for the future. However, we are not really sure how to approach this type of modeling, especially with a topic that is so complex and that we have such little data for. It's been a bit frustrating only being able to access a decade's worth of data, as this has made it harder to distinguish whether changes are part of larger trends or just flukes. 

### Questions

1. Do you have any advice regarding how we could implement a model that predicts what family structures will look like in the future, or is this too complicated of an endeavour? 

2. So far, a lot of our project consists of just looking at and organizing past data; we've had some trouble adding originality to it. Is this okay? Do you have any advice for moving past this?

3. The download feature was a late addition as we realized it could be a useful feature. Are there any changes/additions in search functionality or table structure you'd recommend? 

# Proposal

## Abstract

The nuclear family has largely come to be seen as the “typical” US family, and this assumption is reflected in legal policies and mainstream media alike. However, as divorce rates are increasing and Americans are delaying marriage (or forgoing it altogether), the era of the nuclear family may also be coming to a close. In this project, we will use census data to examine how family structures have been evolving over the past several decades. We will construct several detailed summary visualizations which will display different aspects of the data depending on user input. All of this information will be collected and displayed on a web app. 

## Planned Deliverables

Our main interface will be a web app on which we will consolidate our summaries, predictions, and visualizations. In the "partial success" scenario, our web app will contain interactive plots which will display the data from different perspectives depending on user input. In the "full success" version, there will additionally be a predictive model that projects how family structures may change in the coming years. This model will be based on the trends that we observe in the data from prior years, and will ideally also factor in additional variables that may affect peoples' family-making decisions. 

## Resources Required

The main need we have for our project is data. We plan to use census data, such as the table here: 
```
https://data.census.gov/cedsci/table?q=Household%20and%20Family&tid=ACSDP1Y2019.DP02
```

In order to access this data, we will use Census APIs via the CensusData package, details of which can be found here: 
```
https://pypi.org/project/CensusData/
```
The main feature of this package that we will use is the `censusdata.download` method, which takes in a given survey type, year, table, and region and retrieves the relevant census information in the form of a pandas dataframe. We have chosen this particular package because we found it to be the most intuitive, and because it allows us to access data as dataframes, which we have ample experience working with. 

In order to find tables of interest, we will use the following site: 
```
https://censusreporter.org/
```

Beyond that, we shouldn't need an unusual amount of computing power, based on this kind of data. If we make the webpage public, we will need to make an account on a program that does that, such as Hiroku.

## Tools and Skills Required

In order to acquire the census data, we will make use of APIs and the CensusData package, which will help us learn how to find and download packages from Github on our own. We will utilize what we have learned about pandas dataframes, as this is the format in which our data will be retrieved and the format in which we will initially analyze the data. Once we become comfortable with the data and start dealing with larger quantities of it, we will probably use databases and SQL with sqlite3 in order to sort and summarize the data. We may also use machine learning to make predictions based on the data. Then we will use the plotly packages for making interactive visualizations. Lastly, we will use flask for the web app, where we will need to figure out how to allow the user to select data to see in the visualization.

## What You Will Learn

We will learn about how to find and gather data from a website, implement machine learning on this kind of data, and use flask to integrate this with a web app. In doing so, we will learn about how to work collaboratively on a coding project through the use of git, including using version control. In creating the project and following the timeline, we will utilize the concept of minimum viable products from software developement.

## Risks

One risk is having to deal with the extremely large census datasets and deciding which parts of it are the most relevant to our project. Family structure is nuanced and dynamic, and it will be challenging to create a comprehensive representation of it. Trying to create a predictive model also poses a considerable risk, as it may be hard to find a model that fits the observed patterns. Even if we do, we will also have to consider various external factors that may influence the trends we are examining. 

## Ethics

Many current legal and societal structures operate on the assumption that the nuclear family is the norm, often at the expense of those who do not reside in such family structures. We hope that our web app will benefit such people, by bringing more awareness to how our perceptions of social norms, as well as the structures that are based on these perceptions, may be outdated. 

Unfortunately, we run the risk of perpetuating stereotypes against certain family structures. For instance, if data shows that certain types of family structures correlate to certain economic statuses, this may appear to imply the superiority of that type of family structure; however, it is crucial that we examine the nuances of any such correlations, and remember that correlation does not equal causation. 

We do nonetheless hope that the world will became an overall better place because of the existence of our web app. This is based on the assumption that increasing awareness regarding how family structures are evolving will promote the development of new legal and social systems that account for a wider variety of family structures, which in turn will help properly address peoples' needs.   

In making our predictive model, we will also have to make a number of assumptions regarding what factors may influence peoples' family-making decisions (i.e., what factors affect if/when they marry or have children). 

## Tentative Timeline

### After two weeks

We will have gathered the data and have a summary visualization in a jupyter notebook.

### After four weeks

We'll have a working web app containing summarized data and different visualizations based on user inputs.

### After six weeks

We'll have a working web app with the same summarized data and visualizations as mentioned above, as well as predictive modeling. 



