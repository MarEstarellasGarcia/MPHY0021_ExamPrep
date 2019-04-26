#a) Write a python function to:
#• Load this data into memory [1]
#• Reformat the data into a dictionary keyed by year, using appropriate data types, an example of the expected output is provided [5]
#• Write the dictionary to disk in JSON format

import os 
import json
import numpy as np
from matplotlib import pyplot as plt

path = "python_language_1"
file = "python_language_1_data.csv"

json_file= "python_data_json.json"
path_to_json = os.path.join(path, json_file)

def read_to_json(path, file):
    path_to_file = os.path.join(path, file)
    data = open(path_to_file)
    station = np.genfromtxt(data, delimiter=',',
                              names=['year','day','rainfall'],
                              dtype=[int, int, float])                            
    the_dict = {}
    
    for i in station[1:]:
      year,day,rain = tuple(i)
      if str(year) not in the_dict.keys():
        the_dict[str(year)] = []
    
      the_dict[str(year)].append(rain)
        
    with open('python_data_json.json', 'w') as f:
        json.dump(the_dict,f)
        




#Create a function that takes the filename of the JSON file, a year, 
#and an optional line colour as arguments and plots a timeseries of daily 
#rainfall for that year. Save a formatted plot in png format showing the data
# for 1998.
    

def plot_timeseries(json_file, year ='1998' , colour='green' ):
    with open(json_file) as rain_json_file:  
        data_rain = json.load(rain_json_file)    
     
    
    plt.plot(data_rain[year], color)
    plt.xlabel('Rainfall')
    plt.ylabel('Days')
    plt.title('Timeseries of daily rainfall')
    plt.savefig('perf_plot.png')   
    

#Write a function that takes the filename of the JSON file and produces a plot 
#showing the mean annual rainfall over a user specified time period. Save a
# formatted plot in png format showing the data from 1988 to 2000 (inclusive).
 
    
def mean_anual_rainfall(jason_file, first_year= 1988, last_year= 2000):
    with open(json_file) as rain_json_file:  
        data_rain = json.load(rain_json_file) 
    
    lista = np.arange(first_year, last_year,1)
    
    mean_rain=[]
    mean_rain_total= []
    
    for year in lista: 
        mean_rain= np.mean(data_rain[np.str(year)])
        mean_rain_total = np.append(mean_rain_total,mean_rain)
    
    
    plt.plot(mean_rain_total)
    
#        
#You discover that for the years 2005 to 2011 the rain gauge was malfunctioning.
#The published correction factor is
#rainfall_value * 1.2 ^ root(2)
#Write a function to apply this equation to a given value and two functions which apply
#this function to all of the data for a given year, returning the year's corrected results as
#a list.
#• Function 1 should solve this using a for loop
#• Function 2 should use a list comprehension [5]
#• In the docstring for one of these functions, evaluate the pros and cons for
#these two approaches to the same task.
    
def return_correct_value(value):
    return value * 1.2 ** np.sqrt(2)
   

def correct_rainfall_numbers(jason_file):
    with open(json_file) as rain_json_file:  
        data_rain = json.load(rain_json_file) 
        
    first_year= 2005
    last_year= 2011
    lista = np.arange(first_year, last_year,1)
    
    correct_numbers_list=  np.empty(((last_year-first_year), np.size(data_rain[np.str(first_year)])))

    for year in lista: 
        incorrect_numbers= np.array(data_rain[np.str(year)])
        correct_numbers= incorrect_numbers * 1.2 ** np.sqrt(2)
        correct_numbers_list = np.stack(correct_numbers, axis=0)
        #data_rain[np.str(year)] = correct_numbers
      
    return list(correct_numbers)




