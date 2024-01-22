import customtkinter as ctk 
from tkinter import filedialog as fd
from PIL import Image
import os
import sys

class Start_Screen():
    def __init__(self, root, known_number = 0, unknown_number = 0, file_name=None, length=0): #setting up window

        # declaring variables given from the main program file
        self.root = root
        self.known_number = known_number
        self.unknown_number = unknown_number
        self.file_name = file_name

        # f there has been a file used before take the normpath of the file and declare it as variable
        if file_name:
            self.file_name =  os.path.basename(os.path.normpath(self.file_name))
        self.length = length

        # set basic size and name for the window
        ctk.set_appearance_mode("system")
        self.root.title("Pylee v1.0.0")
        self.root.geometry("780x530")
        self.root.minsize(780, 520)
        self.root.iconbitmap("images/PyLee_Logo_iconbitmap2.ico")

        # configuring the basic layout of the window
        self.root.grid_columnconfigure(0,weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        # declaring some basic fonts for the window
        self.font20 = "Inter", 20
        self.font14 = "Inter", 14
        self.font24 = "Inter", 24
        
        # declaring the basic color of the window
        self.color = "#1a4570"
        self.hover_color = "#3c638a"
        self.extra_color = "#1b6bad"

        # creating a different frame for everything start_screen
        self.root_frame = ctk.CTkFrame(self.root)
        self.root_frame.grid(row=0,rowspan=2, column=0, sticky="nswe")
        
        # configuring the layout of the frame
        self.root_frame.grid_columnconfigure(0,weight=2)
        self.root_frame.grid_columnconfigure(1,weight=1)

        self.root_frame.grid_rowconfigure(0, weight=1)


        # declaring the variables which will later open the next program
        self.open_file_btn_pressed = False
        self.new_file_btn_pressed = False
        
        # calling the create function to create the start screen
        self.create()


    def create(self):

        # creating and configuring the frame for the left side
        self.left_frame = ctk.CTkFrame(self.root_frame, border_width=1, fg_color="#19456F")
        self.left_frame.grid(column=0,row=0,sticky="nswe")
        self.left_frame.grid_propagate(False)
        self.left_frame.grid_columnconfigure(0,weight=1)
        self.left_frame.grid_columnconfigure(1,weight=1)

        self.left_frame.grid_rowconfigure(0,weight=2)
        self.left_frame.grid_rowconfigure(1,weight=2)
        self.left_frame.grid_rowconfigure(2,weight=2)
        self.left_frame.grid_rowconfigure(3,weight=1)

        try:
            image = os.path.join(sys._MEIPASS, "images/Pylee_Logo.png")
        except:
            image = "images/Pylee_Logo.png"
        # creating the image for the logo and placing it in a label
        self.logo_img = ctk.CTkImage(Image.open(image),size=(450,450),)
        self.logo_label = ctk.CTkLabel(self.left_frame, image=self.logo_img, text="")
        self.logo_label.grid(row=0, column=0, columnspan=2, sticky="nswe", pady=(2,2), padx=(2,2))

        # creating the button to open the file creater 
        self.file_menu_button =ctk.CTkButton(self.left_frame, text="File Creator", font=self.font24, command=self.new_file, fg_color="#1b4571", corner_radius=3)
        self.file_menu_button.grid(row=3, column=0, sticky="nswe", padx=(5,0), pady=(0,5))

        # creating the button to open the menu to choose the learn mode etc.
        self.choose_mode_button =ctk.CTkButton(self.left_frame, text="Choose File", font=self.font24, command=self.open_file, fg_color="#1b4571", corner_radius=3)
        self.choose_mode_button.grid(row=3, column=1, sticky="nswe", padx=(0,5) , pady=(0,5))
        
        # creating and configuring the right frame for extra informations
        self.right_frame = ctk.CTkFrame(self.root_frame, border_width=1)
        self.right_frame.grid(column=1,row=0,sticky="nswe")
        self.right_frame.grid_propagate(False)
        self.right_frame.grid_columnconfigure(0,weight=1)

        self.right_frame.grid_rowconfigure(0,weight=6, minsize=5)
        self.right_frame.grid_rowconfigure(1,weight=6, minsize=5)
        self.right_frame.grid_rowconfigure(2,weight=6, minsize=5)
        self.right_frame.grid_rowconfigure(3,weight=6, minsize=5)
        self.right_frame.grid_rowconfigure(4,weight=6, minsize=5)
        self.right_frame.grid_rowconfigure(5,weight=1, minsize=1)

        # creating the frame where the version changes will be displayed
        self.update_frame =ctk.CTkFrame(self.right_frame, border_width=1)
        self.update_frame.grid(column=0, row=1, padx=20, pady=10, sticky="nswe")

        self.update_label =ctk.CTkLabel(self.update_frame,text="Version 1.0.0 Changes:", text_color=("black","white"),font=self.font20)
        self.update_label.grid(column=0,row=0,padx=10,pady=5,sticky="w")

        self.info_label =ctk.CTkLabel(self.update_frame,text="● Progressbars added", text_color=("black","white"),font=self.font14)
        self.info_label.grid(column=0,row=1,padx=20,pady=1,sticky="w")

        self.info_label =ctk.CTkLabel(self.update_frame,text="● File Editor can open files", text_color=("black","white"),font=self.font14)
        self.info_label.grid(column=0,row=2,padx=20,pady=1,sticky="w")

        self.info_label =ctk.CTkLabel(self.update_frame,text="● Redesign of endscreen", text_color=("black","white"),font=self.font14)
        self.info_label.grid(column=0,row=3,padx=20,pady=1,sticky="w")


        # ceating an extra frame for the credits and help button
        self.button_frame = ctk.CTkFrame(self.right_frame)
        self.button_frame.grid(column=0,row=5,sticky="snwe",padx=(40,10),pady=(30,10))

        self.button_frame.grid_columnconfigure(0,weight=1)
        self.button_frame.grid_columnconfigure(1,weight=1)
        self.button_frame.grid_rowconfigure(0,weight=1)

        # creating the button for the credit and the help window
        self.credits_button = ctk.CTkButton(self.button_frame, text="Help",command=self.help, width=100, state="disabled", fg_color=self.color, hover_color=self.hover_color)
        self.credits_button.grid(row=0,column=0,padx=2,pady=2, sticky="nswe")

        self.credits_button = ctk.CTkButton(self.button_frame, text="Credits",command=self.credits, width=100, fg_color=self.color, hover_color=self.hover_color,)
        self.credits_button.grid(row=0,column=1,padx=2,pady=2,sticky="nswe")
        if self.file_name != None:
            self.progress()


    def credits(self):
        # creating a credit frame with the different people involved in this project
        credits_window = ctk.CTkToplevel(fg_color="#19456F")
        credits_window.geometry("500x500")
        credits_window.title("Credits")

        credits_window.grid_columnconfigure(0, weight=1)

        title_label = ctk.CTkLabel(credits_window, text="A programm made by:", font=self.font20, text_color="white")
        title_label.grid(row=0, column=0, padx=20, pady=(40,30))

        credit_label = ctk.CTkLabel(credits_window, text="Elias Brugger\nTanish Acharya\nFelix Angerer", font=self.font20, text_color="white")
        credit_label.grid(row=1, column=0, padx=20, pady=20)

        credit_label = ctk.CTkLabel(credits_window, text="Special thanks to our testers:", font=self.font20, text_color="white")
        credit_label.grid(row=2, column=0, padx=20, pady=20)

        credit_label = ctk.CTkLabel(credits_window, text="Andrin Ganster\nAttila Pinter", font=self.font20, text_color="white")
        credit_label.grid(row=3, column=0, padx=20, pady=20)

        design_label = ctk.CTkLabel(credits_window, text="Logo and icon design:", font=self.font20, text_color="white")
        design_label.grid(row=5, column=0, padx=20, pady=20)

        design_label = ctk.CTkLabel(credits_window, text="Attila Pinter", font=self.font20, text_color="white")
        design_label.grid(row=6, column=0, padx=20, pady=20)        


    def progress(self):
        # creating a frame if there has already been a file learned
        self.learn_frame =ctk.CTkFrame(self.right_frame, border_width=1)
        self.learn_frame.grid(column=0, row=0, padx=20, pady=10, sticky="nswe",ipady=5)

        self.learn_frame.grid_columnconfigure(0,weight=1)

        self.learn_frame.grid_rowconfigure(0,weight=1)
        self.learn_frame.grid_rowconfigure(1,weight=1)
        self.learn_frame.grid_rowconfigure(2,weight=1)
        self.learn_frame.grid_rowconfigure(3,weight=1)

        # displaying informations from the file
        self.title_label = ctk.CTkLabel(self.learn_frame, text="last learned file:", font=self.font20, text_color=("black","white"))
        self.title_label.grid(column=0,columnspan=2, row=0, padx=20, pady=(10,5), sticky="w")

        self.file_label =ctk.CTkLabel(self.learn_frame, text="File:", text_color=("black","white"),font=self.font14)
        self.file_label.grid(column=0, row=1, padx=20, pady=0, sticky="w")
        
        self.file_label_input =ctk.CTkLabel(self.learn_frame, text=self.file_name, wraplength=80, text_color=("black","white"),font=self.font14)
        self.file_label_input.grid(column=1, row=1, padx=20, pady=0, sticky="w", columnspan=2)

        self.words_label =ctk.CTkLabel(self.learn_frame, text="Word amount:", text_color=("black","white"),font=self.font14)
        self.words_label.grid(column=0, row=2, padx=20, pady=0, sticky="w")
        
        self.words_label_input =ctk.CTkLabel(self.learn_frame, text=self.length, text_color=("black","white"),font=self.font14)
        self.words_label_input.grid(column=1, row=2, padx=20, pady=0, sticky="w")

        self.correct_label =ctk.CTkLabel(self.learn_frame, text="Correct words:", text_color=("black","white"),font=self.font14)
        self.correct_label.grid(column=0, row=3, padx=20, pady=0, sticky="w")   

        # checks if all words of the file are either in known or unknown and if not the difference will be added to unknown
        if self.known_number + self.unknown_number == self.length:
            pass
        else:
            self.unknown_number = self.length - self.known_number
        
        self.correct_label_input =ctk.CTkLabel(self.learn_frame, text=self.known_number, text_color=("black","white"),font=self.font14)
        self.correct_label_input.grid(column=1, row=3, padx=20, pady=0, sticky="w")

        
        self.incorrect_label =ctk.CTkLabel(self.learn_frame, text="Wrong words:", text_color=("black","white"),font=self.font14)
        self.incorrect_label.grid(column=0, row=4, padx=20, pady=(0,10), sticky="w")
        
        self.incorrect_label_input =ctk.CTkLabel(self.learn_frame, text=self.unknown_number, text_color=("black","white"),font=self.font14)
        self.incorrect_label_input.grid(column=1, row=4, padx=20, pady=(0,10), sticky="w")
    
    
    def new_file(self): # if new file btn pressed
        # opens the file creator
        self.new_file_btn_pressed = True


    def open_file(self):
        # asks for a csv file to learn
        self.filename = fd.askopenfilename()
        if self.filename != "" and self.filename.endswith(".csv"):
            # opens the choose_mode part
            self.open_file_btn_pressed = True  


    def help(self):
        # creating a toplevel for helpful information
        help_window = ctk.CTkToplevel(fg_color="#19456F")
        help_window.geometry("600x428")
        help_window.title("Help start_screen v0.0.3")

        help_window.grid_rowconfigure(0, weight=1)
        help_window.grid_columnconfigure(0, weight=1)
        img = ctk.CTkImage(light_image=Image.open("images\start_screen_v0.0.3.png"),size=(600,428))
        img_label = ctk.CTkLabel(help_window,text=None, image=img)
        img_label.grid(row=0, column=0, sticky="nswe", pady=(5,0), padx=2)

# for testing the individual program
if __name__ == "__main__":
    Start_Screen(ctk.CTk()).root.mainloop()