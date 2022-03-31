import re

def timeConversion(s):
    hours, minutes, seconds = s.split(":")
    meridiem = seconds[2:]
    seconds = re.sub('[PM]', '', seconds)
    seconds = re.sub('[AM]', '', seconds)

    if meridiem == 'AM' and hours == '12':
        hours =  '00'
    elif meridiem == 'PM' and hours != '12':
        hours = int(hours) + 12
        hours = str(hours)
    
    return hours + ':' +  minutes + ':' + seconds

print(timeConversion("10:00:00PM"))