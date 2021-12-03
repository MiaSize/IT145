
def make_album(name,title):
    person = {'artist': name, 'album': title}
    return person
while True:
    print("\nPlease tell me the name of your favorite artist:")
    print("(enter 'q' at any time to quit)")
    name = input('Artist: ')
    if name == 'q':
        break
    title = input('Album: ')
    if title == 'q':
        break
    entered = make_album(name,title)
    print(entered)



