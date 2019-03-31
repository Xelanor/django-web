from selenium.webdriver.chrome.options import Options
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import os
import pickle
#from proxy_extension import create_proxy_extension
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from time import sleep

#aprint(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Insta():
    
    def __init__(self):
        #self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        #chromedriver_location = os.path.join(#self.BASE_DIR,
        #                                        'app/InstaPy/assets',
        #                                        'chromedriver')
        #print(chromedriver_location)
        chrome_options = Options()
        #chrome_options.add_argument("--mute-audio")
        #chrome_options.add_argument('--dns-prefetch-disable')
        #chrome_options.add_argument('--lang=en-US')
        #chrome_options.add_argument('--disable-setuid-sandbox')
        chrome_options.add_argument('--headless') # Headless
        chrome_options.add_argument('--no-sandbox') # Headless
        #capabilities = DesiredCapabilities.CHROME
        #proxy = 'xelanor:RKe5tuXt@185.225.36.88:11475'
        #chrome_options.add_extension(create_proxy_extension(proxy))
        #os.chmod('/app/InstaPy/assets/chromedriver', 0o755)
        #self.driver = webdriver.Chrome("C:\\Users\\beroz\\Google Drive (berkezelsel@gmail.com)\\Python_works\\first_app\\python-docs-samples\\appengine\\standard_python37\\hello_world\\python-getting-started\\InstaPy\\assets\\chromedriver.exe", chrome_options=chrome_options)
        self.driver = webdriver.Chrome("/usr/local/bin/chromedriver", chrome_options=chrome_options)
        
    def login_user(self, username, password):
        driver = self.driver
        #log_location = os.path.join(self.BASE_DIR, 'InstaPy/logs')
        #logfolder = '{0}{1}{2}{1}'.format(log_location, os.path.sep, username)
        ig_homepage = "https://www.instagram.com"
        driver.get(ig_homepage)
        print("OPENEDEDEDEADEDEDED")
        sleep(2)
        print("OPENEDEDEDEADEDEDED")
        #try:
        #    for cookie in pickle.load(open('{0}{1}_cookie.pkl'
        #                                .format(logfolder, username), 'rb')):
        #        driver.add_cookie(cookie)
        #        cookie_loaded = True
        #except (WebDriverException, OSError, IOError):
        #    print("Cookie file not found, creating cookie...")

        # include time.sleep(1) to prevent getting stuck on google.com
        sleep(1)

        language_element_ENG = driver.find_element_by_xpath(
            "//select[@class='hztqj']/option[text()='English']")
        language_element_ENG.click()

        driver.get(ig_homepage)

        # if user is still not logged in, then there is an issue with the cookie
        # so go create a new cookie..

        # Check if the first div is 'Create an Account' or 'Log In'
        login_elem = driver.find_element_by_xpath(
            "//article//a[text()='Log in']")

        if login_elem is not None:
            try:
                (ActionChains(driver)
                .move_to_element(login_elem)
                .click()
                .perform())
            except MoveTargetOutOfBoundsException:
                login_elem.click()
        sleep(2)

        # wait until the 'username' input element is located and visible
        input_username_XP = "//input[@name='username']"

        input_username = driver.find_element_by_xpath(input_username_XP)

        (ActionChains(driver)
        .move_to_element(input_username)
        .click()
        .send_keys("username")
        .perform())

        sleep(1)

        #  password
        input_password = driver.find_elements_by_xpath(
            "//input[@name='password']")

        (ActionChains(driver)
        .move_to_element(input_password[0])
        .click()
        .send_keys("password")
        .perform())

        sleep(2)

        login_button = driver.find_element_by_xpath(
            "//button[text()='Log in']")

        (ActionChains(driver)
        .move_to_element(login_button)
        .click()
        .perform())

        sleep(2)

        return True
    def login_users(self, username, password):
        drivers = self.driver
        #log_location = os.path.join(self.BASE_DIR, 'InstaPy/logs')
        #logfolder = '{0}{1}{2}{1}'.format(log_location, os.path.sep, username)
        ig_homepage = "https://www.instagram.com"
        drivers.get(ig_homepage)
        print("OPENEDEDEDEADEDEDED")
        sleep(2)
        print("OPENEDEDEDEADEDEDED")
        #try:
        #    for cookie in pickle.load(open('{0}{1}_cookie.pkl'
        #                                .format(logfolder, username), 'rb')):
        #        driver.add_cookie(cookie)
        #        cookie_loaded = True
        #except (WebDriverException, OSError, IOError):
        #    print("Cookie file not found, creating cookie...")

        # include time.sleep(1) to prevent getting stuck on google.com
        sleep(1)

        language_element_ENG = driver.find_element_by_xpath(
            "//select[@class='hztqj']/option[text()='English']")
        language_element_ENG.click()

        driver.get(ig_homepage)

        # if user is still not logged in, then there is an issue with the cookie
        # so go create a new cookie..

        # Check if the first div is 'Create an Account' or 'Log In'
        login_elem = driver.find_element_by_xpath(
            "//article//a[text()='Log in']")

        if login_elem is not None:
            try:
                (ActionChains(driver)
                .move_to_element(login_elem)
                .click()
                .perform())
            except MoveTargetOutOfBoundsException:
                login_elem.click()

        # Enter username and password and logs the user in
        # Sometimes the element name isn't 'Username' and 'Password'
        # (valid for placeholder too)

        sleep(2)

        # wait until the 'username' input element is located and visible
        input_username_XP = "//input[@name='username']"

        input_username = driver.find_element_by_xpath(input_username_XP)

        (ActionChains(driver)
        .move_to_element(input_username)
        .click()
        .send_keys(username)
        .perform())

        sleep(1)

        #  password
        input_password = driver.find_elements_by_xpath(
            "//input[@name='password']")

        if not isinstance(password, str):
            password = str(password)

        (ActionChains(driver)
        .move_to_element(input_password[0])
        .click()
        .send_keys(password)
        .perform())

        sleep(2)

        login_button = driver.find_element_by_xpath(
            "//button[text()='Log in']")

        (ActionChains(driver)
        .move_to_element(login_button)
        .click()
        .perform())

        sleep(2)

        try:
            close_button = driver.find_element_by_xpath("[text()='Close']")

            (ActionChains(driver)
            .move_to_element(close_button)
            .click()
            .perform())

            sleep(1)

        except NoSuchElementException:
            pass

        try:
            # click on "This was me" button if challenge page was called
            this_was_me_button = driver.find_element_by_xpath(
                "//button[@name='choice'][text()='This Was Me']")

            (ActionChains(driver)
            .move_to_element(this_was_me_button)
            .click()
            .perform())

            sleep(1)

        except NoSuchElementException:
            # no verification needed
            pass

        try:
            choice = driver.find_element_by_xpath(
                "//label[@for='choice_1']").text

        except NoSuchElementException:
            try:
                choice = driver.find_element_by_xpath(
                    "//label[@class='_q0nt5']").text

            except Exception:
                try:
                    choice = driver.find_element_by_xpath(
                        "//label[@class='_q0nt5 _a7z3k']").text

                except Exception:
                    print("Unable to locate email or phone button, maybe "
                        "bypass_suspicious_login=True isn't needed anymore.")
                    return False

        send_security_code_button = driver.find_element_by_xpath(
            "//button[text()='Send Security Code']")
        sleep(1)

        (ActionChains(driver)
        .move_to_element(send_security_code_button)
        .click()
        .perform())

        print('Instagram detected an unusual login attempt')
        print('A security code was sent to your mail')


    def verification(self, username, verif):
        driver = self.driver
        username = username
        log_location = os.path.join(self.BASE_DIR, 'InstaPy/logs')
        logfolder = '{0}{1}{2}{1}'.format(log_location, os.path.sep, username)

        sleep(2)

        security_code = verif

        security_code_field = driver.find_element_by_xpath((
            "//input[@id='security_code']"))

        (ActionChains(driver)
        .move_to_element(security_code_field)
        .click()
        .send_keys(security_code)
        .perform())

        sleep(40)

        submit_security_code_button = driver.find_element_by_xpath(
            "//button[text()='Submit']")

        (ActionChains(driver)
        .move_to_element(submit_security_code_button)
        .click()
        .perform())

        sleep(1)

        try:
            sleep(2)
            # locate wrong security code message
            wrong_login = driver.find_element_by_xpath((
                "//p[text()='Please check the code we sent you and try "
                "again.']"))

            if wrong_login is not None:
                print(('Wrong security code! Please check the code Instagram'
                    'sent you and try again.'))

        except NoSuchElementException:
            # correct security code
            pass

        sleep(3)

        # Check if user is logged-in (If there's two 'nav' elements)
        nav = driver.find_elements_by_xpath('//nav')
        if len(nav) == 2:
            # create cookie for username
            pickle.dump(driver.get_cookies(), open(
                '{0}{1}_cookie.pkl'.format(logfolder, username), 'wb'))
            return True
        else:
            return False