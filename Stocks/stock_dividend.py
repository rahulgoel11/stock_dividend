import pandas as pd
import numpy as np
import datetime


class Dividend:

    def get_dividend(self):

        data = pd.read_html('http://www.moneycontrol.com/stocks/marketinfo/dividends_declared',match='COMPANY NAME',skiprows=1)

        face_value = pd.read_excel('D:/stocks/facevalue.xlsx').rename(columns={'Stock': 'COMPANY NAME'}) #read the face value file that was downloaded
        face_value['COMPANY NAME'] = face_value['COMPANY NAME'].str.lower()

        face_value['Face_Value'] = face_value['Face_Value'].replace('-', 0).fillna(0).astype('float64') # Some face value are - in website so replacing it with 0

        my_stock = pd.read_excel(r'D:/stock_list.xlsx')  #Tracking dividend on my stocks
        my_stock['COMPANY NAME'] = my_stock['COMPANY NAME'].str.lower()

        div_data = data[0]  #data is fetched in form of array and stored in index 0, storing the same

        #column name is stored as value so dynamically identifying the rows to be skipped
        col_name = []
        skip_count = 0
        for index, rows in div_data.iterrows():
            skip_count += 1
            if rows[0] == 'COMPANY NAME':
                col_name = rows.values
                break

        div_data = div_data.iloc[skip_count:]
        div_data.columns = col_name
        div_data['%'] = div_data['%'].astype('float64')
        div_data['COMPANY NAME'] = div_data['COMPANY NAME'].str.lower()

        # Calculating the dividend
        div_fv_df = pd.merge(div_data, face_value, on='COMPANY NAME')

        div_fv_df['Div_paid'] = (div_fv_df['%']/100)*div_fv_df['Face_Value'] #This is individual entry of dividend declared

        consolidated_div_pay = div_fv_df.groupby('COMPANY NAME')['Div_paid'].sum().sort_values(ascending=False).to_frame().reset_index() #consolidated sum of all companies dividend

        my_dividend = pd.merge(my_stock, div_fv_df, on='COMPANY NAME') #Dividend of owned stocks

        op_path = r'D:\stocks\my_dividend_%s_%s.xlsx' % (str(datetime.datetime.now().month), str(datetime.datetime.now().year))

        all_div_path = r'D:\stocks\all_dividend_%s_%s.xlsx'%(str(datetime.datetime.now().month),str(datetime.datetime.now().year))

        my_dividend.to_excel(op_path, index=False)

        writer = pd.ExcelWriter(all_div_path, engine='xlsxwriter')
        div_fv_df.to_excel(writer, sheet_name='ALL', index=False)
        consolidated_div_pay.to_excel(writer, sheet_name='Consolidated', index=False)
        writer.save()


if __name__ == "__main__":
    a = Dividend()
    a.get_dividend()
