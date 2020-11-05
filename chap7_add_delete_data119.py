#dictionary 
user_info = {
    'name' : 'hamza',
    'age' : 22,
    'fav_movies' : ['coco' , 'kiwi no na'],
    'fav_tunes' : ['iphone tune' , 'tun tun'],
}

#how to add data in dic
# user_info ['fav_songs'] = ['song1','song2']
# print(user_info)

#how to pop method in dic
# popped_items = user_info.pop('age')
# print(popped_items)
# print(user_info)

#for popeitem method    
popped_items = user_info.popitem()
print(popped_items)
print(user_info)

