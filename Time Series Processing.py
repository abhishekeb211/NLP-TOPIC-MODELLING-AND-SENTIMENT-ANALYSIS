import pandas as Pd
import numpy as Np
import simplejson

d=Pd.read_csv("DATASET.csv", error_bad_lines=False)
DATASET=d.copy()
# print(DATASET.columns)
# print(DATASET.shape)
# print(DATASET.iloc[0,5])
# print(DATASET.iloc[0,7])

 DATES3=['2018-03-01 00:00','2018-03-04 00:00','2018-03-11 00:00','2018-03-18 00:00','2018-03-25 00:00','2018-03-31 00:00']   
# DATES4=['2018-04-01 00:00','2018-04-08 00:00','2018-04-15 00:00','2018-04-22 00:00','2018-04-29 00:00','2018-04-31 00:00']   
# DATES5=['2018-05-01 00:00','2018-05-06 00:00','2018-05-13 00:00','2018-05-20 00:00','2018-05-27 00:00','2018-05-31 00:00']   
# DATES6=['2018-06-01 00:00','2018-06-03 00:00','2018-06-10 00:00','2018-06-17 00:00','2018-06-24 00:00','2018-06-31 00:00']   
# DATES7=['2018-07-01 00:00','2018-07-08 00:00','2018-07-15 00:00','2018-07-22 00:00','2018-07-29 00:00','2018-07-31 00:00']   
# DATES8=['2018-08-01 00:00','2018-08-02 00:00'] 

fb=[]
for i in range(0,3758571):#375871 rows print(DATASET.shape) 
#     print(DATASET.iloc[i,5])
    if (DATASET.iloc[i,5])<=DATES3[1]:
        
#         print(DATASETS.iloc[i,5])
        
            if (DATASET.iloc[i,5])>DATES3[0]:
                print(DATASET.iloc[i,5])
                print(i)
                fb.append(DATASET.iloc[i,7])
                
f = open('3_1_WEEK.txt', 'w')
simplejson.dump(fb, f)
f.close()        
