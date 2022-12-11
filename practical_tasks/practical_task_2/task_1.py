days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
weekdays = [days_of_week[i] for i in range(len(days_of_week)) if i <= 4]
weekends = {days_of_week[i] for i in range(len(days_of_week)) if i > 4}

print(weekdays)
print(weekends)