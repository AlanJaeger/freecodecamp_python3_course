#rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours using functions

def computepay(hours, rate):
    if float(hours)>40:
        extra_hour = float(hours) - 40
        new_rate = float(rate)*1.5
        value_of_payrate = extra_hour * float(new_rate)

        normal_hour = 40
        payrate = (float(normal_hour) * float(rate))

        new_payrate = value_of_payrate + payrate

        print('your pay rate is: ',new_payrate)
    else:
        payrate = (float(hours) * float(rate))
        print('your pay rate is: ',payrate)

hours = input('Enter hours: ')
rate = input('Enter rate: ')

computepay(hours,rate)





