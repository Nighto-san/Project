def title_case(string, exceptions=''):
    if exceptions is None:
        exceptions = ''

    words = string.split()

    title_case_words = [word.capitalize() if word.lower() not in exceptions.lower().split() else word.lower() for word in words]
    if title_case_words:
        title_case_words[0] = title_case_words[0].capitalize()
    result = ' '.join(title_case_words)

    return result

print(title_case('THE WIND IN THE WILLOWS', 'The In'))
print('The Wind in the Willows')

#print(title_case('a clash of KINGS', 'a an the of'), 'A Clash of Kings')