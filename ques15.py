import csv
f= open("C:\Users\S540\Downloads\username.csv",'r')

freader= csv.reader(f)
for row in freader:
    print(row)
    print("Data printed successfully")
    f.close()