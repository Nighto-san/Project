
def pig_it(text):
    r = []
    for word in text.split():
        if word.isalpha():
            r.append(word[1:] + word[:1] + "ay")
        else:
            r.append(word)
    return " ".join(r)

print(pig_it('Pig latin is cool'),"                      ",'igPay atinlay siay oolcay')