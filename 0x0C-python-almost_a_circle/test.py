list = [{"name": "ali", "age": 34}, {"job": "??", "doc": "pro"}]
obj = {}

for i in range(len(list)):
    obj.update(list[i])
print(obj)
