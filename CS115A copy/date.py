'''
Created on Nov 27, 2018
@author: Brandon Cao
bcao4
I pledge my honor that I have abided by the Stevens Honor System.
CS115 - Hw 11 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        """This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value."""
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        '''Returns a new object with the same month, day, year
        as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and self.day == d2.day

    def tomorrow(self):
        """changes the calling object so that it represents one calendar day after the date it originally represented"""
        DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.day += 1
        if self.isLeapYear():
            DAYS_IN_MONTH[2] = 29
        if DAYS_IN_MONTH[self.month] < self.day:
            self.day = 1
            if self.month == 12:
                self.month = 1
                self.year += 1
            else:
                self.month += 1
        return self

    def yesterday(self):
        """changes the calling object so that it represents one calendar day before the date it originally
        represented """
        DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.day - 1 > 0:
            self.day -= 1
        else:
            if self.isLeapYear():
                DAYS_IN_MONTH[2] = 29
            if self.month == 1:
                self.month = 12
                self.day = 31
                self.year -= 1
            else:
                self.day = DAYS_IN_MONTH[self.month - 1]
                self.month -= 1
        return self

    def addNDays(self, N):
        """changes the calling object so that it represents N calendar days after the date it originally represented"""
        print(self)
        i = 0
        for i in range(N):
            self.tomorrow()
            print(self)
        return

    def subNDays(self, N):
        """changes the calling object so that it represents N calendar days before the date it originally represented"""
        print(self)
        i = 0
        for i in range(N):
            self.yesterday()
            print(self)
        return

    def isBefore(self, d2):
        """This method should return True if the calling object is a calendar date before the input
        named d2 (which will always be an object of type Date). If self and d2 represent the same day,
        this method should return False. Similarly, if self is after d2, this should returnFalse"""
        if d2.year == self.year:
            if d2.month == self.month:
                if d2.day > self.day:
                    return True
                else:
                    return False
            elif d2.month > self.month:
                return True
            else:
                return False
        elif d2.year > self.year:
            return True
        else:
            return False

    def isAfter(self, d2):
        """This method should return True if the calling object is a calendar date after the input
        named d2 (which will always be an object of type Date). If self and d2 represent the same day,
        this method should return False. Similarly, if self is before d2, this should returnFalse."""
        if d2.year == self.year:
            if d2.month == self.month:
                if d2.day > self.day or d2.day == self.day:
                    return False
                else:
                    return True
            elif d2.month > self.month:
                return False
            else:
                return True
        elif d2.year > self.year:
            return False
        else:
            return True

    def diff(self, d2):
        """returns an integer representing the number of days between self and d2."""
        day1 = self.copy()
        day2 = d2.copy()
        i = 0
        if self.equals(d2):
            return 0
        while not day1.equals(day2):
            if day1.isBefore(day2):
                day1.tomorrow()
                i -= 1
            else:
                day2.isAfter(day1)
                day2.tomorrow()
                i += 1
        return i

    def dow(self):
        """returns a string that indicates the day of the week of the object that calls it"""
        dates = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
        day= self.diff(Date(11, 9, 2011))
        return dates[day % 7]


