# Final-Group-Project - CS.601.265 (Spring 2019) 

## Team Members

1. Elif Bilgin (elifbilgin97)
2. David Francisco (dfrancisco1998)
3. Ben Karyo (bk3015)
4. Jonathan Wang (jonathanwangjhu)

## The demographics of length of stay 

Description of Interactive Chart: 

As a group concerned about the distribution and equity found in the healthcare system, we want to be able to see how insurance (the econmic strata) and race (the socical strata) affect how long a person stays in the ICU in order to make those people's experience better to ideally improve healthcare to contain no socioeconmic discrimination. With the box plots based upon length of stay and race and insurance we will be able to get a glimpse in the discrimination within our healthcare system. 

## Access and Running Instructions

Our Github is located [here](https://github.com/health-IT-apps-spring2019/hw5-jwang246-bk3015-dfrancisco-elifbilgin97).

The deployed visualization is [here](http://jonathanwangjhu.pythonanywhere.com/).

To run locally, clone our repo, and change the filepaths to TABLE_LOS.csv in compute.py to the full filepath on your machine. Then, run controller.py.

Login information for example app:
* Username: hw5example
* Password: testtest

At the top of the GitHub project, replace the one-line description (i.e., replace "final-xxxx created by GitHub Classroom")


## Design details

### Storyboard

The original storyboard design, as shown below, includes the usage of a drop down menu in order to select Insurance or Race as the group to graph on the X-axis. However, we had difficuly implementing this. Consequently, we included the drop down menu as an option to visualize what our intended design should have been. The actual functaionality is in an html table that lets the user select the desired group to graph. 

![](NewStoryboard.jpeg?raw=true)

### Database and data description

The data that we are primarily interested in is as follows: race, insurance, and length of stay in ICU. We think that these features may affect the length will play an important factor in the treamtnet of these peopel during their stay at ICU and therefore most likley how long they stay. Since these two factors are accounted for by almost every physician the data will be very useful. and mostly complete. The data is mainly categorical and we mainly want to see the distributions between different races and insurances in order to compare differnt types of treatments due to socioeconomic backgrounds. 

### MIMIC-III Query

CREATE TABLE patients (<br/>
    &nbsp;&nbsp;PATIENT_ID INT,<br/>
    &nbsp;&nbsp;INSURANCE VARCHAR(255),<br/>
    &nbsp;&nbsp;RACE VARCHAR(255),<br/>
    &nbsp;&nbsp;LANGUAGE VARCHAR(255),<br/>
    &nbsp;&nbsp;MARITAL VARCHAR(255),<br/>
    &nbsp;&nbsp;LOS INT,<br/>
    &nbsp;&nbsp;PRIMARY KEY (PATIENT_ID)<br/>
);<br/>

LOAD DATA LOCAL INFILE '/home/bk3015/TABLE_LOS.csv'<br/>
INTO TABLE patients<br/>
FIELDS TERMINATED BY ','<br/>
LINES TERMINATED BY '\n'<br/>
IGNORE 1 ROWS<br/>
(PATIENT_ID, INSURANCE, RACE, LANGUAGE, MARITAL, LOS);<br/>


### Database setup description 
We access the database and perform the above queries using the following code:

import mysql.connector

mydb = mysql.connector.connect(
  host='bk3015.mysql.pythonanywhere-services.com',
  user='bk3015',
  passwd='los12345',
  database='bk3015$los'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM patients")

myresult = mycursor.fetchall()


### Learning algorithm description

We are using linear regression to predict the length of stay in a hospital. The features we have selected for this prediction problem are Race, Insurance, Marital Status and Language. 

### Interaction

The webapp will show a screen with a graph, with a few buttons on the top. The buttons will allow the user to choose different features to be plotted against the length of stay at the hospital. This way, they can gain insight to the expected length of stay for different features, such as gender, race, or age-range. Ideally, we will try to replace the buttons on top with the drop down menu option we have on our deployed app at the moment. 

## Development Process
  
Our code builds on the code on bokeh github visualization example--crossfilter. 

  
## Data Source Acknowledgement

For your assignment, include:
* MIMIC-III, a freely accessible critical care database. Johnson AEW, Pollard TJ, Shen L, Lehman L, Feng M, Ghassemi M, Moody B, Szolovits P, Celi LA, and Mark RG. Scientific Data (2016). DOI: 10.1038/sdata.2016.35. Available at: http://www.nature.com/articles/sdata201635

Include copyright (as written below):

©2019 THE JOHNS HOPKINS UNIVERSITY, ALL RIGHTS RESERVED. BALTIMORE, MARYLAND.
