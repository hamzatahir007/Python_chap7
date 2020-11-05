

d = {'name' : 'hamza' , 'age' : 22}

#or

d = dict(name = 'hamza' , age = 22)

#or

d = {
    'name' : 'hamza',
    'age' : 22,
    'fav_movies' : 'avegarse'
}

#hiw to access data from dictionary 
#d[0] not like thus because dictionary is in un orderd

#syntax
#print(dictname[keyname])
# print(d['name'])


#add data in empty dic
empty_dic = {}
empty_dic['key'] = 'value1'
empty_dic['key2'] = 'value2'
# print(empty_dic)


#check if existing of value in dic
#use in key word for check keys
# if 'name' in d:


#how to iterate over inside dict
# for key, value in d.items():
    # print(f'key is {key} and value is {value}')


#to print all keys
# for i in d:
#     print(i)

# #to print values
# for i in d.values():
#     print(i)


#get methods
#to access a key and check existance
# print(d.get('name'))``


#whay we use get method
# to get rid error
# exampel
# print(d['name'])
# print(d.get('names'))



#to delete items 

popped = d.pop('age')
# print(popped)


# popitem
popped_item = d.popitem()
print(popped_item)