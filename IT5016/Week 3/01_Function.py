def get_minutes(hours, minutes):
    total = hours * 60 + minutes
    return total

hours = float(input("Enter Hours: "))
minutes = float(input("Enter Minutes: "))

total_minutes = get_minutes(3,44)
print(total_minutes)

print(get_minutes(6,36))

print(get_minutes(hours,minutes))
