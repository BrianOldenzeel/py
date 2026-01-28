class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __repr__(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year:04d}"
    
    def is_leap_year(self):
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        date_copy = Date(self.day, self.month, self.year)
        return date_copy

    def equals(self, d2):
        if self.day == d2.day and self.month == d2.month and self.year == d2.year:
            return True
        else:
            return False
    
    def is_before(self, d2):
        if self.day > d2.day or self.month > d2.month or self.year > d2.year:
            return True
        else:
            return False

    def is_after(self, d2):
        if self.day < d2.day or self.month < d2.month or self.year < d2.year:
            return True
        else:
            return False

    def tomorrow(self):
    # Months with 30 days
        if self.month in (4, 6, 9, 11):
            if self.day < 30:
                self.day += 1
            else:
                self.day = 1
                self.month += 1

        # February
        elif self.month == 2:
            if self.is_leap_year():
                if self.day < 29:
                    self.day += 1
                else:
                    self.day = 1
                    self.month += 1
            else:
                if self.day < 28:
                    self.day += 1
                else:
                    self.day = 1
                    self.month += 1

        # Months with 31 days
        else:
            if self.day < 31:
                self.day += 1
            else:
                self.day = 1
                if self.month == 12:
                    self.month = 1
                    self.year += 1
                else:
                    self.month += 1

    def yesterday(self):
        # If not the first day of the month, just go back one day
        if self.day > 1:
            self.day -= 1
            return

        # Now we know self.day == 1 → move to previous month
        if self.month == 1:
            self.month = 12
            self.year -= 1
        else:
            self.month -= 1

        # Set day to the last day of the new month
        if self.month in (4, 6, 9, 11):
            self.day = 30

        elif self.month == 2:
            self.day = 29 if self.is_leap_year() else 28

        else:
            self.day = 31

    def add_n_days(self, n):
        for days in range(n):
                # Months with 30 days
            if self.month in (4, 6, 9, 11):
                if self.day < 30:
                    self.day += 1
                else:
                    self.day = 1
                    self.month += 1

            # February
            elif self.month == 2:
                if self.is_leap_year():
                    if self.day < 29:
                        self.day += 1
                    else:
                        self.day = 1
                        self.month += 1
                else:
                    if self.day < 28:
                        self.day += 1
                    else:
                        self.day = 1
                        self.month += 1

            # Months with 31 days
            else:
                if self.day < 31:
                    self.day += 1
                else:
                    self.day = 1
                    if self.month == 12:
                        self.month = 1
                        self.year += 1
                    else:
                        self.month += 1

d = Date(7, 4, 2003)
d2 = d
d3 = d.copy()
d4 = Date(7, 4, 2004)
print(id(d))
print(id(d2))
print(id(d3))
print(d.equals(d3))
print(d.is_before(d4))
print(d.is_after(d4))
print(d)
print(d.is_leap_year())
newday = Date(31, 3, 2000)
newday.tomorrow()
print(newday)
newday2 = Date(1, 8, 2006)
newday2.yesterday()
print(newday2)
newday3 = Date(4, 8, 2007)
newday3.add_n_days(5)
print(newday3)