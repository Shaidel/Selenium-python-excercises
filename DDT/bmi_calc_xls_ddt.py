import pandas as pd

import ddt
import csv, unittest
from ddt import ddt, data, unpack
from selenium import webdriver


#
read_file = pd.read_excel (r'testdata1.xlsx')
read_file.to_csv (r'testdata1.csv', index = None, header=True)



def get_data(file_name):
    # utworzenie pustej listy do przechowywania wierszy
    rows = []
    # otwarcie pliku CSV
    data_file = open("testdata1.csv")
    # utworzenie obiektu CSV Reader na podstawie pliku CSV
    reader = csv.reader(data_file)
    # pominięcie nagłówków
    next(reader, None)
    # dodanie wierszy z obiektu reader do listy
    for row in reader:
        rows.append(row)
    return rows


@ddt
class SearchCsvDDT(unittest.TestCase):
    def setUp(self):
        # utworzenie nowej sesji Firefox
        self.driver = webdriver.Firefox(executable_path=r'C:\AT_WiN\3\geckodriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # przejście do strony kalkulatora BMI
        self.driver.get("http://cookbook.seleniumacademy.com/bmicalculator.html")

    # pobranie danych z podanego pliku csv file poprzez wywołanie funkcji get_data
    @data(*get_data("testdata1.csv"))
    @unpack
    def test_bmi_calc(self, height, weight, bmi, category):
        driver = self.driver

        height_field = driver.find_element_by_name("heightCMS")
        height_field.clear()
        height_field.send_keys(height)

        weight_field = driver.find_element_by_name("weightKg")
        weight_field.clear()
        weight_field.send_keys(weight)

        calculate_button = driver.find_element_by_id("Calculate")
        calculate_button.click()

        bmi_label = driver.find_element_by_name("bmi")
        bmi_category_label = driver.find_element_by_name("bmi_category")

        self.assertEqual(bmi, bmi_label.get_attribute("value"))
        self.assertEqual(category, bmi_category_label.get_attribute("value"))

    def tearDown(self):
        # zamknij okno przeglądarki
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
