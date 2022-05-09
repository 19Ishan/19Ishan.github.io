# $ pip install plotly
import streamlit as st
import pandas as pd
from PIL import Image
# import graph_objects as go

#import yfinance

st.write("""This is the python project


""")
image = Image.open("https://drive.google.com/file/d/1CsHZpLtO3gxneeuifLjiIgULSLMYlgCR/view?usp=sharing")
st.image(image, use_column_width=True)
st.sidebar.header('User Input')

def get_input():#This functions take the user data
    s_date = st.sidebar.text_input("Start Date", "2020-01-02")
    e_date = st.sidebar.text_input("End Date", "2020-08-04")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "AMZN")
    return s_date,e_date,stock_symbol

def get_company_name(symbol):#getting the company name
    if symbol == 'AMZN':
        return 'Amazon'
    elif symbol == 'TSLA':
        return 'Tesla'
    elif symbol == 'GOOG':
        return 'Google'
    elif symbol == 'TCS':
        return 'TCS'
    elif symbol == 'AIRTEL':
        return 'Airtel'
    elif symbol == 'WIPRO':
        return 'Wipro'
    else:
        return 'None'

def get_data(symbol, start, end):#here we are getting company data from the start date to the end date
    if symbol.upper() == 'AMZN':
        df = pd.read_csv("https://drive.google.com/file/d/1Z2bHUuMibuQLr98QVRZcjJUIDKPb64OA/view?usp=sharing")#copy path  for amzn.csv
    elif symbol.upper() == 'TSLA':
        df = pd.read_csv("https://drive.google.com/file/d/1rYS79wma7eWj74qU_Rhgag8WXSPgMQXv/view?usp=sharing")#copy path  for tsla.csv
    elif symbol.upper() == 'GOOG':
        df = pd.read_csv("https://drive.google.com/file/d/1ZPX5XNyUoaiwH0KKMF2YwgoBpVMGPkW-/view?usp=sharing")#copy path  for Goog.csv
    elif symbol.upper() == 'TCS':
        df = pd.read_csv("https://drive.google.com/file/d/1UbUoif9AVhLCok5CV_yvkiTxaEvbLhwI/view?usp=sharing")#copy path  for tcs.csv
    elif symbol.upper() == 'AIRTEL':
        df = pd.read_csv("https://drive.google.com/file/d/1dpdso9uzRNsPcPeFvIGLIxt-v_-zaV0L/view?usp=sharing")#copy path  for airtel.csv
    elif symbol.upper() == 'WIPRO':
        df = pd.read_csv("https://drive.google.com/file/d/1ltjmwU7G1GOkQXDkoz9eaI0FiBjuTfMX/view?usp=sharing")#copy path  for wipro.csv
    else:
        df = pd.DataFrame(columns=['Date','Close', 'Open', 'Volume', 'Adj Close', 'High', 'Low'])

    start = pd.to_datetime(start)
    end = pd.to_datetime(end)
    start_row = 0
    end_row = 0
    for i in range(0, len(df)):
        if start <= pd.to_datetime(df['Date'][i]):
            start_row = i
            break

    #start from the bottom of the data and go up to see if user end date is greater or equal to the datat in data set.
    for j in range(0, len(df)):
        if end >= pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row = len(df)-1-j
            break
    df = df.set_index(pd.DatetimeIndex(df['Date'].values))
    return df.iloc[start_row:end_row +1,:]
#get user input
start, end, symbol = get_input()
#getting the data
df = get_data(symbol, start, end)
#getting the company name
company_name = get_company_name(symbol.upper())

#Display the close prize
st.header(company_name+' Close prize\n')
# st.line_chart(df['Close'])


#Display the Volume
st.header(company_name+' Volume\n')
# st.line_chart(df['Volume'])

#Get statistics on the data
st.header('Data Statistics')
st.write(df.describe())
