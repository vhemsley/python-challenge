#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Pybank

# Dependencies
import csv
import os 

#Loading Files and Output Data
loading_file = os.path.join("budget_data.csv")
file_to_output = os.path.join("budget_thorough_analysis")

#Financial Data Parameters
Number_Of_Months = 0
Number_Of_Months_of_Change = []
Net_Change_List = []
The_Greatest_Increase_In_Profits = ["", 0]
The_Greatest_Decrease_In_Losses = ["", 99999]
The_Total_Net = 0

# Read CSV and Convert it into List Dictionaries 
with open(loading_file) as financial_data: 
    reader = csv.reader(financial_data)
    
    #Read Title Row 
    
    Title_Row = next(reader)
    
    #Remove First Row to Avoid Irrevelant Calculation to Net_Change_List
    
    First_Row = next(reader)
    The_Total_Net = The_Total_Net + int(First_Row[1])
    The_Previous_Net = int(First_Row[1])
    print(The_Total_Net)
    print(The_Previous_Net)
    
    #Looping Through Data
    for ROW in reader:
        
        #Tracking Total
        Number_Of_Months = Number_Of_Months + 1 
        The_Total_Net = The_Total_Net + int(ROW[1])
        print(The_Total_Net)
        
        #Tracking New Change
        The_Net_Change = int(ROW[1]) - The_Previous_Net 
        The_Previous_Net = int(ROW[1])
        Net_Change_List = Net_Change_List + [The_Net_Change]
        Number_Of_Months_of_Change = Number_Of_Months_of_Change + [ROW[0]]
        
        if The_Net_Change > The_Greatest_Increase_In_Profits[1]:
            The_Greatest_Increase_In_Profits[0] = ROW[0]
            The_Greatest_Increase_In_Profits[1] = The_Net_Change
            
        if The_Net_Change < The_Greatest_Decrease_In_Losses[1]:
            The_Greatest_Decrease_In_Losses[0] = ROW[0]
            The_Greatest_Decrease_In_Losses[1] = The_Net_Change
            
    #Calculate the Average Net Change
    The_Net_Monthly_Average = sum(Net_Change_List) / len(Net_Change_List)
        
Output = (
    
    f"\nFinancial Thorough Analysis\n"
    f"===============================\n"
    f"Number Of Months: {Number_Of_Months}\n"
    f"Total: ${The_Total_Net}\n"
    f"Average Change: ${The_Net_Monthly_Average:.2f}\n"
    f"The Greatest Increase In Profits {The_Greatest_Increase_In_Profits[0]}, (${The_Greatest_Increase_In_Profits[1]})\n"
    f"The Greatest Decrease In Profits {The_Greatest_Decrease_In_Losses[0]}, (${The_Greatest_Decrease_In_Losses[1]})\n"

)

print(Output)

with open(file_to_output, "w") as txt_file: 
    txt_file.write(Output)


# In[ ]:





# In[ ]:




