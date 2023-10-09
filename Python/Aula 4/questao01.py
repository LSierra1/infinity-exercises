seconds = input("Enter the time that the factory has been active (in seconds): ")

if seconds.isalpha():
    print("NaN")
    exit()

def timerConversion(seconds):
    # 86400 seg -> 1 day
    # 3600 seg -> 1h
    # 60 seg -> 1 min
    # 1 seg -> 1 seg
    days = seconds // 86400
    seconds -= days * 86400
    hours = seconds // 3600
    seconds -= hours * 3600
    minutes = seconds // 60
    seconds -= minutes * 60
    # return days, hours, minutes, seconds (possivelmente errado)
    return f"Days: {days}\n" f"Hours: {hours}\n" f"Minutes: {minutes}\n" f"Seconds: {seconds}."

print(timerConversion(seconds))