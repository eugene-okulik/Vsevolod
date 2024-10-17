text = ('"Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"')

text_add = text.split()

for word in text_add:
    if word.endswith(','):
        word = word.strip(',')
        word = (word + 'ing')
        word = (word + ',')
        print(word)
    elif word.endswith('.'):
        word = word.strip('.')
        word = (word + 'ing')
        word = (word + '.')
        print(word)
    elif word.endswith('"'):
        word = word.strip('"')
        word = (word + 'ing')
        word = (word + '"')
        print(word)
    else:
        print(word + 'ing')
