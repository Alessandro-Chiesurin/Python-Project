
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from models import choose_option
import tkinter as tk
from tkinter import ttk, messagebox
import os                         
   #per lavorare sui percorsi di file 
base_path = os.path.dirname(__file__) 
#__file__ it's a special variable that contains the current script path 
#os.path.dirname takes only the folder without the file name 

file_path = os.path.join(base_path, "../data/BGG_Data_Set.xlsx") 
#os.path.join command to join different paths 

data = pd.read_excel(file_path)
#read the excel file and upload in a dataframe 

print(data.head())

print(data.columns)

#data cleaning 
#eliminating usless collcolumns for the analysis 
C_data = data.drop(columns=["Owned Users"])
C_data = C_data.drop(columns=["Mechanics"])
C_data = C_data.drop(columns=["Domains"]) #i saw this colum misses a lot of data
#dropping rows with missing values
C_data = C_data.dropna()  
#dropping wrong values 
C_data = C_data[C_data["Min Players"] > 0] 
C_data = C_data[C_data["Year Published"] > 0] 
C_data = C_data[C_data["Max Players"] > 0]
C_data = C_data[(C_data["Play Time"] > 0) & (C_data["Play Time"] < 10000)]
C_data = C_data[(C_data["Min Age"] > 0) & (C_data["Min Age"] < 99)]
C_data = C_data[C_data["Users Rated"] > 0]
C_data = C_data[(C_data["Rating Average"] > 0) & (C_data["Rating Average"] < 10)]
C_data = C_data[(C_data["Complexity Average"] > 0) & (C_data["Complexity Average"] <= 5)] #in BGG complexity sacles 1-5

C_data

#--ANALYSIS PART--
correlation = C_data["BGG Rank"].corr(C_data["Complexity Average"])
print(f"Rank-Complexity correlation: {correlation:.2f}") #,2f=float con due cifre decimali

correlation = C_data["BGG Rank"].corr(C_data["Users Rated"])
print(f"Rank-Users rated correlation: {correlation:.2f}")

correlation = C_data["BGG Rank"].corr(C_data["Play Time"])
print(f"Rank-Playtime correlation: {correlation:.2f}") 
correlation = C_data["BGG Rank"].corr(C_data["Year Published"])
print(f"Rank-year of pubblication correlation: {correlation:.2f}")

correlation = C_data["BGG Rank"].corr(C_data["Max Players"])
print(f"Rank-Max players correlation: {correlation:.2f}")

correlation = C_data["BGG Rank"].corr(C_data["Min Players"])
print(f"Rank-Min players correlation: {correlation:.2f}") 

correlation = C_data["BGG Rank"].corr(C_data["Rating Average"])
print(f"Rank-Rating correlation: {correlation:.2f}") 
# solo una leggera correlazione tra difficoltà e rating, quella con users rated e rating sono ovvie


plt.figure(figsize=(8, 6))

plt.scatter(
    C_data["Rating Average"],
    C_data["Complexity Average"],
    alpha=0.7,
    s=10,   # point dimension     
)

plt.title("Rating vs Complexity", fontsize=16, pad=15)
plt.xlabel("Rating Average", fontsize=12)
plt.ylabel("Complexity Average", fontsize=12)


plt.grid(  #graphic grid  
    True,
    linestyle='--',
    alpha=0.4
)

plt.style.use("seaborn-v0_8-whitegrid") #applaying a cleaner style 

plt.tight_layout()
plt.show()

#2
plt.figure(figsize=(8, 6))

plt.scatter(
    C_data["Rating Average"],
    C_data["BGG Rank"],
    alpha=0.7,
    s=10,               
)

plt.title("Rating vs Rank", fontsize=16, pad=15)
plt.xlabel("Rating Average", fontsize=12)
plt.ylabel("Rank", fontsize=12)

plt.gca().invert_yaxis()  

plt.grid(
    True,
    linestyle='--',
    alpha=0.4
)

plt.style.use("seaborn-v0_8-whitegrid")

plt.tight_layout()
plt.show()



#User choice 
#we want to have a userbased ranking with the following parameters:
#-year published 
#-Min players 
#-Max Players
#-complexity 

#asking for variables 

years=["after 1980","after 1990","after 2000", "after 2010","every Year"]
chosen_year=choose_option(years)
min_players=["at least 1 min player","at least 2 min players","at least 3 min players",
             "at least 4 min players","any min players"]
chosen_min_players=choose_option(min_players)
max_players=["1 max player","2 max players","3 max players","4 max players","5 max players",
             "6 max players","7 max players","8 max players","9 max players","10 max players",
             "any max players"]
chosen_max_players=choose_option(max_players)
complexity=["easy", "medium","hard", "every difficulty"]
chosen_complexity=choose_option(complexity)

if chosen_year == "after 1980":
   C_data=C_data[C_data["Year Published"]>= 1980]
elif chosen_year == "after 1990":
   C_data=C_data[C_data["Year Published"]>= 1990]
elif chosen_year == "after 2000":
   C_data=C_data[C_data["Year Published"]>= 2000]
elif chosen_year == "after 2010":
   C_data=C_data[C_data["Year Published"]>= 2010]
elif chosen_year == "every year":
   pass 

if chosen_min_players == "at least 1 min player":
   C_data=C_data[C_data["Min Players"]>= 1]
elif chosen_min_players == "at least 2 min players":
   C_data=C_data[C_data["Min Players"]>= 2]
elif chosen_min_players == "at least 3 min players":
   C_data=C_data[C_data["Min Players"]>= 3]
elif chosen_min_players == "at least 4 min players":
   C_data=C_data[C_data["Min Players"]>= 4]
elif chosen_min_players == "any min players":
    pass

if chosen_max_players == "1 max player":
   C_data=C_data[C_data["Max Players"]<= 1]
elif chosen_max_players == "2 max players":
   C_data=C_data[C_data["Max Players"]<= 2]
elif chosen_max_players == "3 max players":
   C_data=C_data[C_data["Max Players"]<= 3]
elif chosen_max_players == "4 max players":
   C_data=C_data[C_data["Max Players"]<= 4]
elif chosen_max_players == "5 max players":
   C_data=C_data[C_data["Max Players"]<= 5]
elif chosen_max_players == "6 max players":
   C_data=C_data[C_data["Max Players"]<= 6]
elif chosen_max_players == "7 max players":
   C_data=C_data[C_data["Max Players"]<= 7]
elif chosen_max_players == "8 max players":
   C_data=C_data[C_data["Max Players"]<= 8]
elif chosen_max_players == "9 max players":
   C_data=C_data[C_data["Max Players"]<= 9]
elif chosen_max_players == "10 max players":
   C_data=C_data[C_data["Max Players"]<= 10]
elif chosen_max_players == "any max players":
    pass

if chosen_complexity == "easy":
   C_data=C_data[C_data["Complexity Average"] < 2]
elif chosen_complexity == "medium":
   C_data=C_data[(C_data["Complexity Average"] > 1.75) & (C_data["Complexity Average"] < 3.50)]
elif chosen_complexity == "hard":
   C_data=C_data[C_data["Complexity Average"] > 3.25]
elif chosen_complexity == "every difficulty":
    pass

#Bayesian mean of the chopped dataset 

#C parameter in bayesian mean 
C = C_data["Rating Average"].mean()

#m parameter in bayesian mean 
m = C_data["Users Rated"].quantile(0.50)

# 3. Calcola la media bayesiana per ogni gioco
C_data["Bayes Rating"] = (
    (C_data["Users Rated"] / (C_data["Users Rated"] + m)) * C_data["Rating Average"] +
    (m / (C_data["Users Rated"] + m)) * C
)

#New order
C_data_sorted = C_data.sort_values(by="Bayes Rating", ascending=False)

print(C_data_sorted.head)

