#convert time entered in hh, min and sec into seconds

#take input
hh = int(input('Enter the hours:'))
min = int(input('Enter the minutes:'))
sec = int(input('Enter the seconds:'))

#perform operations 
TotalSeconds = (hh * 3600) + (min * 60) + sec

#disply result
print(f'The time converted in seconds is {TotalSeconds}.')
