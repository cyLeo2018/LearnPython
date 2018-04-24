import datetime

def Yesterday():
    Today = datetime.date.today()
    Oneday = datetime.timedelta(days=1)
    Yesterday = Today - Oneday
    return Yesterday

print(Yesterday())
