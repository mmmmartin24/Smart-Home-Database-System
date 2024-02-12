from tkinter import *
import MySmartHomeService as service
import threading
import MySmartHomeDb as db
import time


#globals
# global Lights1
# Lights1 =
# global AC1
# AC1 = 0
# global MUSIC1
# MUSIC1 = 0
# global Lights2
# Lights2 = 0
# global MUSIC2
# MUSIC2 = 0
# global Lights3
# Lights3 = 0
# global AC3
# AC3 = 0
# global MUSIC3
# MUSIC3 = 0
# global Lights4
# Lights4 =0
# global AC4
# AC4 = 0
# global MUSIC4
# MUSIC4 = 0

global root
root = Tk()

def login_window():

    root.title("Login")
    label1 = Label(root,text='Login Info',font=("Gotham 18 bold"))
    label1.grid(row=0,column=0,columnspan=2,sticky=W)

    label2 = Label(root, text="Username", font="Gotham 9")
    label3 = Label(root, text="Password", font="Gotham 9")

    entry1 = Entry(root, width=30)
    entry1.insert(0, "Username")
    entry2 = Entry(root, width=30)
    entry2.insert(1, "Password")

    label2.grid(row=1,column=0, sticky="w",columnspan=2)
    label3.grid(row=2,column=0, sticky="w",columnspan=2)
    entry1.grid(row=1,column=2,sticky=W)
    entry2.grid(row=2,column=2,sticky=W)

    button1 = Button(root, text="Login", command=lambda: service.login(entry1.get(),entry2.get(),root))
    button1.grid(row=3,column=1,sticky=W)

    button3 = Button(root,text='Create account',command=lambda: service.account_window())
    button3.grid(row=4,column=1, sticky="w")




    root.mainloop()

def create_admin(root4):
    root.withdraw()
    label1 = Label(root4,text='FORGOT PASSWORD',font=("Gotham 18 bold"))
    label1.grid(row=0,column=0,columnspan=2,sticky=W)

    label2 = Label(root4, text="Email", font="Gotham 9")
    label3 = Label(root4, text="New Password", font="Gotham 9")
    entry1 = Entry(root4, width=30)
    entry1.insert(0, "Email")
    entry2 = Entry(root4, width=30)
    entry2.insert(1, "New Password")


    entry1.grid(row=1,column=2,sticky=W)
    entry2.grid(row=2,column=2,sticky=W)    
    label2.grid(row=1,column=0,columnspan=2,sticky=W)
    label3.grid(row=2,column=0,columnspan=2,sticky=W)

    def update_password(email, new_password):
        db.update_email(email, new_password)
        print(new_password)
        label3 = Label(root4,text='Password updated!', font="Gotham 9")
        label3.grid(row=3,column=2,sticky=W)

    def exit():
        root4.withdraw()
        root.deiconify()

    button2 = Button(root4, text="Send", command=lambda: update_password(entry1.get(),entry2.get()))
    button2.grid(row=3,column=1,sticky=W)
    button3 = Button(root4, text="Exit", command=exit)
    button3.grid(row=7,column=1,sticky=W)


def create_acc(root3):
    root.withdraw()
    label1 = Label(root3,text='Create Account',font=("Gotham 18 bold"))
    label1.grid(row=0,column=0,columnspan=2,sticky=W)

    label2 = Label(root3, text="New Username", font="Gotham 9")
    label3 = Label(root3, text="New Password", font="Gotham 9")
    label4 = Label(root3, text="Email", font="Gotham 9")
    label6 = Label(root3, text="Type", font="Gotham 9")

    entry1 = Entry(root3, width=30)
    entry1.insert(0, "Username")
    entry2 = Entry(root3, width=30)
    entry2.insert(1, "Password")
    entry3 = Entry(root3, width=30)
    entry3.insert(2, "Email")
    entry11 = Entry(root3, width=30)
    entry11.insert(3, "Parent, Child, Admin or Guest")

    label2.grid(row=1,column=0, sticky="w",columnspan=2)
    label3.grid(row=2,column=0, sticky="w",columnspan=2)
    label4.grid(row=3,column=0,sticky="w",columnspan=2)
    label6.grid(row=4,column=0,sticky="w",columnspan=2)
    entry1.grid(row=1,column=2,sticky=W)
    entry2.grid(row=2,column=2,sticky=W)
    entry3.grid(row=3,column=2,sticky=W)
    entry11.grid(row=4,column=2,sticky=W)


    def create_account():
        print('Created')
        name = entry1.get()
        password = entry2.get()
        email = entry3.get()
        db.add_users(name, password, email)
        label5 = Label(root3,text='Account created!')
        label5.grid(row=5,column=2,sticky=W)

    def exit():
        root3.withdraw()
        root.deiconify()

    button1 = Button(root3, text="Create Account", command=create_account)
    button1.grid(row=5,column=1,sticky=W)
    button3 = Button(root3, text="Exit", command=exit)
    button3.grid(row=7,column=1,sticky=W)

def settings(root2, type):
    root.withdraw()
    mode = IntVar(value=db.check_mode())
    label5 = Label(root2, text="Select mode", font="Gotham 9")
    label5.grid(row=5,column=0, sticky="w",columnspan=2)
    Radiobutton1 = Radiobutton(root2, text="Manual", variable=mode,value=1,state=NORMAL,command=lambda: service.update_mode(mode,Radiobutton3,Radiobutton4,Radiobutton5,Radiobutton6,Radiobutton7,Radiobutton8,Radiobutton9,Radiobutton10,Radiobutton11,Radiobutton12,Radiobutton13,Radiobutton14,Radiobutton15,Radiobutton16,Radiobutton17,Radiobutton18,Radiobutton19,Radiobutton20,Radiobutton21,Radiobutton22,Radiobutton23,Radiobutton24,Radiobutton25,Radiobutton26,))
    Radiobutton1.grid(row=6, column=0, padx=15, sticky="w",columnspan=2)
    Radiobutton2 = Radiobutton(root2, text="Automatic",variable=mode, value=0,state=NORMAL,command=lambda: service.update_mode(mode,Radiobutton3,Radiobutton4,Radiobutton5,Radiobutton6,Radiobutton7,Radiobutton8,Radiobutton9,Radiobutton10,Radiobutton11,Radiobutton12,Radiobutton13,Radiobutton14,Radiobutton15,Radiobutton16,Radiobutton17,Radiobutton18,Radiobutton19,Radiobutton20,Radiobutton21,Radiobutton22,Radiobutton23,Radiobutton24,Radiobutton25,Radiobutton26,))
    Radiobutton2.grid(row=7, column=0, padx=15, pady=(0, 15), sticky="w",columnspan=2)

    #BEDROOM
    Lights1 = IntVar(value=db.lamp_status('bed_room'))
    AC1 = IntVar(value=db.ac_status('bed_room'))
    MUSIC1 = IntVar(value=db.music_status('bed_room'))
        
    label9 = Label(root2, text="BEDROOM", font="Gotham 9 underline")
    label9.grid(row=8,column=0, sticky="w",columnspan=2)

    label6 = Label(root2, text="Lights", font="Gotham 9")
    label6.grid(row=9,column=0, sticky="w",columnspan=2)
    username,password = db.login_info()
    def update_lights(room, variable):
        db.set_lamp_status(room, variable.get())
        # print("result", username, db.check_type(username, password)[0][0], db.check_mode(), room, db.lamp_status(room)[0][0],db.ac_status(room)[0][0], db.music_status(room)[0][0], db.check_guest_mode(), service.current_hour())
        service.update_history(room)

    def update_ac(room, variable):
        db.set_ac_status(room, variable.get())
        service.update_history(room)

    def update_music(room, variable):
        db.set_music_status(room, variable.get())
        service.update_history(room)


    Radiobutton3 = Radiobutton(root2, text="ON",variable=Lights1, value=1,state=NORMAL,command=lambda:update_lights('bed_room',Lights1))
    Radiobutton3.grid(row=10, column=0, padx=15, sticky="w",columnspan=2)

    Radiobutton4 = Radiobutton(root2, text="OFF",variable=Lights1, value=0,state=NORMAL,command=lambda:update_lights('bed_room',Lights1))
    Radiobutton4.grid(row=11, column=0, padx=15, pady=(0, 15), sticky="w",columnspan=2)

    label7 = Label(root2, text="AC", font="Gotham 9")
    label7.grid(row=12,column=0, sticky="w",columnspan=2)

    Radiobutton5 = Radiobutton(root2, text="ON",variable=AC1, value=1,state=NORMAL,command=lambda:update_ac('bed_room',AC1))
    Radiobutton5.grid(row=13, column=0, padx=15, sticky="w",columnspan=2)

    Radiobutton6 = Radiobutton(root2, text="OFF",variable=AC1, value=0,state=NORMAL,command=lambda:update_ac('bed_room',AC1))
    Radiobutton6.grid(row=14, column=0, padx=15, pady=(0, 15), sticky="w",columnspan=2)

    label8 = Label(root2, text="MUSIC", font="Gotham 9")
    label8.grid(row=15,column=0, sticky="w",columnspan=2)

    Radiobutton7 = Radiobutton(root2, text="ON",variable=MUSIC1, value=1,state=NORMAL,command=lambda:update_music('bed_room',MUSIC1))
    Radiobutton7.grid(row=16, column=0, padx=15, sticky="w",columnspan=2)

    Radiobutton8 = Radiobutton(root2, text="OFF",variable=MUSIC1, value=0,state=NORMAL,command=lambda:update_music('bed_room',MUSIC1))
    Radiobutton8.grid(row=17, column=0, padx=15, pady=(0, 15), sticky="w",columnspan=2)

    #BATHROOM
    Lights2 = IntVar(value=db.lamp_status('bath_room'))
    MUSIC2 = IntVar(value=db.music_status('bath_room'))
        
    label9 = Label(root2, text="BATHROOM", font="Gotham 9 underline")
    label9.grid(row=8,column=2, sticky="w",columnspan=5)

    label6 = Label(root2, text="Lights", font="Gotham 9")
    label6.grid(row=9,column=2, sticky="w",columnspan=2)

    Radiobutton9 = Radiobutton(root2, text="ON",variable=Lights2, value=1,state=NORMAL,command=lambda:update_lights('bath_room',Lights2))
    Radiobutton9.grid(row=10, column=2, padx=15, sticky="w",columnspan=2)

    Radiobutton10 = Radiobutton(root2, text="OFF",variable=Lights2, value=0,state=NORMAL,command=lambda:update_lights('bath_room',Lights2))
    Radiobutton10.grid(row=11, column=2, padx=15, pady=(0, 15), sticky="w",columnspan=2)

    label8 = Label(root2, text="MUSIC", font="Gotham 9")
    label8.grid(row=12,column=2, sticky="w",columnspan=2)

    Radiobutton11 = Radiobutton(root2, text="ON",variable=MUSIC2, value=1,state=NORMAL,command=lambda:update_music('bath_room',MUSIC2))
    Radiobutton11.grid(row=13, column=2, padx=15, sticky="w",columnspan=2)

    Radiobutton12 = Radiobutton(root2, text="OFF",variable=MUSIC2, value=0,state=NORMAL,command=lambda:update_music('bath_room',MUSIC2))
    Radiobutton12.grid(row=14, column=2, padx=15, pady=(0, 15), sticky="w",columnspan=2)

    #LIVING ROOM
    Lights3 = IntVar(value=db.lamp_status('living_room'))
    AC3 = IntVar(value=db.ac_status('living_room'))
    MUSIC3 = IntVar(value=db.music_status('living_room'))
        
    label9 = Label(root2, text="LV ROOM", font="Gotham 9 underline")
    label9.grid(row=18,column=0, sticky="w",columnspan=2)

    label6 = Label(root2, text="Lights", font="Gotham 9")
    label6.grid(row=19,column=0, sticky="w",columnspan=2)

    Radiobutton13 = Radiobutton(root2, text="ON",variable=Lights3, value=1,state=NORMAL,command=lambda:update_lights('living_room',Lights3))
    Radiobutton13.grid(row=20, column=0, padx=15, sticky="w",columnspan=2)

    Radiobutton14 = Radiobutton(root2, text="OFF",variable=Lights3, value=0,state=NORMAL,command=lambda:update_lights('living_room',Lights3))
    Radiobutton14.grid(row=21, column=0, padx=15, pady=(0, 15), sticky="w",columnspan=2)

    label7 = Label(root2, text="AC", font="Gotham 9")
    label7.grid(row=22,column=0, sticky="w",columnspan=2)

    Radiobutton15 = Radiobutton(root2, text="ON",variable=AC3, value=1,state=NORMAL,command=lambda:update_ac('living_room',AC3))
    Radiobutton15.grid(row=23, column=0, padx=15, sticky="w",columnspan=2)

    Radiobutton16 = Radiobutton(root2, text="OFF",variable=AC3, value=0,state=NORMAL,command=lambda:update_ac('living_room',AC3))
    Radiobutton16.grid(row=24, column=0, padx=15, pady=(0, 15), sticky="w",columnspan=2)

    label8 = Label(root2, text="MUSIC", font="Gotham 9")
    label8.grid(row=25,column=0, sticky="w",columnspan=2)

    Radiobutton17 = Radiobutton(root2, text="ON",variable=MUSIC3, value=1,state=NORMAL,command=lambda:update_music('living_room',MUSIC3))
    Radiobutton17.grid(row=26, column=0, padx=15, sticky="w",columnspan=2)

    Radiobutton18 = Radiobutton(root2, text="OFF",variable=MUSIC3, value=0,state=NORMAL,command=lambda:update_music('living_room',MUSIC3))
    Radiobutton18.grid(row=27, column=0, padx=15, pady=(0, 15), sticky="w",columnspan=2)

    #KITCHEN
    Lights4 = IntVar(value=db.lamp_status('kitchen_room'))
    AC4 = IntVar(value=db.ac_status('kitchen_room'))
    MUSIC4 = IntVar(value=db.music_status('kitchen_room'))
        
    label9 = Label(root2, text="KITCHEN", font="Gotham 9 underline")
    label9.grid(row=18,column=2, sticky="w",columnspan=2)

    label6 = Label(root2, text="Lights", font="Gotham 9")
    label6.grid(row=19,column=2, sticky="w",columnspan=2)

    Radiobutton19 = Radiobutton(root2, text="ON",variable=Lights4, value=1,state=NORMAL,command=lambda:update_lights('kitchen_room',Lights4))
    Radiobutton19.grid(row=20, column=2, padx=15, sticky="w",columnspan=2)

    Radiobutton20 = Radiobutton(root2, text="OFF",variable=Lights4, value=0,state=NORMAL,command=lambda:update_lights('kitchen_room',Lights4))
    Radiobutton20.grid(row=21, column=2, padx=15, pady=(0, 15), sticky="w",columnspan=2)

    label7 = Label(root2, text="AC", font="Gotham 9")
    label7.grid(row=22,column=2, sticky="w",columnspan=2)

    Radiobutton21 = Radiobutton(root2, text="ON",variable=AC4, value=1,state=NORMAL,command=lambda:update_ac('kitchen_room',AC4))
    Radiobutton21.grid(row=23, column=2, padx=15, sticky="w",columnspan=2)

    Radiobutton22 = Radiobutton(root2, text="OFF",variable=AC4, value=0,state=NORMAL,command=lambda:update_ac('kitchen_room',MUSIC4))
    Radiobutton22.grid(row=24, column=2, padx=15, pady=(0, 15), sticky="w",columnspan=2)

    label8 = Label(root2, text="MUSIC", font="Gotham 9")
    label8.grid(row=25,column=2, sticky="w",columnspan=2)

    Radiobutton23 = Radiobutton(root2, text="ON",variable=MUSIC4, value=1,state=NORMAL,command=lambda:update_music('kitchen_room',MUSIC4))
    Radiobutton23.grid(row=26, column=2, padx=15, sticky="w",columnspan=2)

    Radiobutton24 = Radiobutton(root2, text="OFF",variable=MUSIC4, value=0,state=NORMAL,command=lambda:update_music('kitchen_room',MUSIC4))
    Radiobutton24.grid(row=27, column=2, padx=15, pady=(0, 15), sticky="w",columnspan=2)

    def check_guest_mode():
        if guest_mode.get() == 1:
            db.set_guest_mode("on")
        else:
            db.set_guest_mode("off")

    guest_mode = IntVar()

    label9 = Label(root2, text="GUESTMODE", font="Gotham 9")
    label9.grid(row=28,column=1, sticky="w",columnspan=2)

    Radiobutton25 = Radiobutton(root2, text="ON",variable=guest_mode, value=1,state=NORMAL)
    Radiobutton25.grid(row=29, column=1, padx=15, sticky="w",columnspan=2)

    Radiobutton26 = Radiobutton(root2, text="OFF",variable=guest_mode, value=0,state=NORMAL)
    Radiobutton26.grid(row=30, column=1, padx=15, pady=(0, 15), sticky="w",columnspan=2)

    button2 = Button(root2, text="confirm", command=check_guest_mode)
    button2.grid(row=31, column=1, padx=15, pady=(0, 15), sticky="w",columnspan=2)

    button1 = Button(root2, text="EXIT", command=lambda:service.exit_settings(root2,root))
    button1.grid(row=6, column=2, padx=15, pady=(0, 15), sticky="w",columnspan=2)


    if type == 'Parent':
        pass

    elif db.check_role_type(type[0][0]) == [(0, 1, 1, 1, 1, 0)]:
        Radiobutton1.configure(state='disabled')
        Radiobutton2.configure(state='disabled')
        Radiobutton25.configure(state='disabled')
        Radiobutton26.configure(state='disabled')
        button2.configure(state='disabled')


    if username == 'automatic' and password == 'automatic':
        pass
    elif db.check_mode() == 0:
        Radiobutton3.configure(state=DISABLED)
        Radiobutton4.configure(state='disabled')
        Radiobutton5.configure(state='disabled')
        Radiobutton6.configure(state='disabled')
        Radiobutton7.configure(state='disabled')
        Radiobutton8.configure(state='disabled')
        Radiobutton9.configure(state='disabled')
        Radiobutton10.configure(state='disabled')
        Radiobutton11.configure(state='disabled')
        Radiobutton12.configure(state='disabled')
        Radiobutton13.configure(state='disabled')
        Radiobutton14.configure(state='disabled')
        Radiobutton15.configure(state='disabled')
        Radiobutton16.configure(state='disabled')
        Radiobutton17.configure(state='disabled')
        Radiobutton18.configure(state='disabled')
        Radiobutton19.configure(state='disabled')
        Radiobutton20.configure(state='disabled')
        Radiobutton21.configure(state='disabled')
        Radiobutton22.configure(state='disabled')
        Radiobutton23.configure(state='disabled')
        Radiobutton24.configure(state='disabled')

    def update_button_status():
        house_room = ["bath_room", "bed_room", "living_room", "kitchen_room"]

        for room_name in house_room:
            if room_name != 'bath_room':
                lamp_status, ac_status, music_status = db.lamp_status(room_name)[0][0], db.ac_status(room_name)[0][0], \
                                                       db.music_status(room_name)[0][0]
                print(lamp_status, ac_status, music_status)
                button_set(room_name, lamp_status, ac_status, music_status)  # ('bath_room,1,1,0)

            else:
                lamp_status, music_status = db.lamp_status(room_name)[0][0], db.music_status(room_name)[0][0]
                button_set(room_name, lamp_status, None, music_status)

    def button_set(room_name, lamp_status, ac_status, music_status):
        if room_name == 'bed_room':
            print('success')
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

    def update_buttons():
        while True:
            print('update button')
            update_button_status()
            time.sleep(2)

    set_thread = threading.Thread(target=update_buttons, args=())
    set_thread.start()