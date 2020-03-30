import pymysql.cursors

#  Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='notepad',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def create_tables():
    with connection.cursor() as Cursor:
        
        create_users_table = "create table users (id int(10) AUTO_INCREMENT PRIMARY KEY NOT NULL, name VARCHAR(100), age INT(20), visits INT(20))"
        Cursor.execute(create_users_table)

        create_notes_table = "CREATE table notes (id int(10) AUTO_INCREMENT PRIMARY KEY NOT NULL , user_id INT, FOREIGN KEY (user_id) REFERENCES `users`(id), title VARCHAR(100), body TEXT)"
        Cursor.execute(create_notes_table)
        
        connection.commit()

def write_note(user_id = "empty", title = "empty", body = "empty"):
    # id	user_id	title	body

    with connection.cursor() as Cursor:
        
        add_note = f"insert into notes (user_id , title , body ) values ({user_id}, '{title}', '{body}')"
        Cursor.execute(add_note)
        
        connection.commit()



def write_user(name = "empty", age = "empty", visits = 0):
    
    with connection.cursor() as Cursor:
        
        add_user = f"insert into users (name , age , visits ) values ('{name}', {age}, {visits})"
        Cursor.execute(add_user)
        
        connection.commit()

def get_user(name = ""):

    with connection.cursor() as Cursor:
        
        get_user_command = f"select * from users where name = '{name}'"
        Cursor.execute(get_user_command)
        
        response = Cursor.fetchall()
        return response
        # print(response)

def get_all_users():

    with connection.cursor() as Cursor:
        
        get_user_command = f"select * from users"
        Cursor.execute(get_user_command)
        
        response = Cursor.fetchall()
        # print(response)
        display_users(response)

def get_note(user_id = ""):

    with connection.cursor() as Cursor:
        
        get_user_command = f"select * from notes where user_id = '{user_id}'"
        Cursor.execute(get_user_command)
        
        response = Cursor.fetchall()
        return (response)

def display_users(users):
    
    print(f"{'id'.ljust(5)}{'name'.ljust(15)}{'age'.ljust(15)}{'visits'.ljust(15)}")
    for user in users:
        print(f"{str(user['id']).ljust(5)}{str(user['name']).ljust(15)}{str(user['age']).ljust(15)}{str(user['visits']).ljust(15)}")

def display_notes(notes):
    if len(notes) == 0:
        print("Sorry you have no notes added yet .")
        return 0
    
    print(f"{'id'.ljust(5)}{'Title'.ljust(15)}{'Body'.ljust(15)}")
    for note in notes:
        print(f"{str(note['id']).ljust(5)}{str(note['title']).ljust(15)}{str(note['body']).ljust(15)}")

def display_one_note(notes, id):

    for note in notes:
        if note["id"] == id:
            print(f"\n{note['title']}")
            print(f"\n{note['body']}")
            break


# get_all_users()
# get_note(user_id = 1)
# get_user(name = 'shade')
# create_tables()
# write_user("Shade", 31, 11)
# write_note("1", title = "Dev Goals", body = "This is the body of my message.")
# write_note("atha", "hello world", "hello world i am a genie")


