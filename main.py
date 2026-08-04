import tkinter as tk
from tkinter import Menu, Toplevel, ttk
import time
from pynput import keyboard






#creating the timer
timer = tk.Tk()




#settings section value
settingssection = None
#run timer values
running = False
start = 0
#the window moving
offset_x = 0
offset_y = 0
#settings offset
soffset_x = 0
soffset_y = 0
#screen and window scales

splits = tk.BooleanVar(value=True)

settings_window_width = 700
settings_window_height = 550

timer_window_width = 300
timer_window_height = 320
#settings window movement
settingswindowmove = False






#the timer window
timer.title("Overlay Timer")
timer.overrideredirect(True)
timer.attributes("-topmost", True)
timer.attributes("-alpha", 0.85)
timer.geometry(f"{timer_window_width}x{timer_window_height}")
timer.configure(bg="black")


#centering settings window
screen_width = timer.winfo_screenwidth()
screen_height = timer.winfo_screenheight()
x_position = (screen_width - settings_window_width) // 2
y_position = (screen_height - settings_window_height) // 2







#run timer
def runtimefunc():
    if running:
        passed = time.time() - start

        minutes = int(passed) // 60
        seconds = int(passed) % 60
        milliseconds = int((passed - int(passed)) * 100)

        timerlabel.config(
            text=f"{minutes:02}:{seconds:02}.{milliseconds:02}"
        )

        timer.after(10, runtimefunc)


#toggling the timer
def toggle_timer():
    global running
    global start

    if running:
        running = False
    else:
        running = True
        start = time.time()
        runtimefunc()






#menu and menu options

#(moving the settings window)
def movingsettings_start(event):
    global soffset_x, soffset_y
    soffset_x = event.x
    soffset_y = event.y

def movingsettings_do(event):
    x = settings_window.winfo_x() + event.x - soffset_x
    y = settings_window.winfo_y() + event.y - soffset_y
    settings_window.geometry(f"+{x}+{y}")

#settings sections/ section options

def presetapplybutton():
    pass



def defaultsettingsapplybutton():
    global timer_window_height, timer_window_width,splits


    if timersizecombobox.get() == "Large":

        if splits.get() == True:
            timer.geometry("420x420")

            timerlabel.config(
            font=("DejaVu Sans", 72, "bold"),
            )



            
        else:
            timer.geometry("420x180")

            timerlabel.config(
            font=("DejaVu Sans", 72, "bold"),
            )            


            
    elif timersizecombobox.get() == "Default":

        if splits.get() == True:
            timer.geometry("300x320")

            timerlabel.config(
            font=("DejaVu Sans", 54, "bold"),
            )




        else:
            timer.geometry("300x140")

            timerlabel.config(
            font=("DejaVu Sans", 54, "bold"),
            )


            
    elif timersizecombobox.get() == "Small":

        if splits.get() == True:
            timer.geometry("220x260")

            timerlabel.config(
            font=("DejaVu Sans", 40, "bold"),
            )


        else:
            timer.geometry("220x110")

            timerlabel.config(
            font=("DejaVu Sans", 40, "bold"),
            )

    else:
        pass




    if splits.get() == True:
            timerlabel.pack_forget()
            timerlabel.pack(fill="x")

    else:
            timerlabel.pack_forget()
            timerlabel.pack(expand=True)

def presetoptions():
    pass




def defaultsettingsoptions():
    global timersizecombobox,splits, splits_checkbox


    timersizelabel = tk.Label(content,
                            text="Timer Size",
                            font=("DejaVu Sans", 12, "bold"),
                            bg="gray10",
                            fg="white",
                            activebackground="gray10",
                            activeforeground="white",
                            highlightthickness=0,
                            bd=0).grid(row=2, column=1)


    timersizecombobox = ttk.Combobox(
                                    content,
                                    values=["Large", "Default", "Small"]
                                    )
    timersizecombobox.set("Default")
    timersizecombobox.grid(row=2, column=2)


    splits_checkbox = tk.Checkbutton(content,

                                    text="splits",
                                    font=("DejaVu Sans", 12, "bold"),
                                    variable=splits,
                                    bg="gray10",
                                    fg="white",
                                    activebackground="gray10",
                                    activeforeground="white",
                                    selectcolor="gray15",
                                    highlightthickness=0,
                                    bd=0)
    splits_checkbox.grid(row=2, column=3)







    defaultsettingssettings_apply = tk.Button(content,
                                            text="Apply",  
                                            font=("DejaVu Sans", 12, "bold"),
                                            bg="gray15",
                                            fg="white",
                                            highlightthickness=0,
                                            bd=0,
                                            activebackground="gray25",
                                            activeforeground="white",
                                            command=defaultsettingsapplybutton).grid(row=3, column=0, columnspan=6)





#sections

def presetsection():
    global settingssection

    presetbutton.config(bg="gray10")
    defaultsettingsbutton.config(bg="gray15")


    if settingssection != "presetsection":

        for widget in content.winfo_children():
            widget.destroy()

        presetoptions()

        tk.Label(content,
                text="Preset Settings",
                font=("DejaVu Sans", 12, "bold"),
                bg="gray10",
                fg="white").grid(row=0, column=0, columnspan=6)

    settingssection = "presetsection"





def defaultsettingssection():
    global settingssection

    defaultsettingsbutton.config(bg="gray10")
    presetbutton.config(bg="gray15")


    
    if settingssection != "defaultsection":

        for widget in content.winfo_children():
            widget.destroy()

        defaultsettingsoptions()
        
        tk.Label(content,
                text="Default Settings",
                font=("DejaVu Sans", 12, "bold"),
                bg="gray10",
                fg="white").grid(row=0, column=0, columnspan=6)

    settingssection = "defaultsection"







def movingwindows():
    global settingswindowmove
    #changes the value from one to another (example: not false = true, not true = false)
    settingswindowmove = not settingswindowmove
    #moving window bind
    if settingswindowmove:
        timer.bind("<ButtonPress-1>", movingwindow_start)
        timer.bind("<B1-Motion>", movingwindow_do)
        settings_window.bind("<ButtonPress-1>", movingsettings_start)
        settings_window.bind("<B1-Motion>", movingsettings_do)
        freemoving.config(bg="gray5")
        
    else:
        timer.unbind("<ButtonPress-1>")
        timer.unbind("<B1-Motion>")
        settings_window.unbind("<ButtonPress-1>")
        settings_window.unbind("<B1-Motion>")
        freemoving.config(bg="gray15")







#open settings
def open_settings():
    global content, settings_window, freemoving, presetbutton, defaultsettingsbutton

    if 'settings_window' in globals() and settings_window.winfo_exists():
        settings_window.destroy()
        return


    settings_window = Toplevel(timer)
    settings_window.title("Settings")
    settings_window.geometry(f"{settings_window_width}x{settings_window_height}+{x_position}+{y_position}")
    settings_window.overrideredirect(True)


    #auto bond if enabled

    #sidebar
    sidebar = tk.Frame(settings_window, bg="gray15", width=120)
    sidebar.pack(side="left", fill="y")

    #content
    content = tk.Frame(settings_window, bg="gray10")
    content.pack(side="right", fill="both", expand=True)

    for i in range(6):
        content.grid_columnconfigure(i, weight=1)


    #the two actual buttons
    presetbutton = tk.Button(sidebar,
                            text="Presets",
                            font=("DejaVu Sans", 9),
                            bg="gray15",
                            fg="white",
                            highlightthickness=0,
                            bd=0,
                            activebackground="gray25",
                            activeforeground="white",
                            anchor="center",
                            justify="center",
                            command=presetsection)

    
    


    defaultsettingsbutton = tk.Button(sidebar,
                                text="Default Settings",
                                font=("DejaVu Sans", 9),
                                bg="gray15",
                                fg="white",
                                highlightthickness=0,
                                bd=0,
                                activebackground="gray25",
                                activeforeground="white",
                                anchor="center",
                                justify="center",
                                command=defaultsettingssection)
    
        
    
    #freemoving button (don't mistake)
    freemoving = tk.Button(sidebar,
                                text="Free Move",
                                font=("DejaVu Sans", 9),
                                bg="gray15",
                                fg="white",
                                highlightthickness=0,
                                bd=0,
                                activebackground="gray30",
                                activeforeground="white",
                                anchor="center",
                                justify="center",
                                command=movingwindows)
    
    presetbutton.pack(fill="x")
    defaultsettingsbutton.pack(fill="x")
    freemoving.pack(fill="x", side="bottom")

    #auto enable moving if settingswindowmove is true
    if settingswindowmove:
        settings_window.bind("<ButtonPress-1>", movingsettings_start)
        settings_window.bind("<B1-Motion>", movingsettings_do)

        timer.bind("<ButtonPress-1>", movingwindow_start)
        timer.bind("<B1-Motion>", movingwindow_do)

        freemoving.config(bg="gray5")







#right click menu
right_click_menu = Menu(timer,
                        fg="white",
                        bg="black",
                        activebackground="gray30",
                        activeforeground="white",
                        font=("DejaVu Sans", 15),
                        tearoff=0)


right_click_menu.add_command(label="Settings", command=open_settings)
right_click_menu.add_command(label="Exit", command=timer.destroy)

def show_settings(event):
    right_click_menu.tk_popup(event.x_root, event.y_root)





#moving the window
def movingwindow_start(event):
    global offset_x, offset_y
    offset_x = event.x
    offset_y = event.y

def movingwindow_do(event):
    x = timer.winfo_x() + event.x - offset_x
    y = timer.winfo_y() + event.y - offset_y
    timer.geometry(f"+{x}+{y}")




#on press
def on_press(key):
    if hasattr(key, "char"):
        if key.char == "u":
            toggle_timer()







#THE HOLY TIME LABEL


timerlabel = tk.Label(
    timer,
    text="00:00.00",
    font=("DejaVu Sans", 54, "bold"),
    fg="white",
    bg="black",
    anchor="center",
    justify="center"
)
#timer window binding
timer.bind("<Button-3>", show_settings)



#keyboard listener
listener = keyboard.Listener(on_press=on_press)
listener.start()


#packing
timerlabel.pack(fill="x")



timer.mainloop()
