import random
import time
import webbrowser
from tkinter import *
from tkinter import messagebox

# MILLIONAIRE GAME GUI IMPLEMENTATION

# List of dictionaries containing the question text and the correct answer letter
QUESTIONS = [
    {"q": "Which of the following animals can run the fastest?",                  "ans": "A"},
    {"q": "What does the term \"SOS\" commonly stand for?",                        "ans": "D"},
    {"q": "Which company is known for publishing the Mario video game?",           "ans": "B"},
    {"q": "What is the rarest type of blood in the human body?",                  "ans": "A"},
    {"q": "What is the name of this symbol: ¶",                                   "ans": "D"},
    {"q": "Which of the following is not an international organisation?",          "ans": "D"},
    {"q": "What is the speed of sound?",                                          "ans": "B"},
    {"q": "In total, how many novels were written by the Bronte sisters?",         "ans": "D"},
    {"q": "What was the first country to use tanks in combat during World War I?", "ans": "C"},
    {"q": "Goulash is a type of beef soup in which country?",                     "ans": "A"},
    {"q": "Which of the following songs was the top-selling hit in 2019?",         "ans": "A"},
    {"q": "We often use sodium bicarbonate in the kitchen. What is its other name?","ans": "D"},
    {"q": "Which was the first film by Disney to be produced in colour?",          "ans": "C"},
    {"q": "Cu is the chemical symbol for which element?",                         "ans": "B"},
    {"q": "In the series \"Game of Thrones\", Winterfell is\n the ancestral home of which family?", "ans": "B"},
]

# Parallel list of choices corresponding to each question index
CHOICES = [
    ["A. Cheetah",        "B. Leopard",    "C. Tiger",                             "D. Lion"],
    ["A. Save Our Sheep", "B. Save Our Ship","C. Save Our Seal",                   "D. Save Our Souls"],
    ["A. Xbox",           "B. Nintendo",   "C. SEGA",                              "D. Electronic Arts"],
    ["A. AB negative",    "B. O positive", "C. B negative",                        "D. A positive"],
    ["A. Biltong",        "B. Fermata",    "C. Interrobang",                       "D. Pilcrow"],
    ["A.FIFA",            "B.NATO",        "C.ASEAN",                              "D.FBI"],
    ["A. 120 km/h",       "B. 1,200 km/h", "C. 400 km/h",                          "D. 700 km/h"],
    ["A.4",               "B.5",           "C.6",                                  "D.7"],
    ["A. France",         "B. Japan",      "C. Britain",                           "D. Germany"],
    ["A. Hungary",        "B. Czech Republic","C. Slovakia",                      "D. Ireland"],
    ["A. Someone You Loved","B. Old Town Road","C. I Don't Care",                 "D. Bad Guy"],
    ["A. Vinegar",        "B. Sugar",      "C. Salt",                              "D. Baking soda"],
    ["A. Toy Story",      "B. Sleeping Beauty","C. Snow White and the Seven Dwarfs","D. Cinderella"],
    ["A. Oxygen",         "B. Copper",     "C. Zinc",                              "D. Helium"],
    ["A. The Lannisters", "B. The Starks", "C. The Tully's",                       "D. The Targaryens"],
]

# Cash prizes corresponding to each question level (0 to 14)
MONEY = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]

# Helper dictionary to map answer letters to list indices
LETTER_TO_INDEX = {"A": 0, "B": 1, "C": 2, "D": 3}



class WelcomeScreen:
    """Displays the initial game screen, including rules and the start option."""

    def __init__(self) -> None:
        # Initialize the main welcome window
        self.window = Tk()
        self.window.geometry("900x400")
        self.window.resizable(False, False)
        self.window.config(background="light yellow")
        self.window.title("Welcome to the millionaire game!")
        
        # Build UI components and enter the main event loop
        self._build()
        self.window.mainloop()

    def _build(self) -> None:
        """Creates and places layout widgets for the welcome screen."""
        # Main Title Header
        Label(self.window,
              text="MILLIONAIRE GAME RULES💡",
              bg="light yellow",
              font=("Helvetica", 16, "bold italic")).pack()

        # Detailed textual description of game rules
        Label(self.window, bg="light yellow", font=("Cambria", 12), text="""
        The Who Wants to Be a Millionaire questions are structured according to five different Levels with each level increasing
        in difficulty. Each level contains three questions.

        Questions that are grouped into the same level will all be of similar difficulty. For example: Questions 1-3 make up the
        first Level and will contain the easiest questions. The second Level (Questions 4 - 6) will be slightly more difficult,
        followed by the third Level (Questions 7-9). The fourth Level (Questions 10-12) will consist of really difficult
        questions, followed by the fifth, and last, level (Questions 13 - 15) that will pose the most difficult questions of
        the game.

        It is important to remember that the questions which make up each level will not necessarily relate to the same or even
        similar topics, but their overall level of difficulty will be the same
    """).pack()

        # Decorative separator using symbols
        Label(self.window, text="♾️" * 20000, bg="light yellow").pack()

        # Start button to initialize the central Game controller
        Button(self.window, bg="#f7c194", text="Start!", width=13, height=2,
               command=self._start, activebackground="light yellow").place(x=270, y=320)

        # Detail rules button to open external official rules via browser
        Button(self.window, bg="#f7c194", text="Detail rules", width=13, height=2,
               command=lambda: webbrowser.open("https://wwbm.com/rules"),
               activebackground="light yellow").place(x=560, y=320)

    def _start(self) -> None:
        """Destroys the welcome window and initiates the core gameplay."""
        self.window.destroy()
        Game().run()



class FiftyFiftyLifeline:
    """Handles the 50-50 lifeline logic by filtering out incorrect answers."""

    @staticmethod
    def apply(choices: list[str], correct_letter: str) -> list[str]:
        """Filters choices down to the correct answer and one random wrong answer."""
        # Find the text variant representing the correct answer
        correct_choice = choices[LETTER_TO_INDEX[correct_letter]]
        
        # Isolate all incorrect options
        wrong_choices  = [c for c in choices if c != correct_choice]
        
        # Select one wrong option at random to keep
        remaining_wrong = random.choice(wrong_choices)
        
        # Group, randomize position, and return the two remaining choices
        result = [correct_choice, remaining_wrong]
        random.shuffle(result)
        return result


class AudienceLifeline:
    """Simulates a public audience poll where the crowd votes for the answer."""

    @staticmethod
    def apply(parent: Tk, correct_letter: str) -> None:
        """Triggers voting simulation alerts and calculates statistical feedback."""
        # Initial notification dialog to prompt waiting period
        messagebox.showinfo(title="Audience is voting",
                            message="Audience is voting, please wait for results!",
                            parent=parent)
        
        # Simulate background processing delay
        time.sleep(4)
        
        # Generate a high probability winning percentage for the correct option
        pct = random.uniform(50.00, 100.00)
        
        # Output final polling metrics to user interface
        messagebox.showinfo(title="RESULTS",
                            message=f"The results go with answer '{correct_letter}' "
                                    f"with a percentage of {pct:.3}%",
                            parent=parent)


class PhoneLifeline:
    """Creates an auxiliary countdown window mimicking a call to a friend."""

    def apply(self, parent: Tk) -> None:
        """Initializes and builds the secondary Toplevel countdown frame."""
        self.phone_window = Toplevel(parent)
        self.phone_window.title("Phone help")
        self.phone_window.config(background="#96ebd4")
        self.phone_window.geometry("500x400")

        # Instructions outlining the lifeline context
        Label(self.phone_window,
              text="Welcome to phone help! You will have\n 45 seconds to call him/her,\n"
                   "ask him the question and the possible answers\n and finally take her/his advice!"
                   " As long as the \nbottom button is orange, your\n time will run. "
                   "Remember you have 45\n seconds available!",
              pady=20, font=("cambria", 15), bg="#96ebd4").pack()

        # Action execution button for launching timer thread simulation
        Button(self.phone_window, text="Start count-down",
               command=self._countdown,
               activebackground="orange", bg="light yellow").pack()

        self.phone_window.mainloop()

    def _countdown(self) -> None:
        """Suspends the runtime for 45 seconds before notifying timer termination."""
        time.sleep(45)
        messagebox.showinfo(title="TIME'S UP",
                            message="Time is up! Return to the question and answer. "
                                    "Keep in mind your friend's advice!",
                            parent=self.phone_window)
        self.phone_window.destroy()



class RoundWindow:
    """Manages rendering, validation, and layout routing for active gaming rounds."""

    def __init__(self, game: "Game", round_index: int,
                 forced_choices: list[str] | None = None) -> None:
        self.game          = game
        self.i             = round_index
        self.correct_letter = QUESTIONS[self.i]["ans"]
        self.correct_index  = LETTER_TO_INDEX[self.correct_letter]

        # Check if custom sub-selections (from 50-50 lifeline) must be instantiated
        if forced_choices:
            self.choices       = forced_choices
            # Dynamically trace the location of the valid answer letter within the partial list
            self.correct_index = next(
                idx for idx, c in enumerate(forced_choices)
                if c.startswith(self.correct_letter)
            )
        else:
            # Fall back to standard option configuration data arrays
            self.choices = CHOICES[self.i]

        self._build()

    def _build(self) -> None:
        """Defines Tkinter canvas constraints and appends interactive UI controls."""
        self.window = Tk()
        self.window.title("Millionaire game")
        self.window.geometry("605x520")
        self.window.resizable(False, False)
        self.window.config(background="#b76eeb")

        # Question header text panel display
        Label(self.window,
              text=QUESTIONS[self.i]["q"],
              width=90, height=5, padx=5,
              font=("impact", 15),
              bg="#3b1f91", fg="white").pack()

        # Variable structure holding tracking value of targeted radio buttons
        self.selected = StringVar()
        
        # Loop to create stylized individual radio selections for choices
        for index, choice in enumerate(self.choices):
            Radiobutton(self.window,
                        text=choice,
                        value=index,
                        padx=10,
                        variable=self.selected,
                        activebackground="orange",
                        selectcolor="orange",
                        bg="#32b1e3",
                        fg="white",
                        font=("impact", 30),
                        indicatoron=False, # Transforms default bubbles into flat pushable buttons
                        width=375,
                        cursor="crosshair").pack(anchor=CENTER)

        # Trigger button for lifelines panel
        Button(self.window, text="Click here for help",
               font=30, padx=10, width=25, height=2,
               bg="#0724a8", fg="white",
               command=self._open_help).pack(anchor=SW)

        # Answer verification processing button
        self.submit_button = Button(self.window, text="Submit your answer",
                                    font=30, padx=10, width=25, height=2,
                                    bg="#0724a8", fg="white",
                                    activebackground="orange",
                                    command=self._submit)
        self.submit_button.place(x=302, y=395)

        # Quit game mechanism button
        Button(self.window, text="Click here to stop",
               font=30, padx=10, width=25, height=2,
               bg="#0724a8", fg="red",
               activebackground="red", activeforeground="black",
               command=self._stop).pack(anchor=S)

        # Context Menu setups
        menu_bar = Menu(self.window)
        self.window.config(menu=menu_bar)
        file_menu = Menu(menu_bar, tearoff=0, font=("Cambria", 12))
        menu_bar.add_cascade(label="Options", menu=file_menu)
        file_menu.add_command(label="Rules", command=lambda: webbrowser.open("https://wwbm.com/rules"))
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=quit)

        self.window.mainloop()

    def _submit(self) -> None:
        """Delays slightly for suspense, then evaluates chosen answer index."""
        time.sleep(3)
        if self.selected.get() == str(self.correct_index):
            self._on_correct()
        else:
            self._on_wrong()

    def _on_correct(self) -> None:
        """Fires success notifications on accurate validations and routes progression."""
        self.submit_button.config(bg="green")

        # Win condition logic triggered on passing the final milestone index (14)
        if self.i == 14:
            messagebox.showinfo(title="WIN",
                                message="Congratulations! You just won 1 million $!\nWHAT A GAME!")
            quit()

        # Regular question clear alert sequences
        messagebox.showinfo(title="RIGHT ANSWER!",
                            message=f"CONGRATULATIONS! +{MONEY[self.i]} $")
        messagebox.showinfo(title="BE READY!",
                            message=f"Press 'ok' to continue to round: {self.i + 2}!\n"
                                    "Now it's your chance to take a small break!")
        self.window.destroy()
        self.game.next_round()

    def _on_wrong(self) -> None:
        """Fires loss diagnostic alerts and system terminations on incorrect choice input."""
        self.submit_button.config(bg="red", fg="black")
        messagebox.showerror(title="FALSE ANSWER",
                             message=f"Bad luck! The right answer was: {self.correct_letter}\nYou are out!")
        self._show_earnings()
        quit()

    def _stop(self) -> None:
        """Handles exit request calculation rules when player manually steps away."""
        if self.i >= 5:
            messagebox.showinfo(title="STOP",
                                message=f"Money earned: {MONEY[self.i - 1] // 3} $")
        else:
            messagebox.showinfo(title="STOP",
                                message="Unfortunately you stopped before 5 rounds. "
                                        "Because of that you leave with empty pockets!")
        quit()

    def _show_earnings(self) -> None:
        """Determines financial fallback payout amounts based on safety tier milestones."""
        if self.i >= 5:
            messagebox.showinfo(title="MONEY EARNED IN SAFE ZONE",
                                message=f"Pockets full of money! Money earned: {MONEY[self.i - 1]} $")
        elif self.i != 0 and self.i < 5:
            messagebox.showinfo(title="MONEY EARNED",
                                message=f"Pockets full of money! Money earned: {MONEY[self.i - 1] // 2} $")

    def _open_help(self) -> None:
        """Instantiates helper windows to present remaining available lifelines."""
        HelpWindow(parent=self.window,
                   game=self.game,
                   round_window=self,
                   round_index=self.i,
                   correct_letter=self.correct_letter)



class HelpWindow:
    """Manages display choices for lifelines that have not been used yet."""

    def __init__(self, parent: Tk, game: "Game", round_window: RoundWindow,
                 round_index: int, correct_letter: str) -> None:
        self.parent         = parent
        self.game           = game
        self.round_window   = round_window
        self.round_index    = round_index
        self.correct_letter = correct_letter

        # Halt operation if the tracking list of available lifelines is exhausted
        if not self.game.helps_remaining:
            messagebox.showerror(title="Out of helps",
                                 message="You have no remaining helps! Think about it!")
            return

        self._build()

    def _build(self) -> None:
        """Generates contextual menu option interfaces to call specific utilities."""
        self.window = Toplevel(self.parent)
        self.window.title("HELP CHAPTER")
        self.window.geometry("400x400")
        self.window.config(background="light blue")
        self.window.resizable(False, False)

        Label(self.window,
              text="WELCOME TO HELP CHAPTER\nCHOOSE YOUR HELP!",
              bg="light blue", pady=10).pack()

        # Mapping key string tokens to their operational method targets
        y = 100
        lifeline_commands = {
            "50-50":        self._use_fifty,
            "audience help": self._use_audience,
            "phone":        self._use_phone,
        }
        
        # Dynamically append interactive control layouts only for unused lifelines
        for help_name in self.game.helps_remaining:
            Button(self.window, text=help_name, width=17, height=3,
                   bg="#db96eb",
                   command=lifeline_commands[help_name]).place(x=140, y=y)
            y += 70

        self.window.mainloop()

    # ── Lifeline executions ──────────────────────────────────────────────────

    def _use_fifty(self) -> None:
        """Consumes 50-50 lifeline and re-initializes the round with 2 options."""
        self.game.helps_remaining.remove("50-50")
        two_choices = FiftyFiftyLifeline.apply(CHOICES[self.round_index], self.correct_letter)
        self.window.destroy()
        self.round_window.window.destroy() # Close regular full round canvas
        # Re-draw the round interface with the restricted choices array layout
        RoundWindow(self.game, self.round_index, forced_choices=two_choices)

    def _use_audience(self) -> None:
        """Consumes audience vote option and spawns polling analytics info dialogues."""
        self.game.helps_remaining.remove("audience help")
        self.window.destroy()
        AudienceLifeline.apply(self.parent, self.correct_letter)

    def _use_phone(self) -> None:
        """Consumes phone-a-friend action lifeline and creates countdown modules."""
        self.game.helps_remaining.remove("phone")
        self.window.destroy()
        PhoneLifeline().apply(self.parent)




class Game:
    """Central engine tracker handling runtime tracking states and game levels."""

    def __init__(self) -> None:
        # State counters and initialization trackers
        self.round_index    : int       = 0
        self.helps_remaining: list[str] = ["50-50", "audience help", "phone"]

    def run(self) -> None:
        """Launches the initial gaming tier context execution loop."""
        RoundWindow(self, self.round_index)

    def next_round(self) -> None:
        """Increments index variables to process progression to following round stages."""
        self.round_index += 1
        RoundWindow(self, self.round_index)

def main() -> None:
    """Safeguards execution flow with safety handlers preventing crash states."""
    try:
        WelcomeScreen()
    except IndexError:
        messagebox.showerror(title="ERROR", message="Oops something went wrong. ERROR 1")
    except Exception:
        messagebox.showerror(title="ERROR", message="Oops something went wrong. ERROR 2")


if __name__ == "__main__":
    # Script entry point execution trigger
    main()
