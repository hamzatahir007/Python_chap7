#dictionary 
user_info = {
    'name' : 'hamza',
    'age' : 22,
    'fav_movies' : ['coco' , 'kiwi no na'],
    'fav_tunes' : ['iphone tune' , 'tun tun'],
}


#for update dic
more_info = { 'name':'talha','state':'karachi' , 'hobbies':['cricket', 'games']}

user_info.update(more_info)
print(user_info)