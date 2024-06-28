import pandas
data= pandas.read_csv("./DAY-25/SQUIRREL_COUNT/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count=len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count=len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels_count=len(data[data["Primary Fur Color"] == "Cinnamon"])
# print(grey_squirrels_count) 
# print(black_squirrels_count)  
# print(cinnamon_squirrels_count)   
data_dic= { "Fur Color": ["Gray","Black","Cinnamon"],
"Count": [grey_squirrels_count,black_squirrels_count,cinnamon_squirrels_count]}

df=pandas.DataFrame(data_dic)
df.to_csv("./DAY-25/SQUIRREL_COUNT/Squirrel_count.csv")