import random
"""
TO DO:
-text in the separate file for future language localization
-language detection
"""


welcome_text="""Welcome to the Cows and Bulls Game aka Code Cracker.
-- To start just press ENTER.
-- To see the manual type \"help\" and press Enter."""
mannual_text = """
---- HOW TO PLAY ----
Your goal is to guess the secret, 4-digit code.
With every attempt You receive a feedback:
\"cow\" represents correct digits in the correct place.
thus \"bulls\" means that the digit is correct but in the wrong place.
Every time You make a quess type 4-digit number and how many \"cows\" and \"bulls\" You have.
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
game_over_text = "CORRECT.\nACCESS GRANTED"
counter_text = "Attempts: "


result = 0
while not(result == '' or result == 'help'):
    print(welcome_text)
    result = input()

#Print manual
if result == 'help':
    print(mannual_text)
    input(exit_manual_text)

#Code generation
secret_code = ''
for i in range(4):
    secret_code += str(random.randint(0,0))

cows = 0
bulls = 0
counter = 0

while cows < 4:
    cows = bulls = 0
    attempt = input("Enter a number:\n")
    #Validation. Only 4-digit numbers can be accepted!
    if len(attempt) != 4:
        continue
    #Comparison
    for i in range(0,4):
        digit = attempt[i]
        if secret_code[i] == digit:
            cows += 1
        elif  digit in secret_code:
            bulls += 1

    counter += 1
    print( str(cows) + (" cow, " if cows == 1 else " cows, ") + str(bulls) + (" bull, " if bulls == 1 else " bulls, "))

#Game over
print(game_over_text)
print(counter_text + str(counter) )











