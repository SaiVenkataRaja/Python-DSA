birthday = datetime(2025, 8, 21)
if birthday < now:
    birthday = birthday.replace(year=now.year + 1)
days_left = (birthday - now).days
print(days_left)
