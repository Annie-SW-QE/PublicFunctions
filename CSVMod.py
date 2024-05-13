#This will be a function that takes a csv file, splits a column, renames those columns and rejoins the dataframes together

#importing pandas and csv modules
import pandas as pd
import csv
#defining the function
## What is passed to the function? 
##### file: the csv file to be read; ex. 'test_2.csv'
##### sep:the delimeter of the majority of the file as a string; ex. ',' , ' ', '/'
##### col_to_split: the name of the column in the file you want to split along a delimeter as a string; ex. 'Credentials'
##### split_delim: the delimeter of the column to be split upon; same input type as sep 
##### labels: the dataframe of new column names of the newly created columns from the split; ex. ['Category 1','Category 2',...]
######## NOTE: you must have a labels dataframe that matches the length of the newly split columns dataframe or the function, 
######## or compiler itself will throw an error


def csvmod(file,sep,col_to_split,split_delim):
    file_to_change= pd.read_csv(file,sep=sep,header=0)
    split_cols = file_to_change[col_to_split].str.split(split_delim)
    exploded_csv = split_cols.explode()
    file_drop = file_to_change.drop([col_to_split],axis=1)
    altered_df = file_drop.join(exploded_csv)
   
    return altered_df
   
    return altered_df