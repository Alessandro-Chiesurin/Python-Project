
import pandas as pan
import os                         
   #per lavorare sui percorsi di file 

base_path = os.path.dirname(__file__) 
#__file__ it's a special variable that contains the current script path 
#os.path.dirname takes only the folder without the file name 

file_path = os.path.join(base_path, "../data/BGG_Data_Set.xlsx") 
#os.path.join command to join different paths 

data = pan.read_excel(file_path)
#read the excel file and upload in a dataframe 

print(data.head())





