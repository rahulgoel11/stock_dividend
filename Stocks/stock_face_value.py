from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
import time
import pandas as pd


class Facevalue:

    def __init__(self):
        options = Options()
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        self.browser = webdriver.Chrome('D:/Rahul/office_work/chromedriver',chrome_options=options)

    def find_xpath(self,inp_path):
        try:
            self.browser.find_element_by_xpath(inp_path)
            return True
        except Exception as e:
            return False

    def main(self):
        #Face Value of stocks which is already saved, to avoid looping it again
        stored_fv_df = pd.read_excel(r'D:\Rahul\stocks\facevalue.xlsx') #Specify your system input path

        self.browser.get('https://www.moneycontrol.com/stocks/marketinfo/dividends_declared/index.php')
        url_obj = self.browser.find_elements_by_class_name('bl_12')

        stock_dict = dict()
        for i in self.browser.find_elements_by_class_name('bl_12'):
            stock_dict[i.text] = i.get_attribute('href')

        stock_dict.pop('')
        for name in stored_fv_df['Stock']:
            if name in stock_dict.keys():
                del stock_dict[name]

        face_value_dict = dict()
        if len(stock_dict) > 0:
            for k,v in stock_dict.items():
                attempt = 0
                self.browser.get(v)
                time.sleep(1)
                # Checking face value it it has loaded
                while self.find_xpath('//*[@id="standalone_valuation"]/ul/li[3]/ul/li[3]/div[2]') is False:
                    self.browser.get(v)
                    time.sleep(1.5)
                    attempt += 1
                    if attempt > 5:
                        break
                if attempt > 3:
                    face_value_dict[k] = None
                    # if page is not loading even after 3 attempt it will store value as None, Verify the value later in output
                    # Above code was added to avoid breaking of code
                else:
                    face_value_dict[k] = self.browser.find_element_by_xpath('//*[@id="standalone_valuation"]/ul/li[3]/ul/li[3]/div[2]').text

        face_val_df = pd.DataFrame(list(face_value_dict.items()), columns=['Stock', 'Face_Value'])

        new_fv_df = stored_fv_df.append(face_val_df)

        #Output Path and file name,Specify you system output path
        new_fv_df.to_excel(r'D:\Rahul\stocks\facevalue.xlsx', index=False)

        self.browser.quit()


if __name__ == "__main__":
    a = Facevalue()
    try:
        a.main()
    except Exception as e:
        a.browser.close()
