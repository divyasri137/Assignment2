import json

mark =  '{"English": "92","Maths":"90","History":"90"}'

print(mark)

y = json.loads(mark) 

a = int(y["English"])
b = int(y["Maths"])
c = int(y["History"])

print(f"TotalMark: {a+b+c}")
