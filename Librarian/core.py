
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import models
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

#TABELLE VD MEGLIO POI
plt.scatter(C_data["Rating Average"], C_data["BGG Rank"], alpha=0.6)
plt.title("Rank vs Rating Average")
plt.xlabel("Rating Avrage")
plt.ylabel("Rank (Lower = better)")
plt.gca().invert_yaxis()  #to show better ranks in the top part 
plt.grid(True, linestyle='--', alpha=0.5) #aggiunge la griglia al grafico 
plt.show()


plt.scatter(C_data["Rating Average"], C_data["BGG Rank"], alpha=0.6)
plt.title("Rank vs Rating Average")
plt.xlabel("Rating Avrage")
plt.ylabel("Rank (Lower = better)")
plt.gca().invert_yaxis()  #to show better ranks in the top part 
plt.grid(True, linestyle='--', alpha=0.5) #aggiunge la griglia al grafico 
plt.show()

#User choice 


