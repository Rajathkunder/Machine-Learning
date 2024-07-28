
def check_letter(letter):
    vowels = 'aeiou'
    if letter in vowels:
        return "The entered letter is a vowel."
    elif letter == 'y':
        return "Sometimes y is a vowel, and sometimes y is a consonant."
    else:
        return "The entered letter is a consonant."


letter = input("Enter a letter of the alphabet: ").lower()


if len(letter) != 1 or not letter.isalpha():
    print("Please enter a single letter of the alphabet.")
else:
    
    result = check_letter(letter)
    print(result)
