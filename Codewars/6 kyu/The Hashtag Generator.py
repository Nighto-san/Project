def generate_hashtag(s):
    if not s or s.strip() == "":
        return False
    words = s.strip().split()
    hashtag = "#" + "".join(word.capitalize() for word in words)
    return hashtag if len(hashtag) <= 140 else False



