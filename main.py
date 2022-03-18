from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

from selenium.webdriver.support.select import Select
product_link = ['https://www.routeco.com/en-gb/shop/atex',
                'https://www.routeco.com/en-gb/shop/cable',
                'https://www.routeco.com/en-gb/shop/cable-accessories',
                'https://www.routeco.com/en-gb/shop/circuit-breakers-fuses',
                'https://www.routeco.com/en-gb/shop/computers',
                'https://www.routeco.com/en-gb/shop/control-gear-switchgear',
                'https://www.routeco.com/en-gb/shop/drives',
                'https://www.routeco.com/en-gb/shop/enclosures',
                'https://www.routeco.com/en-gb/shop/i-o-systems',
                'https://www.routeco.com/en-gb/shop/meters',
                'https://www.routeco.com/en-gb/shop/motion-control',
                'https://www.routeco.com/en-gb/shop/networks-communications',
                'https://www.routeco.com/en-gb/shop/operator-interface',
                'https://www.routeco.com/en-gb/shop/panel-accessories',
                'https://www.routeco.com/en-gb/shop/pneumatics',
                'https://www.routeco.com/en-gb/shop/power-conditioning',
                'https://www.routeco.com/en-gb/shop/process-instrumentation',
                'https://www.routeco.com/en-gb/shop/programmable-controllers',
                'https://www.routeco.com/en-gb/shop/safety',
                'https://www.routeco.com/en-gb/shop/sensors',
                'https://www.routeco.com/en-gb/shop/software',
                'https://www.routeco.com/en-gb/shop/terminals-connectors',
                'https://www.routeco.com/en-gb/shop/vision-systems',
                'https://www.routeco.com/en-gb/shop/wiring-accessories']
driver = webdriver.Firefox()
with open('products.csv', 'w',newline='') as file:
    def my_function(product_url):
        fieldnames = ['Brand','Part_code','Description','Qty']
        thewriter = csv.DictWriter(file,fieldnames = fieldnames)
        thewriter.writeheader()

        # driver = webdriver.Firefox()
        # driver.get('https://www.routeco.com/en-gb/shop/process-instrumentation')
        driver.get(product_url)

        time.sleep(4)
        try:
            driver.find_element(By.CSS_SELECTOR,'#p_lt_AcceptAllButton').click()
            driver.execute_script("window.scrollTo(0, 600)") 
        except:
            print('')


        # if driver.find_element(By.CSS_SELECTOR,'#p_lt_AcceptAllButton'):
        #     driver.find_element(By.CSS_SELECTOR,'#p_lt_AcceptAllButton').click()

        product_data_desc = []
        product_data_qty = []
        product_data_brand = []
        product_data_part = []
        disct = {}

        for k in range(600):
            product_data_desc = []
            product_data_qty = []
            product_data_brand = []
            product_data_part = []
            if 'aspNetDisabled' in driver.find_element(By.CSS_SELECTOR,'#p_lt_ctl03_pageplaceholder_p_lt_zoneMainContent_ProductListing_btnNext').get_attribute('class').split():
                print('element is disabled')
                break
            else:
                print("---------------------------------------")
            productName= driver.find_elements(By.CSS_SELECTOR,".ProductName")
            productRow= driver.find_elements(By.CSS_SELECTOR,".product-row")
            productStock= driver.find_elements(By.CSS_SELECTOR,".col-md-6 span")
            productDesc= driver.find_elements(By.CSS_SELECTOR,".ProductDescription")
            for desc in productDesc:
                product_data_desc.append(desc.text)

            for stock in productStock:
                v = stock.text.split(':')
                for singleArr in v:
                    res = [int(i) for i in singleArr.split() if i.isdigit()]
                    if len(res)>0:
                        product_data_qty.append(res)
                        

            for row in productRow:
                product_data_brand.append(row.get_attribute('data-brand'))

            for span in productName:
                product_data_part.append(span.text)
            nextBtn= driver.find_element(By.CSS_SELECTOR,'#p_lt_ctl03_pageplaceholder_p_lt_zoneMainContent_ProductListing_btnNext').click()

            print(product_data_part)
            # print(len(product_data_part))
            # print(len(product_data_brand))
            # print(len(product_data_qty))
            # print(len(product_data_desc))
            for index in range(len(product_data_qty)):
                thewriter.writerow({'Part_code':product_data_part[index],'Brand': product_data_brand[index],'Qty':product_data_qty[index],'Description':product_data_desc[index]})
            time.sleep(6)
        print("break")

    for link in product_link:
        my_function(link)