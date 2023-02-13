from tkinter import *
from tkinter import messagebox as mb

# Questions, options, answers dictionary
data={
    "ques": [
        "Q1. What is the data type of print(type(10))?",
        "Q2. In Python 3, what is the output of type(range(5)).",
        "Q3. What is the output of the expression  print(-18 // 4)?",
        "Q4. Which operator has higher precedence in the following list?",
        "Q5. Choose the correct function to get the ASCII code of a character."
    ],
    "ans": [
        3,
        2,
        3,
        1,
        2
    ],
    "marks": [
        2,
        3,
        2,
        5,
        5
    ],
    "choices": [
        [
            "float",
            "integer",
            "int",
            "None"
        ],
        [
            "int",
            "range",
            "list",
            "None"
        ],
        [
            "-4",
            "4",
            "-5",
            "5"
        ],
        [
            "** (Exponent)",
            "& (BitWise AND)",
            "% (Modulus)",
            "> (Comparison)"
        ],
        [
            "char('char')",
            "ord('char')",
            "ascii('char')",
            "All of them"
        ]
    ]
}

questions = data["ques"]
answer = data["ans"]
options = data["choices"]
points = data["marks"]
scoreboard={}

# Welcome page function
def welcome():
    win = Tk()
    win.title("PSN Quiz")
    win.geometry("1000x450")

    def startQuiz():
        global user
        user= name.get()
        if True:
            if user=="":
                mb.showwarning("Warning","Please enter name!")
            else:
                win.destroy()
                print(user)



    welcome_message = Label(
        win,  
        text = "Welcome to PSN Quiz",
        width = 60,  
        font = ('Times New Roman', 20, 'bold')  
    )
    welcome_message.place(x=50,y=50)

    name_message = Label(
        win,  
        text = "Enter you name: ",  
        font = ('Arial', 14, 'bold')  
    )
    name_message.place(x=50,y=150)
    user_name = StringVar()
    name = Entry(
        win,
        textvariable=user_name,
        width=40,
        font=('Arial',14)

    )
    name.place(x=250, y=150)
    button=Button(
        win, 
        text="Start Quiz", 
        command=startQuiz,
        width = 20,  
        bg = "Green",  
        fg = "white",  
        font = ("ariel", 16, " bold")
    )
    button.place(x=350, y=300)

    # Credit sections
    makers = ['Saisha Sarangi - S328959','Pooja Pokharel - S361202','Md Abdullah Al Noman Majumder - S363292']
    Label(
        win,
        text = "Created By",
        width = 20,  
        font = ('Times New Roman', 14, 'bold')
    ).place(x=650,y=350)
    y_pos=360
    for i in makers:
        y_pos+=20
        Label(
            win,
            text = i,  
            font = ('Times New Roman', 12, 'bold')
        ).place(x=680,y=y_pos) 
    win.mainloop()

# restrat of the quiz functions
def restart(win):
    win.destroy()
    welcome()
    global quizWindow
    quizWindow = Tk()
    quizWindow.title('PSN Quiz')
    quizWindow.geometry("1000x450")
    quiz1=My_Quiz()

# quit the quiz funtions
def quit(win):
    temp = mb.askquestion('Quit','Are you sure?')
    print(temp)
    if temp=='yes':
        win.destroy()

def restart_button(win):
        restart_button= Button(
            win,
            text='Restart Test',
            background='Maroon',
            foreground='White',
            width=10,
            command=lambda: restart(win),
            font=('Arial',16,'bold')
        )
        restart_button.place(x=350,y=280)

def leaderboard(win):
    win.destroy()
    leaderboard_win = Tk()
    leaderboard_win.title('Leaderboard')
    leaderboard_win.geometry("1000x450")

    keys=list(scoreboard.keys())
    y_pos = 50
    Label(
        leaderboard_win,
        text='Leaderboard',
        width=60,
        font=('Arial',20,'bold'),
        background='#D389e4',
        foreground='White'
    ).place(x=0,y=2)

# show how many users take the test and their points
    for key in keys:
        Label(
            leaderboard_win,
            text=key,
            width=20,
            font=('Arial',20,'bold'),
            background='#1bb8c1',
            foreground='White'
        ).place(x=50,y=y_pos)
        Label(
            leaderboard_win,
            text=scoreboard[key],
            width=5,
            font=('Arial',20,'bold'),
            background='#09a6af',
            foreground='White'
        ).place(x=600,y=y_pos)

        y_pos += 50
    
    restart_button(leaderboard_win)
    Button(
        leaderboard_win,
        text='Quit',
        background='Red',
        foreground='White',
        width=10,
        font=('Arial',16,'bold'),
        command= lambda : quit(leaderboard_win)
    ).place(x=500,y=280)


# creating My_Quiz class for quiz questions
class My_Quiz:
    def __init__(self):
        self.question_number = 0
        self.right_answer = 0
        self.marks = 0
        self.total_question = len(questions)
        self.total_marks = sum(points)
        self.display_title()
        self.display_questions()
        self.option_select = IntVar()
        self.options = self.options_button()
        self.display_options()
        self.button()

    #  Header display for quiz window
    def display_title(self):
        myTitle = Label(  
            quizWindow,  
            text = f"Welcome {user}! Take the test.",  
            width = 60,  
            bg = "Sky Blue",  
            fg = "white",  
            font = ("Arial", 20, "bold")  
        )  
             
        myTitle.place(x = 0, y = 2)     

    #  Display only questions
    def display_questions(self):
        question_label = Label(
            quizWindow,
            text=questions[self.question_number],
            font = ('ariel', 16, 'bold'),  
            anchor = 'w'
        )
        question_label.place(x = 70, y = 100)

        points_label = Label(
            quizWindow,
            text=f'{points[self.question_number]} points',
            font = ('ariel', 16),  
        )
        points_label.place(x = 800, y = 150)

    # Display all options button
    def options_button(self):
        option_list = []
        y_pos = 150

        while(len(option_list)<4):
            radio_button = Radiobutton(
                quizWindow,
                text = " ",  
                variable = self.option_select,  
                value = len(option_list) + 1,  
                font = ("Arial", 14)
            )

            option_list.append(radio_button)
            radio_button.place(x = 100, y = y_pos)
            y_pos += 40

        return option_list

    # Display all options button with options of the questions
    def display_options(self):
        val = 0
        self.option_select.set(0)
        for opt in options[self.question_number]:  
            self.options[val]['text'] = opt  
            val += 1

    # Checking answer after every questions
    def check_answer(self,q_number):
        if self.option_select.get() == answer[q_number]:
            self.right_answer +=1
            self.marks += points[q_number]

    # Display result after completing the test
    def display_results(self):
        quizWindow.destroy()
        result_win = Tk()
        result_win.geometry("1000x450")
        result_win.title('Result')

        Label(
            result_win,
            text='Result',
            background='Green',
            foreground='White',
            width=60,
            font=('Arial',20,'bold')
        ).place(x=0,y=2)
        result_label = Label(
            result_win,
            text=f"You got {self.marks} points (out of {self.total_marks} points).",
            font=('Arial',20,'bold'),
            width=60
        )
        result_label.place(x=0,y=150)
        scoreboard[user]=self.marks

        #restart button
        restart_button(result_win)
        leaderboard_button= Button(
            result_win,
            text='See Leaderboard',
            background='#D389e4',
            foreground='White',
            width=20,
            command=lambda: leaderboard(result_win),
            font=('Arial',16,'bold')
        )
        leaderboard_button.place(x=500,y=280)

        
    # Next button to go next questions
    def next_button(self):
        # Checking if user choose an options or not
        if self.option_select.get() == 0: 
            mb.showwarning('Warning!','Please select an option!')
        
        self.check_answer(self.question_number)
        self.question_number += 1

        if self.question_number == self.total_question:
            print(f'Test over {self.right_answer}')
            self.display_results()

        else:
            self.display_questions()
            self.display_options()



    def button(self):
        next_button = Button(
            quizWindow,
            text='Next',
            command=self.next_button,
            width = 12,  
            bg = "Maroon",  
            fg = "white",  
            font = ("Arial", 16, "bold")
        )
        next_button.place(x = 350, y = 380)

# calling welcome window
welcome()


quizWindow = Tk()
quizWindow.title('PSN Quiz')
quizWindow.geometry("1000x450")

# create an object of quiz
quiz=My_Quiz()

quizWindow.mainloop()