import random
import time
import webbrowser
from tkinter import *
from tkinter import messagebox

# lists with questions , answers and money
questions_1 = {"Which of the following animals can run the fastest?": "A",
               "What does the term “SOS” commonly stand for?": "D",
               "Which company is known for publishing the Mario video game?": "B",
               "What is the rarest type of blood in the human body?": "A",
               "What is the name of this symbol: ¶": "D",
               "Which of the following is not an international organisation?": "D",
               "What is the speed of sound?": "B",
               "In total, how many novels were written by the Bronte sisters?": "D",
               "What was the first country to use tanks in combat during World War I?": "C",
               "Goulash is a type of beef soup in which country?": 'A',
               "Which of the following songs was the top-selling hit in 2019?": "A",
               "We often use sodium bicarbonate in the kitchen. What is its other name?": "D",
               "Which was the first film by Disney to be produced in colour?": "C",
               "Cu is the chemical symbol for which element?": "B",
               "In the series “Game of Thrones”, Winterfell is\n the ancestral home of which family?": "B",
               }

answers_1 = [["A. Cheetah", "B. Leopard", "C. Tiger", "D. Lion"],
             ["A. Save Our Sheep", "B. Save Our Ship", "C. Save Our Seal", "D. Save Our Souls"],
             ["A. Xbox", "B. Nintendo", "C. SEGA", "D. Electronic Arts"],
             ["A. AB negative", "B. O positive", "C. B negative", "D. A positive"],
             ["A. Biltong", "B. Fermata", "C. Interrobang", "D. Pilcrow"],
             ["A.FIFA", "B.NATO", "C.ASEAN", "D.FBI"],
             ["A. 120 km/h", "B. 1,200 km/h", "C. 400 km/h", "D. 700 km/h"],
             ["A.4", "B.5", "C.6", "D.7"],
             ["A. France", "B. Japan", "C. Britain", "D. Germany"],
             ["A. Hungary", "B. Czech Republic", "C. Slovakia", "D. Ireland"],
             ["A. Someone You Loved", "B. Old Town Road", "C. I Don’t Care", "D. Bad Guy"],
             ["A. Vinegar", "B. Sugar", "C. Salt", "D. Baking soda"],
             ["A. Toy Story", "B. Sleeping Beauty", "C. Snow White and the Seven Dwarfs", "D. Cinderella"],
             ["A. Oxygen", "B. Copper", "C. Zinc", "D. Helium"],
             ["A. The Lannisters", "B. The Starks", "C. The Tully’s", "D. The Targaryens"]]

money_list = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]


# start the coding----------------------------------------------------------------------------------------------------

def rounds():
    """
    rounds function is for each round. We have a not resizable window which shows the answer and the possible questions
    we have buttons for help , stop , and submit button. The command for the submit button is function submit.In this
    function we will check if the final answer of the player is correct or incorrect.
    """
    helps_ = ["50-50", "audience help", "phone"]
    i = 0
    while True:
        def helps():
            # 50-50 help
            def fif():
                def submit_f():
                    time.sleep(3)
                    if x2.get() == str(0):
                        submit_button_f.config(bg="green")
                        if i == 14:
                            messagebox.showinfo(title="WIN", message="Congratulations!You just won 1 million $!\n"
                                                                     "WHAT A GAME!")
                            quit()

                        messagebox.showinfo(title="RIGHT ANSWER!",
                                            message="CONGRATULATIONS!+{one} $".format(one=money_list[i]))
                        messagebox.showinfo(title="BE READY!",
                                            message="Press 'ok' in order to continue to round:{}!\n"
                                                    "Now it's your chance to take a small break!".format(i + 2))
                    else:
                        submit_button_f.config(bg="red", fg="black")
                        messagebox.showerror(title="FALSE ANSWER",
                                             message=f"Bad luck!The right answer was:{right_ABCD}\n"
                                                     f"You are out!")
                        if i >= 5:
                            messagebox.showinfo(title="MONEY EARNED IN SAFE ZONE",
                                                message="Pockets full of money!Money earned:"
                                                        "{} $".format(money_list[i - 1]))
                        elif i != 0 and i < 5:
                            messagebox.showinfo(title="MONEY EARNED", message="Pockets full of money!Money earned:{} $"
                                                .format(money_list[i - 1] // 2))
                        quit()
                    fif_window.destroy()

                fifty = []
                helps_.remove("50-50")
                help_window.destroy()
                window.destroy()
                fif_window = Tk()
                fif_window.title("50-50 HELP")
                fif_window.geometry("605x475")
                fif_window.config(background="#83ebca")
                one = answers_1[i][right]
                fifty.append(one)
                answers_1[i].remove(one)
                two = random.choice(answers_1[i])
                fifty.append(two)
                (Label(fif_window, bg="#83ebca", font=("cambria", 14),
                       text="You have now only 2 choices!\n It's 50-50!",
                       pady=20).pack())
                Label(fif_window, text=key, width=90, height=5, padx=10, font=("impact", 15),
                      bg="#3b1f91", fg="white").pack()
                x2 = StringVar()
                for index_2 in range(len(fifty)):
                    radio_fif = Radiobutton(fif_window,
                                            text=fifty[index_2],  # adds text to radio buttons
                                            value=index_2,  # assigns each radio button in different value
                                            padx=10,  # adds padding on x-axis
                                            variable=x2,
                                            activebackground="orange",
                                            selectcolor="orange",
                                            bg="#32b1e3",
                                            fg="white",
                                            font=("impact", 30),
                                            indicatoron=False,  # eliminate circle indicators
                                            width=50,
                                            cursor="crosshair",
                                            )
                    radio_fif.pack(anchor=CENTER)
                help_button_f = Button(fif_window, text="Click here for help", font=30, padx=10, width=25, height=2,
                                       bg="#0724a8", fg="white", command=helps)  # for help
                help_button_f.pack(anchor=SW)

                submit_button_f = Button(fif_window, text="Submit your answer", font=30, padx=10, width=25, height=2,
                                         command=submit_f, bg="#0724a8", fg="white",
                                         activebackground="orange")  # for help
                submit_button_f.place(x=303, y=351)
                stop_button_f = Button(fif_window, text="Click here to stop", font=30, padx=10, width=25, height=2,
                                       command=stop, bg="#0724a8", fg="red", activebackground="red",
                                       activeforeground="black")
                stop_button_f.pack(anchor=S)

                fif_window.mainloop()

            # audience help
            def aud():
                helps_.remove("audience help")
                help_window.destroy()
                messagebox.showinfo(title="Audience is voting", message="Audience is voting,please wait for results!")
                time.sleep(4)
                messagebox.showinfo(title="RESULTS", message=f"The results go with answer "
                                                             f"'{right_ABCD}' with a percentage of "
                                                             f"{random.uniform(50.00, 100.00):.3} %")

            # phone help
            def phone():
                def cnt():
                    time.sleep(45)
                    messagebox.showinfo(title="TIME'S UP",
                                        message="Time is up! Return to the question and answer. Keep "
                                                "in mind your friends advice!")
                    phone_window.destroy()

                helps_.remove("phone")
                help_window.destroy()
                phone_window = Tk()
                phone_window.title("Phone help")
                phone_window.config(background="#96ebd4")
                phone_window.geometry("500x400")
                Label(phone_window, text="Welcome to phone help!You will have\n 45 seconds to call him/her,\n"
                                         "ask him the question"
                                         " and the possible answers\n and finally take her/his advice!"
                                         " As long as the \nbottom button is orange,your\n time will run. "
                                         "Remember you have 45\n seconds available!",
                      pady=20,
                      font=("cambria", 15), bg="#96ebd4").pack()
                Button(phone_window, text="Start count-down", command=cnt, activebackground="orange",
                       bg="light yellow").pack()

                phone_window.mainloop()

            # main help chapter
            if len(helps_) == 0:
                messagebox.showerror(title="Out of helps", message="You have no remaining helps!Think about it!")
            else:
                help_window = Tk()
                help_window.title("HELP CHAPTER")
                help_window.geometry("400x400")
                help_window.config(background="light blue")
                help_window.resizable(False, False)
                # -------------------------
                Label(help_window, text="WELCOME TO HELP CHAPTER\nCHOOSE YOUR HELP!", bg="light blue", pady=10).pack()

                Y = 100
                for help__ in helps_:
                    if help__ == "50-50":
                        Button(help_window, text=help__, width=17, height=3, command=fif, bg="#db96eb").place(x=140,
                                                                                                              y=Y)
                    elif help__ == "audience help":
                        Button(help_window, text=help__, width=17, height=3, command=aud, bg="#db96eb").place(x=140,
                                                                                                              y=Y)
                    elif help__ == "phone":
                        (Button(help_window, text=help__, width=17, height=3, command=phone, bg="#db96eb")
                         .place(x=140, y=Y))
                    Y += 70
                help_window.mainloop()

        def submit():

            time.sleep(3)
            if x.get() == str(right):
                submit_button.config(bg="green")
                if i == 14:
                    messagebox.showinfo(title="WIN", message="Congratulations!You just won 1 million $!\n"
                                                             "WHAT A GAME!")
                    quit()

                messagebox.showinfo(title="RIGHT ANSWER!", message="CONGRATULATIONS!+{one} $".format(one=money_list[i]))
                messagebox.showinfo(title="BE READY!", message="Press 'ok' in order to continue to round: {}!\n"
                                                               "Now it's your chance to take a small break!"
                                    .format(i + 2))

            else:
                submit_button.config(bg="red", fg="black")
                messagebox.showerror(title="FALSE ANSWER", message=f"Bad luck!The right answer was:{right_ABCD}\n"
                                                                   f"You are out!")
                if i >= 5:
                    messagebox.showinfo(title="MONEY EARNED IN SAFE ZONE", message="Pockets full of money!Money earned:"
                                                                                   "{} $".format(money_list[i - 1]))
                elif i != 0 and i < 5:
                    messagebox.showinfo(title="MONEY EARNED", message="Pockets full of money!Money earned:{} $"
                                        .format(money_list[i - 1] // 2))
                quit()
            window.destroy()

        def stop():
            if i >= 5:
                messagebox.showinfo(title="STOP", message="Money earned:{} $".format(money_list[i - 1] // 3))
            else:
                messagebox.showinfo(title="STOP", message="Unfortunately you stopped before 5 rounds.Because of"
                                                          " that you leave with empty pockets!")
            quit()

        window = Tk()
        window.title("Millionaire game")
        window.geometry("605x520")
        window.resizable(False, False)
        window.config(background="#b76eeb")

        key = list(questions_1)[i]
        right_ABCD = questions_1[key]
        right = 3
        if right_ABCD == "A":
            right = 0
        elif right_ABCD == "B":
            right = 1
        elif right_ABCD == "C":
            right = 2
        # answers
        answer_list = answers_1[i]
        question_label = Label(window, text=key, width=90, height=5, padx=5, font=("impact", 15),
                               bg="#3b1f91", fg="white")
        question_label.pack()
        x = StringVar()
        answer_list = answers_1[i]
        for index in range(len(answer_list)):
            radio = Radiobutton(window,
                                text=answer_list[index],  # adds text to radio buttons
                                value=index,  # assigns each radio button in different value
                                padx=10,  # adds padding on x-axis
                                variable=x,
                                activebackground="orange",
                                selectcolor="orange",
                                bg="#32b1e3",
                                fg="white",
                                font=("impact", 30),
                                indicatoron=False,  # eliminate circle indicators
                                width=375,
                                cursor="crosshair",
                                )
            radio.pack(anchor=CENTER)
        help_button = Button(window, text="Click here for help", font=30, padx=10, width=25, height=2,
                             bg="#0724a8", fg="white", command=helps)  # for help
        help_button.pack(anchor=SW)

        submit_button = Button(window, text="Submit your answer", font=30, padx=10, width=25, height=2,
                               command=submit, bg="#0724a8", fg="white", activebackground="orange")  # for help
        submit_button.place(x=302, y=395)
        stop_button = Button(window, text="Click here to stop", font=30, padx=10, width=25, height=2,
                             command=stop, bg="#0724a8", fg="red", activebackground="red", activeforeground="black")
        stop_button.pack(anchor=S)

        # menu
        def rules():
            webbrowser.open("https://wwbm.com/rules")

        menu_bar = Menu(window)
        window.config(menu=menu_bar)

        fileMenu = Menu(menu_bar, tearoff=0, font=("Cambria", 12))
        menu_bar.add_cascade(label="Options", menu=fileMenu)
        fileMenu.add_command(label="Rules", command=rules)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=quit)
        window.mainloop()
        i += 1


def main():
    # this is the main function
    try:
        def rules():
            webbrowser.open("https://wwbm.com/rules")

        def start():
            window.destroy()
            rounds()

        window = Tk()
        window.geometry("900x400")
        window.resizable(False, False)
        window.config(background="light yellow")
        window.title("Welcome to the millionaire game!")
        Label(window, text="MILLIONAIRE GAME RULES💡", bg="light yellow", font=("Helvetica", 16, "bold italic")).pack()
        Label(window, text="""
        The Who Wants to Be a Millionaire questions are structured according to five different Levels with each level  increasing
        in difficulty. Each level contains three questions.
        
        Questions that are grouped into the same level will all be of similar difficulty. For example: Questions 1-3 make up the
        first Level and will contain the easiest questions. The second Level (Questions 4 - 6) will be slightly more difficult,
        followed by the third Level (Questions 7-9). The fourth Level (Questions 10-12) will consist of really difficult
        questions, followed by the fifth, and last, level (Questions 13 - 15) that will pose the most difficult questions of
        the game.
        
        It is important to remember that the questions which make up each level will not necessarily relate to the same or even
        similar topics, but their overall level of difficulty will be the same
    """
              , bg="light yellow", font=("Cambria", 12)).pack()
        Label(window, text="♾️" * 20000, bg="light yellow").pack()
        Button(window, bg="#f7c194", text="Start!", width=13, height=2, command=start,
               activebackground="light yellow").place(x=270, y=320)
        Button(window, bg="#f7c194", text="Detail rules", width=13, height=2, command=rules,
               activebackground="light yellow").place(x=560, y=320)
        window.mainloop()
    except IndexError:
        messagebox.showerror(title="ERROR", message="Oops something went wrong.ERROR 1")
    except Exception:
        messagebox.showerror(title="ERROR", message="Oops something went wrong. ERROR 2")


if __name__ == "__main__":
    main()
