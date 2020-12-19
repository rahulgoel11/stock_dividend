# stock_dividend
Python Script which helps to get the dividend declared by Companies of Indian Stock Market from Moneycontrol.com

Requirement :-
  Python 3.6+
    Library :-
      1) Selenium
      2) Pandas



Python Files

1) stock_face_value.py
    Run this script 1st to Update the facevalue.xlsx file
  
    This file is uses Selenium to get the FaceValue data from MoneyControl Website
  
    It Gets the intial details of conapny which has declared dividend for the year and scrape through the website and store the face value of company in excel
  
    facevalue file as on 19th December 2020 :- facevalue.xlsx
  
    Note :- Use the facevalue file as a base file and store the file in same folder in which the script is place or you can specify the file path in script (@ read_excel and   to_excel)
  
  

2) stock_dividend.py
    Post running the stock_face_value.py script run the script to calculate the dividend declared by the companies
   
    Specify the list of stocks in stock_list.xlsx (use this site to get the format of name you should enter for you stock https://www.moneycontrol.com/india/stockpricequote/)
   
    Two output will be generated 1 of you stock and other having dividend of all stocks
   
    have provided the dividend info of stock for year 2020 till 19th December 2020 (all_dividend_12_2020.xlsx)
   
    Note :- Use the file as a base file and store the file in same folder in which the script is place or you can specify the file path in script (@ read_excel and to_excel)
   
PS :- Above Code is getting data from MoneyControl.com. If there is any change in Website the code may not work, If there is any changes will provide and Updated Code
