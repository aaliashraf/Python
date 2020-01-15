import csv
import pandas as pd
import numpy as np
import math
distance=[]
initial=0
movie=(285)
with open('links.csv','r') as csvfile:
    reader=csv.reader(csvfile)
    for coloum in reader:
        initial=initial+1
        if(initial>1):
            fasla=pow((int(row[0])-int(movie[0])),2)+pow((int(row[1])-int(movie[1])),2)
            edistance=math.sqrt(fasla)
            distance.append((edistance,row[0]))
distance.sort()
print(distance)
print("smallest:",min(distance))

        
