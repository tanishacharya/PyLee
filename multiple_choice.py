import customtkinter as ctk
from tkinter import messagebox
import csv
import random
import webbrowser

class Multiple_Choice:
    def __init__(self,root, word_random=0, word_or_def=1, total_time=None, word_time=None) -> None:
        # declairing all the basic variables from the selected settings
        self.total_time = total_time
        self.word_random= word_random
        self.word_or_def = word_or_def
        # checking if there is a time per word given 
        if word_time != None and word_time != "None":
            try:
                # tries to converts the string format of the selected setting into an int
                self.word_time = int(word_time.replace("s",""))
            except:
                pass
        else:
            self.word_time = None
        
        # basic window settings (window name, size, etc.)
        self.root = root
        self.root.geometry("780x520")
        self.root.title("Multiple Choice Beta v1.0.0")

        self.root.iconbitmap("images/PyLee_Logo_iconbitmap2.ico")

        ctk.set_appearance_mode("system")
        
        self.root.grid_columnconfigure(0,weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=100)

        # basic colors for the window
        self.color = "#1a4570"
        self.hover_color = "#3c638a"
        self.extra_color = "#1b6bad"
        #basic fonts and sizes for the window
        self.font14 = "Inter", 14
        self.font16 = "Inter", 16
        self.font20 = "Inter", 20
        self.font25 = "Inter", 25

        # variables for the timer
        self.time_sec = 0
        self.counting_word_time = 0

        # declairing the variables for the program to finish/go back
        self.not_enough_words2learn = False
        self.back=False
        self.finished = False

        # file path
        self.filename = "learn_list.csv"
        
        # variables to store the words from the list
        self.words2learn = {}
        self.known = {}
        self.unknown = {}

        # checking if the given file is accesable
        try:
            self.make_dict(file=self.filename)
        except FileNotFoundError:
            messagebox.showerror("File not found", f"Error: {self.filename} doesn't exist in this directory. (use \"cd saved_csv\" ")

        self.window()
    
    def window(self) -> None: # configures the window further

        # creates a menu_bar with back and help button
        self.menu_bar = ctk.CTkFrame(self.root, height=20, corner_radius=3, border_color="grey", border_width=1)
        self.menu_bar.grid(row=0, column=0, sticky="nwe")

        self.help_button = ctk.CTkButton(self.menu_bar, height=18, width=70,text="Help", fg_color="transparent", hover_color=self.hover_color, corner_radius=2, text_color=("black","white"), state="disabled")
        self.help_button.grid(row=0, column=0, padx=(20,5) ,pady=1)

        self.back_button = ctk.CTkButton(self.menu_bar, height=18, width=70,text="Back", fg_color="transparent", hover_color=self.hover_color, corner_radius=2, command=self.back_button_pressed, text_color=("black","white"))
        self.back_button.grid(row=0, column=1, padx=5 ,pady=1)
        
        #====================basic frame====================
        self.mainframe = ctk.CTkFrame(self.root)
        self.mainframe.grid(row=1,column=0,sticky="nswe", padx=5,pady=(40,80))
        self.mainframe.grid_propagate(False)

        self.mainframe.grid_rowconfigure(0, weight=1)

        self.mainframe.grid_columnconfigure(0, weight=1)
        self.mainframe.grid_columnconfigure(1, weight=7)


        #====================left frame====================
        self.left_frame = ctk.CTkFrame(self.mainframe)
        self.left_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nswe")

        self.left_frame.grid_columnconfigure(0, weight=1)
        self.left_frame.grid_propagate(False)


        #====================middle frame====================
        self.middle_frame = ctk.CTkFrame(self.mainframe)
        self.middle_frame.grid(row=0, column=1, padx=(0,30), pady=10, sticky="nswe")
        self.middle_frame.grid_propagate(False)

        self.middle_frame.grid_columnconfigure(0, weight=1)
        self.middle_frame.grid_rowconfigure(0,weight=1)
        self.middle_frame.grid_rowconfigure(1,weight=100)
        self.middle_frame.grid_rowconfigure(2,weight=1)



        self.question_label = ctk.CTkLabel(self.middle_frame, text="", font=self.font20, wraplength=300)
        self.question_label.grid(row=0, column=0, sticky="nswe", padx=5, pady=(10,0))

        # creates the frame where the actual questions and answeres will be displayed
        self.question_frame = ctk.CTkFrame(self.middle_frame, corner_radius=5)
        self.question_frame.grid(row=1, column=0, sticky="nswe", padx=20, pady=(10,20))
        self.question_frame.grid_propagate(False)

        self.question_frame.grid_rowconfigure(0,weight=1, minsize=1)
        self.question_frame.grid_rowconfigure(1,weight=1)
        self.question_frame.grid_rowconfigure(2,weight=1)
        self.question_frame.grid_rowconfigure(3,weight=1)
        self.question_frame.grid_rowconfigure(4,weight=1)
        self.question_frame.grid_rowconfigure(5,weight=1, minsize=1)

        # displays the fime learned of if a time limit has been selected displays the time left
        self.label_time = ctk.CTkLabel(self.left_frame, text="Time learned", text_color=("black","white"), font=self.font20)
        self.label_time.grid(row=0, pady=(20,5), padx=20,sticky="", column=0)

        self.time_label = ctk.CTkLabel(self.left_frame, text="00:00:00", font=self.font20, text_color=("black","white"))
        self.time_label.grid(row=1, pady=(5,20), padx=20,sticky="", column=0)

        # show how much of the file has been learned 
        self.progress_label = ctk.CTkLabel(self.left_frame, text="Progress", font=self.font20)
        self.progress_label.grid(row=2, column=0, sticky="", padx=10, pady=(20,5))

        self.pg1_speed = 50 / self.dict_size
        self.progressbar = ctk.CTkProgressBar(self.left_frame, mode="determinate", determinate_speed=self.pg1_speed, height=15, progress_color=self.color, corner_radius=5, border_width=2)
        self.progressbar.grid(row=3, pady=0, padx=20,sticky="we", column=0)
        self.progressbar.set(0)

        self.progress_int = 0
        self.len_words2learn = len(self.words2learn)
        self.progress_int_label = ctk.CTkLabel(self.left_frame, text=f"{round((self.progress_int/self.len_words2learn)*100)}%", font=self.font20)
        self.progress_int_label.grid(row=4, column=0, sticky="", padx=10, pady=(5,20))

        # checks if a time for the exercise has been selected
        if self.total_time != "None" and self.total_time != None:
            self.total_time = int(self.total_time.replace("min",""))
            
            self.time_sec = self.total_time * 60

            self.label_time.configure(text="Time left")

        # starts the clock and the excercise
        self.clock()
        self.clock_word_time()
        self.actual_multiple_choice()
        
    def actual_multiple_choice(self):
        # checks if there are words to learn left if not destroys the excercise window
        if len(self.words2learn) == 0:
            self.not_enough_words2learn = True
            self.mainframe.destroy()
            self.menu_bar.destroy()
        else:
            # else the question, answer and wrong possiblilities get declaired
            self.question, self.answer, self.possiblities = self.all_question()

            # tries to destroy the button to generate the new ones
            try:
                self.rb1.destroy()
                self.rb2.destroy()
                self.rb3.destroy()
                self.rb4.destroy()

            except:
                pass

            # displays the new answer
            self.question_label.configure(text=f"What does \"{self.question}\" mean?")

            # shuffles list and stores the answers in seperate variables
            self.possiblities.append(self.answer)
            while True:
                random.shuffle(self.possiblities)
                if len(self.possiblities) == 4 or self.possiblities[4] == self.answer:
                    break
                else:
                    continue
                
            # assigns the different answer prssibilities to the button variables
            self.a1 = self.possiblities[0]
            self.a2 = self.possiblities[1]
            self.a3 = self.possiblities[2]
            self.a4 = self.possiblities[3]


            # stores the users answer as a variable
            self.user_answer = ctk.StringVar()

            self.rb1 = ctk.CTkRadioButton(self.question_frame, text=self.a1, font=self.font16, variable=self.user_answer, value=self.a1, fg_color=self.color, radiobutton_height=26, radiobutton_width=26)
            self.rb1.grid(row=1, column=0, pady=10, sticky="nswe", padx=30)

            self.rb2 = ctk.CTkRadioButton(self.question_frame, text=self.a2, font=self.font16, variable=self.user_answer, value=self.a2, fg_color=self.color, radiobutton_height=26, radiobutton_width=26, height=26)
            self.rb2.grid(row=2, column=0, pady=10, sticky="nswe", padx=30)

            self.rb3 = ctk.CTkRadioButton(self.question_frame, text=self.a3, font=self.font16, variable=self.user_answer, value=self.a3, fg_color=self.color, radiobutton_height=26, radiobutton_width=26, height=26)
            self.rb3.grid(row=3, column=0, pady=10, sticky="nswe", padx=30)

            self.rb4 = ctk.CTkRadioButton(self.question_frame, text=self.a4, font=self.font16, variable=self.user_answer, value=self.a4, fg_color=self.color, radiobutton_height=26, radiobutton_width=26, height=26)
            self.rb4.grid(row=4, column=0, pady=10, sticky="nswe", padx=30)




            # creates a frame for the "answer" and "next" button
            self.button_frame = ctk.CTkFrame(self.middle_frame, height=28)
            self.button_frame.grid(row=3, column=0, pady=(15, 0), sticky="we")

            self.button_frame.grid_rowconfigure(0, weight=1)
            self.button_frame.grid_columnconfigure(0, weight=1)

            self.answer_btn = ctk.CTkButton(self.button_frame, text="Answer", font=self.font16, fg_color=self.color, hover_color=self.hover_color, command=self.answer_btn_clicked)
            self.answer_btn.grid(row=0, column=0, sticky="ew")

    def make_dict(self, file) -> None:
        # gets the words stored in the csv file and transformes them into a dict depending on which meaning of the word should come first
        if self.word_or_def == 2:
            with open(file) as self.something:
                reader = csv.DictReader(self.something)
                for row in reader:
                    self.words2learn.update({row["word"]: row["definition"]})
        else:
            with open(file) as self.something:
                reader = csv.DictReader(self.something)
                for row in reader:
                    self.words2learn.update({row["definition"]: row["word"]})
        self.dict_size = len(list(self.words2learn))

    def all_question(self) -> str: #form question and 4 answer possibilities

        while True:
            if self.word_random == 1: # checks if the word should be chosen randomly
                current_question = random.choice(list(self.words2learn.keys()))
                current_answer = self.words2learn[current_question]
            else: # else selects the next word form the dict
                current_question = list(self.words2learn)[0]
                current_answer = self.words2learn[current_question]
            if current_answer not in self.known:    # word shouldn't be in the known words
                break
            else:
                continue
        answer_choices = []
        temp_dict = self.words2learn | self.known   # "|" is the merge operator for dicts
        #generate answer possibilities and stores them in a list
        x = 0
        while x != 3:
            random_word = random.choice(list(temp_dict.values()))
            if random_word != current_answer and random_word not in answer_choices:
                answer_choices.append(random_word)
                x += 1
                continue

            else:
                continue
        
        return current_question, current_answer, answer_choices

    def answer_btn_clicked(self):
        # destroys the answer button
        self.answer_btn.destroy()

        # reveals the answer
        self.question_label.configure(text=f"\"{self.question}\" means \"{self.answer}\"")

        if self.user_answer.get() == self.answer: # checks if the answer was correct$

            # updates the progress label and progress bar
            self.progress_int += 1
            self.progress_int_label.configure(text=f"{round((self.progress_int/self.len_words2learn)*100)}%")
            self.progressbar.step()

            # saves the word as known
            self.known.update({self.question: self.answer})

            # deletes the word from the dict of words2learn
            del self.words2learn[self.question]

            # continues the learning process
            self.actual_multiple_choice()

            

        else:
            # saves the word as unknown
            self.unknown[self.answer] = self.question

            # deletes the word from the dict of words2learn
            del self.words2learn[self.question]

            self.rb1.configure(state="disabled")
            self.rb2.configure(state="disabled")
            self.rb3.configure(state="disabled")
            self.rb4.configure(state="disabled")

            # runs through the answer options and selects the one which would have been correct
            for button in [self.rb1, self.rb2, self.rb3, self.rb4]:
                if button.cget("text") == self.answer:
                    button.select()
                    button.configure(fg_color="red")
            # creates the continue button to move on 
            self.continue_btn = ctk.CTkButton(self.button_frame, text="Continue", font=self.font16, fg_color=self.color, hover_color=self.hover_color, command=self.actual_multiple_choice)
            self.continue_btn.grid(row=0, column=0, sticky="nsew")
 
    def known_unknown_get(self): # returns the known and unknown dicts to be displyed in the end screen
        return self.known, self.unknown  

    def back_button_pressed(self): # opens the choose mode program
        self.back = True

    def clock(self):
        if self.total_time == "None" or self.total_time == None: # checks if a time for the excercise has been selected
            # if not adds each second 1 to the time_sec 
            self.time_sec += 1
            # splits the seconds into minutes and hous 
            seconds = self.time_sec
            seconds = seconds % (24 * 3600)
            hour = seconds // 3600
            seconds %= 3600
            minutes = seconds // 60
            seconds %= 60
            # conigures the label on how much time has passed
            try:
                self.time_label.configure(text="%02d:%02d:%02d" % (hour, minutes, seconds))
            except:
                pass
            # calls the clock again after 1 second
            self.root.after(1000, self.clock)
        else:
            # else the time for the excersice will be counted down in seconds
            self.time_sec -= 1
            # splits the seconds left into minutes and hours
            seconds = self.time_sec
            seconds = seconds % (24 * 3600)
            hour = seconds // 3600
            seconds %= 3600
            minutes = seconds // 60
            seconds %= 60
            # displayes the time left 
            self.time_label.configure(text="%02d:%02d:%02d" % (hour, minutes, seconds))

            if self.time_sec == 0:# if there isn't any time left closes the program
                self.finished = True
                self.mainframe.destroy()
                self.menu_bar.destroy()
                
            else:
                # else calls the function again after 1 second
                self.root.after(1000, self.clock)

    def clock_word_time(self):
        # checks if there has been a time selected for each word
        if self.word_time != None:
            # creates a ne progress bar to display how much time is left for the word
            self.word_progressbar = ctk.CTkProgressBar(self.left_frame, height=10,mode="determinate", progress_color=self.color, corner_radius=5, border_width=2)
            self.word_progressbar.grid(row=5, column=0, padx=40,pady=(40,0))
            self.word_progressbar.set(1)
            # counts down on the time left for the word
            self.counting_word_time -= 1


            # configures the progress bar
            self.word_progressbar.set(1/self.word_time*self.counting_word_time)


            if self.counting_word_time <= 0: # if there isn't any time left moves on and starts the word selcection process
                self.actual_multiple_choice()
            # calls the function again after 1 seconf
            self.root.after(1000, self.clock_word_time)


if __name__ == "__main__":
    mc = Multiple_Choice(ctk.CTk())
    mc.root.mainloop()