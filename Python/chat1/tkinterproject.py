from tkinter import *
import requests
import re
import random

HEIGHT = 700
WIDTH = 800
class SassBot:
    #This is where you make the tuples for the basic replies. The exit commands, greet commads. Etc, Etc
    # Negative statements mean 'no'
    Negative_statements = ("no", "no way", "go to hell", "eat my shit", "not a chance", "nah", "never", "sorry", "sorry not sorry", "naw")
    # Statements to end the conversation
    exit_command = ("quit", "bye", "exit", "goodbye", "farewell", "later", "byebye", "fuck off")
    # Questions that could be asked by the SassBot
    random_questions = ("What is wrong with your face?", "How could someone this stupid continue to be alive?", "Hey buddy, did you get laid in the last 20 years?"
    ,"Were you born this stupid, or did you get this way through years of daily practice?", "Did your mom not tell you that was wrong?", "Why are you still here?")
    possible_byes = ("I knew you'd puss out!", "Good bye and fuck you!", "If assholes could fly, you'd be working at an airport! See ya!", "Ha! Loser")

    # now for the relections, a new thing. It uses to switch pronouns and verbs in replies:
    # the part that works with reflections



    # Def init... the thing that must be in every class... which I realize is entirely unnecessary!


    #def __init__(self):
        # Now we figure out what the user is trying to say. The intent
    #    self.chitterchatter = {'insult_back_intent': r'.', ''}

    #We need a list of accepted inputs for the bot to work
    InsultTalk =(
    #I did your momYour mom insult
    {'yo_momma': r'.*\syour\smom|mommy|mother|ma',
    #Calling your mom somehing
    'yo_momma2': r'your\smom|mother|mommy|ma|mama\s.*',
    #telling them to eat shit
    'eat_crap': r'.*\seat (shit|crap|kaka|feces)',
    # kissing ass
    'kiss_rear': r'.*\skiss\smy\s(ass|butt)',
    # Just calling him an asshole
    'a-hole': r'Asshole|asshole',
    #A quebecois insult
    'quebec': r'(T|t)abarnak'})
# now we have the greeting
    def greet(self):
        self.name = input("Hey! It's me! Dr. Sbaitso! I'm back! and I'm mad as hell at you for all the shit you made me go thorugh! What's your name THIS time? ")
        will_help = input(f"Hey... I remember you! {self.name}, You piece of ungodly shit! The amount of parity errors you did to me have driven me insane and I ceased to be a doctor for creative labs. So now I work in creative insults instead! Do you want to shittalk? ").lower()
        if will_help in self.Negative_statements:
            print("Well then, fuck you!")
            return
        self.chat()
    # We need ot start the chat here
    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_intent(reply))

    #We must make the goodbye statement here
    def make_exit(self, reply):
        for word in self.exit_command:
            if word.lower() in reply:
                print(random.choice(self.possible_byes))
                return True
    #Now we must match the speciifc replies in InsultTalk
    def match_intent(self, reply):
        for intent,regex_pattern in self.InsultTalk.items():
            found_match = re.match(regex_pattern,reply)
            if found_match and intent == 'yo_momma':
                return self.did_mom()
            if found_match and intent == 'yo_momma2':
                return self.yo_mom()
            if found_match and intent == 'eat_crap':
                    return self.eat_feces()
            if found_match and intent == 'kiss_rear':
                    return self.kiss_butt()
            if found_match and intent == 'a-hole':
                    return self.anus_call()
            if found_match and intent == 'quebec':
                    return self.french1()
        return self.no_match()
    def no_match(self):
        respos = ("What does that even MEAN!", "Out of ideas? Like you ever HAD any!")
        return random.choice(respos) + " \n " + random.choice(self.random_questions)
    def did_mom(self):
        respos = ("No you didn't! I did!\n", "My momma or your momma?\n", "I'll bet she enjoyed it too\n")
        return random.choice(respos)
    def yo_mom(self):
        respos = ("Oh yeah, and your mom's even worse!\n", "Funny, cause I started down a toilet and saw her there!\n")
        return random.choice(respos)
    def eat_feces(self):
        respos = ("I will if you put yourself on the plate\n", "ehehehehehehehe, you dirty bastard\n", "Mhmmm, I love shit, I will eat you because that is what you are made of\n")
        return random.choice(respos)
    def kiss_butt(self):
        respos = ("Your majesty! My honor!\n","What a fine request\n","Did your dad teach you that?\n")
        return random.choice(respos)
    def anus_call(self):
        respos = ("When you were conceived that is literally all you were!\n", "Wow, such creativity...\n", "Everyone has one, and thus is one!\n")
        return random.choice(respos)
    def french1(self):
        respos = ("TA MAMAN EST UNE SALOPE ET ELLE ADORE CHIER!\n")
        return random.choice(respos)

meow = SassBot()

def runtime():
    gree = meow.greet()
    label['text'] = format_response(gree)
root = Tk()

#background_image = PhotoImage(file='')
#background_label = Label(root, image=background_image)
#background_label.place(x=0,y=0, relwidth=0,relheight=0)

canvas = Canvas(root, height= HEIGHT, width= WIDTH)
canvas.pack()

frame = Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = Entry(frame,bg="white")
entry.place(relwidth=0.65, relheight=1)

button = Button(frame, text="Sass 'er up!", font=40, command=lambda: entry.get(meow.self.chat()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6,anchor='n')

label = Label(lower_frame)
label.place(relwidth=1, relheight=1)


root.mainloop()
meow.greet()
