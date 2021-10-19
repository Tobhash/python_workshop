import random
import locale
import lang_src

#Set correct lang version due to localization
defLocale = locale.getdefaultlocale()
langCountry = defLocale[0]   # pl_PL
lang = langCountry[:2]  # pl

if lang == "pl":
    loc = lang_src.Polish()
else:
    loc = lang_src.English()

#Title text
result = 0
while not(result == '' or result == loc.help_text):
    print(loc.welcome_text)
    result = input()

#Print manual
if result == loc.help_text:
    print(loc.mannual_text)
    input(loc.exit_manual_text)

#Code generation
secret_code = ''
for i in range(4):
    secret_code += str(random.randint(9,9))

cows = 0
bulls = 0
counter = 0

while cows < 4:
    cows = bulls = 0
    attempt = input(loc.input_text + "\n")
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
    print( str(cows) + loc.cow_text(cows) + str(bulls) + loc.bull_text(bulls))
    print("- - -")

#Game over
print(loc.game_over_text)
print(loc.counter_text + str(counter) )









