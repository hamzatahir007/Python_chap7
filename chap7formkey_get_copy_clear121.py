#formkeys
# dic = {'name':'unknown','age':'unknown'}

# d= dict.fromkeys(['name','age'], 'unknow')
# print(d)


#for get methods
dic = {'name':'hamza','age':'unknown'}
# print(dic['names'])

# print(dic.get('names')) #better for error handling


#HOW TO CLEAR  DIC
# dic.clear()
# print(dic)


#how to copy dictionary
d1 = dic.copy()
# print(d1.popitem())
# print(dic)

print(d1 == dic)