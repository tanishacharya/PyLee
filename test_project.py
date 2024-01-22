import project
from tkinter.ttk import *
import time
import customtkinter as ctk
import pytest
import time

root = ctk.CTk()


# does not work due to issues with the customtkinter CTkImage function
"""
def test_start_screen():

    assert project.start_screen_win(root) == True
    
    def window_test():
        assert project.start_screen.root_frame.winfo_ismapped() == True
        root.quit()
    
    root.after(1000, window_test)
    root.mainloop()
"""

def test_file_menu():
    assert project.file_menu_win(root) == True
    
    def window_test():
        assert project.file_menu.root_frame.winfo_ismapped() == True
        root.quit()
    
    root.after(1000, window_test)
    root.mainloop()

def test_choose_mode():
    assert project.choose_mode_win(root, "learn_list.csv") == True
    
    def window_test():
        assert project.choose_mode.root_frame.winfo_ismapped() == True
        root.quit()
    
    root.after(1000, window_test)
    root.mainloop()

def test_flash_cards():
    assert project.flash_cards_win(root) == True
    
    def window_test():
        assert project.flash_cards.root_frame.winfo_ismapped() == True
        root.quit()
    
    root.after(1000, window_test)
    root.mainloop()

def test_multiple_choice():
    assert project.multiple_choice_win(root) == True
    
    def window_test():
        assert project.multiple_choice.mainframe.winfo_ismapped() == True
        root.quit()
    
    root.after(1000, window_test)
    root.mainloop()

def test_quiz():
    assert project.quiz_win(root) == True
    
    def window_test():
        assert project.quiz.main_frame.winfo_ismapped() == True
        root.quit()
    
    root.after(1000, window_test)
    root.mainloop()

def test_match():
    assert project.match_win(root) == True
    
    def window_test():
        assert project.match.mainframe.winfo_ismapped() == True
        root.quit()
    
    root.after(1000, window_test)
    root.mainloop()

def test_is_csv():
    assert project.is_csv("file.csv") == True
    assert project.is_csv("a.csv") == True
    assert project.is_csv("Really long and with numbers 123.csv") == True
    assert project.is_csv("file.csw") == False
    assert project.is_csv("file.csvsomething") == False
    assert project.is_csv("somethingcsv") == False
    assert project.is_csv("thing.csv otherthing") == False



if __name__ == "__main__":
    #test_start_screen()
    test_file_menu()
    test_choose_mode()
    test_flash_cards()
    test_multiple_choice()
    test_quiz()
    test_match()