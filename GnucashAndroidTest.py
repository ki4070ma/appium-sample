#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import unittest


from page.account.accounts import Accounts
from page.initialsetup.welcome import Welcome
from page.common.utils import get_window_size, GlobalVar

from appium import webdriver


# Returns abs path relative to this file and not cwd
def PATH(p: str) -> str: return os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


caps = {
    'platformName': "Android",
    'deviceName': "Android Emulator",
    'appPackage': "org.gnucash.android",
    'appActivity': ".ui.account.AccountsActivity",
    'app': PATH('./gnucash.apk'),
    'automationName': "uiautomator2",
}


class BaseTestCase(unittest.TestCase):
    def __init__(self, method_name: str) -> None:
        super(BaseTestCase, self).__init__(method_name)
        self.caps = caps

    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', self.caps)
        self.width, self.height = get_window_size(self.driver)

        # Start taking evidence
        self.make_log_dir(self._testMethodName)
        self.driver.start_recording_screen()

    def tearDown(self) -> None:
        # Stop taking evidence
        payload = self.driver.stop_recording_screen()
        with open(os.path.join(GlobalVar().log_dir, "cap.mp4"), "wb") as fd:
            import base64
            fd.write(base64.b64decode(payload))

        with open(os.path.join(GlobalVar().log_dir, "log.txt"), "w") as fd:
            logs = self.driver.get_log('logcat')
            for lines in logs:
                for line in lines['message'].split('¥n'):
                    fd.write(line + '\n')

        # end the session
        self.driver.quit()

    @staticmethod
    def make_log_dir(dir_name: str) -> None:
        GlobalVar().log_dir = os.path.join(GlobalVar().log_root_dir, dir_name)
        os.path.isdir(GlobalVar().log_dir) or os.makedirs(GlobalVar().log_dir)


class GnucashAndroidInitialSetupTest(BaseTestCase):

    def test_scenario1_complete_initial_setup(self) -> None:

        welcome = Welcome(self.driver)
        self.assertEqual(welcome.get_title(), "Welcome to GnuCash")

        default_currency = welcome.next()
        self.assertEqual(default_currency.get_title(), "Default Currency")
        default_currency.scroll_and_select_item("Other")

        select_currency = default_currency.next()
        self.assertEqual(select_currency.get_title(), "Select Currency")
        currency = "AOA - Kwanza"  # For debug
        # currency = "JPY - Yen"
        select_currency.scroll_and_select_item(currency)

        account_setup = select_currency.next()
        self.assertEqual(account_setup.get_title(), "Account Setup")
        account_setup.scroll_and_select_item("Create default accounts")

        feedback_options = account_setup.next()
        self.assertEqual(feedback_options.get_title(), "Feedback Options")
        feedback_options.scroll_and_select_item("Disable crash reports")

        review = feedback_options.next()
        self.assertEqual(review.get_title(), "Review")
        expects = [
            ("DEFAULT CURRENCY", u"Other…"),
            ("SELECT CURRENCY", "AOA"),  # For debug
            # ("SELECT CURRENCY", "JPY"),
            ("ACCOUNT SETUP", "Create default accounts"),
            ("FEEDBACK OPTIONS", "Disable crash reports"),
        ]
        for val, expect in zip(review.get_list(), expects):
            self.assertEqual(val, expect)

        whats_new = review.done()

        self.assertEqual(whats_new.get_title(), "What's New - v2.3.0")
        accounts_all = whats_new.dismiss()

        self.assertEqual(accounts_all.get_title(), "Accounts")

        expect = ["Assets", "Equity", "Expenses", "Income", "Liabilities"]
        self.assertEqual(accounts_all.get_labels(), expect)

        x, y = accounts_all.get_position_create_btn()
        self.assertTrue(
            x > self.width / 2,
            "Checking create btn location is right side(width)")
        self.assertTrue(
            y > self.height / 2,
            "Checking create btn location is bottom side(height)")

        x, y = accounts_all.get_position_three_line_menu()
        self.assertTrue(
            x < self.width / 2,
            "Checking menu location is left side(width)")
        self.assertTrue(
            y < self.height / 2,
            "Checking menu btn location is top side(height)")


class GnucashAndroidAccountTests(BaseTestCase):

    def setUp(self) -> None:
        self.caps['noReset'] = True  # Uses state with scenario1 finished
        super(GnucashAndroidAccountTests, self).setUp()

    def test_scenario2_register_new_transaction(self) -> None:
        self.skipTest('Skip for now')
        accounts_all = Accounts(self.driver)
        self.assertEqual(accounts_all.get_title(), "Accounts")

        sub_label = "Income"
        income = accounts_all.account(sub_label)
        self.assertEqual(income.get_title(), sub_label)

        expect = [
            "Bonus",
            "Gifts Received",
            "Interest Income",
            "Other Income",
            "Salary"]
        self.assertEqual(income.get_labels(), expect)

        subsub_label = "Salary"
        income_salary = income.account(subsub_label)
        self.assertEqual(income_salary.get_title(),
                         ':'.join([sub_label, subsub_label]))

        x, y = income_salary.get_position_new_transaction_btn()
        self.assertTrue(
            x > self.width / 2,
            "Checking new transaction btn location is right side(width)")
        self.assertTrue(
            y > self.height / 2,
            "Checking new transaction btn location is bottom side(height)")
        new_transaction_page = income_salary.new_transaction()
        self.assertEqual(new_transaction_page.get_title(), "New transaction")

        desc = "Part-time salary"
        amount = 50000
        new_transaction_page.input_description(desc)
        new_transaction_page.input_amount(amount)

        new_transaction_page.set_income_transaction_type()
        # TODO Now transaction type returns 'Income Income', not 'Income'
        self.assertTrue(
            "Income" in new_transaction_page.get_transaction_type())

        new_transaction_page.set_date("2018", "June", "4")

        income_salary = new_transaction_page.save()

        self.assertTrue(desc in income_salary.get_labels()[0])

        accounts_all = income_salary\
            .three_line_menu()\
            .gnucash_label()

        # self.assertEqual(accounts_all.get_balance('Assets'), 'JP¥50,000')
        self.assertEqual(
            accounts_all.get_balance('Assets'),
            "Kz50,000.00")  # For debug

        # self.assertEqual(accounts_all.get_balance('Income'), 'JP¥50,000')
        self.assertEqual(
            accounts_all.get_balance('Income'),
            "Kz50,000.00")  # For debug

    def test_scenario3_add_favorite(self) -> None:
        self.skipTest('Skip for now')
        accounts_all = Accounts(self.driver)
        self.assertEqual(accounts_all.get_title(), "Accounts")
        self.assertTrue(accounts_all.is_tab_focused("ALL"))

        accounts_favorites = accounts_all\
            .three_line_menu()\
            .favorites()

        self.assertTrue(accounts_favorites.is_tab_focused('FAVORITES'))
        self.assertEqual(len(accounts_favorites.get_labels()), 0)

        label = 'Assets'
        accounts_all = accounts_favorites\
            .three_line_menu()\
            .gnucash_label()
        self.assertTrue(accounts_all.is_tab_focused('ALL'))
        accounts_all.favorite_icon(label)

        accounts_favorites = accounts_all\
            .three_line_menu()\
            .favorites()
        self.assertTrue(accounts_favorites.is_tab_focused('FAVORITES'))
        self.assertEqual(len(accounts_favorites.get_labels()), 1)
        self.assertEqual(accounts_favorites.get_labels()[0], label)


if __name__ == '__main__':
    import datetime as dt
    GlobalVar().log_root_dir = os.path.join(PATH('.'), 'output', dt.datetime.now().strftime('%y%m%d-%H%M%S'))
    os.path.isdir(GlobalVar().log_root_dir) or os.makedirs(GlobalVar().log_root_dir)

    suite = unittest.TestLoader().loadTestsFromTestCase(GnucashAndroidInitialSetupTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # suite = unittest.TestLoader().loadTestsFromTestCase(GnucashAndroidAccountTests)
    # unittest.TextTestRunner(verbosity=2).run(suite)
