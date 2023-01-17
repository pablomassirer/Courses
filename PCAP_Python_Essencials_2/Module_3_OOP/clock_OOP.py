class Clock:
    def __init__(self, hour, minutes, seconds):
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds
        self.time_in_seconds = (self.hour * 3600) + (self.minutes * 60) + seconds

    def convert(self):
        self.converted_hour = self.time_in_seconds // 3600
        self.converted_minutes = int(self.time_in_seconds / 60 / 24)
        self.converted_minutes = "00" if self.converted_minutes == 60 else self.converted_minutes
        self.converted_seconds = int(self.time_in_seconds - (self.hour * 3600 + self.minutes * 60))
        self.converted_seconds = "00" if self.converted_seconds == 60 else self.converted_seconds

    def increase(self):
        self.time_in_seconds += 1
        self.convert()

    def decrease(self):
        self.time_in_seconds -= 1
        self.convert()

    def __str__(self):
        return f"{self.converted_hour}:{self.converted_minutes}:{self.converted_seconds}"

clock = Clock(23, 59, 59)
clock.increase()
print(clock)
clock.decrease()
print(clock)
