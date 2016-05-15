def get_bottle_phrase(n):
    if (n==1):
        return '{0} bottle'.format(n)
    elif (n==0):
        return 'no more bottles'
    else:
        return '{0} bottles'.format(n)

def display_song(n, is_first_call, last_line):
    if(is_first_call):
       last_line = 'No more bottles of beer on the wall, no more bottles of beer. \nGo to the store and buy some more, {0} bottles of beer on the wall.\n\n'.format(n)
    
    if(n==0):
        print(last_line)
    else:
        print('{0} of beer on the wall, {0} of beer.\nTake one down and pass it around, {1} of beer on the wall.\n'.format(get_bottle_phrase(n), get_bottle_phrase(n-1)))
        display_song(n-1, False, last_line)
    
display_song(99, True, '')