import numpy as np
import time
import pandas as pd
import os
import matplotlib.pyplot as plt
import csv
import argparse

f = open('./covid-19/data/countries-aggregated.csv','r')

os.system('rm ./main/*')

parser = argparse.ArgumentParser()
parser.add_argument('-c','--countries', nargs='+', help='<Required> Set flag', required=True)
parser.add_argument('-t', '--type_col', help='shows output', default = 'confirmed')
parser.add_argument('-d', '--days', help='shows output', default = '')
args = parser.parse_args()
countries = args.countries
col = args.type_col
days = args.days

type_col = {
  "confirmed": "2",
  "recovered": "3",
  "deaths": "4"
}
num = type_col.get(col)
for line in f:
  for i in countries:
    if i in line:
      g= open("./main/%s.csv" %(i),"a+")
      g.write(line)
      g.close()

count = 0
point = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '#e377c2']
for i in countries:
  data = csv.reader(open('./main/%s.csv' %(i), 'r'), delimiter=",", quotechar='|')
  column1 = []
  for row in data:
      if row[2] != '0':
        column1.append(int(row[int(num)]))
  
  if days == '':
    x = range(len(column1[:]))
    y = column1[:] 
  
  else:
    # x-axis values 
    x = range(len(column1[:int(days)]))
    # y-axis values 
    y = column1[:int(days)]
    
  # plotting points as a scatter plot 
  plt.scatter(x, y, label= i, color= point[count], marker= "*", s=20) 
  count = count + 1

# x-axis label 
plt.xlabel('x - Days from D0') 
# frequency label 
plt.ylabel('y - %s cases' %(col)) 
# plot title 
plt.title('Days from the beginning vs %s cases' %(col)) 
# showing legend 
plt.legend() 
  
# function to show the plot 
plt.show() 
