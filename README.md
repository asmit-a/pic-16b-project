# Aca-coder's Project

by Eva Mars and Asmita Majumder

## Abstract

The nuclear family has largely come to be seen as the “typical” US family, and this assumption is reflected in legal policies and mainstream media alike. However, as divorce rates are increasing and Americans are delaying marriage (or forgoing it altogether), the era of the nuclear family may also be coming to a close. In this project, we will use census data to examine how family structures have been evolving over the past several decades. We will construct several detailed summary visualizations which will display different aspects of the data depending on user input. All of this information will be collected and displayed on a web app. 

## Planned Deliverables

Our main interface will be a webapp on which we will consolidate our summaries, predictions, and visualizations. In the "partial success" scenario, our webapp will contain interactive plots which will display the data from different perspectives depending on user input. In the "full success" version, there will additionally be a predictive model that projects how family structures will change in the coming years. This model will be based on the trends we observe in the data from prior years, and will ideally also factor in additional variables that may affect peoples' family-making decisions. 

## Resources Required

The main need we have for our project is data. We planned to use census data, such as the table here:  
​​https://data.census.gov/cedsci/table?q=Household%20and%20Family&tid=ACSDP1Y2019.DP02

Beyong that, we shouldn't need an unusual amount of computing power, based on this kind of data. If we make the webpage public, we will need to make an account on a program that does that, such as Hiroku.

## Tools and Skills Required

We may need to do some web scraping to get data, for which we would use the scapy package, but we could probably find datasets elsewhere. Once we get the data, we will probably use databases and SQL with sqlite3 in order to sort and summarize the data. We may also use machine learning to make predictions based on the data. Then we will use the plotly packages for making interactive visualizations. Lastly, we will use flask for the web app, where we will need to figure out how to allow to user to select data to see in the visualization.

## What You Will Learn

We will learn about how to find and gather data from a website, implement machine learning on this kind of data, and use flask to integrate this with a web app. In doing so, we will learn about how to work collaboratively on a coding project through the use of git, including using version control. In creating the project and following the timeline, we will utilize the concept of minimum viable products from software developement.

## Risks

One risk is having to deal with the extremely large datasets available via the census and deciding which parts of it are the most relevant to our project. Family structure is nuanced and dynamic, and it will be challenging to create a comprehensive representation of it. Trying to create a predictive model also poses a considerable risk, as it may be hard to find a model that fits the observed patterns. Even if we do, we will also have to consider various outside factors that may influence the trends we are examining. 

## Ethics

## Tentative Timeline

### After two weeks

We will have gathered the data and have a summary visualization.

### After four weeks

We'll have a working web app containing summarized data and different visualizations based on user inputs 

### After six weeks

We'll have a working web app with same summarized data and visualizations as mentioned above, as well as predictive modeling 


