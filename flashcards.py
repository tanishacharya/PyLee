import customtkinter as ctk
import csv


class Flashcards:
    def __init__(self, main_root , word_or_def=1,random_order=0):
        
        self.root = main_root
        self.root.geometry("800x520")
        self.root.title("Flashcards Beta v1.0.0")

        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")

        self.font = "Arial Black"
        self.font_size = 35
        self.filename = "learn_list.csv"
        self.word_or_def = word_or_def
        self.random_order = random_order
        
        self.max_word_length = 14

        self.front = []
        self.back = []
        self.card_index = 0

        self.make_dicts(self.filename)

        # Makes Text better!
        # self.make_dicts_better()

        self.current_text = self.front[self.card_index]
        self.side_up = "front"
        
        self.color = "#1a4570"
        self.hover_color = "#3c638a"
        self.extra_color = "#1b6bad"

        self._back = False
        self.finished = False

        self.build()


    def build(self): # Builds all the UI elements

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=100)

        # The menubar that I copied in here
        self.menubar = ctk.CTkFrame(self.root, height=20, corner_radius=3, border_width=1, border_color="grey")
        self.menubar.grid(row=0, column=0, sticky="new")

        # The buttons in the menubar
        self.help_button = ctk.CTkButton(self.menubar, height=18, width=70,text="Help", fg_color="transparent", hover_color=self.hover_color, corner_radius=2, text_color=("black","white"), state="disabled")
        self.help_button.grid(row=0, column=0, padx=(20,5) ,pady=1)

        self.back_button = ctk.CTkButton(self.menubar, height=18, width=70,text="Back", fg_color="transparent", hover_color=self.hover_color, corner_radius=2, command=self.back_button_pressed, text_color=("black","white"))
        self.back_button.grid(row=0, column=1, padx=5 ,pady=1)

        # A Frame for everything
        self.root_frame = ctk.CTkFrame(self.root)
        self.root_frame.grid(row=1, column=0, sticky="news", ipadx=30)

        self.root_frame.grid_columnconfigure(0, weight=1)
        self.root_frame.grid_rowconfigure(1, weight=1)

        # Frame where the Flashcard will be displayed
        self.card = ctk.CTkFrame(self.root_frame, corner_radius=7, border_width=0, border_color="#111111", fg_color="#ffffff")
        self.card.grid(padx=70, pady=50, column=0, row=1, sticky="nswe")

        self.card.grid_columnconfigure(0,weight=1)
        self.card.grid_rowconfigure(0,weight=1)

        # Frame where the Flashcard will be displayed
        self.card_frame = ctk.CTkFrame(self.card, corner_radius=7, border_width=0, border_color="#222222", fg_color="#ffffff", )
        self.card_frame.grid(padx=(2,6), pady=(2,5), column=0, row=0, sticky="nswe")
        #self.card_frame.grid_propagate(False)

        self.card_frame.grid_columnconfigure(0, weight=1)
        self.card_frame.grid_columnconfigure(1, weight=40)
        self.card_frame.grid_columnconfigure(2, weight=1)
        self.card_frame.grid_rowconfigure(1, weight=1)

 
        # Next button
        self.next_button = ctk.CTkButton(self.card_frame, text="❱", command=self.next, font=("Inter", 40),text_color="black", fg_color="#ffffff", corner_radius=0, round_width_to_even_numbers=False, hover=False)
        self.next_button.grid(column=2, row=1 ,padx=(0,10), pady=10, sticky="nswe")
        self.next_button.grid_propagate(False)


        # Previous card button
        self.back_button = ctk.CTkButton(self.card_frame, text="❰", command=self.previous, font=("Inter", 40),text_color="black", fg_color="#ffffff", corner_radius=0, round_width_to_even_numbers=False, hover=False)
        self.back_button.grid(column=0, row=1, padx=(10,0), pady=10, sticky="nswe")
        self.back_button.grid_propagate(False)

        # The Label where the text will be displayed
        self.card_text = ctk.CTkButton(self.card_frame, text=self.current_text, font=(self.font, self.font_size), text_color = "black", command=self.turn, fg_color="#ffffff", corner_radius=0, round_width_to_even_numbers=False, hover=False)
        self.card_text.grid(column=1, row=1, padx=0, pady=10, sticky="nswe")
        self.card_text.grid_propagate(False)

       
    def make_dicts(self, file):
        if self.word_or_def == 2:
                with open(file) as self.file:
                    reader = csv.DictReader(self.file)
                    for row in reader:
                        self.front.append(row["definition"])
                        self.back.append(row["word"])

        else:
            with open(file) as self.file:
                reader = csv.DictReader(self.file)
                for row in reader:
                    self.front.append(row["word"])
                    self.back.append(row["definition"])


    def update(self):

        if self.side_up == "front":
            self.current_text = self.front[self.card_index]
        else:
            self.current_text = self.back[self.card_index]

        self.current_text = self.make_strings_better(self.current_text)

        self.card_text.configure(text=self.current_text)
    

    def make_dicts_better(self):
        
        new_front =  []
        new_back = []

        for obj in self.front:
            new_front += self.make_strings_better(obj)
        for obj2 in self.back:
            new_back += self.make_strings_better(obj2)

        self.front = new_front
        self.back = new_back

    def make_strings_better(self,string):
    
        max_word_length = self.max_word_length

        counter = 0
        better_string = ""
        piece = ""

        if len(string) <= max_word_length:
            return string

        for char in string:

            piece = piece + char
            counter += 1
            if counter == max_word_length:
                piece += "-\n"
                better_string += piece
                counter = 0
                piece = ""
        if counter != 0:
            better_string += piece 

        better_string = better_string.strip("-\n")

        return better_string

    # Functons when the buttons are pressed
    def next(self):
        if self.card_index < len(self.front) - 1:
            self.card_index += 1
            self.side_up = "back"
            self.turn()
            self.update()
        else:
            self.finished = True


    def previous(self):
        if self.card_index > 0:
            self.card_index -= 1
            self.update()


    def turn(self):
        if self.side_up == "front":
            self.card_text.configure(fg_color="#19456f")
            self.next_button.configure(fg_color="#19456f")
            self.back_button.configure(fg_color="#19456f")
            self.card_frame.configure(fg_color="#19456f")
            self.card.configure(fg_color="#19456f")
            self.card_text.configure(text_color="white")
            self.side_up = "back"
        else:
            self.card_text.configure(fg_color="#ffffff")
            self.next_button.configure(fg_color="#ffffff")
            self.back_button.configure(fg_color="#ffffff")
            self.card_frame.configure(fg_color="#ffffff")
            self.card.configure(fg_color="#ffffff")
            self.card_text.configure(text_color="black")
            self.side_up = "front"
        self.update()
        
        
    def back_button_pressed(self):
        self._back = True

        
if __name__ == "__main__":
    Flashcards(ctk.CTk).root.mainloop()
