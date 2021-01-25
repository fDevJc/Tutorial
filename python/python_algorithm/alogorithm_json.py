import json
user = {
    "id" : "gildong",
    "password" : "1q2w3e4r",
    "age" : 31,
    "hobby" : ["soccer","Programming"]
}

#파이썬 변수를 JSON 객체로 변환
json_data = json.dumps(user, indent=4)
print(json_data)