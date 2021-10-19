"""
    This file provides strings in two language versions.
    Only polish and english versions are avaliable right now.
"""

class English:
    welcome_text="""Welcome to the Cows and Bulls Game aka Code Cracker.
    -- To start just press ENTER.
    -- To learn how to play type \"help\" and press Enter."""
    help_text = "help"
    mannual_text = """
    ---- HOW TO PLAY ----
    Your goal is to guess the secret, 4-digit code.
    With every attempt You receive a feedback:
    \"cow\" represents correct digits in the correct place,
    while \"bulls\" means that the digit is correct but in the wrong place.
    Every time You make a quess type 4 digits and see how many \"cows\" and \"bulls\" You have.
    Keep track of previous attempts to break the code.

    For example the secret code is 2048:
    Enter a number:
    >>> 1234
    0 cows, 2 bulls
    >>> 2222
    1 cow, 3 bulls
    ...

    --------------------"""
    exit_manual_text = "To start the game press ENTER."
    input_text = "Enter a number:"
    game_over_text = "CORRECT.\nACCESS GRANTED."
    counter_text = "Attempts: "

    def cow_text(quantity):
        return (" cow, " if quantity == 1 else " cows, ")

    def bull_text(quantity):
        return (" bull." if quantity == 1 else " bulls.")

# - - - - -

class Polish:
    welcome_text="""Witaj w grze Krowy i Byki aka Łamacz Kodu.
    -- Aby rozpocząć wciśnij ENTER.
    -- Jeśli chcesz zobaczyć zasady wpisz \"help\" i zatwierdź klawiszem Enter."""
    help_text = "pomoc"
    mannual_text = """
    ---- ZASADY GRY ----
    Twoim zadaniem jest odgadnięcie 4-cyfrowego kodu.
    Przy każdej próbie otrzymasz informację o:
    \"krowach\", które reprezentują poprawne cyfry na poprawnych miejscach,
    natomiast \"byki\" oznaczają, że cyfra jest poprawna ale wstawiona na złym miejscu.
    Przy każdej próbie wprowadź 4 cyfry i przekonaj się ile \"krów\" i \"byków\" otrzymasz.
    Zapamiętuj rezultaty każdej próby aby szybciej złąmać kod.

    Przykłądowe wyniki dla kodu 2048:
    Podaj liczbę:
    >>> 1234
    0 krów, 2 byki
    >>> 2222
    1 krowa, 3 byki
    ...

    --------------------"""
    exit_manual_text = "By rozpocząć grę wciśnij ENTER."
    input_text = "Podaj liczbę:"
    game_over_text = "POPRAWNY KOD.\nUZYSKANIE DOSTĘPU."
    counter_text = "Próby: "

    def cow_text(self, quantity: int):
        if quantity == 0 :
            return " krów, "
        elif quantity == 1:
            return " krowa, "
        else:
            return " krowy, "

    def bull_text(self, quantity: int):
        if quantity == 0 :
            return " byków."
        elif quantity == 1:
            return " byk."
        else:
            return " byki."