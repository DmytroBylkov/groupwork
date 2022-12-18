"""
A very advanced employee management system
"""

import logging
from dataclasses import dataclass
import settings as Errors

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


@dataclass
class Employee:
    """Basic employee representation"""

    first_name: str
    last_name: str
    role: str
    vacation_days: int = 25

    @property
    def fullname(self):
        return self.first_name, self.last_name

    def __str__(self) -> str:
        """Return a string version of an instance"""

        return self.fullname

    def take_holiday(self, payout: bool = False) -> None:
        """Take a single holiday or a payout vacation"""

        try:
            days = 5 if payout else 1
            if self.vacation_days < days:
                raise Errors.NoMoreDaysError(self, days)

            self.vacation_days -= days
            msg = f"{self.fullname} taking a holiday. Remaining vacation days: {self.vacation_days}"
            logger.info(msg)
        except Errors.NoMoreDaysError as DayError:
            logger.warning(DayError)

@dataclass
class HourlyEmployee(Employee):
    """Represents employees who are paid on worked hours base"""

    amount: int = 0
    hourly_rate: int = 50

    def log_work(self, hours: int) -> None:
        """Log working hours"""

        self.amount += hours



@dataclass
class SalariedEmployee(Employee):
    """Represents employees who are paid on a monthly salary base"""

    salary: int = 5000



class Company:
    """A company representation"""

    title: str
    employees: list[Employee] = []

    def get_ceos(self) -> list[Employee]:
        """Return employees list with role of CEO"""

        result = []
        for employee in self.employees:
            if employee.role == "CEO":
                result.append(employee)
        return result

    def get_managers(self) -> list[Employee]:
        """Return employees list with role of manager"""

        result = []
        for employee in self.employees:
            if employee.role == "manager":
                result.append(employee)
        return result

    def get_developers(self) -> list[Employee]:
        """Return employees list with role of developer"""

        result = []
        for employee in self.employees:
            if employee.role == "dev":
                result.append(employee)
        return result

    @staticmethod
    def pay(employee: Employee) -> None:
        """Pay to employee"""

        if isinstance(employee, SalariedEmployee):
            msg = (
                "Paying monthly salary of %.2f to %s"
            ) % (employee.salary, employee)
            logger.info(f"Paying monthly salary to {employee}")

        if isinstance(employee, HourlyEmployee):
            msg = (
                "Paying %s hourly rate of %.2f for %d hours"
            ) % (employee, employee.hourly_rate, employee.amount)
            logger.info(msg)

    def pay_all(self) -> None:
        """Pay all the employees in this company"""

        for employee in self.employees:
                self.pay(employee)