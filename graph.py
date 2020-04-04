import numpy as np
import time
import pandas as pd
import os
import matplotlib.pyplot as plt
import csv
import argparse

f = open('./covid-19/data/countries-aggregated.csv','r')
try:
  os.system("rm ./main/*")
except:
  pass
parser = argparse.ArgumentParser()
parser.add_argument('-c','--countries', nargs='+', help='<Required> Set flag', required=True)
parser.add_argument('-d', '--days', help='How many days from D0', default = '')
parser.add_argument('-D', '--DPI', help='Output DPI', default = '320')
parser.add_argument('-o', '--output', help='Output to save PNG', default = './png')
parser.add_argument('-t', '--type_col', help='Type of case: confirmed, recovered, deaths', default = 'confirmed')
parser.add_argument('-v', '--view', help='View result: yes(y) or no(n)', default = 'no')
parser.add_argument('-diff', '--diff', help='difference between days', default = 'no')
args = parser.parse_args()
countries = args.countries
col = args.type_col
days = args.days
view = args.view
dpi_v = args.DPI
out = args.output
diff = args.diff
type_col = {
  "confirmed": "2",
  "recovered": "3",
  "deaths": "4",
  "Confirmed": "2",
  "Recovered": "3",
  "Deaths": "4"
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
symbols = ['<', '>', '.', 's', '*', 'p', 'D', 'v']
name=[]
for i in countries:
  size = countries.index(i)
  data = csv.reader(open('./main/%s.csv' %(i), 'r'), delimiter=",", quotechar='|')
  column1 = []
  column2 = []
  for row in data:
    if row[2] != '0':
      column1.append(int(row[int(num)]))
      if len(column1) > 1: 
        column2.append(column1[len(column1)-1] - column1[len(column1)-2])
  if days == '':
    if diff == 'y' or diff == 'yes':
      x = range(len(column2[:]))
      y = column2[:] 
    else:
      x = range(len(column1[:]))
      y = column1[:] 
  
  else:
    # x-axis values 
    if diff == 'y' or diff == 'yes':
      x = range(len(column2[:int(days)]))
      y = column2[:int(days)]
    else:
      x = range(len(column1[:int(days)]))
      y = column1[:int(days)]
    # y-axis values 
    
  # plotting points as a scatter plot 
  if diff == 'y' or diff == 'yes':
    plt.plot(x, y, label= i, color= point[count], marker= symbols[count])
  else:
    plt.scatter(x, y, label= i, color= point[count], marker= symbols[count], s=55 - (size*6)) 
  count = count + 1

# x-axis label 
plt.xlabel('x - Days from D0') 
# frequency label 
plt.ylabel('y - %s cases' %(col)) 
# plot title 
if diff == 'y' or diff == 'yes':
  plt.title('Daily cases from D0 vs Diff of number of %s cases' %(col)) 
else:
  plt.title('Daily cases from D0 vs Total of %s cases' %(col)) 
# showing legend 
plt.legend()
name = "" 
for i in countries:
  name = str(i) + "_" + name
name = name + str(col)
if diff == 'y' or diff == 'yes':
  plt.savefig('%s/%s_diff.png' %(out,name), dpi=int(dpi_v))
else:
  plt.savefig('%s/%s.png' %(out,name), dpi=int(dpi_v))

if view == 'y' or view == 'yes': 
  # function to show the plot 
  plt.show() 
