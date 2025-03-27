import sqlite3
import requests

# comments =requests.get('https://jsonplaceholder.typicode.com/comments').json()
#
#
# for comment in comments:
#     postId = comment['postId']
#     id = comment['id']
#     name = comment['name']
#     email = comment['email']
#     body = comment['body']
#
#     database = sqlite3.connect('comments.db')
#     cursor = database.cursor()
#
#
#     cursor.execute("""
#     INSERT INTO comment(postId, id, name, email, body)
#     VALUES(?, ?, ?, ?, ?)""", (postId, id, name, email, body))
#     database.commit()
#     database.close()

# albums =requests.get('https://jsonplaceholder.typicode.com/albums').json()
#
#
# for album in albums:
#     userId = album['userId']
#     id = album['id']
#     title = album['title']
#
#
#     database = sqlite3.connect('albums.db')
#     cursor = database.cursor()
#
#
#     cursor.execute("""
#     INSERT INTO album(userId, id, title)
#     VALUES(?, ?, ?)""", (userId, id, title))
#     database.commit()
#     database.close()

# photos =requests.get('https://jsonplaceholder.typicode.com/photos').json()
#
#
# for photo in photos:
#     albumId = photo['albumId']
#     id = photo['id']
#     title = photo['title']
#     url = photo['url']
#     thumbnailUrl = photo['thumbnailUrl']
#
#
#     database = sqlite3.connect('photos.db')
#     cursor = database.cursor()
#
#
#     cursor.execute("""
#     INSERT INTO photo(albumId, id, title, url, thumbnailUrl)
#     VALUES(?, ?, ?, ?, ?)""", (albumId, id, title, url, thumbnailUrl))
#     database.commit()
#     database.close()



# todos =requests.get('https://jsonplaceholder.typicode.com/todos').json()
#
#
# for todo in todos:
#     userId = todo['userId']
#     id = todo['id']
#     title = todo['title']
#     completed = todo['completed']
#
#
#     database = sqlite3.connect('todos.db')
#     cursor = database.cursor()
#
#
#     cursor.execute("""
#     INSERT INTO todo(userId, id, title, completed)
#     VALUES(?, ?, ?, ?)""", (userId, id, title, completed))
#     database.commit()
#     database.close()


users = requests.get('https://jsonplaceholder.typicode.com/users').json()

for user in users:
    id = user['id']
    name = user['name']
    username = user['username']
    email = user['email']
    street = user['address']['street']
    suite = user['address']['suite']
    city = user['address']['city']
    zip = user['address']['zipcode']
    lat = user['address']['geo']['lat']
    lng = user['address']['geo']['lng']
    phone = user['phone']
    website = user['website']
    company_name = user['company']['name']
    company_catchphrase = user['company']['catchPhrase']
    company_bs = user['company']['bs']

    database = sqlite3.connect('users.db')
    cursor = database.cursor()

    cursor.execute("""
    INSERT INTO user(id, name, username, email, street, suite, city, zipcode, lat, lng, phone, website, company_name, company_catchphrase, company_bs)
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, (id, name, username, email, street,suite, city, zip, lat, lng, phone, website, company_name, company_catchphrase, company_bs ))

    database.commit()
    database.close()