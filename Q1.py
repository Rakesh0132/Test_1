data = {"a": {"b": 42}}
paths = ["a,b" , "a,b,c"]
for path in paths:
    keys = path.split(",")
    current = data
    try:
        for key in keys:
            current = current[key]
        print(current)
    except:
        print(None)