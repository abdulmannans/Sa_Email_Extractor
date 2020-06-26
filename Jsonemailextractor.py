#Author: SAM[Siddiquei Abdul Mannan]
import json

#create new directory
#copy all the json files there
#copy this file in the Directory
#select all files and rename it as 1
#all the files will be like:-
''' 1 (1).json
    1 (2).json
    1 (3).json  And so on
    1 (x).json'''


Total= 54 #number of sa you created

for x in range(1 ,Total+1):
    with open('1 ('+str(x)+').json') as f:
        data = json.load(f)
        email=data['client_email']
        sa = open("Emails.csv","a")
        sa.write(email+"\n")
        sa.close()
print('Done')


#if you Don't Get The Output Follow Steps Carefully
    

        
