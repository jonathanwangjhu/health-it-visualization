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

At the top of the GitHub project, add a website link to your final work so people can access it directly from the CS.601.265 GitHub page.

## Design details

### Storyboard

The original storyboard design, as shown below, includes the usage of a drop down menu in order to select Insurance or Race as the group to graph on the X-axis. However, we had difficuly implementing this. Consequently, we included the drop down menu as an option to visualize what our intended design should have been. The actual functaionality is in an html table that lets the user select the desired group to graph. 

![](StoryboardUpdate.jpeg?raw=true)

### Database and data description

The data that we are primarily interested in is as follows: race, insurance, and length of stay in ICU. We think that these features may affect the length will play an important factor in the treamtnet of these peopel during their stay at ICU and therefore most likley how long they stay. Since these two factors are accounted for by almost every physician the data will be very useful. and mostly complete. The data is mainly categorical and we mainly want to see the distributions between different races and insurances in order to compare differnt types of treatments due to socioeconomic backgrounds. 

### MIMIC-III Query

SELECT p.subject_id, p.insurance, p.ethnicity, p.language, p.marital_status,  ROUND((cast(p.dischtime as  date) - cast(p.admittime as data)),2) AS length_of_stay
FROM admissions p

### Database setup description 


### Learning algorithm description

Include:
* 2-4 sentences describing the learning algorithm.

### Interaction

The webapp will show a screen with a graph, with a few buttons on the top. The buttons will allow the user to choose different features to be plotted against the length of stay at the hospital. This way, they can gain insight to the expected length of stay for different features, such as gender, race, or age-range. Ideally, we will try to replace the buttons on top with the drop down menu option we have on our deployed app at the moment. 

## Development Process
  
Elif Bilgin: Set up visualization graph, deployment

David Francisco: Set up visualization graph, drop down menu option, deployment

Ben Karyo: Storyboarding, SQL queries

Jonathan Wang: Storyboarding, SQL queries, deployment

We spent around 4-5 days developing our app, as we didn't have a lot of experience with Flask and HTML. So a large portion of our time went into educating ourselves with the tech we were using, as well as creating the storyboard. The aspect that took the most time was understanding how the python scripts and the HTML scripts interacted with each other, to build on the initial example project provided. We were able to get our visualization working locally, but once we tried to deploy, the actual image of the plot itself wouldn't show up. We suspect this being due to pythonanywhere not liking relative pathnames, but we couldn't come up with a solution to be able to dynamically generate filenames and serve them live. Our code builds on the code provided by Prof. Taylor and Prof. Shpitser. 

  
## Data Source Acknowledgement

For your assignment, include:
* MIMIC-III, a freely accessible critical care database. Johnson AEW, Pollard TJ, Shen L, Lehman L, Feng M, Ghassemi M, Moody B, Szolovits P, Celi LA, and Mark RG. Scientific Data (2016). DOI: 10.1038/sdata.2016.35. Available at: http://www.nature.com/articles/sdata201635

Include copyright (as written below):

©2019 THE JOHNS HOPKINS UNIVERSITY, ALL RIGHTS RESERVED. BALTIMORE, MARYLAND.
