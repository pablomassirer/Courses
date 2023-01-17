class WeekDayError(Exception):
    pass
	

class Weeker:

    def __init__(self, day):
        self.day = day
        self.days_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        if self.day in self.days_list:
            self.index_day = self.days_list.index(day)
            self.result = self.day
        else:
            raise WeekDayError
        
    def __str__(self):
        return f'{self.result}'
        
    def add_days(self, n):
        n %= 7
        self.result = self.days_list[ self.index_day : n + 1 ][1]
        
    def subtract_days(self, n):
        n %= 7 
        self.result = self.days_list[ - n + self.index_day + 1 ]

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
    
