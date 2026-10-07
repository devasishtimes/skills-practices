def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                tranlation =translation + "g"
            translation = translation + "G"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))