#write a program to prompt the user for hours and rate per hour to compute gross pay.
hours = input('Enter hours: ')
rate = input('Enter rate: ')

payrate = float(hours) * float(rate)

print('your pay rate is: ',payrate)