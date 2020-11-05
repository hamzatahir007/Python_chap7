#take input and store in dic
user_info = {}

name = input("Enter your name: ")
age = input("Enter your age: ")
fav_movie = input("Enter your fav movie sperated by comma: ").split(',')
fav_songs = input("Enter your fav songs sperated by comma: ").split(',')

user_info['name'] = name
user_info['age'] = age
user_info['fav_movie'] = fav_movie
user_info['fav_songs'] = fav_songs

for key, value in user_info.items():
    print(f'{key} : {value}')

    




