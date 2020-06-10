import random
import tkinter as tk
window=tk.Tk()
window.geometry("500x500")
window.title("Rock,Paper,Scissor game")
User_score=0
computer_score=0
User_choice=''
computer_choice=''
def choice_to_letter(choice):
    rps={'rock':'R','paper':'P','scissor':'S'}
    return rps[choice]

def letter_to_choice(letter):
    rps={'R':'rock','P':'paper','S':'scissor'}
    return rps[letter]

def computer_choice():
    return random.choice(['rock','paper','scissor'])

def result(human_choice,computer_choice):
    global User_score
    global computer_score
    user=choice_to_letter(human_choice)
    computer=choice_to_letter(computer_choice)
    if user==computer:
        print('Draw match')
    elif(user=='P'and computer=='S') or (user=='S' and computer=='R') or (user=='R' and computer=='P'):
        print('computer wins')
        computer_score+=1

    else:
        print('You win')
        User_score+=1
    text_area=tk.Text(master=window,height=10,width=30,bg='#4285F4')
    text_area.grid(column=0,row=4)
    answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} ".format(uc=User_Choice,cc=Computer_choice,u=User_score,c=Computer_score)    
    text_area.insert(tk.END,answer)
def rock():
    global User_choice
    global computer_Choice
    User_choice='rock'
    computer_choice=computer_choice()
    result(User_Choice,computer_choice)
def paper():
    global User_choice
    global computer_choice
    User_choice='paper'
    computer_choice=computer_choice()
    result(User_choice,computer_choice)
def scissor():
    global User_choice
    global computer_choice
    User_choice='scissor'
    comp_choice=computer_choice() 
    result(User_choice,computer_choice)
button1 = tk.Button(text="       Rock       ",bg="red",command=rock)
button1.grid(column=0,row=1)
button2 = tk.Button(text="       Paper      ",bg="skyblue",command=paper)
button2.grid(column=0,row=2)
button3 = tk.Button(text="      Scissor     ",bg="lightgreen",command=scissor)
button3.grid(column=0,row=3)
window.mainloop()
