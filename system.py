"""
A very advanced employee management system
"""

import logging
from dataclasses import dataclass, field
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
    def fullname(self) -> str:
        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'

    def __repr__(self) -> str:
        """Return a string version of an instance"""
        
        return f'Name: {self.fullname.split()[0]}; Surname: {self.fullname.split()[1]}; Appointment: {self.role}'

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
    
    @property
    def earned_for_now(self) -> int:
        """Shows salary for current working period"""

        return self.amount * self.hourly_rate

    def __repr__(self):
        return super().__repr__()


@dataclass
class SalariedEmployee(Employee):
    """Represents employees who are paid on a monthly salary base"""

    salary: int = 5000

    def __repr__(self):
        return super().__repr__()


@dataclass
class Company:
    """A company representation"""

    title: str
    employees: list[Employee] = field(default_factory=list)

    def add_employee(self, employee: Employee):
        """Adds an employee to the employees list"""
        
        self.employees.append(employee)

    def get_role_list(self, role: str) -> list[Employee]:
        """Return employees list with chosen role (CEO, dev, manager)"""

        result = []
        for employee in self.employees:
            if employee.role == role:
                result.append(employee)
        return result

    def remove_employee(self, name: str, surname: str) -> None:
        """Removes an employee"""

        for employee in self.employees:
            if employee.first_name.lower() == name.lower() and \
                employee.last_name.lower() == surname.lower():
                self.employees.remove(employee)

    @staticmethod
    def pay(employee: Employee) -> None:
        """Pay to employee"""

        if isinstance(employee, SalariedEmployee):
            msg = f"Paying monthly salary of {employee.salary} to {employee.fullname}"
        else:
            msg = f"Paying {employee.fullname} hourly rate summary equal to {employee.earned_for_now} for {employee.amount} hours"
        logger.info(msg)

    def pay_all(self) -> None:
        """Pay all the employees in this company"""

        for employee in self.employees:
                self.pay(employee)
