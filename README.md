# Python-Project

## Description
In this project i will use a Board Game database coming from BoardGameGeek, a website specialized in board game with an inner ranking. The aim of this project is to create a new rating based on the user preferences.

To achive this objective i need to understan how a Board Game Ranking works, so the forst part of the project is an analysis of what leads the site to the current ranking.

In the second part I will chop the dataset based on user preferences and the create a new personalized ranking 

## Project Structure

```
Python-Project/
├── Data/
│   └── BGG_Data_set.xlsx
├── Librarian/
│   ├── __init__.py
│   ├── app.py
│   ├── core.py
│   └── models.py
├── Presentation/
│   └── Project_analysis.ipynb
├── project_ideas.txt
└── requirements.txt
```

## Installation 
1-Clone the repository 

2-create and activate a virtual enviroment 

3-Install the requirment dependecies 

4-Copy the data set from https://drive.google.com/drive/folders/1NKABXxXy4N6OeeoYjzAIpOB3tX2PwZcA?usp=drive_link and paste in in the Data folder 

## Usage
You need to use Project_analysis.ipynb to look at the project in its entirety but if you want to look only at some parts in the Librarian folder there are specific .py files dedicated to specific parts of the project 

There is also the streamlit web application to enjoy this analysis from a different point of view 

to run the web application write "streamlit run app.py" in the terminal 

In this web application you can enjoy your new sorted dataset and see how many each value is influencing the bayesian mean 

## Requirments 
Python 3.13.9

pandas==2.3.3

numpy==2.3.4

matplotlib==3.10.7

seaborn==0.13.2

openpyxl==3.1.5

streamlit




