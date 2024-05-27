def first_non_repeating_letter(s):
    for i in range(len(s)):
        if s.lower().count(s[i].lower()) == 1:
            return s[i]
    return ''

print(first_non_repeating_letter('stress'))