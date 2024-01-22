import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import csv
import random

class learning_frame:
    def __init__(self, root, word_random=0, Case=0, First=1, total_time=None, word_time=None, minor_mistakes=0, auto_check=0):
        
        # checks if a time limit per word has been set and then changes the string with the s for seconds to an integer
        if word_time != None and word_time != "None":
            try:
                self.word_time = int(word_time.replace("s",""))
            except:
                pass
        else:
            self.word_time = None

        # declairs variable from the settings
        self.minor_mistakes = minor_mistakes
        self.total_time = total_time
        self.first = First
        self.case = Case
        self.word_random = word_random
        self.auto_check = auto_check

        
        # declairing often used fonts and colors for the window
        self.Font24 = "Concert One", 24
        self.Font = "Concert One", 16
        self.font18 = "Inter", 18
        self.font20 = "Inter", 20
        self.font14 = "Inter", 14

        self.color = "#1a4570"
        self.hover_color = "#3c638a"
        self.extra_color = "#1b6bad"

        # setting up the basics for the window structure
        ctk.set_appearance_mode("system")
        self.root = root
        self.root.geometry("780x520")
        self.root.title("Quiz Beta v1.0.0")
        self.root.iconbitmap("images/PyLee_Logo_iconbitmap2.ico")


        self.root.grid_columnconfigure(0, weight=1)

        self.root.grid_rowconfigure(0,weight=1)
        self.root.grid_rowconfigure(1,weight=100)




        # declairing variables which are later used in functions 
        self.word = ""
        self.double_enter = 0
        self.count = 0
        self.actual_count = 0
        self.finished = False
        self.back = False
        self.time_sec = 0
        self.counting_word_time= self.word_time

        # variables that have to do with the word file
        self.inputmem = {}
        self.used_file = {}
        self.file = {}
        self.known = {}
        self.unknown = {}
        self.file_mem = {}
        self.file_name = "learn_list.csv" 

        # trying to open and read the file and displaying an error if that isn't possible
        try:
            self.get_dict()
        except:
            messagebox.showerror("File Error", "Error: couldn't open word_file")

        # creates all the widgets for the window
        self.learn_window()


    def get_dict(self):
        # reads the file depending on which part of the word should be learned
        if self.first == 2:
            with open(self.file_name, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.used_file[row["word"]] = row["definition"]
                    self.file[row["word"]] = row["definition"]
            self.dict_size = len(list(self.file))

        else:
            with open(self.file_name, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.used_file[row["definition"]] = row["word"]
                    self.file[row["definition"]] = row["word"]
            self.dict_size = len(list(self.file))


    def choose_word(self):
        # checks if there are any words left to learn and closes the window if there aren't any left
        if len(list(self.used_file)) == 0:
            self.finished = True
            self.main_frame.destroy()
            self.menu_bar.destroy()

        # checks if a new word should be chosen or if a previous word should be selected
        elif self.actual_count <= self.count:
            try:
                self.word = self.file_mem[self.actual_count]
            except AttributeError: 
                pass
        
        # checks if a random word should be chosen based on the selected setting
        elif self.word_random == 1:
            self.word = random.choice(list(self.used_file))
            self.count += 1
            self.file_mem[self.count] = self.word  

        # selects the next word in line of the list
        elif self.word_random == 0:
            self.word = list(self.file)[self.count]
            self.count += 1
            self.file_mem[self.count] = self.word  
        

    def learn_window(self):
        
        # creates the menu bar for the help and back button
        self.menu_bar = ctk.CTkFrame(self.root, height=20, corner_radius=3, border_width=1, border_color="grey")
        self.menu_bar.grid(row=0, column=0, sticky="nwe")

        self.help_button = ctk.CTkButton(self.menu_bar, height=18, width=70,text="Help", fg_color="transparent", hover_color=self.hover_color, corner_radius=2, state="disabled", text_color=("black","white"))
        self.help_button.grid(row=0, column=0, padx=(20,5) ,pady=1)

        self.back_button = ctk.CTkButton(self.menu_bar, height=18, width=70,text="Back", fg_color="transparent", hover_color=self.hover_color, corner_radius=2, command=self.back_button_pressed, text_color=("black","white"))
        self.back_button.grid(row=0, column=1, padx=5 ,pady=1)
        
        # chooses the first word
        self.actual_count += 1
        self.choose_word()

        # creates a main frame for the rest of the quiz program to go in
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.grid(row=1,column=0,sticky="nswe", pady=(0,30))
        
        self.main_frame.grid_columnconfigure(0, weight=5)
        self.main_frame.grid_columnconfigure(1, weight=1)

        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=10)




        

        # ========frame middle  ========
        self.Label = ctk.CTkLabel(self.main_frame, text="Quiz", font=self.font20, text_color=("black","white"))
        self.Label.grid(row=0, column=0, padx=20, pady=(20,0),sticky="n")

        self.middle_frame = ctk.CTkFrame(self.main_frame, border_color="grey", border_width=1)
        self.middle_frame.grid(row=1, column=0, padx=(50,0), pady=20, sticky="nswe")

        self.middle_frame.grid_columnconfigure(0, weight=1)

        self.middle_frame.grid_rowconfigure(0,weight=10)
        self.middle_frame.grid_rowconfigure(0,weight=1)
        self.middle_frame.grid_rowconfigure(0,weight=1)


        self.learn_frame = ctk.CTkFrame(self.middle_frame)
        self.learn_frame.grid(column=0,padx=20, pady=(20,0),sticky="nswe")
        self.learn_frame.grid_propagate(False)

        #self.learn_frame.grid_columnconfigure(0, weight=1)

        # ========inside the learn frame=======

        self.translate_label= ctk.CTkLabel(self.learn_frame,text="translate:", font=self.Font, justify="left")
        self.translate_label.grid(row=0,column=0,padx=(40,10), pady=(20,0), sticky="w")

        self.learn_label = ctk.CTkLabel(self.learn_frame, text=self.word, font=self.Font24, wraplength=400, justify="left", )
        self.learn_label.grid(row=1,column=0,padx=(40,10), pady=10, sticky="w")


        self.answer_label = ctk.CTkLabel(self.learn_frame, text="", font=self.Font, wraplength=400, justify="left")
        self.answer_label.grid(row=2,column=0,padx=(40,10),pady=10, sticky="w")

        self.solution_label = ctk.CTkLabel(self.learn_frame, text="", font=self.Font, wraplength=400, justify="left")
        self.solution_label.grid(row=3,column=0,padx=(40,10),pady=10, sticky="w")
        if self.word_time != None:
            self.word_progressbar = ctk.CTkProgressBar(self.learn_frame, height=10,mode="determinate", progress_color=self.color, corner_radius=5, border_width=2)
            self.word_progressbar.grid(row=4, column=0, padx=40,pady=(40,0))
            self.word_progressbar.set(1)
            #self.word_progressbar.start()
        
        #========buttons, frame , entry ========

        self.button_frame = ctk.CTkFrame(self.middle_frame, border_width=1, )
        self.button_frame.grid(column=0, padx=50,sticky="we")

        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)
        self.button_frame.grid_columnconfigure(2, weight=1)

        self.back_button = ctk.CTkButton(self.button_frame,text="< Back",width=90, height=26, corner_radius=3, command=self.last_word, fg_color=self.color, hover_color=self.hover_color, text_color=("white","white"))
        self.back_button.grid(row=0,column=0, padx=(5,2),pady=1,sticky="nswe")
        if self.word_time != None:
            self.back_button.configure(state="disabled")
        
        self.answer_button = ctk.CTkButton(self.button_frame,text="Reveal answer",width=90, height=26, corner_radius=3, command=self.show_answer, fg_color=self.color, hover_color=self.hover_color, text_color=("white","white"))
        self.answer_button.grid(row=0,column=1,pady=1,sticky="nswe")
        
        self.next_button = ctk.CTkButton(self.button_frame,text="Next >",width=90, height=26, corner_radius=3, command=self.next_word, fg_color=self.color, hover_color=self.hover_color, text_color=("white","white"))
        self.next_button.grid(row=0,column=2, padx=(2,5),pady=1,sticky="nswe")

        self.word_entry = ctk.CTkEntry(self.middle_frame, placeholder_text="Enter word", placeholder_text_color=("black","white"))
        self.word_entry.bind('<Return>', self.check_answer)
        self.word_entry.grid(column=0,padx=20, pady=20)
        

        #========frame right========
        self.frame_right = ctk.CTkFrame(self.main_frame, )
        self.frame_right.grid(row=1, column=1,padx=0, pady=20, sticky="nse")
        self.frame_right.grid_propagate(False)

        self.frame_right.grid_columnconfigure(0,weight=1)

        self.frame_right.grid_rowconfigure(0,weight=1)
        self.frame_right.grid_rowconfigure(1,weight=1)
        self.frame_right.grid_rowconfigure(2,weight=1)
        self.frame_right.grid_rowconfigure(3,weight=1)
        self.frame_right.grid_rowconfigure(4,weight=1)
        self.frame_right.grid_rowconfigure(5,weight=1)

        # label for the time learned 
        self.label_time = ctk.CTkLabel(self.frame_right, text="Time learned", text_color=("black","white"), font=self.font14)
        self.label_time.grid(row=0, pady=(20,0), padx=20,sticky="", column=0)

        self.time_label = ctk.CTkLabel(self.frame_right, text="00:00:00", font=self.font14, text_color=("black","white"))
        self.time_label.grid(row=1, pady=(0,10), padx=20,sticky="n", column=0)

        # progressbar and labels for the percentage of the learned words
        self.progressbar_label = ctk.CTkLabel(self.frame_right, text="Words learned", text_color=("black","white"), font=self.font14) 
        self.progressbar_label.grid(row=2, pady=(10,0), padx=20,sticky="", column=0)
        

        self.pg1_speed = 50 / self.dict_size
        self.progressbar = ctk.CTkProgressBar(self.frame_right, mode="determinate", determinate_speed=self.pg1_speed, height=15, progress_color=self.color, corner_radius=5, border_width=2)
        self.progressbar.grid(row=3, pady=0, padx=20,sticky="we")
        self.progressbar.set(0)
        

        self.percent_label = ctk.CTkLabel(self.frame_right, text="0.0%", font=self.font14) 
        self.percent_label.grid(row=4, pady=(0,10), padx=20,sticky="n", column=0)
        
        # labels and progressbar fot the ration of known and unknown words
        self.known_progressbar_label = ctk.CTkLabel(self.frame_right, text="Words known" , font=self.font14)
        self.known_progressbar_label.grid(row=5, pady=(10,0), padx=20,sticky="", column=0)
        
        self.known_progressbar = ctk.CTkProgressBar(self.frame_right, height=15,mode="determinate", progress_color="green",fg_color="red", corner_radius=5, border_width=2)
        self.known_progressbar.grid(row=6, pady=0, padx=20, sticky="we")
        
        self.known_percent_label = ctk.CTkLabel(self.frame_right, text="0.0%", font=self.font14) 
        self.known_percent_label.grid(row=7, pady=(0,20), padx=20,sticky="n", column=0)

        # checks if there has been a time selected for the total exercise and transforms the selected amount from str to int
        if self.total_time != "None" and self.total_time != None:
            self.total_time = int(self.total_time.replace("min",""))
            
            self.time_sec = self.total_time * 60

            self.label_time.configure(text="Time left")

        # starts the clock for the exercise
        self.clock()

        # starts the time per word timer 
        self.clock2()
        

    def check_answer(self, event=None):
        # declaires a variable for the entered word
        word_entry = self.word_entry.get()

        # if the entry is empty pass
        if not word_entry:
            pass
        # checks if the word is not in the unknown dict
        elif self.word not in self.unknown:
            # checks if the case of the entry should be regarded
            if self.case == 1 and self.minor_mistakes != 1:
                
                # matches the correct word and the entry
                if word_entry.lower() != (self.file[self.word]).lower():
                    
                    if self.auto_check != 1 or event:
                        
                        # if there hasen't been a match the inputed words get displayed in red color
                        self.answer_label.configure(text=f'Your answer:\n"{word_entry}"',text_color="red")

                        # adds the word to the unknown dict and the entry to the input memory
                        self.unknown[self.word] = self.file[self.word]
                        self.inputmem[self.word] = word_entry
                    
                
                else:

                    # else the entry gets displayed in green color
                    self.answer_label.configure(text=f'Your answer:\n"{word_entry}"',text_color="green")

                    # the word gets added to the known dict and the input to the input memory
                    self.known[self.word] = self.file[self.word]
                    self.inputmem[self.word] = word_entry

                if self.auto_check != 1 or event:
                    # in addition displayes the correct word green
                    self.solution_label.configure(text=f'"{(self.file[self.word]).lower()}"', text_color="green")

            # checks if minor mistakes should be allowed
            elif self.minor_mistakes == 1:
                # matches the two words with up to 3 mistakes
                if self.compare_words(self.file[self.word],word_entry):
                    # if the input has less then 3 mistakes the input will be displayed green
                    self.answer_label.configure(text=f'Your answer:\n"{word_entry}"',text_color="green")

                    # the word gets added to the known dict and the input to the input memory
                    self.known[self.word] = self.file[self.word]
                    self.inputmem[self.word] = word_entry
                    
            

                else:
                    if self.auto_check != 1 or event:
                        # if there were more than 3 mistakes the input will be displayed red
                        self.answer_label.configure(text=f'Your answer:\n"{word_entry}"',text_color="red")

                        # the word will get added to the unkown dict and the input to the input memory
                        self.unknown[self.word] = self.file[self.word]
                        self.inputmem[self.word] = word_entry

                if self.auto_check != 1 or event:
                    # in addition displayes the correct word green
                    self.solution_label.configure(text=f'"{(self.file[self.word])}"',text_color="green")
            
            # if no special exceptions have been selected if just matches the words normaly
            else:
                # checks if the input and the solution are identical
                if word_entry != self.file[self.word]:
                    if self.auto_check != 1 or event:
                        # if not the input will be displayed red
                        self.answer_label.configure(text=f'Your answer:\n"{word_entry}"',text_color="red")
                        # the word will get added to the unkown dict and the input to the input memory
                        self.unknown[self.word] = self.file[self.word]
                        self.inputmem[self.word] = word_entry
                    
                
                else:
                    # if the words match the input will be displayed green
                    self.answer_label.configure(text=f'Your answer:\n"{word_entry}"',text_color="green")
                    # the word will get added to the known dict and the input to the input memory
                    self.known[self.word] = self.file[self.word]
                    self.inputmem[self.word] = word_entry

                if self.auto_check != 1 or event:
                    # in addition displayes the correct word green
                    self.solution_label.configure(text=f'"{self.file[self.word]}"', text_color="green")
        
        # checks if the enter button for this word has already been pressed once and if so it will smove to the next move
        if self.double_enter > 0:
            self.next_word()
        # checks if the autockeck has called this function 
        elif not event:
            pass
        # if this was the first time this function was called for this word the variable will be set to one
        else:
            self.double_enter = 1

    def next_word(self):
        # tries to delet the word from the used file
        try:
            del self.used_file[self.word]
        except KeyError:
            pass
        # resets the timer per word if this option has been selected previously
        if self.word_time != None:
            self.counting_word_time = self.word_time
        # tries to update the percentage and progressbars
        try:
            self.percent_label.configure(text=str(round((100/self.dict_size)*(self.dict_size - len(list(self.used_file))),2))+"%")
            self.known_progressbar.set(1/(len(list(self.known))+len(list(self.unknown)))*len(list(self.known)))
            self.known_percent_label.configure(text=str(round(100/(len(list(self.known))+len(list(self.unknown)))*len(list(self.known)),2))+"%")
        except ZeroDivisionError:
            pass
        if self.progressbar.get() + self.pg1_speed * 0.02 > 1:
            self.progressbar.set(1)
        else:
            self.progressbar.step()

        # destroyes and creates a new entry for the next word
        self.word_entry.destroy()
        self.word_entry = ctk.CTkEntry(self.middle_frame, placeholder_text="Enter word", placeholder_text_color=("black","white"))
        self.word_entry.bind('<Return>', self.check_answer)
        self.word_entry.grid(column=0,padx=20, pady=20)
        self.word_entry.focus()
        self.double_enter = 0
        
        # checks it there are any more words to learn
        if len(list(self.used_file)) > 0:
            # increases the count of the shown word
            self.actual_count += 1
            # chooses a new word
            self.choose_word()

            # checks if lower case has been selected and shows the chosen word accordingly
            if self.case == 1:
                self.learn_label.configure(text=self.word.lower())
            else:
                self.learn_label.configure(text=self.word)

            # checks if the word is in the known dict and if it is displayes it with the input memorys answer
            if self.word in self.known:
                self.answer_label.configure(text=f'Your answer:\n"{self.inputmem[self.word]}"',text_color="green")
                self.solution_label.configure(text=f'"{self.word}" means "{self.file[self.word]}"')
            # checks if the word is in the unknown dict and if it is displayes it with the wrong input memoryes answer
            elif self.word in self.unknown:
                self.answer_label.configure(text=f'Your answer:\n"{self.inputmem[self.word]}"',text_color="red")
                self.solution_label.configure(text=f'"{self.word}" means "{self.file[self.word]}"')
            # else just doesn't display any answer
            else:
                self.answer_label.configure(text="")
                self.solution_label.configure(text="")
        else:
            self.finished = True
            self.main_frame.destroy()
            self.menu_bar.destroy()

    def show_answer(self):
        # configures the input label to show that the answer has been revealed
        self.answer_label.configure(text="Answer revealed",text_color="red")
        # configures the solution label to show the correct answer
        self.solution_label.configure(text=f'"{self.word}" means "{self.file[self.word]}"')
        # adds the word to the unknown dict
        self.unknown[self.word] = self.file[self.word]
        # adds to the input memory that the answer has been revealed
        self.inputmem[self.word] = "No input\nAnswer was revealed"
        
        # configures the entry so that there can't be anything tiped in
        self.word_entry.configure(placeholder_text="Answer revealed", placeholder_text_color=self.color)
        self.word_entry.configure(state="disabled")

    def last_word(self):
        # decreases the count for the shown word
        if self.actual_count > 1:
            self.actual_count -= 1
        # chooses the word based on the actual count and the memory of the already displayed worsd
        self.choose_word()
        self.learn_label.configure(text=self.word)

        # checks if the word is in the known dict and if it is displayes it with the input memorys answer
        if self.word in self.known:
            self.answer_label.configure(text=f'Your answer:\n"{self.inputmem[self.word]}"',text_color="green")
            self.solution_label.configure(text=f'"{self.word}" means "{self.file[self.word]}"')
        # checks if the word is in the unknown dict and if it is displayes it with the wrong input memoryes answer
        elif self.word in self.unknown:
            self.answer_label.configure(text=f'Your answer:\n"{self.inputmem[self.word]}"',text_color="red")
            self.solution_label.configure(text=f'"{self.word}" means "{self.file[self.word]}"')
        # else just doesn't display any answer
        else:
            self.answer_label.configure(text="")
            self.solution_label.configure(text="")


    def known_unknown_get(self): # returnes the known and unknown dict for the end screen 
        return self.known, self.unknown

    def back_button_pressed(self): # returnes to the choose mode program
        self.back = True

    def clock(self):
        # if there hasn't been a total time selected the clock will count up
        if self.total_time == "None" or self.total_time == None:
            self.time_sec += 1
            seconds = self.time_sec
            seconds = seconds % (24 * 3600)
            hour = seconds // 3600
            seconds %= 3600
            minutes = seconds // 60
            seconds %= 60
            try:
                self.time_label.configure(text="%02d:%02d:%02d" % (hour, minutes, seconds))
            except:
                pass
        # else the clock will count down and finish the program
        else:
            self.time_sec -= 1
            seconds = self.time_sec
            seconds = seconds % (24 * 3600)
            hour = seconds // 3600
            seconds %= 3600
            minutes = seconds // 60
            seconds %= 60
            self.time_label.configure(text="%02d:%02d:%02d" % (hour, minutes, seconds))
            if self.time_sec == 0:
                self.finished = True
                self.main_frame.destroy()
                self.menu_bar.destroy()
        # checks the anser automaticaly if the option as been selected
        if self.auto_check == 1:
            self.check_answer()
        self.root.after(1000, self.clock)

    def clock2(self):
         #checks if there has been a total time per word selected
        if self.word_time != None:

            # counts down and updates the progressbar 
            self.counting_word_time -= 1
            self.word_progressbar.set(1/self.word_time*self.counting_word_time)

            # if there isn't any time left the answer will be checked and the next word shown
            if self.counting_word_time <= 0:
                self.check_answer()
                self.next_word()
            self.root.after(1000, self.clock2)
            
    def compare_words(self,w1, w2):
        # compares the input word and the correct answer on multiple differences and returns if there are less then 3 differences Ture
        w1 = w1.lower().strip()
        w2 = w2.lower().strip()
        w1 = w1.replace(" ","")
        w2 = w2.replace(" ","")
        w_letters=0
        for letter in w2:
            if letter not in w1:
                w_letters+=1
                w2= w2.replace(letter,"")
        if w1 != w2:
            if len(w1) < len(w2):
                count=0
                wrong=""
                for l in w2:
                    if l == w1[count]:
                        count+=1
                    else:
                        wrong+=l
                if len(wrong)+w_letters < 4:
                    return True
                else:
                    return False
                
            elif len(w1) > len(w2):
                count=0
                missing = ""
                missing += "_" * (len(w1)-len(w2))
                for l in w2:
                    if count >= len(w1):
                        missing+="*"
                    elif l == w1[count]:
                        count+=1
                    elif l == w1[(count+1)]:
                        missing += w1[count]
                        count+=2
                    elif l == w1[(count+2)]:
                        missing += w1[count]
                        missing += w1[count+1]
                        count+=3
                    else:
                        missing += w1[count]
                        count +=1
                if len(missing)+w_letters < 4:
                    return True
                else:
                    return False
            elif len(w1) == len(w2):
                count=0
                wrong=""
                for l in w2:
                    if l == w1[count]:
                        count+=1
                    elif count +1 <= len(w1):
                        if w2[count+1] == w1[count+1]:
                            wrong += l
                            count+=1
                    else:
                        wrong+=l
                        count+=1
                if len(wrong)+w_letters<4:
                    return True
                else:
                    return False
        else:
            if w_letters < 3:
                return True
            else:
                return False
if __name__ == "__main__":     
    learning_frame(ctk.CTk()).root.mainloop()