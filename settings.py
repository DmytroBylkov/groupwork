class NoMoreDaysError(Exception):
    def __init__(self, obj, days):
        self.obj = obj
        self.days = days

    def __str__(self):
            msg = f"{self.obj.fullname} has not enough vacation days.\
                \nRemaining days: {self.obj.vacation_days}. Requested: {self.days}"
            return msg
