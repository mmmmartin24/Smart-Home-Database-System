import MySmartHomeService as service
import MySmartHomeGUI as ui
import MySmartHomeDb as db
import threading
from tkinter import *

def main():
    db.main()
    time_thread = threading.Thread(target=service.read_time, args=())
    time_thread.start()

    service.simulation()
    db.make_data()
    ui.login_window()
    service.account_window()

    root.mainloop()



if __name__ == '__main__':
    main()

