import customtkinter as ctk
from tkinter import messagebox
import csv
import re
from tkinter import filedialog as fd
import os

class File_Menu:
    def __init__(self, root):

        # configuring the main components of the window
        self.root = root
        self.root.title("PyLee File Creator Beta v1.0.0")
        self.root.geometry("780x520")
        self.root.iconbitmap("images/PyLee_Logo_iconbitmap2.ico")

        # setting up the basic structure
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")

        self.root.grid_columnconfigure(0,weight=1)
        self.root.grid_rowconfigure(1,weight=100)

        # creating an extra frame for everything file_menu
        self.root_frame = ctk.CTkFrame(self.root, corner_radius=0)
        self.root_frame.grid(row=1,column=0,sticky="nswe")


        # declaring the variables for the program to go save the file and to go back 
        self.save_quit_btn = False
        self.back = False

        # declaring basic font and color variables
        self.font = "Inter"
        self.color = "#1a4570"
        self.hover_color = "#3c638a"
        self.extra_color = "#1b6bad"

        self.file_menu()

          
    def file_menu(self): # makes the window
        
        # creating a menu bar
        self.menu_bar = ctk.CTkFrame(self.root, height=20, corner_radius=3, border_width=1)
        self.menu_bar.grid(row=0, column=0, sticky="nwe")

        self.help_button = ctk.CTkButton(self.menu_bar, height=18, width=70,text="Help", fg_color="transparent", hover_color=self.hover_color, corner_radius=2, state="disabled", text_color=("black","white"))
        self.help_button.grid(row=0, column=0, padx=(20,5) ,pady=1)

        self.back_button = ctk.CTkButton(self.menu_bar, height=18, width=70,text="Back", fg_color="transparent", hover_color=self.hover_color, corner_radius=2, command=self.back_button_pressed, text_color=("black","white"))
        self.back_button.grid(row=0, column=1, padx=5 ,pady=1)

        self.open_button = ctk.CTkButton(self.menu_bar, height=18, width=70,text="Open File", fg_color="transparent", hover_color=self.hover_color, corner_radius=2, command=self.open_file, text_color=("black","white"))
        self.open_button.grid(row=0, column=2, padx=5 ,pady=1)
    

        self.file_name_without_csv = ctk.StringVar()
        
        # creating main_frame in main window
        self.main_frame = ctk.CTkFrame(self.root_frame)
        self.main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # creating title_frame for getting file name
        self.title_frame = ctk.CTkFrame(self.main_frame, height=100)
        self.title_frame.pack(padx=10, pady=10, fill="x")

        # creating labels and an entry for the name to save the list as
        self.save_as_text = ctk.CTkLabel(self.title_frame, text="Save list as", font=(self.font, 20), anchor="e", text_color=("black","white"))
        self.save_as_text.grid(column=1, row=0, padx=10)

        self.file_entry = ctk.CTkEntry(self.title_frame, font=(self.font, 15), textvariable=self.file_name_without_csv)
        self.file_entry.grid(column=2, row=0,)

        self.csv_text = ctk.CTkLabel(self.title_frame, text=" .csv", font=(self.font, 20), anchor="w", width=50, text_color=("black","white"))
        self.csv_text.grid(column=3, row=0,)

        # creating the textbox to edit the list
        self.textbox = ctk.CTkTextbox(self.main_frame, font=(self.font, 18), activate_scrollbars=True)
        self.textbox.pack(padx=10, pady=10, side="left", fill="both", expand=True)

        # creating the frame to add words to the list
        self.edit_frame = ctk.CTkFrame(self.main_frame)
        self.edit_frame.pack(padx=10, pady=10, side="right", fill="both", expand=True)
  
        # creating a frame under the mainframe for the save button because tk.pack() is trash
        self.bottom_frame = ctk.CTkFrame(self.root_frame, height=50, width=760)
        self.bottom_frame.pack(pady=5)

        # creating the save button !!!command!!!
        self.save_button = ctk.CTkButton(self.bottom_frame, text="Save and quit", font=(self.font, 25), command=self.save_quit, fg_color=self.color, hover_color=self.hover_color, text_color=("white","white"))
        self.save_button.pack()

        # creating the entrys to add words
        self.word_entry = ctk.CTkEntry(self.edit_frame, placeholder_text="word", font=(self.font, 20), width=200)
        self.word_entry.pack(pady=20)
        self.word_entry.bind('<Return>', self.word_entry_enter)

        self.definition_entry = ctk.CTkEntry(self.edit_frame, placeholder_text="definition", font=(self.font, 20), width=200)
        self.definition_entry.pack(pady=20)
        self.definition_entry.bind('<Return>', self.add_word)

        # creating the button to add words
        self.add_button = ctk.CTkButton(self.edit_frame, text="Add", font=(self.font, 20), command=self.add_word, fg_color=self.color, hover_color=self.hover_color)
        self.add_button.pack(pady=20)


    def update(self):
        # creates the variables file_dict where the the file will be saved as a dictionary
        self.file_dict= {}
        # gets everything inside the textbox and strips
        rows = self.textbox.get(1.0, ctk.END).strip().split("\n")
        for row in rows:
            if row:
                # splits the line into two words based on the comma and the quotation marks
                definition, word = row.split('","')
                self.file_dict[definition.strip('"')] = word.strip('"')
        

    def add_word(self, event=None):
        # gets th the values in the word and definition entry
        self.word = self.word_entry.get()
        self.definition = self.definition_entry.get()

        # checks for extra quotation marks that could brake the program later on and replaces them with single quotes
        if '"' in self.definition:
            self.definition = self.definition.replace('"',"'")
        if '"' in self.word:
            self.word = self.word.replace('"',"'")

        # inserts the values in the textbox
        self.textbox.insert(ctk.END,text=f'"{self.definition}","{self.word}"\n')

        # clears the word and definition entry
        self.word_entry.delete(0,"end")
        self.definition_entry.delete(0,"end")
        # focuses the word entry so the user can directly continue writing
        self.word_entry.focus()

        
    def save_quit(self):
        
        self.save_quit_btn = True

        self.update()

        # checks if in the chosen file name are any not allowed characters
        if re.search(r"^[\w\-. ]+$", self.file_name_without_csv.get()):
            
            # saves the full directory of the file name for the following program
            target_file = "saved_csv/" + self.file_name_without_csv.get() + ".csv"       

            # creates a new file with the given name and words
            with open(target_file, "w", newline="") as target:
                writer = csv.DictWriter(target, ["definition", "word"])
                writer.writeheader()
                for row in self.file_dict:
                    writer.writerow({"definition":row,"word":self.file_dict[row]})

        else:
            # shows an error if the file name contains any not allowed characters
            messagebox.showerror("Error", f"Invalid file name (can't be blank or contain certain special characters)")
    
    
    def back_button_pressed(self):
        # sets the back variable to True so that the main program file can go back to the start screen
        self.back = True
    
    
    def word_entry_enter(self, event=None):
        # sets the definition entry in focus to make the inputing of words more convenient
        self.definition_entry.focus()

    def open_file(self):
        # opens an already existing file so that it can be edited
        self.filename = fd.askopenfilename()
        if self.filename != "":
            with open(self.filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.textbox.insert(ctk.END,text=f'"{row["definition"]}","{row["word"]}"\n')
                self.file_entry.insert(ctk.END,os.path.basename(os.path.normpath(self.filename)).removesuffix(".csv"))


# for individual testing of this file
if __name__ == "__main__":
    File_Menu(ctk.CTk()).root.mainloop()
    