from tkinter import *
import MySmartHomeDb as db
import MySmartHomeGUI as ui
import threading
import time


def current_hour():
    current_hour = 0
    return current_hour

def login(usernames,pw,root):
    db.update_login_info(usernames,pw)
    username, password = db.login_info()
    if db.check_account(username, password) == True:
        type = db.check_type(username,password)[0][0]
        role_type = db.check_role_type(type)
        if role_type == [(0, 1, 1, 1, 1, 0)] and type == 'Guest' and db.check_guest_mode() == 'off':
            mylabel3 = Label(root,text='GUESTMODE OFF')
            mylabel3.grid(row=3,column=2)
        elif db.check_role_type(type[0][0]) == [(0, 0, 0, 0, 0, 0)]:
            root4 = Toplevel()
            root4.title = 'Admin window'
            ui.create_admin(root4)
        elif db.check_account(username, pw) ==  True:
            type = db.check_type(username, pw)
            mylabel1 = Label(root,text='LOGIN SUCCESSFUL')
            mylabel1.grid(row=3,column=2)
            root2 = Toplevel()
            root2.title('SmartHome')
            ui.settings(root2, type)
    else:
        mylabel2 = Label(root,text='IMPOSTOR')
        mylabel2.grid(row=3,column=2)

def account_window():
    global root3
    root3 = Toplevel()
    root3.title('Create Account') 
    ui.create_acc(root3)

def exit_settings(root2,root):
    root2.withdraw()
    root.deiconify()

def update_mode(mode,Radiobutton3,Radiobutton4,Radiobutton5,Radiobutton6,Radiobutton7,Radiobutton8,Radiobutton9,
                Radiobutton10,Radiobutton11,Radiobutton12,Radiobutton13,Radiobutton14,Radiobutton15,Radiobutton16,
                Radiobutton17,Radiobutton18,Radiobutton19,Radiobutton20,Radiobutton21,Radiobutton22,Radiobutton23,
                Radiobutton24,Radiobutton25,Radiobutton26,):
    db.set_mode(mode.get())
    update_history(None)
    username, password = db.login_info()
    if username == 'automatic' and password == 'automatic':
        pass
    elif db.check_mode() == 0:
        Radiobutton3.configure(state = DISABLED)
        Radiobutton4.configure(state = 'disabled')
        Radiobutton5.configure(state = 'disabled')
        Radiobutton6.configure(state = 'disabled')
        Radiobutton7.configure(state = 'disabled')
        Radiobutton8.configure(state = 'disabled')
        Radiobutton9.configure(state = 'disabled')
        Radiobutton10.configure(state = 'disabled')
        Radiobutton11.configure(state = 'disabled')
        Radiobutton12.configure(state = 'disabled')
        Radiobutton13.configure(state = 'disabled')
        Radiobutton14.configure(state = 'disabled')
        Radiobutton15.configure(state = 'disabled')
        Radiobutton16.configure(state = 'disabled')
        Radiobutton17.configure(state = 'disabled')
        Radiobutton18.configure(state = 'disabled')
        Radiobutton19.configure(state = 'disabled')
        Radiobutton20.configure(state = 'disabled')
        Radiobutton21.configure(state = 'disabled')
        Radiobutton22.configure(state = 'disabled')
        Radiobutton23.configure(state = 'disabled')
        Radiobutton24.configure(state = 'disabled')

    elif db.check_mode() == 1:
        Radiobutton3.configure(state = 'normal')
        Radiobutton4.configure(state = 'normal')
        Radiobutton5.configure(state = 'normal')
        Radiobutton6.configure(state = 'normal')
        Radiobutton7.configure(state = 'normal')
        Radiobutton8.configure(state = 'normal')
        Radiobutton9.configure(state = 'normal')
        Radiobutton10.configure(state = 'normal')
        Radiobutton11.configure(state = 'normal')
        Radiobutton12.configure(state = 'normal')
        Radiobutton13.configure(state = 'normal')
        Radiobutton14.configure(state = 'normal')
        Radiobutton15.configure(state = 'normal')
        Radiobutton16.configure(state = 'normal')
        Radiobutton17.configure(state = 'normal')
        Radiobutton18.configure(state = 'normal')
        Radiobutton19.configure(state = 'normal')
        Radiobutton20.configure(state = 'normal')
        Radiobutton21.configure(state = 'normal')
        Radiobutton22.configure(state = 'normal')
        Radiobutton23.configure(state = 'normal')
        Radiobutton24.configure(state = 'normal')
    #buat untuk user

# SENSOR AUTOMATIC
def room_service_auto():
    automatic_room_service(current_hours)

def automatic_service():
    if db.check_mode() == 0:
        room_service_auto()

def sensor_sense(room):
    db.sensor_history(db.check_mode(), room, db.sensor_status(room, "motion_sensor"),db.sensor_status(room, "temperature_sensor"),db.sensor_status(room, "light_sensor"),current_hours)

def update_history(room):
    username, password = db.login_info()
    house_room = ["bed_room", "living_room", "kitchen_room"]

    if room == None:
        print("Mode updated")
        db.update_history(username, db.check_type(username, password)[0][0],  db.check_mode(), None,
                          1, 1, 1,
                          db.check_guest_mode(), current_hours)
    elif room == "bath_room":
        print("Status updated in", room)
        db.update_history(username, db.check_type(username, password)[0][0], db.check_mode(), room,
                          db.lamp_status(room)[0][0],
                          0, db.music_status(room)[0][0], db.check_guest_mode(),
                          current_hours)
    elif room in house_room:
        print("Status updated in", room)
        db.update_history(username, db.check_type(username, password)[0][0], db.check_mode(), room, db.lamp_status(room)[0][0],db.ac_status(room)[0][0], db.music_status(room)[0][0], db.check_guest_mode(),current_hours)

def automatic_room_service(current_hours):
    username, password = db.login_info()
    print("work")
    if username == "automatic" or db.check_mode() == 0:
        def music_automatic_service():
            if current_hours >= 8 and current_hours<= 11:
                print("music automatic service on")
                house_room = ["bath_room", "bed_room", "living_room", "kitchen_room"]
                music_status = "1"
                for room_name in house_room:
                    if db.music_status(room_name)[0][0] == 0:
                        db.set_music_status(room_name, music_status)
                        # update_history(room_name)

            elif current_hours >= 0 and current_hours <= 23:
                print("music automatic service off")
                house_room = ["bath_room", "bed_room", "living_room", "kitchen_room"]
                music_status = "0"
                for room_name in house_room:
                    if db.music_status(room_name)[0][0] == 1:
                        db.set_music_status(room_name, music_status)
                        # update_history(room_name)

        def bed_room_service():
            if current_hours >= 22 or current_hours <= 6:
                print("bedroom service on")
                if db.lamp_status("bed_room")[0][0] == 1 or db.music_status("bed_room")[0][0] == 1:
                    print("Bedroom Lamp and Lights are off")
                    db.set_lamp_status("bed_room", "0")
                    db.set_music_status("bed_room", "0")
                    update_history("bed_room")

            elif db.sensor_status("bed_room", "motion_sensor") == 0:
                print("Motion detected in bed room")
                if db.lamp_status("bed_room")[0][0] == 1 or db.music_status("bed_room")[0][0] == 1:
                    print("Bedroom Lamp and Lights are off")
                    db.set_lamp_status("bed_room", "0")
                    db.set_music_status("bed_room", "1")
                    update_history("bed_room")

            elif current_hours >= 6:
                print("bedroom service on")
                if db.lamp_status("bed_room")[0][0] == 0 or db.music_status("bed_room")[0][0] == 0:
                    print("Bedroom Lamp and Lights are off")
                    db.set_lamp_status("bed_room", "1")
                    db.set_music_status("bed_room", "1")
                    update_history("bed_room")


        music_automatic_service()
        bed_room_service()

    else:
        print("Automatic room services are not working in manual mode")

def motion_sensor(room_name,sensor):
    if sensor == 1:
        lamp_status = "1"
        ac_status = "1"
        music_status = "1"
        db.set_lamp_status(room_name, lamp_status)
        db.set_ac_status(room_name, ac_status)
        db.set_music_status(room_name, music_status)
        update_history(room_name)


    else:
        lamp_status = "0"
        ac_status = "0"
        music_status = "0"
        db.set_lamp_status(room_name, lamp_status)
        db.set_ac_status(room_name, ac_status)
        db.set_music_status(room_name, music_status)
        update_history(room_name)

def temperature_sensor(room_name, sensor):
    if sensor == 1:
        ac_status = "1"
        db.set_ac_status(room_name, ac_status)
        update_history(room_name)
    else:
        ac_status = "0"
        db.set_ac_status(room_name, ac_status)
        update_history(room_name)


def light_sensor(room_name, sensor):
    if sensor == 1:
        lamp_status = "1"
        db.set_lamp_status(room_name, lamp_status)
        update_history(room_name)
    else:
        lamp_status = "0"
        db.set_lamp_status(room_name, lamp_status)
        update_history(room_name)

def simulation():
    root5 = Tk()
    #update functions
    def update_motion_sensor(room_name, sensor):
        if db.check_mode() == 0:
            motion_sensor(room_name, sensor)
            db.motion_sensor(room_name, sensor)
            sensor_sense(room_name)
        else:
            print("Sensors are not working in manual mode")

    def update_light_sensor(room_name, sensor):
        if db.check_mode() == 0:
            light_sensor(room_name, sensor)
            db.light_sensor(room_name, sensor)
            sensor_sense(room_name)
        else:
            print("Sensors are not working in manual mode")

    def update_temp_sensor(room_name, sensor):
        if db.check_mode() == 0:
            temperature_sensor(room_name, sensor)
            db.temperature_sensor(room_name, sensor)
            sensor_sense(room_name)
        else:
            print("Sensors are not working in manual mode")

    #globals
    global bed_room_motion
    global bed_room_temp
    global bed_room_light

    global bath_room_motion
    global bath_room_temp
    global bath_room_light

    global living_room_motion
    global living_room_temp
    global living_room_light

    global kitchen_room_motion
    global kitchen_room_temp
    global kitchen_room_light


    #bedroom
    label2 = Label(root5,text='Bedroom',font="Gotham 9 underline")
    label3 = Label(root5,text='motion sensor')
    bed_room_motion = IntVar()
    radiobutton1 = Radiobutton(root5,text='MOTION DETECTED',variable=bed_room_motion,value=1,command=lambda: update_motion_sensor('bed_room',1))
    radiobutton2 = Radiobutton(root5,text='MOTION NOT DETECTED',variable=bed_room_motion,value=0,command=lambda:update_motion_sensor('bed_room',0))
    label5 = Label(root5, text='temperature sensor')
    bed_room_temp = IntVar()
    radiobutton5 = Radiobutton(root5,text='HOT',variable=bed_room_temp,value=1,command=lambda: update_temp_sensor('bed_room',1))
    radiobutton6 = Radiobutton(root5,text='NOT HOT',variable=bed_room_temp,value=0,command=lambda: update_temp_sensor('bed_room',0))
    label7 = Label(root5,text='light sensor')
    bed_room_light = IntVar()
    radiobutton3 = Radiobutton(root5,text='LIGHT DETECTED',variable=bed_room_light,value=0,command=lambda: update_light_sensor('bed_room',1))
    radiobutton4 = Radiobutton(root5,text='NO LIGHT DETECTED',variable=bed_room_light,value=1,command=lambda: update_light_sensor('bed_room',0))

    #placemnt
    label2.grid(row=1,column=0, sticky="w",columnspan=2)
    label3.grid(row=2,column=0, sticky="w",columnspan=2)
    radiobutton1.grid(row=3, column=0, padx=15, pady=(0, 15), sticky="w",columnspan=2)
    radiobutton2.grid(row=4, column=0, padx=15, pady=(0, 15), sticky="w",columnspan=2)
    label5.grid(row=5,column=0, sticky="w",columnspan=2)
    radiobutton5.grid(row=6, column=0, padx=15, pady=(0, 15), sticky="w",columnspan=2)
    radiobutton6.grid(row=7, column=0, padx=15, pady=(0, 15), sticky="w",columnspan=2)
    label7.grid(row=8,column=0, sticky="w",columnspan=2)
    radiobutton3.grid(row=9, column=0, padx=15, pady=(0, 15), sticky="w",columnspan=2)
    radiobutton4.grid(row=10, column=0, padx=15, pady=(0, 15), sticky="w",columnspan=2)

    #bathroom
    label8 = Label(root5,text='Bathroom',font="Gotham 9 underline")
    label9 = Label(root5,text='motion sensor')
    bath_room_motion = IntVar()
    radiobutton7 = Radiobutton(root5,text='MOTION DETECTED',variable=bath_room_motion,value=1,command=lambda: update_motion_sensor('bath_room',1))
    radiobutton8 = Radiobutton(root5,text='MOTION NOT DETECTED',variable=bath_room_motion,value=0,command=lambda: update_motion_sensor('bath_room',0))
    label10 = Label(root5, text='temperature sensor')
    bath_room_temp = IntVar()
    radiobutton9 = Radiobutton(root5,text='HOT',variable=bath_room_temp,value=1,command=lambda: update_temp_sensor('bath_room',1))
    radiobutton10 = Radiobutton(root5,text='NOT HOT',variable=bath_room_temp,value=0,command=lambda: update_temp_sensor('bath_room',0))
    label12 = Label(root5,text='light sensor')
    bath_room_light = IntVar()
    radiobutton11 = Radiobutton(root5,text='LIGHT DETECTED',variable=bath_room_light,value=0,command=lambda: update_light_sensor('bath_room',0))
    radiobutton12 = Radiobutton(root5,text='NO LIGHT DETECTED',variable=bath_room_light,value=1,command=lambda: update_light_sensor('bath_room',1))

    #placemnt
    label8.grid(row=1,column=2, sticky="w",columnspan=2)
    label9.grid(row=2,column=2, sticky="w",columnspan=2)
    radiobutton7.grid(row=3, column=2, padx=15, pady=(0, 15), sticky="w",columnspan=2)
    radiobutton8.grid(row=4, column=2, padx=15, pady=(0, 15), sticky="w",columnspan=2)
    label10.grid(row=5,column=2, sticky="w",columnspan=2)
    radiobutton9.grid(row=6, column=2, padx=15, pady=(0, 15), sticky="w",columnspan=2)
    radiobutton10.grid(row=7, column=2, padx=15, pady=(0, 15), sticky="w",columnspan=2)
    label12.grid(row=8,column=2, sticky="w",columnspan=2)
    radiobutton11.grid(row=9, column=2, padx=15, pady=(0, 15), sticky="w",columnspan=2)
    radiobutton12.grid(row=10, column=2, padx=15, pady=(0, 15), sticky="w",columnspan=2)

    #living room
    label13 = Label(root5,text='Living room',font="Gotham 9 underline")
    label14 = Label(root5,text='motion sensor')
    living_room_motion = IntVar()
    radiobutton13 = Radiobutton(root5,text='MOTION DETECTED',variable=living_room_motion,value=1,command=lambda: update_motion_sensor('living_room',1))
    radiobutton14 = Radiobutton(root5,text='MOTION NOT DETECTED',variable=living_room_motion,value=0,command=lambda: update_motion_sensor('living_room',0))
    label15 = Label(root5, text='temperature sensor')
    living_room_temp = IntVar()
    radiobutton15 = Radiobutton(root5,text='HOT',variable=living_room_temp,value=1,command=lambda: update_temp_sensor('living_room',1))
    radiobutton16 = Radiobutton(root5,text='NOT HOT',variable=living_room_temp,value=0,command=lambda: update_temp_sensor('living_room',0))
    label16 = Label(root5,text='light sensor')
    living_room_light = IntVar()
    radiobutton17 = Radiobutton(root5,text='LIGHT DETECTED',variable=living_room_light,value=0,command=lambda: update_light_sensor('living_room',0))
    radiobutton18 = Radiobutton(root5,text='NO LIGHT DETECTED',variable=living_room_light,value=1,command=lambda: update_light_sensor('living_room',1))

    #placemnt
    label13.grid(row=1,column=4, sticky="w",columnspan=2)
    label14.grid(row=2,column=4, sticky="w",columnspan=2)
    radiobutton13.grid(row=3, column=4, padx=15, pady=(0, 15), sticky="w",columnspan=2)
    radiobutton14.grid(row=4, column=4, padx=15, pady=(0, 15), sticky="w",columnspan=2)
    label15.grid(row=5,column=4, sticky="w",columnspan=2)
    radiobutton15.grid(row=6, column=4, padx=15, pady=(0, 15), sticky="w",columnspan=2)
    radiobutton16.grid(row=7, column=4, padx=15, pady=(0, 15), sticky="w",columnspan=2)
    label16.grid(row=8,column=4, sticky="w",columnspan=2)
    radiobutton17.grid(row=9, column=4, padx=15, pady=(0, 15), sticky="w",columnspan=2)
    radiobutton18.grid(row=10, column=4, padx=15, pady=(0, 15), sticky="w",columnspan=2)

    #kitchen
    label17 = Label(root5,text='Kitchen',font="Gotham 9 underline")
    label18 = Label(root5,text='motion sensor')
    kitchen_room_motion = IntVar()
    radiobutton17 = Radiobutton(root5,text='MOTION DETECTED',variable=kitchen_room_motion,value=1,command=lambda: update_motion_sensor('kitchen_room',1))
    radiobutton18 = Radiobutton(root5,text='MOTION NOT DETECTED',variable=kitchen_room_motion,value=0,command=lambda: update_motion_sensor('kitchen_room',0))
    label19 = Label(root5, text='temperature sensor')
    kitchen_room_temp = IntVar()
    radiobutton19 = Radiobutton(root5,text='HOT',variable=kitchen_room_temp,value=1,command=lambda: update_temp_sensor('kitchen_room',1))
    radiobutton20 = Radiobutton(root5,text='NOT HOT',variable=kitchen_room_temp,value=0,command=lambda: update_temp_sensor('kitchen_room',0))
    label20 = Label(root5,text='light sensor')
    kitchen_room_light = IntVar()
    radiobutton21 = Radiobutton(root5,text='LIGHT DETECTED',variable=kitchen_room_light,value=0,command=lambda: update_light_sensor('kitchen_room',0))
    radiobutton22 = Radiobutton(root5,text='NO LIGHT DETECTED',variable=kitchen_room_light,value=1,command=lambda: update_light_sensor('kitchen_room',1))

    #placemnt
    label17.grid(row=1,column=6, sticky="w",columnspan=2)
    label18.grid(row=2,column=6, sticky="w",columnspan=2)
    radiobutton17.grid(row=3, column=6, padx=15, pady=(0, 15), sticky="w",columnspan=2)
    radiobutton18.grid(row=4, column=6, padx=15, pady=(0, 15), sticky="w",columnspan=2)
    label19.grid(row=5,column=6, sticky="w",columnspan=2)
    radiobutton19.grid(row=6, column=6, padx=15, pady=(0, 15), sticky="w",columnspan=2)
    radiobutton20.grid(row=7, column=6, padx=15, pady=(0, 15), sticky="w",columnspan=2)
    label20.grid(row=8,column=6, sticky="w",columnspan=2)
    radiobutton21.grid(row=9, column=6, padx=15, pady=(0, 15), sticky="w",columnspan=2)
    radiobutton22.grid(row=10, column=6, padx=15, pady=(0, 15), sticky="w",columnspan=2)

    root5.title('Simulation')

def read_time():
    while True:
        lock.acquire()
        global current_hours
        my_hour = current_hours
        time.sleep(1)
        if my_hour == 23:
            my_hour = -1
        my_hour = my_hour + 1
        current_hours = my_hour
        if db.check_mode() == 0:
            automatic_room_service(current_hours)
            # update_button_status()
        print(current_hours)
        lock.release()

def update_buttons():
    pass



lock = threading.Lock()
current_hours = current_hour()

# def update_buttons():
#     while True:
#         lock.acquire()
#
#         print('s')
#         lock.release()

# if db.check_mode() == 0:
#     automatic_room_service(current_hours)
#     update_button_status()


def update_button_status():
    house_room = ["bath_room", "bed_room", "living_room", "kitchen_room"]
    for room_name in house_room:
        if room_name != 'bath_room':
            lamp_status, ac_status, music_status = db.lamp_status(room_name)[0][0], db.ac_status(room_name)[0][0], \
                                                   db.music_status(room_name)[0][0]
            button_set(room_name, lamp_status, ac_status, music_status)  # ('bath_room,1,1,0)
        else:
            lamp_status, music_status = db.lamp_status(room_name)[0][0], db.music_status(room_name)[0][0]
            button_set(room_name, lamp_status, None, music_status)

def button_set(room_name, lamp_status, ac_status, music_status):
    if room_name == 'bed_room':
        Lights1.set(lamp_status)
        AC1.set(ac_status)
        MUSIC1.set(music_status)
    elif room_name == 'bath_room':
        Lights2.set(lamp_status)
        MUSIC2.set(music_status)
    elif room_name == 'kitchen_room':
        Lights3.set(lamp_status)
        AC3.set(ac_status)
        MUSIC3.set(music_status)
    elif room_name == 'living_room':
        Lights4.set(lamp_status)
        AC4.set(ac_status)
        MUSIC4.set(music_status)
