import customtkinter as ctk
from tkinter import messagebox
import csv


class Choose_Mode():
    def __init__(self,root, filename="learn_list.csv"):

        # assigning the variables from the main program to a variable
        self.file_name = filename
        
        # configuring the main values for the window
        self.root = root
        self.root.title("Choose Mode Pylee Beta v1.0.0")
        self.root.geometry("780x520")
        self.root.minsize(780, 520)
        ctk.set_appearance_mode("system")
        self.root.iconbitmap("images/PyLee_Logo_iconbitmap2.ico")
        
        self.root.grid_columnconfigure(0,weight=1)
        self.root.grid_rowconfigure(0,weight=1)
        self.root.grid_rowconfigure(1,weight=100)

        # creating the frame for the choose_mode program
        self.root_frame = ctk.CTkFrame(self.root)

        self.root_frame.grid_columnconfigure(0, weight=1)
        self.root_frame.grid_columnconfigure(1, weight=5)
        self.root_frame.grid_columnconfigure(2, weight=1,minsize=5)

        self.root_frame.grid_rowconfigure(0, weight=1)

        # defining the basic fonts and colors
        self.font18 = "Inter", 18
        self.font = "Inter", 14
        self.font12 = "Inter", 12
        
        self.color = "#1a4570"
        self.hover_color = "#3c638a"
        self.extra_color = "#1b6bad"

        # definint variables for the file, mode which has been selected, the start lerning button and the back button
        self.file = {}
        self.mode = "" # which btn has been pressed?
        self.start_learning_btn_pressed = False
        self.back = False


        self.window()


    def window(self):
        
        # creating the menu bar for back and help
        self.menu_bar = ctk.CTkFrame(self.root, height=20, corner_radius=3, border_color="grey", border_width=1)
        self.menu_bar.grid(row=0, column=0, sticky="nwe")

        self.help_button = ctk.CTkButton(self.menu_bar, height=18, width=70,text="Help", fg_color="transparent", hover_color=self.hover_color, corner_radius=2, text_color=("black","white"),state="disabled")
        self.help_button.grid(row=0, column=0, padx=(20,5) ,pady=1)

        self.back_button = ctk.CTkButton(self.menu_bar, height=18, width=70,text="Back", fg_color="transparent", hover_color=self.hover_color, corner_radius=2, command=self.back_button_pressed, text_color=("black","white"))
        self.back_button.grid(row=0, column=1, padx=5 ,pady=1)

        # creating a frame for the different modes on the left side
        self.frame_left = ctk.CTkFrame(self.root_frame, corner_radius=7)
        self.frame_left.grid(row=0, column=0, padx=0, pady=10, sticky="nswe")

        self.frame_left.grid_columnconfigure(0, weight=1)

        self.frame_left.grid_rowconfigure(0, weight=1)
        self.frame_left.grid_rowconfigure(1, weight=1)
        self.frame_left.grid_rowconfigure(2, weight=1)
        self.frame_left.grid_rowconfigure(3, weight=1)
        self.frame_left.grid_rowconfigure(4, weight=1)
        self.frame_left.grid_rowconfigure(5, minsize=20, weight=5)
        self.frame_left.grid_rowconfigure(6, weight=1)

   

        # creating the title label
        self.label_right = ctk.CTkLabel(self.frame_left, text="Choose Mode", font=self.font18, text_color=("black","white"))
        self.label_right.grid(row=0, column=0, padx=30, pady=25, sticky="nswe")

        # creating diffrent buttons for modes
        self.button_mode1 = ctk.CTkButton(self.frame_left, text="Flash Cards", height=35, width=140, command=self.mode1, font=self.font, fg_color=self.color, hover_color=self.hover_color, text_color=("white","white"))
        self.button_mode1.grid(row=1, column=0, padx=30, pady=0, sticky="we")

        self.button_mode2 = ctk.CTkButton(self.frame_left, text="Multiple Choice", height=35, width=140, command=self.mode2, font=self.font, fg_color=self.color, hover_color=self.hover_color, text_color=("white","white"))
        self.button_mode2.grid(row=2, column=0, padx=30, pady=0, sticky="we")

        self.button_mode3 = ctk.CTkButton(self.frame_left, text="Quiz", height=35, width=140, command=self.mode3, font=self.font, fg_color=self.color, hover_color=self.hover_color, text_color=("white","white"))
        self.button_mode3.grid(row=3, column=0, padx=30, pady=0, sticky="we")

        self.button_mode4 = ctk.CTkButton(self.frame_left, text="Match", height=35, width=140, command=self.mode4, font=self.font, fg_color=self.color, hover_color=self.hover_color, text_color=("white","white"))
        self.button_mode4.grid(row=4, column=0, padx=30, pady=0, sticky="we")
        
        self.button_start= ctk.CTkButton(self.frame_left, text="Start learning", height=35, width=140, command=self.start_learning, font=self.font, fg_color=self.color, hover_color=self.hover_color, state="disabled", text_color=("white","white"))
        self.button_start.grid(row=6, column=0, padx=30, pady=0, sticky="we")
    
        # creating the frame in the middle for the settings frame and the words from the list
        self.frame_middle = ctk.CTkFrame(self.root_frame, height=200, width=200, corner_radius=15)
        self.frame_middle.grid(row=0,column=1, padx=(10,0), pady=10, sticky="nswe")
        
        self.frame_middle.rowconfigure(0,weight=10)
        self.frame_middle.rowconfigure(1, weight=1)
        self.frame_middle.rowconfigure(3, weight=10)

        self.frame_middle.columnconfigure(0, weight=1)

        # creating the settings frame
        self.settings_frame = ctk.CTkFrame(self.frame_middle, border_width=2, corner_radius=0)
        self.settings_frame.grid(column=0,sticky="nswe",padx=0,pady=0)

        self.settings_frame.grid_columnconfigure(0, weight=1)
        self.settings_frame.grid_columnconfigure(1, weight=1)
        self.settings_frame.grid_columnconfigure(2, weight=2)

        self.settings_frame.grid_rowconfigure(0, weight=1)
        self.settings_frame.grid_rowconfigure(1, weight=1)
        self.settings_frame.grid_rowconfigure(2, weight=1)
        self.settings_frame.grid_rowconfigure(3, weight=1)
        self.settings_frame.grid_rowconfigure(4, weight=1)
        self.settings_frame.grid_rowconfigure(5, weight=1)
        self.settings_frame.grid_rowconfigure(6, weight=1)
        self.settings_frame.grid_rowconfigure(7, weight=1)
        self.settings_frame.grid_rowconfigure(8, weight=1)

        #==================== first column ====================
        self.case_sensitive = ctk.CTkSwitch(self.settings_frame, text="case insensitive", font=self.font12, progress_color=self.color, text_color=("black","white"))
        self.case_sensitive.grid(row=0, column=0,padx=(40,0), pady=(20,2.5), sticky="nswe")

        self.minor_mistakes = ctk.CTkSwitch(self.settings_frame, text="accept minor mistakes", font=self.font12, progress_color=self.color, text_color=("black","white"))
        self.minor_mistakes.grid(row=1, column=0,padx=(40,0), pady=2.5, sticky="nswe")
        self.minor_mistakes.configure(state="disabled")

        self.autocheck = ctk.CTkSwitch(self.settings_frame, text="autocheck answer",font=self.font12, progress_color=self.color, text_color=("black","white"))
        self.autocheck.grid(row=2, column=0,padx=(40,0), pady=2.5, sticky="nswe")
        self.autocheck.configure(state="disabled")

        self.ask_word_known = ctk.CTkSwitch(self.settings_frame, text="ask if word was known", font=self.font12, progress_color=self.color, text_color=("black","white"))
        self.ask_word_known.grid(row=3, column=0,padx=(40,0), pady=(2.5,10), sticky="nswe")
        self.ask_word_known.configure(state="disabled")
        
        #==================== second column ====================
        
        self.time_total_label = ctk.CTkLabel(self.settings_frame, text="Total time for exercises", font=self.font12, text_color=("black","white"),justify="left")
        self.time_total_label.grid(row=0, column=1, padx=(0,20), pady=5, sticky="ns")

        self.time_total = ctk.CTkOptionMenu(self.settings_frame, values=["None","5min","10min","15min","20min"], width=105,height=24,dynamic_resizing=True, fg_color=self.color, button_color=self.color, button_hover_color=self.hover_color, text_color=("white","white"))
        self.time_total.grid(row=1, column=1, padx=(0,20), pady=5, sticky="nswe")
        self.time_total.configure(state="disabled")

        self.time_word_label = ctk.CTkLabel(self.settings_frame, text="Time per word", font=self.font12, text_color=("black","white"),justify="left")
        self.time_word_label.grid(row=2, column=1, padx=(0,20), pady=5, sticky="ns")

        self.time_word = ctk.CTkOptionMenu(self.settings_frame, values=["None","10s","20s","30s","60s"],width=105,height=24, dynamic_resizing=True, fg_color=self.color, button_color=self.color, button_hover_color=self.hover_color, text_color=("white","white"))
        self.time_word.grid(row=3, column=1, padx=(0,20), pady=5, sticky="nswe")
        self.time_word.configure(state="disabled")

        #==================== third column ====================

        self.FirstVar = ctk.IntVar()
        self.RandomVar = ctk.IntVar()

        self.first_radio_button1 = ctk.CTkRadioButton(self.settings_frame, text="learn definition",radiobutton_height=20,radiobutton_width=20,variable=self.FirstVar, value=1, font=self.font12, fg_color=self.color, hover_color=self.hover_color, text_color=("black","white"))
        self.first_radio_button1.grid(row=1, column=2, padx=(20,3), pady=0, sticky="nswe")
        self.first_radio_button1.invoke()

        self.first_radio_button2 = ctk.CTkRadioButton(self.settings_frame, text="learn word",radiobutton_height=20,radiobutton_width=20,variable=self.FirstVar, value=2, font=self.font12, fg_color=self.color, hover_color=self.hover_color, text_color=("black","white"))
        self.first_radio_button2.grid(row=2, column=2, padx=(20,3), pady=0, sticky="nswe")

        self.RandomCheckbox = ctk.CTkCheckBox(self.settings_frame, text="Random Order",checkbox_height=20,checkbox_width=20, variable=self.RandomVar, font=self.font12, fg_color=self.color, hover_color=self.hover_color, text_color=("black","white"))
        self.RandomCheckbox.grid(row=3, column=2, padx=(20,3), pady=0, sticky="nswe")



        #==================== button middle row====================

        self.get_dict()

        self.word_split_label = ctk.CTkLabel(self.settings_frame, text="How much do you want to learn at a time",font=self.font, text_color=("black","white"))
        self.word_split_label.grid(row=5, columnspan=3, column=0, padx=40, pady=(10,0), sticky="nswe")

        self.word_split = ctk.CTkSegmentedButton(self.settings_frame,values=["All","Half","Thirds","Fourths"], dynamic_resizing=True, command=self.dict_split, selected_color=self.color, selected_hover_color=self.hover_color, text_color=("white","white"))
        self.word_split.grid(row=6, columnspan=3, column=0, padx=40, pady=0, sticky="nswe")
        self.word_split.set("All")
        self.dict_split("All")

        self.word_part_label = ctk.CTkLabel(self.settings_frame, text="Which part would you like to learn",font=self.font, text_color=("black","white"))
        self.word_part_label.grid(row=7, columnspan=3, column=0, padx=40, pady=0, sticky="")

        self.word_part = ctk.CTkSegmentedButton(self.settings_frame,values=["1/1"], dynamic_resizing=True, command=self.update_textbox, selected_color=self.color, selected_hover_color=self.hover_color, text_color=("white","white"))
        self.word_part.grid(row=8, columnspan=3, column=0, padx=40, pady=(0,10), sticky="nsew")
        self.word_part.set("1/1")
        self.update_textbox("1/1")

        self.root_frame.grid(row=1, column=0,sticky="nswe")


    def dict_split(self, value):
        # declaring variables for the different word amounts
        self.mem_file1 = {}
        self.mem_file2 = {}
        self.mem_file3 = {}
        self.mem_file4 ={}

        # spliting the words into four equal parts and assigning them to four variables
        if value == "Fourths":
            self.mem_file1 = list(self.file)[0:int(len(self.file)/4)]
            self.mem_file2 = list(self.file)[int(len(self.file)/4):int((len(self.file)/4)*2)]
            self.mem_file3 = list(self.file)[int((len(self.file)/4)*2):int((len(self.file)/4)*3)]
            self.mem_file4 = list(self.file)[int((len(self.file)/4)*3):]
            self.word_part.destroy()

            # creating a segmented button with the different four parts of the file
            self.word_part = ctk.CTkSegmentedButton(self.settings_frame,values=["1/4", "2/4", "3/4", "4/4"], dynamic_resizing=True, command=self.update_textbox, selected_color=self.color, selected_hover_color=self.hover_color, text_color=("white","white"))
            self.word_part.grid(row=8, columnspan=3, column=0, padx=40, pady=(0,10), sticky="nsew")
            self.word_part.set("1/4")
            self.update_textbox("1/4")

        # spliting the words int thirds and assigning them to three variables
        elif value == "Thirds":
            self.mem_file1 = list(self.file)[0:int(len(self.file)/3)]
            self.mem_file2 = list(self.file)[int(len(self.file)/3):int((len(self.file)/3)*2)]
            self.mem_file3 = list(self.file)[int((len(self.file)/3)*2):]
            self.word_part.destroy()

            # creating a segmented button with the three different options
            self.word_part = ctk.CTkSegmentedButton(self.settings_frame,values=["1/3", "2/3", "3/3"], dynamic_resizing=True, command=self.update_textbox, selected_color=self.color, selected_hover_color=self.hover_color, text_color=("white","white"))
            self.word_part.grid(row=8, columnspan=3, column=0, padx=40, pady=(0,10), sticky="nsew")
            self.word_part.set("1/3")
            self.update_textbox("1/3")

        # spliting the words into two halfs and assigning them to two variables
        elif value == "Half":
            self.mem_file1 = list(self.file)[0:int(len(self.file)/2)]
            self.mem_file2 = list(self.file)[int(len(self.file)/2):]
            self.word_part.destroy()

            # creating a segmented button with the two words amount options
            self.word_part = ctk.CTkSegmentedButton(self.settings_frame,values=["1/2", "2/2"], dynamic_resizing=True, command=self.update_textbox, selected_color=self.color, selected_hover_color=self.hover_color, text_color=("white","white"))
            self.word_part.grid(row=8, columnspan=3, column=0, padx=40, pady=(0,10), sticky="nsew")
            self.word_part.set("1/2")
            self.update_textbox("1/2")
        
        # just displaying all of the words
        elif value == "All":
            try:
                self.word_part.destroy()
            except AttributeError:
                pass
            self.mem_file1 = self.file

            # creating a segmented button with only one selected option
            self.word_part = ctk.CTkSegmentedButton(self.settings_frame,values=["1/1"], dynamic_resizing=True, command=self.update_textbox, selected_color=self.color, selected_hover_color=self.hover_color, text_color=("white","white"))
            self.word_part.grid(row=8, columnspan=3, column=0, padx=40, pady=(0,10), sticky="nsew")
            self.word_part.set("1/1")
            self.update_textbox("1/1")
            
            
    def update_textbox(self, part):
        # tries to delete the textbox label which displayes the word amount
        try:
            self.textbox_label.destroy()
        except AttributeError:
            pass
        
        # mathes the selected list part with the mem variables 
        match part:
            case "1/1" | "1/2" | "1/3" | "1/4":
                self.learn_file = self.mem_file1
            case "2/2" | "2/3" | "2/4":
                self.learn_file = self.mem_file2
            case "3/3" | "3/4":
                self.learn_file = self.mem_file3
            case "4/4":
                self.learn_file = self.mem_file4

        # creates a label which displayes the amount of words selected
        self.textbox_label = ctk.CTkLabel(self.frame_middle, font=self.font,text=f"Selected word amount {len(self.learn_file)} words:", text_color=("black","white"))
        self.textbox_label.grid(row=2, column=0,sticky="nswe")

        # creates a textbox with the chosen words inside
        self.textbox = ctk.CTkTextbox(self.frame_middle, font=self.font,padx=20, height=160)
        self.textbox.grid(row=3,column=0, sticky="nswe", padx=40, pady=10)
        self.textbox.insert(ctk.END,"definition, word\n")
        for line in self.learn_file:
            self.textbox.insert(ctk.END,f"{line} : {self.file[line]}\n")
        self.textbox.configure(state="disabled")


    def get_dict(self): # gets the words from the selected file and puts them into a variable
        with open(self.file_name, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.file[row["word"]] = row["definition"]
    

    def mode1(self): 
        
        # changes color to show which mode is selected
        self.button_mode1.configure(fg_color=self.extra_color)
        self.button_mode2.configure(fg_color=self.color)
        self.button_mode3.configure(fg_color=self.color)
        self.button_mode4.configure(fg_color=self.color)

        # enables the start button
        self.button_start.configure(state="normal")

        # activates and deactevates options based on the selected mode
        self.case_sensitive.deselect()
        self.case_sensitive.configure(state="disabled")
        self.minor_mistakes.deselect()
        self.minor_mistakes.configure(state="disabled")
        self.autocheck.deselect()
        self.autocheck.configure(state="disabled")
        self.ask_word_known.configure(state="normal")

        self.time_total.set("None")
        self.time_total.configure(state="disabled")
        self.time_word.configure(state="normal")

        self.first_radio_button1.configure(state="normal")
        self.first_radio_button2.configure(state="normal")
        self.RandomCheckbox.configure(state="normal")

        # sets mode variable on the selected mode
        self.mode = "flashcards"


    def mode2(self):

        # changes color to show which mode is selected
        self.button_mode1.configure(fg_color=self.color)
        self.button_mode2.configure(fg_color=self.extra_color)
        self.button_mode3.configure(fg_color=self.color)
        self.button_mode4.configure(fg_color=self.color)
        if len(list(self.file)) < 4:
            messagebox.showerror("Invalid list size", "Multiple choice needs at least 4 words in the file")
        else:

            # enables the start button
            self.button_start.configure(state="normal")
            
            # activates and deactevates options based on the selected mode
            self.case_sensitive.deselect()
            self.case_sensitive.configure(state="disabled")
            
            self.minor_mistakes.deselect()
            self.minor_mistakes.configure(state="disabled")

            self.autocheck.select()
            self.autocheck.configure(state="disabled")
            
            self.ask_word_known.deselect()
            self.ask_word_known.configure(state="disabled")

            self.time_word.configure(state="disabled")#problem with the skipping of words
            
            self.time_total.configure(state="normal")

            self.first_radio_button1.configure(state="normal")
            self.first_radio_button2.configure(state="normal")
            self.RandomCheckbox.configure(state="normal")

            # sets mode variable on the selected mode
            self.mode = "multiple choice"


    def mode3(self):

        # changes color to show which mode is selected
        self.button_mode1.configure(fg_color=self.color)
        self.button_mode2.configure(fg_color=self.color)
        self.button_mode3.configure(fg_color=self.extra_color)
        self.button_mode4.configure(fg_color=self.color)

        # enables the start button
        self.button_start.configure(state="normal")

        # activates and deactevates options based on the selected mode
        self.case_sensitive.configure(state="normal")
        
        self.minor_mistakes.configure(state="normal")
        
        self.autocheck.configure(state="normal")

        self.ask_word_known.deselect()
        self.ask_word_known.configure(state="disabled")
        
        self.time_total.configure(state="normal")
        self.time_word.configure(state="normal")
        
        self.first_radio_button1.configure(state="normal")
        self.first_radio_button2.configure(state="normal")
        self.RandomCheckbox.configure(state="normal")

        # sets mode variable on the selected mode
        self.mode = "quiz"


    def mode4(self):

        # changes color to show which mode is selected
        self.button_mode1.configure(fg_color=self.color)
        self.button_mode2.configure(fg_color=self.color)
        self.button_mode3.configure(fg_color=self.color)
        self.button_mode4.configure(fg_color=self.extra_color)

        # enables the start button
        self.button_start.configure(state="normal")

        # activates and deactevates options based on the selected mode
        self.case_sensitive.deselect()
        self.case_sensitive.configure(state="disabled")

        self.minor_mistakes.deselect()
        self.minor_mistakes.configure(state="disabled")

        self.autocheck.select()
        self.autocheck.configure(state="disabled")

        self.ask_word_known.deselect()
        self.ask_word_known.configure(state="disabled")

        self.time_total.configure(state="normal")
        self.time_word.set("None")
        self.time_word.configure(state="disabled")

        self.first_radio_button1.configure(state="normal")
        self.first_radio_button2.configure(state="normal")
        self.RandomCheckbox.configure(state="normal")

        # sets mode variable on the selected mode
        self.mode = "match"


    def start_learning(self):
        
        # writes the selected word amount into a seperat csv file depending on definiton or word first
        with open("learn_list.csv", "w", newline="") as target:
            if self.FirstVar.get() == 1:
                writer = csv.DictWriter(target, ["definition", "word"])
                writer.writeheader()
                for row in self.learn_file:
                    writer.writerow({"definition":row,"word":self.file[row]})
                print("finished1")

            elif self.FirstVar.get() == 2:
                writer = csv.DictWriter(target, ["word", "definition"])
                writer.writeheader()
                for row in self.learn_file:
                    writer.writerow({"word":self.file[row], "definition":row})
                print("finished2")
        
        # sets start variable on True which should start the selected learning mode
        self.start_learning_btn_pressed = True


    def get_values(self): # function returns the selected setting variables to the main program file
        return self.case_sensitive.get(),self.FirstVar.get(), self.RandomVar.get(), len(list(self.file)), self.file_name, self.time_total.get(), self.time_word.get(), self.minor_mistakes.get(), self.autocheck.get()


    def back_button_pressed(self): # returns to the start screen
        self.back = True

if __name__ == "__main__":
    Choose_Mode(ctk.CTk()).root.mainloop()