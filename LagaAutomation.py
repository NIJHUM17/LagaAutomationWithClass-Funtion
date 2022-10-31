import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
class LagaAutomation:

    def setup(self):
        s = Service("D:/Python/chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)

    def Open_WebBrowser(self):
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.maximize_window()
        print(self.driver.title)
        time.sleep(3)


    def Reg(self):
        self.driver.find_element("xpath", "//a[@class='login']").click()

    def email(self, myemail):
        self.driver.find_element("id", "email_create").send_keys(myemail)
        time.sleep(2)
        self.driver.find_element("xpath", "//button[@id='SubmitCreate']").click()
        time.sleep(7)

    def name(self, firstname, lastname, password):
        self.driver.find_element("xpath", "//input[@id='id_gender2']").click()
        self.driver.find_element("id", "customer_firstname").send_keys(firstname)
        self.driver.find_element("id", "customer_lastname").send_keys(lastname)
        self.driver.find_element("id", "passwd").send_keys(password)

    def dob(self, day, month, year):
        self.driver.find_element("id", "days").send_keys(day)
        self.driver.find_element("id", "months").send_keys(month)
        self.driver.find_element("id", "years").send_keys(year)
        time.sleep(2)
        self.driver.find_element("xpath", "//input[@id='newsletter']").click()
        self.driver.find_element("xpath", "//input[@id='optin']").click()

    def personal_info(self, firstname, lastname, company, address, addressLine2, city, state, zip_code, others ,Home_phone, mobile):
        self.driver.find_element("id", "firstname").send_keys(firstname)
        self.driver.find_element("id", "lastname").send_keys(lastname)
        self.driver.find_element("id", "company").send_keys(company)
        self.driver.find_element("id", "address1").send_keys(address)
        self.driver.find_element("id", "address2").send_keys(addressLine2)
        self.driver.find_element("id", "city").send_keys(city)
        self.driver.find_element("id", "id_state").send_keys(state)
        self.driver.find_element("id", "postcode").send_keys(zip_code)
        self.driver.find_element("id", "other").send_keys(others)
        self.driver.find_element("id", "phone").send_keys(Home_phone)
        self.driver.find_element("id", "phone_mobile").send_keys(mobile)
        self.driver.find_element("id", "alias").send_keys(address)

        self.driver.find_element("xpath", "//button[@id='submitAccount']").click()

    '''
    def login(self,emailid):
        self.driver.find_element("id", "email").send_keys(emailid)
        time.sleep(2)
        self.driver.find_element("id", "passwd").send_keys("123Nipu")
        time.sleep(2)
        self.driver.find_element("xpath", "//button[@id='SubmitLogin']").click()'''

    def search(self, searching):
        self.driver.find_element("id", "search_query_top").send_keys(searching)
        time.sleep(2)
        self.driver.find_element("xpath", "//button[@name='submit_search']").click()
        time.sleep(10)

    # Add
    def add(self):
        self.driver.find_element("xpath", "//a[@class = 'product-name']").click()
        time.sleep(10)
        self.driver.find_element("xpath", "//button[@class ='exclusive']").click()
        time.sleep(10)

    # proceed to checkout
    def proceed_to_checkout(self):
        self.driver.find_element("xpath", "//a[@class = 'btn btn-default button button-medium']").click()
        time.sleep(10)

lagaWebsite = LagaAutomation()
lagaWebsite.setup()
lagaWebsite.Open_WebBrowser()
lagaWebsite.Reg()
lagaWebsite.email("tahsinanijum5199@gmail.com")
lagaWebsite.name("Tahsin", "Nijhum", "123Nipu*")
lagaWebsite.dob(5,"January", 2000)
lagaWebsite.personal_info("Tahsin Adiba", "Nijhum", "Red.Dot", "Downey", "Dominant Dream", "South Gate", "California", "90280", "Information will be added later if needed" ,"+12022563030", "+8801629099448")
#lagaWebsite.login("tahsinanijum5199@gmail.com")
lagaWebsite.search("Dress")
lagaWebsite.add()
lagaWebsite.proceed_to_checkout()



