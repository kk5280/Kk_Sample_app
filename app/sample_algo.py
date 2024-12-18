from flask import Flask
import pdb
from Dhan_Tradehull_V2 import Tradehull
import pandas as pd
import numpy as np
import talib
import time
import datetime
import logging
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
  client_code = "1101482038"
  token_id = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzM0ODkyMjI3LCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMTQ4MjAzOCJ9.pFvXykNFYu9yTChHV4GjkfY7s_OqVMwo5KoBrWsHjepoG37bl9zBjztSy3Vl692r1A3aWQMjF6LV-G8E_9Bjag"

  time.sleep(0.2)
  tsl = Tradehull(client_code,token_id)


  Historical_Data_Start_Date_For_Day_Chart=datetime.datetime.now()-datetime.timedelta(days=4)
  Historical_Data_Start_Date_For_IntraDay_Chart=datetime.datetime.now()-datetime.timedelta(days=4)
  NIFTY_Monthly_Expiry_Date = '26-12-2024'
  Avg_Period = 14
  Index_expiry_date = {"NIFTY":'05-12-2024',  "BANKNIFTY":'24-12-2024'}
  Index_script_exchange = {"NIFTY":'INDEX',  "BANKNIFTY":'INDEX'}
  #watchlist=['INDIANB', 'BANKINDIA', 'KEI', 'OBEROIRLTY', 'CYIENT', 'DEEPAKNTR', 'GAIL', 'RECLTD', 'RBLBANK','M&MFIN', 'IRFC', 'PFC', 'HDFCLIFE', 'JSL', 'HDFCAMC', 'SBILIFE', 'MANAPPURAM', 'ZOMATO', 'CANBK', 'AARTIIND', 'UNIONBANK', 'COROMANDEL', 'NTPC', 'WIPRO', 'POONAWALLA', 'OIL', 'CHAMBLFERT', 'MFSL', 'CHOLAFIN', 'PAYTM', 'ICICIGI', 'GUJGASLTD', 'BPCL', 'NYKAA', 'TCS', 'SIEMENS', 'UPL', 'BHARATFORG', 'SJVN', 'BEL', 'ITC', 'LTF', 'HUDCO', 'GRANULES', 'BAJFINANCE', 'MPHASIS', 'BANKBARODA', 'PETRONET', 'LT', 'TECHM', 'SONACOMS', 'BATAINDIA', 'ABFRL', 'IRB', 'INFY', 'CDSL', 'CGPOWER', 'CANFINHOME', 'VBL', 'FEDERALBNK', 'PNB', 'LICHSGFIN', 'NHPC', 'ABB', 'CUB', 'SRF', 'HDFCBANK', 'ICICIPRULI', 'BHEL', 'SBICARD', 'ALKEM', 'CAMS', 'IEX', 'HCLTECH', 'BANDHANBNK', 'LTIM', 'DMART', 'VOLTAS', 'BAJAJFINSV', 'APOLLOHOSP', 'BSOFT', 'DABUR', 'JIOFIN', 'EXIDEIND', 'BRITANNIA', 'APOLLOTYRE', 'GNFC', 'TATACOMM', 'INDIGO', 'CESC', 'HINDPETRO', 'TITAN', 'BALKRISIND', 'SYNGENE', 'ATUL', 'JSWENERGY', 'LICI', 'MAXHEALTH', 'GODREJCP', 'HFCL', 'CUMMINSIND', 'APLAPOLLO', 'SBIN', 'HAL', 'TATAPOWER', 'ONGC', 'IDFCFIRSTB', 'INDIAMART', 'CROMPTON', 'IGL', 'YESBANK', 'LTTS', 'INDUSINDBK', 'CONCOR', 'HINDCOPPER', 'AUBANK', 'NATIONALUM', 'IDEA', 'ASIANPAINT', 'IOC', 'KOTAKBANK', 'ADANIENSOL', 'BAJAJ-AUTO', 'TATACONSUM', 'POWERGRID', 'SHRIRAMFIN', 'GMRINFRA', 'NESTLEIND', 'KPITTECH', 'EICHERMOT', 'INDHOTEL', 'TATACHEM', 'COALINDIA', 'PIIND', 'JINDALSTEL', 'INDUSTOWER', 'NCC', 'ICICIBANK', 'TATAELXSI', 'IRCTC', 'LAURUSLABS', 'JSWSTEEL', 'DLF', 'DELHIVERY', 'TVSMOTOR', 'UBL', 'LODHA', 'VEDL', 'COFORGE', 'NAVINFLUOR', 'MUTHOOTFIN', 'ASTRAL', 'ABCAPITAL', 'SUNTV', 'AMBUJACEM', 'SUPREMEIND', 'HEROMOTOCO', 'GRASIM', 'SAIL', 'PVRINOX', 'POLYCAB', 'AXISBANK', 'BSE', 'ESCORTS', 'M&M', 'SUNPHARMA', 'HINDALCO', 'TIINDIA', 'POLICYBZR', 'MCX', 'BERGEPAINT', 'ANGELONE', 'LALPATHLAB', 'NMDC', 'HINDUNILVR', 'PEL', 'TRENT', 'PIDILITIND', 'RAMCOCEM', 'PRESTIGE', 'JUBLFOOD', 'DRREDDY', 'PERSISTENT', 'NAUKRI', 'MARICO', 'DIVISLAB', 'METROPOLIS', 'DALBHARAT', 'TATASTEEL', 'GLENMARK', 'MOTHERSON', 'ADANIPORTS', 'TATAMOTORS', 'UNITDSPR', 'ADANIENT', 'ZYDUSLIFE', 'MGL', 'LUPIN', 'KALYANKJIL', 'ASHOKLEY', 'RELIANCE', 'HAVELLS', 'TORNTPHARM', 'IPCALAB', 'BIOCON', 'GODREJPROP', 'ACC', 'BHARTIARTL', 'CIPLA', 'JKCEMENT', 'COLPAL', 'ATGL', 'AUROPHARMA', 'ADANIGREEN']
  Ignorewatchlist = ['IRB','ATGL', 'BSE', 'M&M', 'POLYCAB', 'KALYANKJIL', 'OIL', 'M&MFIN', 'HDFCAMC', 'SBILIFE','COROMANDEL', 'CHOLAFIN', 'PAYTM', 'ICICIGI', 'SIEMENS', 'BHARATFORG', 'BAJFINANCE', 'MPHASIS','LT', 'TECHM']
  # Probabale igorant list CDSL
  #late start NCC,  'POONAWALLA',
  watchlist=['BPCL', 'VEDL', 'BEL', 'ONGC', 'BHEL', 'TATAPOWER', 'POWERGRID']

  #OPTSTK, OPTIDX


  # Reading FNO Volume
  fno_with_volume = {}
  SelForTrade = {}
  print("Historical_Data_Start_Date_For_IntraDay_Chart ", Historical_Data_Start_Date_For_IntraDay_Chart)
  current_time = datetime.datetime.now()
  print("Current  Time", current_time)
  time_change = datetime.timedelta(minutes=15) 
  updated_time = current_time + time_change
  print("Updated  Time", updated_time)

  order_status=tsl.get_order_status(None)

  print("order_status of blank ", order_status)

  Curr_Poistion_Count = len(tsl.get_positions())
  print("Current  Position count", Curr_Poistion_Count)

  Curr_Open_Poistion = tsl.get_positions()
  print("Current Open Position ", Curr_Open_Poistion)

  Curr_orderbook = tsl.get_orderbook()
  print("Current Order Curr_orderbook ", Curr_orderbook)

  Curr_tradebook = tsl.get_trade_book()
  print("Current Trade Book ", Curr_tradebook)

  open_position = 0

  for i in range(len(tsl.get_positions())):
    print("buy qty ", Curr_Open_Poistion[i]['buyQty'])
    print("sell qty ", Curr_Open_Poistion[i]['sellQty'])
    if(Curr_Open_Poistion[i]['buyQty']==Curr_Open_Poistion[i]['sellQty']):
      continue
    else:
      open_position = open_position+1

  print("Current Open Position ", open_position)

  return 'Well Done!'

if __name__ == '__main__':
  app.run()
