# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 09:28:04 2019

@author: Muhammad Babar Kamal
"""
rows=4
cols=4
img=[[1,2],
     [3,4]]
img2=[[0 for x in range(rows)] for y in range(cols)]


ri=0;

r=0;
for i in range(rows):
   c=0; 
   ci=0;
   
   for j in range(cols):
         
        img2[i][j]=img[r][c]
        ci=ci+1
        if ci>1:
            c=c+1;
            ci=0;
                 
   ri=ri+1
   if ri>1:
       r=r+1;
       ri=0;
        




        