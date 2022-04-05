import csv
import os
import matplotlib.pyplot as plt

cwd = os.getcwd()
os.chdir(cwd + '\\Csv')
cwd = os.getcwd()
# Check if there is Csv File
listDir = os.listdir()

#Scelta Anno
year = input('Choose Year: ')

thereis = False
#Check if the Folder exist
for j in range(0, len(listDir), 1):
    if((cwd + '\\' + listDir[j]) == (cwd + "\\" + str(year) + ".csv")):
        thereis = True

if(thereis == False):
    print("File Csv not exist")
elif(thereis == True):
    file = open(cwd + "\\" + str(year) + ".csv")

    csvreader = csv.reader(file)

    header = []
    header = next(csvreader)

    rows = []
    for row in csvreader:
        rows.append(row)

    file.close()

    # x axis values
    x = []
    # corresponding y axis values
    y = []

    for i in range(0, len(rows), 1):
        x.append(rows[i][0])
        y.append(float(rows[i][1]))

    sorted(y)

    plt.figure('Grafico Anno Bitcoin da Csv')
    
    # plotting the points
    plt.plot(x, y)
    
    # naming the x axis
    plt.xlabel('Data')
    # naming the y axis
    plt.ylabel('Valore in Euro')
    
    # giving a title to my graph
    plt.title('Grafico')
    
    # function to show the plot
    plt.show()