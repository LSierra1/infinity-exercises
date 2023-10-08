seconds = int(input("Enter the time that the factory has been active (in seconds): "))

def timerConversion(seconds):
    minutes = seconds // 60
    seconds -= minutes * 60
    hours = seconds // 3600
    seconds -= hours * 3600
    days = seconds // 86400
    seconds -= days * 86400
    # return days, hours, minutes, seconds (possivelmente errado)
    return f"{seconds}, {minutes}, {hours}, {days}"

print(timerConversion(seconds))