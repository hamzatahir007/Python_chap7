#dic
user_info = {
    'name' : 'hamza',
    'age' : 22,
    'fav_movies' : ['coco' , 'kiwi no na'],
    'fav_tunes' : ['iphone tune' , 'tun tun'],
}

#check if key access in dictionary 
# if 'name' in user_info:
#     print('present')
# else:
#     print('not present')


#check if value access in dictionary 
# if 22 in user_info.values():
#     print('present')
# else:
#     print('not present')


#loops in dictionary
# for i in user_info.values():
#     print(i)

#another way 
# for i in user_info:
#     print(user_info[i])


#values method
# user_info_value = user_info.values()
# print(user_info_value)
# print(type(user_info_value))

# user_info_keys = user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))


#items method
# user_info_items = user_info.items()
# print(user_info_items)
# print(type(user_info_items))

for i,j in user_info.items():
    print(f"The key is {i}, and the value is {j}")