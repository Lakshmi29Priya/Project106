import csv
import numpy as np

def getData(data_path):
    temperature=[]
    icecream=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            temperature.append(float(row["Temperature"]))
            icecream.append(float(row["Ice-cream Sales"])) 
    return {"x":temperature,"y":icecream} 

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"]) 
    print("Correlation coefficient of icecream vs temperature /n",correlation[0,1]) 

def setup():
    data_path="iceCream.csv"
    dataSource=getData(data_path)
    findCorrelation(dataSource)
setup()    


