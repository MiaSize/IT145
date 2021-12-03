
prompt = ('If you could go anywhere for vaction, where would you go?')
prompt += ('\n(enter quit if you want to end the poll)' '\nEnter here:')
message = ''
poll = []
active = True
while active:
    message = input(prompt)
    poll.append(message)
    if message == 'quit':
        active = False
        print('Ending the program...')
    else:
        print(poll)

