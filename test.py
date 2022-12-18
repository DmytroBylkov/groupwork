import unittest
import system as sys


class EmployeeClassesTestCases(unittest.TestCase):
    def setUp(self):
        self.andrii = sys.HourlyEmployee('Andrii', 'Horbanov', 'dev', amount=37)
        self.igor = sys.SalariedEmployee('Igor', 'Ilov', 'CEO')

    def test_employee_obj_creation(self):
        """Obj of HourlyEmployee class"""

        self.assertEqual(self.andrii.first_name, 'Andrii')
        self.assertEqual(self.andrii.last_name, 'Horbanov')
        self.assertEqual(self.andrii.role, 'dev')
        self.assertEqual(self.andrii.amount, 37)
        """Obj of SalariedEmployee class"""

        self.assertEqual(self.igor.first_name, 'Igor')
        self.assertEqual(self.igor.last_name, 'Ilov')
        self.assertEqual(self.igor.role, 'CEO')
        self.assertEqual(self.igor.salary, 5000)

    def test_fullname(self):
        self.assertEqual(self.andrii.fullname, 'Andrii Horbanov')

    def test_repr(self):
        self.assertEqual(self.andrii.__repr__(), 'Name: Andrii; Surname: Horbanov; Appointment: dev')

    def test_take_holiday(self):
        """Just method test"""

        with self.assertLogs(level='INFO') as cm:
            self.andrii.take_holiday()
        self.assertEqual(cm.output, ['INFO:root:Andrii Horbanov taking a holiday. Remaining vacation days: 24'])
        self.andrii.vacation_days = 5
