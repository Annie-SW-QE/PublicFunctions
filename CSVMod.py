#This will be a function that takes a csv file, splits a column, renames those columns and rejoins the dataframes together
import pandas as pd
import csv

def csvmod(file,sep,col_to_split,split_delim,labels):
    file_to_change= pd.read_csv(file,sep=sep,header=0)
    split_cols = file_to_change[col_to_split].str.split(split_delim,expand=True)
    file_drop = file_to_change.drop([col_to_split],axis=1)
    new_file = split_cols.set_axis(labels, axis='columns')
    altered_df = file_drop.join(new_file)
   
    return altered_df