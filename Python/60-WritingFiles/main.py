import json
import csv

employees={
    "name":"Spongebob",
    "age":30,
    "job":"cook"
}

employee=[["Name","Age","Job"],
          ["Spongebob",30,"Cook"],
          ["Patrick",37,"Unemployed"],
          ["Sandy",40,"Manager"]]

txt_data="I like pizza!"

file_path="Python/60-WritingFiles/output.csv"
try:
    with open(file_path,"w",newline="") as file:
        #json.dump(employees,file,indent=4)
        writer=csv.writer(file)
        for row in employee:
            writer.writerow(row)
        print(f"Csv file {file_path} was created")
except FileExistsError:
    print("That file already exists")