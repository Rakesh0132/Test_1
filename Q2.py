name = ["ball","ball","glove","glove","glove"]
price = [2,3,1,2,1]
weight = [2,5,1,1,1]
products = []
duplicate = 0
for i in range(len(name)):
    item = (name[i], price[i], weight[i])
    if item in products:
        duplicate += 1
    else:
        products.append(item)
print(duplicate)