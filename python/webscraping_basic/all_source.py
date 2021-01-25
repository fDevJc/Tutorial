import os

path = "./"
file_list = os.listdir(path)

file_name = "all_source.txt"

for file in file_list:
    if file.find(".py") > 0:
        with open(file_name,"a",encoding="utf8") as wf:
            with open(file,"r",encoding="utf8") as rf:
                wf.write(rf.read())
                print(file,": 종료")
