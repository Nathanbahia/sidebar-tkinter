### github.com/nathanbahia
### linkedin.com/in/nathanbahia
### instagram.com/noobpythonbr

try:
    from tkinter import * # <-- If you use Python 3
except:
    from Tkinter import * # <-- If you use Python 2

class Window:
    def __init__(self, master=None):

        # Window size
        self.width, self.height = 800, 500
        
        # Main screen
        self.frame_position = 0
        self.main_frame = Frame(master)
        self.main_frame.configure(background = "#151515")
        self.main_frame.place(x = self.frame_position, y = 0, w = self.width, h = self.height)

        # Texts on the screen
        self.title = Label(self.main_frame, text = "@noobpythonbr", font = "System 30 bold", fg = "#ffffff", bg = "#151515")
        self.title.place(x = 0, y = 80, w = self.width)

        self.github = Label(self.main_frame, text = "github.com/nathanbahia/sidebar", font = "System 20 bold", fg = "#ffffff", bg = "#151515")
        self.github.place(x = 0, y = 300, w = self.width)

        # Sidebar
        self.sidebar_position = -200
        self.sidebar = Frame(master)
        self.sidebar.configure(background = "#bfff00")
        self.sidebar.place(x = self.sidebar_position, y = 0, w = 200, h = self.height)
        self.sidebar_is_open = False        

        # Button on sidebar
        self.btn_close = Button(self.sidebar, text = "EXIT", fg = "#ffffff",  bg = "#b40404", font = "System 14 bold", command = root.destroy)
        self.btn_close.place(x = 10, y = 350, w = 180)

        # Fotter on sidebar
        self.footer_label = Label(self.sidebar, text="@noobpythonbr", font="System 14 bold", fg = "#ffffff", bg = "#787878")
        self.footer_label.place(x = 0, y = 450, w = 200, h = 50)

        # Button Menu
        self.btn = Button(self.main_frame, text = "MENU", command = self.controll_sidebar)
        self.btn.place(x = 0, y = 0 )

    def controll_sidebar(self):
        
        # A - Checks if th sidebar is opened or no and changes de speed value

        if self.sidebar_is_open == True:
            self.sidebar_speed = -10        
        else:
            self.sidebar_speed = +10
        
        # B - Start the animation

        if -200 <= self.sidebar_position <= 0:
            self.sidebar_position += self.sidebar_speed
        
        # C - Checks if the animation is finished

        if self.sidebar_position == 0:
            self.sidebar_is_open = True        
        elif self.sidebar_position == -200:
            self.sidebar_is_open = False        
        
        # Checks if the position isn't the same of the (B) and call the function until the 
        # sentence return False
        if self.sidebar_position != -200 and self.sidebar_position != 0:            
            self.sidebar.after(10, self.controll_sidebar)

        # Refreshing the sidebar position         
        self.sidebar.place(x = self.sidebar_position, y = 0, w = 200, h = self.height)

        # Refreshing the main frame position         
        self.frame_position += self.sidebar_speed
        self.main_frame.place(x = self.frame_position, y = 0, w = self.width, h = self.height)

root = Tk()
Window(root)
root.geometry("{}x{}+0+0".format(Window().width, Window().height))
root.title("@noobpythonbr")
root.mainloop()
