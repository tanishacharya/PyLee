# PyLee
This is our final project for CS50’s Introduction to programming with Python.  
#### Video Demo
https://youtu.be/vimtdQEhCLI
## Introduction
PyLee is a program which helps students learn vocabulary *like a pro*.  
It has got many different learning modes which are listed below:  
- flash cards
- multiple choice
- quiz
- match

They will be explained further below.

Depending on the mode, you can choose from different settings:  
- case insensitivity  
- accept minor mistakes  
- autocheck mistake  
- ask if word was known  

If you only want to learn a part of the given words, you can divide it into halfs/thirds/fourths.  
It's possible to set a timer per exercise or even per word (depending on the learning mode).  
Of course the user can choose if they want to learn the word or definition.  
There are progress bars, so that they can easily see their progress.

When the program is started, the user is greeted with a home screen. There they can either make a new (csv-) file or open a csv file.  
The changes to the respective version are described as well.  

## Learning Modes
### Flash Cards
In this mode, a word is shown and depending on if the user selected that a "known-prompt" should come, it asks if the word was known. In case the word isn't given in time when the they selected time per word, it simply is skipped.  
When you click on the flash card, it is flipped and the meaning is revealed.  

### Multiple Choice
In this mode, the user can set a timer. If not, a stopwatch is started.  
The program asks them for the meaning of a word and is given 4 options to choose from.  
If the answer is wrong, the answer is shown. Otherwise it goes to the next question.  

### Quiz
In this mode, the user can choose from all the settings, except to ask if the word was wrong. If the timer option isn't selected, a countdown is started.  
The program prompts the user for a (written) answer (&rarr; press enter to check answer). If the answer is wrong, it shows them the right answer. They can also reveal the answer, in case the forgot it. To skip the word simply click next.  

### Match
Here, only a timer can be set.  
This mode is similar to the game "memory". The user has to select a word from the left column and one from the right column.  
If the allocation is correct, the color of the button is changed to green. If it's wrong, both buttons are colored red.  
As soon as all are matched, the next set of words is shown.  

### The Ending
When the previously selected mode has asked all the words, a summary is shown.  
Here the user can see all their correct and wrong words listed. They can choose if they want to learn only the wrong words of if they want to restart PyLee.  

## Other
### Menu Bar
We really wanted to have a menu bar, where the user could go back. We tried to use the inbuilt CTkOptionmenu. It worked on Windows but not on Mac so we put it *inside* the window on the top.  

### Custom Tkinter
After we'd choosen what out final project should do, we had to choose a GUI library.  
After a lot of research, we selected Custom Tkinter because its syntax in pretty easy and it looks more modern than the normal Tkinter. 