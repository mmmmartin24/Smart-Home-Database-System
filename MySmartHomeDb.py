import sqlite3
from sqlite3 import Error
import os

# CREATE ACCOUNT
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(c, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def show_table(conn):
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM users")
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()

def initialize_rooms(c, conn):
    try:
        # c.execute("INSERT INTO living_room VALUES (?,?,?,?)", [1, 0, 0, 0])
        # c.execute("INSERT INTO kitchen_room VALUES (?,?,?,?)", [1, 0, 0, 0])
        # c.execute("INSERT INTO bath_room VALUES (?,?,?)", [1, 0, 0])
        # c.execute("INSERT INTO bed_room VALUES (?,?,?,?)", [1, 0, 0, 0])
        c.execute("INSERT INTO living_room(room_id) VALUES (?)", [1])
        c.execute("INSERT INTO kitchen_room(room_id) VALUES (?)", [1])
        c.execute("INSERT INTO bath_room(room_id) VALUES (?)", [1])
        c.execute("INSERT INTO bed_room(room_id) VALUES (?)", [1])
        c.execute("INSERT INTO modes(id) VALUES (?)", [1])
        c.execute("INSERT INTO guest_mode(id) VALUES (?)", [1])
        c.execute("INSERT INTO role_type(type, house_mode, living_room, bed_room, bath_room, kitchen_room, guest_mode) VALUES (?,?,?,?,?,?,?)", ["Parent", 1, 1, 1, 1, 1, 1])
        c.execute("INSERT INTO role_type(type, house_mode, living_room, bed_room, bath_room, kitchen_room, guest_mode) VALUES (?,?,?,?,?,?,?)", ["Child", 0, 1, 1, 1, 1, 0])
        c.execute("INSERT INTO role_type(type, house_mode, living_room, bed_room, bath_room, kitchen_room, guest_mode) VALUES (?,?,?,?,?,?,?)", ["Guest", 0, 1, 1, 1, 1, 0])
        c.execute("INSERT INTO role_type(type, house_mode, living_room, bed_room, bath_room, kitchen_room, guest_mode) VALUES (?,?,?,?,?,?,?)", ["Admin", 0, 0, 0, 0, 0, 0])
        c.execute("INSERT INTO role_type(type, house_mode, living_room, bed_room, bath_room, kitchen_room, guest_mode) VALUES (?,?,?,?,?,?,?)",["Automatic", 1, 1, 1, 1, 1, 1])
        c.execute("INSERT INTO login_information(id) VALUES (?)", [1])
        # (type, house_mode, living_room, bed_room, bath_room, guest_mode)
    except Error as e:
        print(e)
    conn.commit()
    conn.close()

# FUNCTION PROCESS TO BE CALLED BY SERVICES
def check_account(name, password):
    drive_letter = os.path.splitdrive(os.getcwd())[0] 
    database = f"{drive_letter}\\SmartHome.db"
    conn = create_connection(database)
    data = (str(name), str(password))
    c = conn.cursor()
    try:
        c.execute("SELECT rowid, * FROM users WHERE name=(?) AND password=(?)", data)
        result = c.fetchall()
        if len(result) == 0:
            return False
        return True
    except Error as e:
        print(e)
    conn.commit()
    conn.close()

def add_users(name, password, email, type):
    drive_letter = os.path.splitdrive(os.getcwd())[0]  # Get the current drive letter
    database = f"{drive_letter}\\SmartHome.db"
    conn = create_connection(database)
    data = (str(name), str(password), str(email), str(type))
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users(name,password,email,type) VALUES (?,?,?,?)", data)
    except Error as e:
        print(e)
    conn.commit()
    conn.close()

def set_lamp_status(room_name, lamp_status):
    drive_letter = os.path.splitdrive(os.getcwd())[0]  # Get the current drive letter
    database = f"{drive_letter}\\SmartHome.db"
    conn = create_connection(database)
    c = conn.cursor()
    try:
        c.execute(f"Update {room_name} set lamp = {lamp_status}")
    except Error as e:
        print(e)
    conn.commit()
    conn.close()

def set_ac_status(room_name, ac_status):
    drive_letter = os.path.splitdrive(os.getcwd())[0]  # Get the current drive letter
    database = f"{drive_letter}\\SmartHome.db"
    conn = create_connection(database)
    c = conn.cursor()
    try:
        c.execute(f"Update {room_name} set ac = {ac_status}")
    except Error as e:
        print(e)
    conn.commit()
    conn.close()

def set_music_status(room_name, music_status):
    drive_letter = os.path.splitdrive(os.getcwd())[0]  # Get the current drive letter
    database = f"{drive_letter}\\SmartHome.db"
    conn = create_connection(database)
    c = conn.cursor()
    try:
        c.execute(f"Update {room_name} set music = {music_status}")
    except Error as e:
        print(e)
    conn.commit()
    conn.close()

def lamp_status(room_name):
    drive_letter = os.path.splitdrive(os.getcwd())[0]  # Get the current drive letter
    database = f"{drive_letter}\\SmartHome.db"
    conn = create_connection(database)
    c = conn.cursor()
    try:
        c.execute(f"SELECT lamp from {room_name}")
    except Error as e:
        print(e)
    status = c.fetchall()
    conn.commit()
    conn.close()
    return status

def ac_status(room_name):
    drive_letter = os.path.splitdrive(os.getcwd())[0]  # Get the current drive letter
    database = f"{drive_letter}\\SmartHome.db"
    conn = create_connection(database)
    c = conn.cursor()
    try:
        c.execute(f"SELECT ac from {room_name}")
    except Error as e:
        print(e)
    status = c.fetchall()
    conn.commit()
    conn.close()
    return status

def music_status(room_name):
    drive_letter = os.path.splitdrive(os.getcwd())[0]  # Get the current drive letter
    database = f"{drive_letter}\\SmartHome.db"
    conn = create_connection(database)
    c = conn.cursor()
    try:
        c.execute(f"SELECT music from {room_name}")
    except Error as e:
        print(e)
    status = c.fetchall()
    conn.commit()
    conn.close()
    return status

def sensor_status(room_name, sensor_name):
    drive_letter = os.path.splitdrive(os.getcwd())[0]  # Get the current drive letter
    database = f"{drive_letter}\\SmartHome.db"
    conn = create_connection(database)
    c = conn.cursor()
    c.execute(f"SELECT {sensor_name} from {room_name}")
    status = c.fetchall()
    sensor_status = status[0][0]
    conn.commit()
    conn.close()
    return sensor_status

def motion_sensor(room_name, motion_sensor):
    drive_letter = os.path.splitdrive(os.getcwd())[0]  # Get the current drive letter
    database = f"{drive_letter}\\SmartHome.db"
    conn = create_connection(database)
    c = conn.cursor()
    try:
        c.execute(f"Update {room_name} set motion_sensor = {motion_sensor}")
    except Error as e:
        print(e)
    conn.commit()
    conn.close()

def temperature_sensor(room_name, temperature_sensor):
    drive_letter = os.path.splitdrive(os.getcwd())[0]  # Get the current drive letter
    database = f"{drive_letter}\\SmartHome.db"
    conn = create_connection(database)
    c = conn.cursor()
    try:
        c.execute(f"Update {room_name} set temperature_sensor = {temperature_sensor}")
    except Error as e:
        print(e)
    conn.commit()
    conn.close()

def light_sensor(room_name, light_sensor):
    drive_letter = os.path.splitdrive(os.getcwd())[0]  # Get the current drive letter
    database = f"{drive_letter}\\SmartHome.db"
    conn = create_connection(database)
    c = conn.cursor()
    try:
        c.execute(f"Update {room_name} set light_sensor = {light_sensor}")
    except Error as e:
        print(e)
    conn.commit()
    conn.close()  

def set_mode(mode_now): #0 = auto 1=manual
    mode_list = [1,0]
    if mode_now not in mode_list:
        print("Status is Wrong!")
        return False
    drive_letter = os.path.splitdrive(os.getcwd())[0]  # Get the current drive letter
    database = f"{drive_letter}\\SmartHome.db"
    conn = create_connection(database)
    c = conn.cursor()
    c.execute(f"UPDATE modes SET mode_status = (?)", [int(mode_now)])
    conn.commit()
    conn.close()

def check_mode(): #0 = auto 1=manual
    drive_letter = os.path.splitdrive(os.getcwd())[0]  # Get the current drive letter
    database = f"{drive_letter}\\SmartHome.db"
    conn = create_connection(database)
    c = conn.cursor()
    c.execute("SELECT rowid, * from modes where id = 1")
    current_mode = c.fetchall()
    conn.commit()
    conn.close()
    if current_mode == [(1,1,'0')]:
        return 0
    else:
        return 1

def check_type(name,password):
    drive_letter = os.path.splitdrive(os.getcwd())[0]  # Get the current drive letter
    database = f"{drive_letter}\\SmartHome.db"
    conn = create_connection(database)
    c = conn.cursor()
    data = (str(name), str(password))
    c.execute("SELECT type from users where name=(?) and password=(?)",data)    
    type = c.fetchall()
    conn.commit()
    conn.close()
    return type

def set_guest_mode(mode_now):
    mode_list = ["on", "off"]
    if mode_now.lower() not in mode_list:
        print("Status is Wrong!")
        return False
    drive_letter = os.path.splitdrive(os.getcwd())[0]  # Get the current drive letter
    database = f"{drive_letter}\\SmartHome.db"
    conn = create_connection(database)
    c = conn.cursor()
    c.execute(f"UPDATE guest_mode SET mode_status = (?)", [str(mode_now)])
    conn.commit()
    conn.close()

def check_guest_mode(): 
    drive_letter = os.path.splitdrive(os.getcwd())[0]  # Get the current drive letter
    database = f"{drive_letter}\\SmartHome.db"
    conn = create_connection(database)
    c = conn.cursor()
    c.execute("SELECT rowid, * from guest_mode where id = 1")
    current_mode = c.fetchall()
    conn.commit()
    conn.close()
    if current_mode == [(1, 1, 'on')]:
        return 'on'
    else:
        return 'off'   

def update_email(email, new_password):
    drive_letter = os.path.splitdrive(os.getcwd())[0]  # Get the current drive letter
    database = f"{drive_letter}\\SmartHome.db"
    conn = create_connection(database)
    c = conn.cursor()
    data = (str(new_password), str(email))
    c.execute(f"UPDATE users SET password = (?) WHERE email = (?)", data)
    conn.commit()
    conn.close()

def update_history(name, type, house_mode, room_name, lamp_status, ac_status, music_status, guest_mode, time): #update history setiap ada pergantian sensor
    drive_letter = os.path.splitdrive(os.getcwd())[0]  # Get the current drive letter
    database = f"{drive_letter}\\SmartHome.db"
    conn = create_connection(database)
    c = conn.cursor()
    data = (str(name), str(type), int(house_mode), str(room_name), int(lamp_status), int(ac_status), int(music_status), str(guest_mode), int(time))
    c.execute(f"INSERT into history(name, type, house_mode, room_name, lamp_status, ac_status, music_status, guest_mode, time) VALUES (?,?,?,?,?,?,?,?,?)", data)
    conn.commit()
    conn.close()

def sensor_history(house_mode, room_name, motion_sensor, temperature_sensor, light_sensor, time): #update history setiap ada pergantian sensor
    drive_letter = os.path.splitdrive(os.getcwd())[0]  # Get the current drive letter
    database = f"{drive_letter}\\SmartHome.db"
    conn = create_connection(database)
    c = conn.cursor()
    data = (str(house_mode), str(room_name), int(motion_sensor), int(temperature_sensor), int(light_sensor), str(time))
    c.execute(f"INSERT into sensor_sense(house_mode, room_name, motion_sensor, temperature_sensor, light_sensor, time) VALUES (?,?,?,?,?,?)", data)
    conn.commit()
    conn.close()

def check_role_type(type): #untuk cek kemampuan setiap type orang
    drive_letter = os.path.splitdrive(os.getcwd())[0]  # Get the current drive letter
    database = f"{drive_letter}\\SmartHome.db"
    conn = create_connection(database)
    c = conn.cursor()
    data = (type,)
    c.execute("SELECT house_mode, living_room, bed_room, bath_room, kitchen_room, guest_mode from role_type where type = (?)", data)
    role = c.fetchall()
    conn.commit()
    conn.close()
    return role

def update_login_info(name, password):
    drive_letter = os.path.splitdrive(os.getcwd())[0]  # Get the current drive letter
    database = f"{drive_letter}\\SmartHome.db"
    conn = create_connection(database)
    c = conn.cursor()
    data = (str(name), str(password))
    c.execute(f"UPDATE login_information SET name = (?), password = (?) ", data)
    conn.commit()
    conn.close()

def login_info():
    drive_letter = os.path.splitdrive(os.getcwd())[0]  # Get the current drive letter
    database = f"{drive_letter}\\SmartHome.db"
    conn = create_connection(database)
    c = conn.cursor()
    c.execute("SELECT name,password from login_information")
    login = c.fetchall()
    name = login[0][0]
    password = login[0][1]
    conn.commit()
    conn.close()
    return name,password


###############################################################################

def main(): # CREATE DATABASES
    drive_letter = os.path.splitdrive(os.getcwd())[0]  # Get the current drive letter
    database = f"{drive_letter}\\SmartHome.db"
    account = """CREATE TABLE IF NOT EXISTS users (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        name TEXT NOT NULL,
                                        password TEXT NOT NULL,
                                        email TEXT NOT NULL,
                                        type TEXT not NULL,
                                        UNIQUE(name, email)
                                        ); """

    house_mode = """CREATE TABLE IF NOT EXISTS modes (
                                        id INTEGER PRIMARY KEY,
                                        mode_status TEXT default 1
                                        ); """

    living_room = """CREATE TABLE IF NOT EXISTS living_room (
                                            room_id INTEGER PRIMARY KEY,
                                            lamp INTEGER NOT NULL default 0,
                                            music INTEGER NULL default 0,
                                            ac INTEGER NOT NULL default 0,
                                            motion_sensor INTEGER NOT NULL default 0,
                                            temperature_sensor INTEGER NOT NULL default 27,
                                            light_sensor INTEGER NOT NULL default 0
                                            ); """

    bed_room = """CREATE TABLE IF NOT EXISTS bed_room (
                                                room_id INTEGER PRIMARY KEY,
                                                lamp INTEGER NOT NULL default 0,
                                                music INTEGER NULL default 0,
                                                ac INTEGER NOT NULL default 0,
                                                motion_sensor INTEGER NOT NULL default 0,
                                                temperature_sensor INTEGER NOT NULL default 27,
                                                light_sensor INTEGER NOT NULL default 0
                                                ); """

    bath_room = """CREATE TABLE IF NOT EXISTS bath_room (
                                                room_id INTEGER PRIMARY KEY,
                                                lamp INTEGER NOT NULL default 0,
                                                music INTEGER NULL default 0,
                                                motion_sensor INTEGER NOT NULL default 0,
                                                temperature_sensor INTEGER NOT NULL default 27,
                                                light_sensor INTEGER NOT NULL default 0
                                                ); """

    kitchen_room = """CREATE TABLE IF NOT EXISTS kitchen_room (
                                                room_id INTEGER PRIMARY KEY,
                                                lamp INTEGER NOT NULL default 0,
                                                music INTEGER NULL default 0,
                                                ac INTEGER NOT NULL default 0,
                                                motion_sensor INTEGER NOT NULL default 0,
                                                temperature_sensor INTEGER NOT NULL default 27,
                                                light_sensor INTEGER NOT NULL default 0
                                                ); """

    guest_mode = """CREATE TABLE IF NOT EXISTS guest_mode (
                                        id INTEGER PRIMARY KEY,
                                        mode_status TEXT default 'off'
                                        ); """

    type_role = """CREATE TABLE IF NOT EXISTS role_type (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        type TEXT,
                                        house_mode INTEGER,
                                        living_room INTEGER,
                                        bed_room INTEGER,
                                        bath_room INTEGER,
                                        kitchen_room INTEGER,
                                        guest_mode INTEGER
                                        ); """

    history = """CREATE TABLE IF NOT EXISTS history (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        name TEXT, 
                                        type TEXT,
                                        house_mode INTEGER,
                                        room_name TEXT,
                                        lamp_status INTEGER,
                                        ac_status INTEGER,
                                        music_status INTEGER,
                                        guest_mode TEXT,
                                        time INTEGER
                                        ); """

    sensor_history =  """CREATE TABLE IF NOT EXISTS sensor_sense (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        house_mode TEXT,
                                        room_name TEXT,
                                        motion_sensor INTEGER,
                                        temperature_sensor INTEGER,
                                        light_sensor INTEGER,
                                        time INTEGER
                                        ); """

    login_info = """CREATE TABLE IF NOT EXISTS login_information (
                                        id INTEGER PRIMARY KEY,
                                        name TEXT,
                                        password TEXT 
                                        ); """
    # create a database connection
    conn = create_connection(database)
    # c = conn.cursor()
    # create tables

    if conn is not None:
        c = conn.cursor()
        # create rooms table for collecting data
        create_table(conn, account)
        create_table(conn, house_mode)
        create_table(conn, living_room)
        create_table(conn, kitchen_room)
        create_table(conn, bath_room)
        create_table(conn, bed_room)
        create_table(conn, guest_mode)
        create_table(conn, type_role)
        create_table(conn, history)
        create_table(conn, sensor_history)
        create_table(conn, login_info)
        initialize_rooms(c, conn) # add first rooms, so that we can change the value of the room sensor
    else:
        print("Error! cannot create the database connection.")
    conn.close()
    # show_table(conn)

def make_data():
    add_users('b','b','Pixelpixel@pixel.com','Parent')
    add_users('yemen','omen','omaigat@pixel.com','Child')
    add_users('a','a','vvv@pixel.com','Guest')
    add_users('-','-','-','Admin')
    add_users('automatic', 'automatic', '-', 'Automatic')

if __name__ == '__main__':
    main()
    make_data()