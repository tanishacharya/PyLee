# TODO:
#   unkown, known for end screen
#   go to end screen
#   remaining matches

import customtkinter as ctk
from tkinter import messagebox
import csv
import random
import functools


class Match:
    def __init__(self, root, seconds: int = 0, minutes: int = 0):
        self.root = root
        self.root.title("Match")
        self.root.geometry("780x520")
        # self.root.resizable(False, False)

        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.back = False

        self.font16 = "Inter", 16
        self.font20 = "Inter", 20
        self.font25 = "Inter", 25

        self.color = "#1b4571"
        self.hover_color = "#305578"
        self.extra_color = "#3d638b"
        self.wrong_color = "#b04040"
        self.wrong_color_hover = "#8f3636"

        self.filename = "learn_list.csv"

        self.btn_left = {}
        self.btn_right = {}

        self.words2learn = {}
        self.buttons = []

        self.text_left = []
        self.text_right = []

        self.known = {}
        self.unknown = {}

        self.button_list = {}

        self.btn_count = 0
        self.progress_int = 0

        self.num = []  # check if 2 btns are pressed
        self.btns = {}

        self.seconds = seconds
        self.minutes = minutes

        self.time_up_secs = 0

        if minutes == 0:
            self.time = False
        else:
            self.time = True
            self.actual_time = minutes * 60 + seconds

        self.finished = False
        self.temp = 0

        self.motivation_list = [
            "PyLee believes in you!",
            "No master has ever fallen from the sky!",
            "A little progress adds up to big results!",
            "Work hard, dream big, never give up!",
            "Dreams don't work unless you do!",
            "Don't stop until you're pround!",
            "Forget mistakes, remember the word!",
            "Keep going!",
            "Pylee is never going to give you up!",
            "Pylee is never going to let you down!",
            "You can do it!",
        ]

        try:
            self.make_dict(file=self.filename)
            self.len_w2l = len(self.words2learn)
            self.still_to_learn_int = self.len_w2l
        except FileNotFoundError:
            messagebox.showerror(
                "File not found",
                f'Error: {self.filename} doesn\'t exist in this directory. (use "cd saved_csv" ',
            )

        self.window()

        """if self.time:
            self.timer()
        else:
            self.timer_up()"""

    def window(self):
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=100)

        self.menu_bar = ctk.CTkFrame(
            self.root, height=20, corner_radius=3, border_width=1
        )
        self.menu_bar.grid(row=0, column=0, sticky="nwe")

        self.help_button = ctk.CTkButton(
            self.menu_bar,
            height=18,
            width=70,
            text="Help",
            fg_color="transparent",
            hover_color=self.hover_color,
            corner_radius=2,
            text_color=("black", "white"),
            state="disabled",
        )
        self.help_button.grid(row=0, column=0, padx=(20, 5), pady=1)

        self.back_button = ctk.CTkButton(
            self.menu_bar,
            height=18,
            width=70,
            text="Back",
            fg_color="transparent",
            hover_color=self.hover_color,
            corner_radius=2,
            text_color=("black", "white"),
            command=self.back_button_pressed,
        )
        self.back_button.grid(row=0, column=1, padx=5, pady=1)
        #        ====================main frame====================
        self.mainframe = ctk.CTkFrame(self.root)
        self.mainframe.grid(row=1, column=0, sticky="nswe")

        self.mainframe.grid_columnconfigure(0, weight=4)  # "main"
        self.mainframe.grid_columnconfigure(2, weight=1)  # progress

        self.mainframe.grid_rowconfigure(0, weight=1)

        #        ====================middle frame====================
        # title
        # self.title_label = ctk.CTkLabel(self.mainframe, text="Select the correct pair:", font=self.font25)
        # self.title_label.grid(row=0, column=2, sticky="nswe")

        #       ====================right frame ====================
        self.right_frame = ctk.CTkFrame(self.mainframe)
        self.right_frame.grid(column=2, row=0, sticky="nswe")
        # self.right_frame.grid_propagate(False)

        self.right_frame.grid_columnconfigure(0, weight=1)

        # check how many are really needed
        self.right_frame.grid_rowconfigure(0, weight=1)
        self.right_frame.grid_rowconfigure(1, weight=1)
        self.right_frame.grid_rowconfigure(2, weight=1)
        self.right_frame.grid_rowconfigure(3, weight=1)
        self.right_frame.grid_rowconfigure(4, weight=1)
        self.right_frame.grid_rowconfigure(5, weight=1)
        self.right_frame.grid_rowconfigure(6, weight=1, minsize=1)
        self.right_frame.grid_rowconfigure(7, weight=1, minsize=1)

        if self.time:
            self.time_left = ctk.CTkLabel(
                self.right_frame, text="Time left:", font=self.font20
            )
            self.time_left.grid(column=0, row=0, sticky="nswe", pady=5)

            self.time_label = ctk.CTkLabel(self.right_frame, font=self.font20, text="")
            self.time_label.grid(column=0, row=1, sticky="nswe", pady=5)

            self.correct_matches = ctk.CTkLabel(
                self.right_frame, text="Correct matches:", font=self.font20
            )
            self.correct_matches.grid(column=0, row=2, sticky="nswe", pady=5)

            self.correct_matches_int = ctk.CTkLabel(
                self.right_frame, text=self.progress_int, font=self.font20
            )
            self.correct_matches_int.grid(column=0, row=3, sticky="nswe", pady=5)

            self.remaining_matches = ctk.CTkLabel(
                self.right_frame, text="Remaining matches:", font=self.font20
            )
            self.remaining_matches.grid(column=0, row=4, sticky="nswe", pady=5)

            self.remaining_matches_int = ctk.CTkLabel(
                self.right_frame, text=self.len_w2l, font=self.font20
            )
            self.remaining_matches_int.grid(column=0, row=5, sticky="nswe", pady=5)

        else:
            self.time_label_title = ctk.CTkLabel(
                self.right_frame, text="Time:", font=self.font20
            )
            self.time_label_title.grid(column=0, row=0, pady=5, sticky="s")

            self.time_label = ctk.CTkLabel(
                self.right_frame, text="00:00", font=self.font20
            )
            self.time_label.grid(column=0, row=1, sticky="n", pady=5)

            self.correct_matches = ctk.CTkLabel(
                self.right_frame, text="Correct matches:", font=self.font20
            )
            self.correct_matches.grid(column=0, row=2, sticky="s", pady=5)

            self.correct_matches_int = ctk.CTkLabel(
                self.right_frame, text=self.progress_int, font=self.font20
            )
            self.correct_matches_int.grid(column=0, row=3, sticky="n", pady=5)

            self.remaining_matches = ctk.CTkLabel(
                self.right_frame, text="Remaining matches:", font=self.font20
            )
            self.remaining_matches.grid(column=0, row=4, sticky="s", pady=5)

            self.remaining_matches_int = ctk.CTkLabel(
                self.right_frame, text=self.len_w2l, font=self.font20
            )
            self.remaining_matches_int.grid(column=0, row=5, sticky="n", pady=5)

        self.actual_match()

        if self.time:
            self.root.after(1000, self.timer)
        else:
            self.root.after(1000, self.timer_up)

    def actual_match(self):
        self.middle_frame = ctk.CTkFrame(self.mainframe)
        self.middle_frame.grid(row=0, column=0, sticky="nswe", padx=5, pady=(10, 0))

        # memory style zuordnen
        # make a 2x5 grid
        self.middle_frame.grid_columnconfigure(0, weight=1)
        self.middle_frame.grid_columnconfigure(1, minsize=1, pad=20)
        self.middle_frame.grid_columnconfigure(2, weight=1)

        self.middle_frame.grid_rowconfigure(0, weight=1)
        self.middle_frame.grid_rowconfigure(1, weight=1)
        self.middle_frame.grid_rowconfigure(2, weight=1)
        self.middle_frame.grid_rowconfigure(3, weight=1)

        self.words, self.definitions = self.all_question()
        self.all = {
            self.words[i]: self.definitions[i] for i in range(len(self.words))
        }  # dict with ALL voci

        random.shuffle(self.words)
        random.shuffle(self.definitions)

        row = [0, 1, 2, 3, 0, 1, 2, 3]
        rindex = 0

        for word in self.words:
            btn_main = ctk.CTkButton(
                self.middle_frame,
                text=word,
                border_width=2,
                fg_color="#7B8FA1",
                hover_color="#567189",
                font=("Inter", 15),
                text_color=("black", "black"),
            )
            btn_main.grid(row=row[rindex], column=0, sticky="nswe", padx=40, pady=20)
            rindex += 1
            self.btn_count += 1
            btn_main.grid_propagate(False)

            self.button_list[btn_main._text] = btn_main
            self.text_left.append(btn_main._text)
            btn_main.configure(
                command=functools.partial(self.btn_pressed, word, btn_main)
            )

        rindex = 0

        for word in self.definitions:
            btn_main = ctk.CTkButton(
                self.middle_frame,
                text=word,
                border_width=2,
                fg_color="#7B8FA1",
                hover_color="#567189",
                font=("Inter", 15),
                text_color=("black", "black"),
            )
            btn_main.grid(row=row[rindex], column=2, sticky="nswe", padx=40, pady=20)
            rindex += 1
            self.btn_count += 1
            btn_main.grid_propagate(False)

            self.button_list[btn_main._text] = btn_main
            self.text_right.append(btn_main._text)
            btn_main.configure(
                command=functools.partial(self.btn_pressed, word, btn_main)
            )

    def btn_pressed(self, word, btn):
        btn.configure(fg_color="#427ac1")
        btn.configure(hover_color="#427ac1")

        try:
            answer = self.all[word]
        except KeyError:
            for key in list(self.all.keys()):
                if self.all[key] == word:
                    answer = key

        if len(self.num) != 1:
            self.num.append(word)

        elif len(self.num) == 1:
            self.num.append(word)

            word1 = self.num[0]
            word2 = self.num[1]

            try:
                temp = self.all[word1]
                if temp == word2:
                    button = self.button_list[word1]
                    button.configure(
                        fg_color="green", hover_color="green", state="disabled"
                    )
                    del self.button_list[word1]
                    del self.words2learn[word1]

                    button = self.button_list[word2]
                    button.configure(
                        fg_color="green", hover_color="green", state="disabled"
                    )
                    del self.button_list[word2]

                    self.progress_int += 1
                    self.correct_matches_int.configure(text=self.progress_int)

                    self.still_to_learn_int -= 1
                    self.len_w2l -= 1
                    self.remaining_matches_int.configure(text=self.len_w2l)

                    self.known.update({word: answer})

                else:
                    button = self.button_list[word1]
                    button.configure(
                        fg_color=self.wrong_color, hover_color=self.wrong_color_hover
                    )

                    button = self.button_list[word2]
                    button.configure(
                        fg_color=self.wrong_color, hover_color=self.wrong_color_hover
                    )

                    self.unknown.update({word: answer})

            except KeyError:
                for key in list(self.all.keys()):
                    if self.all[key] == word2:
                        answer = key
                    else:
                        pass
                if answer == word1:
                    button = self.button_list[word1]
                    button.configure(
                        fg_color="green", hover_color="green", state="disabled"
                    )
                    del self.button_list[word1]

                    button = self.button_list[word2]
                    button.configure(
                        fg_color="green", hover_color="green", state="disabled"
                    )
                    del self.button_list[word2]
                    del self.words2learn[word2]

                    self.progress_int += 1
                    self.correct_matches_int.configure(text=self.progress_int)

                    self.still_to_learn_int -= 1

                    self.len_w2l -= 1
                    self.remaining_matches_int.configure(text=self.len_w2l)

                    self.known.update({word: answer})

                else:
                    button = self.button_list[word1]
                    button.configure(
                        fg_color=self.wrong_color, hover_color=self.wrong_color_hover
                    )

                    button = self.button_list[word2]
                    button.configure(
                        fg_color=self.wrong_color, hover_color=self.wrong_color_hover
                    )

                    self.unknown.update({word: answer})

            self.num.clear()

        if len(self.words2learn) >= 1:
            pass
        else:
            self.temp = 1
            # messagebox.showwarning("Error", "There aren't enough words to be learned (at least five)\nor\n All words to be learned have been learned!")

        if self.temp == 1:
            self.done()

        elif len(self.button_list) == 0:
            self.middle_frame.destroy()
            self.actual_match()
        else:
            pass

    def all_question(self) -> list:
        chosen_word = []
        chosen_def = []
        word_count = 0  # for loop
        while word_count < 4:
            word = random.choice(list(self.words2learn.keys()))
            definition = self.words2learn[word]
            if word not in chosen_word:
                chosen_word.append(word)
                chosen_def.append(definition)
                word_count += 1
            else:
                pass

        return chosen_word, chosen_def

    def make_dict(self, file) -> None:  # convert csv file to dict
        with open(file) as self.something:
            reader = csv.DictReader(self.something)
            for row in reader:
                self.words2learn.update({row["word"]: row["definition"]})

    def timer(self):
        minutes, seconds = divmod(self.actual_time, 60)
        self.time_label.configure(text="%02d:%02d" % (minutes, seconds))
        self.actual_time -= 1
        temp = self.time_label._text
        if minutes == 0 and seconds == 0:
            # messagebox.showwarning("Error", "Timer finished!")
            self.done()

        else:
            self.root.after(1000, self.timer)

    def timer_up(self):
        minutes, seconds = divmod(self.time_up_secs, 60)
        self.time_label.configure(text="%02d:%02d" % (minutes, seconds))
        self.time_up_secs += 1
        self.root.after(1000, self.timer_up)

    def back_button_pressed(self):
        self.back = True

    def known_unknown_get(self):
        return self.known, self.unknown

    def finished_def(self):
        self.finished = True

    def done(self):
        self.mainframe.destroy()
        self.menu_bar.destroy()
        self.finished_def()


if __name__ == "__main__":
    Match(ctk.CTk()).root.mainloop()
