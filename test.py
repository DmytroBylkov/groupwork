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
        """Test with an argument"""

        with self.assertLogs(level='INFO') as cm:
            self.andrii.take_holiday(True)
        self.assertEqual(cm.output, ['INFO:root:Andrii Horbanov taking a holiday. Remaining vacation days: 0'])
        """Warning through raise error exception"""
        
        with self.assertLogs(level='INFO') as cm:
            self.andrii.take_holiday()
        self.assertEqual(cm.output, ["WARNING:root:Andrii Horbanov has not enough vacation days.\
                \nRemaining days: 0. Requested: 1"])

    def test_log_work(self):
        self.andrii.log_work(13)
        self.assertEqual(self.andrii.amount, 50)

    def test_earned_for_now(self):
        self.assertEqual(self.andrii.earned_for_now, 1850)

class CompanyAndEmployeeClassesTestCases(unittest.TestCase):
    def setUp(self):
        self.andrey = sys.SalariedEmployee('Andrey', 'Mlinin', 'manager')
        self.oleg = sys.HourlyEmployee('Oleg', 'Osov', 'CEO', amount=50)
        self.big_c = sys.Company('tech', [])
        self.big_c.add_employee(self.andrey)
        self.big_c.add_employee(self.oleg)
    
    def test_company_attributes(self):
        self.assertListEqual(self.big_c.employees, [self.andrey, self.oleg])
        self.assertEqual(self.big_c.title, 'tech')

    def test_get_role(self):
        self.assertEqual(self.big_c.get_role_list('CEO'), [self.oleg])
        self.assertEqual(self.big_c.get_role_list('manager'), [self.andrey])
    
    def test_remove_employee(self):
        self.big_c.remove_employee('oleg', 'osov')
        self.assertEqual(self.big_c.employees, [self.andrey])
    
    def test_pay_and_pay_all(self):
        with self.assertLogs(level='INFO') as cm:
            self.big_c.pay_all()
        self.assertEqual(cm.output, ['INFO:root:Paying monthly salary of 5000 to Andrey Mlinin',
        'INFO:root:Paying Oleg Osov hourly rate summary equal to 2500 for 50 hours'])


if __name__ == '__main__':
    unittest.main()