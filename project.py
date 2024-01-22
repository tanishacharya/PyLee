import sys
#sys.path.append('c:/users/elias/appdata/local/packages/pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0/localcache/local-packages/python310/site-packages')
import customtkinter as ctk

# importing the different program files
from start_screen import Start_Screen
from choose_mode import Choose_Mode
from quiz import learning_frame
from file_menu import File_Menu
from multiple_choice import Multiple_Choice
from flashcards import Flashcards
from match_beta import Match

import csv
import os
from tkinter.ttk import *
import re

# number and words of known and unknown
known_number=0
known={}
unknown={}
unknown_number=0
# saves the selected file
file_name=None
# length of the file in words
length= 0
event="start"
open_end_screen = 0
file_mode = None

# the main programm handels all the transitions from the different window setups
def main(event="start"):

    global file_name, known, unknown, length, main_root
    # start event starts the mainloop
    if event == "start":
        
        main_root = ctk.CTk()

        start_screen_win(main_root, known_number, unknown_number, file_name, length)

        main_root.mainloop()

    # the file_mode event gets handels the file which will be learned
    elif event == "file_mode":
        if file_mode == "create":

            file_menu_win(main_root)

        elif file_mode == "open":

            choose_mode_win(main_root, file_name)

    # choose_mode event handels which specific learning settings were selected
    elif event == "choose_mode":

        case, first, random, length, file_name,total_time, word_time, minor_mistakes, auto_check= choose_mode.get_values()

        if choose_mode.mode == "flashcards":
            
            flash_cards_win(main_root, first)

        elif choose_mode.mode == "multiple choice":

            multiple_choice_win(main_root, first, random, total_time, word_time)
            ...
        elif choose_mode.mode == "quiz":

            quiz_win(main_root,case,first,random,total_time,word_time,minor_mistakes,auto_check)
            ...
        elif choose_mode.mode == "match":
            try:
                minutes_ = int(choose_mode.time_total.get().removesuffix("min"))
            except:
                minutes_ = 0
            seconds = 0
            match_win(main_root,seconds, minutes_)

    # after the learning has been done the end_screen apeares with a summary 
    elif event == "end screen":

        end_screen_win(main_root,known, unknown)

    # takes the wrong word and puts them into ther learning list, starts the choose_mode window again
    elif event == "learn unknown":

        with open("wrong_words.csv", "w", newline="") as target:
            writer = csv.DictWriter(target, ["definition", "word"])
            writer.writeheader()
            for row in unknown:
                writer.writerow({"definition":unknown[row],"word":row})

        choose_mode_win(main_root, file_name="wrong_words.csv")

    # restarts the program
    elif event == "restart":
        print(unknown_number)
        print(file_name)
        main_root.quit()
        main_root = ctk.CTk()
        start_screen_win(main_root, known_number, unknown_number, file_name, length)
        ...

def start_screen_win(root,known_number=0, unknown_number=0,file_name=None, length=0):

    global start_screen

    # handels the different events like the back button etc.
    def start_screen_events():
        global file_mode ,file_name

        if start_screen.open_file_btn_pressed:
            
            file_mode = "open"

            file_name = start_screen.filename

            start_screen.root_frame.destroy()

            main(event="file_mode")

        elif start_screen.new_file_btn_pressed:
            
            file_mode = "create"

            start_screen.root_frame.destroy()
            
            main(event="file_mode")
        else:
            root.after(1000,start_screen_events)

    # creates the start screen frames
    start_screen = Start_Screen(root, known_number, unknown_number, file_name, length)

    root.after(1000,start_screen_events)

    # after finishing everything succesfully return True
    return True

def file_menu_win(root):

    global file_menu

    # handels the different events like the back button etc.
    def file_menu_events():
        global file_mode

        if file_menu.save_quit_btn:
            
            file_name = "saved_csv/" + file_menu.file_name_without_csv.get() + ".csv"

            file_menu.root_frame.destroy()
            file_menu.menu_bar.destroy()

            file_mode = "open"

            main(event="file_mode")


        elif file_menu.back:

            file_menu.root_frame.destroy()
            file_menu.menu_bar.destroy()

            start_screen_win(root)

        else:

            root.after(1000, file_menu_events)

    # creates the file menu frames
    file_menu = File_Menu(root)

    root.after(1000,file_menu_events)

    # after finishing everything succesfully return True
    return True

def choose_mode_win(root, file_name):

    global choose_mode
    
    # handels the different events like the back button etc.
    def choose_mode_events():
        
        if choose_mode.start_learning_btn_pressed:

            choose_mode.root_frame.destroy()
            choose_mode.menu_bar.destroy()

            main(event="choose_mode")

        elif choose_mode.back:

            choose_mode.root_frame.destroy()
            choose_mode.menu_bar.destroy()

            start_screen_win(root)
        
        else:
            root.after(1000,choose_mode_events)

    # creates the choose mode frames
    choose_mode = Choose_Mode(root, file_name)

    root.after(1000, choose_mode_events)

    # after finishing everything succesfully return True
    return True

def flash_cards_win(root, first=0):

    global flash_cards
    
    # handels the different events like the back button etc.
    def flash_cards_events():
        if flash_cards.finished:

            flash_cards.root_frame.destroy()
            flash_cards.menubar.destroy()

            main(event="end screen")

        elif flash_cards._back:
            flash_cards.root_frame.destroy()
            flash_cards.menubar.destroy()

            choose_mode_win(root, "learn_list.csv")
        else:
            root.after(1000, flash_cards_events)

    # creates the flash card frames
    flash_cards = Flashcards(root,first)

    root.after(1000, flash_cards_events)

    # after finishing everything succesfully return True
    return True

def multiple_choice_win(root, first=0, random=0, total_time=None, word_time=None):

    global multiple_choice
    
    # handels the different events like the back button etc.
    def multiple_choice_events():
        global known, unknown
        if multiple_choice.not_enough_words2learn:

            multiple_choice.mainframe.destroy()
            multiple_choice.menu_bar.destroy()

            known, unknown = multiple_choice.known_unknown_get()

            main(event="end screen")

        elif multiple_choice.back:

            multiple_choice.mainframe.destroy()
            multiple_choice.menu_bar.destroy()
        
            choose_mode_win(root, file_name="learn_list.csv")

        else:
            root.after(1000, multiple_choice_events)

    # creates the flash card frames
    multiple_choice = Multiple_Choice(root,word_random=random,word_or_def=first,total_time=total_time,word_time=word_time)
    
    root.after(1000, multiple_choice_events)

    # after finishing everything succesfully return True
    return True

def quiz_win(root, case=0, first=0, random=0, total_time=None, word_time=None, minor_mistakes=0, auto_check=0):
    
    global quiz

    # handels the different events like the back button etc.
    def quiz_events():
        global known, unknown
        if quiz.finished:

            quiz.main_frame.destroy()
            quiz.menu_bar.destroy()

            known, unknown = quiz.known_unknown_get()

            main(event="end screen")

        elif quiz.back:

            quiz.main_frame.destroy()
            quiz.menu_bar.destroy()

            choose_mode_win(root, file_name="learn_list.csv")
        else:
            root.after(1000, quiz_events)
 
    # creates the quiz frames   
    quiz = learning_frame(root,word_random=random, Case=case, First=first,total_time=total_time, word_time=word_time,minor_mistakes=minor_mistakes, auto_check=auto_check)
    
    root.after(1000,quiz_events)

    # after finishing everything succesfully return True
    return True

def match_win(root, sec=0, min=0):
    
    global match

    # handels the different events like the back button etc.
    def match_events():
        global known, unknown
        if match.finished:

            match.mainframe.destroy()
            match.menubar.destroy()

            known, unknown = match.known_unknown_get()

            match(event="end screen")

        elif match.back:

            match.mainframe.destroy()
            match.menubar.destroy()

            choose_mode_win(root, file_name="learn_list.csv")
        else:
            root.after(1000, match_events)
   
    # creates the match frames    
    match = Match(root,sec, min)
    
    root.after(1000,match_events)

    # after finishing everything succesfully return True
    return True

def end_screen_win(root, known, unknown):

    global unknown_number, known_number

    # calls main to learn the unknown
    def learn_unknown():
        root_frame.destroy()
        main(event="learn unknown")

    # calls main to restart the program
    def restart():
        root_frame.destroy()
        main(event="restart")

    # ============ creates the window ============

    # declaring the colors for the end screen
    color = "#1a4570"
    _hover_color = "#3c638a"
    extra_color = "#1b6bad"

    root.title("Summary Beta v0.0.3")
    root.geometry("780x520")
    
    root.grid_columnconfigure(0,weight=1)

    root.grid_rowconfigure(0,weight=1)

    root_frame = ctk.CTkFrame(root)

    root_frame.grid_columnconfigure(0,weight=4)
    root_frame.grid_columnconfigure(1,weight=1)

    root_frame.grid_rowconfigure(0,weight=1)

    # creating a left frame for the known, unknown words and the buttons
    left_frame = ctk.CTkFrame(root_frame, border_width=2)
    left_frame.grid(row=0, column=0, sticky="nswe")

    left_frame.grid_rowconfigure(0,weight=1)
    left_frame.grid_rowconfigure(1,weight=1)
    left_frame.grid_rowconfigure(2,weight=2)

    left_frame.grid_columnconfigure(0,weight=1)
    left_frame.grid_columnconfigure(1,weight=1)

    left_title = ctk.CTkLabel(left_frame, text="Summary", font=("Inter", 30))
    left_title.grid(row=0,columnspan=2, column=0,sticky="nswe", padx=10, pady=10)

    # textbox to show the correctly inputed words
    correct_textbox = ctk.CTkTextbox(left_frame, font=("Inter", 18),padx=10, border_color="green", border_width=2, activate_scrollbars=True)
    correct_textbox.grid(row=1, column=0,sticky="nswe",padx=5,pady=5)
    correct_textbox.insert(ctk.END,"Correct Words\n\n")

    # inserts the known word into the textbox
    if known != {}:
        for row in known:
            correct_textbox.insert(ctk.END,f"{row}: {known[row]}\n")
    # there aren't any correct words display " No correct anwsers"
    else:
        correct_textbox.insert(ctk.END,"No correct answers")
    correct_textbox.configure(state="disabled")

    # textbox with the wrong words
    incorrect_textbox = ctk.CTkTextbox(left_frame, font=("Inter", 18),padx=10, border_color="red", border_width=2, activate_scrollbars=True)
    incorrect_textbox.grid(row=1, column=1, sticky="nswe",padx=5,pady=5)
    incorrect_textbox.insert(ctk.END,"Wrong Words\n\n")

    # inserts the unknwon words
    if unknown != {}:
        for row in unknown:
            incorrect_textbox.insert(ctk.END,f"{row}: {unknown[row]}\n")
    else:
        # if there aren't any display " No incorrect answers"
        incorrect_textbox.insert(ctk.END,"No incorrect answers")
    incorrect_textbox.configure(state="disabled")

    # creating right frame for additional information for the file
    right_frame = ctk.CTkFrame(root_frame)
    right_frame.grid(row=0, column=1, sticky="nsew", padx=(20,0))

    right_frame.grid_columnconfigure(0, weight=1)

    display_frame = ctk.CTkFrame(right_frame)
    display_frame.grid(row=0, rowspan=5, sticky="nswe",padx=10)
    display_frame.grid_columnconfigure(0,weight=1)

    # shows the file name
    file_label = ctk.CTkLabel(display_frame, text=f"File path:",font=("Inter", 20) ,wraplength=200,)
    file_label.grid(row=0, column=0, pady=(40,15))

    file_label = ctk.CTkLabel(display_frame, text=f'"{os.path.basename(os.path.normpath(file_name))}"',font=("Inter", 16) ,wraplength=200)
    file_label.grid(row=1, column=0, pady=(0,15))

    known_number = len(list(known))
    unknown_number = len(list(unknown))

    # shows the amount of correct words
    c_amount_label = ctk.CTkLabel(display_frame, text=f"Correct:", font=("Inter", 20))
    c_amount_label.grid(row=2, column=0, pady=15)

    c_amount_label = ctk.CTkLabel(display_frame, text=f"{known_number}", font=("Inter", 16))
    c_amount_label.grid(row=3, column=0, pady=(0,15))

    # shows the amount of wrong words
    w_amount_label = ctk.CTkLabel(display_frame, text=f"Wrong:", font=("Inter", 20))
    w_amount_label.grid(row=4, column=0, pady=15)

    w_amount_label = ctk.CTkLabel(display_frame, text=f"{unknown_number}", font=("Inter", 16))
    w_amount_label.grid(row=5, column=0, pady=(0,25))

    # checks if there have been any wrong answers and if there were creates a button to learn these words again
    if unknown_number != 0:
        unknown_restart_button = ctk.CTkButton(right_frame, text="learn wrong words", command=learn_unknown, width=180, height=40, fg_color=color, hover_color=_hover_color)
        unknown_restart_button.grid(row=6, column=0, pady=20,sticky="s",padx=25)
    
    else:
        # else creates a button to finish the programme
        finish_button = ctk.CTkButton(right_frame, text="Finish programm", command=lambda : sys.exit(), width=180, height=40, fg_color=color, hover_color=_hover_color)
        finish_button.grid(row=6, column=0, pady=20,sticky="s",padx=25)

    # creates a button to restart the programme
    restart_button = ctk.CTkButton(right_frame, text="Restart program", command=restart, width=180, height=40, fg_color=color, hover_color=_hover_color)
    restart_button.grid(row=7, column=0, pady=20,sticky="s",padx=25)

    root_frame.grid(row=0,rowspan=2,column=0, sticky="nswe")

    # return True after everything has been created succesfully
    return True

def is_csv(string):
    print(string)
    if re.search(r".+\.csv$", string):
        return True
    else: 
        return False

if __name__ =="__main__":
    main()