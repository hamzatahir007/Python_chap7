#dictionary intro
#Q - why we used dictionary
#A - because of list limitation, list is not enough for real life data


#examlpe
user = ['hamza' , 22 , ['coco' , 'kiwi no na'] , ['iphone tune' , 'tun tun']]
#this list consider user name, age , fav movie, fav tunes

# Q - what are dictionaries
# a - unorderd collection of data in key: value pair.


#how to create dictionaries
user = {'name' : 'hamza', 'age' : 22}
# print(user)
# print(type(user))


#another way to create dict
# user1 = dict(name = "hamza" , age = 22)
# print(user1)
# print(user[0])  #error because dic is un orderd list


#how to access data in dictionaries
#there is no indexing because to un orderd list
print(user['name'])
print(user['age'])


#which type of data dictionaries can store

user_info = {
    'name' : 'hamza',
    'age' : 22,
    'fav_movies' : ['coco' , 'kiwi no na'],
    'fav_tunes' : ['iphone tune' , 'tun tun'],
}

# print(user_info)


#how to add data\ in empty dic
user_info = {}
user_info['name'] = 'talha'
user_info['age'] = 24
print(user_info)