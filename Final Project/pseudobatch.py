import requests
from sqlalchemy import create_engine

# URL for 5 Stocks

##APPLE 
aapl_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=aapl&apikey=4XURQ7C5RRTJ6U1O'
aapl_response = requests.request("GET", aapl_url)
aapl_data = aapl_response.json()


# ## MICROSOFT
msft_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=msft&apikey=4XURQ7C5RRTJ6U1O'
msft_response = requests.request("GET", msft_url)
msft_data = msft_response.json()

# # GOOGLE
goog_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=goog&apikey=4XURQ7C5RRTJ6U1O'
goog_response = requests.request("GET", goog_url)
goog_data = goog_response.json()

# # # TESLA 
tsla_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=tsla&apikey=4XURQ7C5RRTJ6U1O'
tsla_response = requests.request("GET", tsla_url)
tsla_data = tsla_response.json()

# # # AMAZON
amzn_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=amzn&apikey=4XURQ7C5RRTJ6U1O'
amzn_response = requests.request("GET", amzn_url)
amzn_data = aapl_response.json()


## Databse connection 

conn = 'mysql+pymysql://c348ns1wkq3sg90k:ym7vv5za2ihd0jym@x71wqc4m22j8e3ql.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/u5bt557nrgzsm40e'

engine = create_engine(conn)
engine.connect()


### INSERTING APPLE STOCKS INFO #########
apple_list = list(aapl_data["Time Series (Daily)"].values())
for i in range(1):
    date = list(aapl_data["Time Series (Daily)"])[i]
    symbol = 'AAPL'
    open = apple_list[i]['1. open']
    high = apple_list[i]['2. high']
    low = apple_list[i]['3. low']
    close = apple_list[i]['4. close']
    volume = apple_list[i]['5. volume']
        
    engine.execute(f"""
    INSERT INTO stocks VALUES ('{date}','{symbol}',{open},{high},{low},{close},{volume});
    """)


### INSERTING MICROSOFT STOCKS INFO #########
msft_list = list(msft_data["Time Series (Daily)"].values())
print("flag 1")
for i in range(1):
    print(i)
    date = list(msft_data["Time Series (Daily)"])[i]
    symbol = 'MSFT'
    open = msft_list[i]['1. open']
    high = msft_list[i]['2. high']
    low = msft_list[i]['3. low']
    close = msft_list[i]['4. close']
    volume = msft_list[i]['5. volume']

    engine.execute(f"""
    INSERT INTO stocks VALUES ('{date}','{symbol}',{open},{high},{low},{close},{volume});
    """)


### INSERTING GOOGLE  STOCKS INFO #########
goog_list = list(goog_data["Time Series (Daily)"].values())
for i in range(1):
    date = list(goog_data["Time Series (Daily)"])[i]
    symbol = 'GOOG'
    open = goog_list[i]['1. open']
    high = goog_list[i]['2. high']
    low = goog_list[i]['3. low']
    close = goog_list[i]['4. close']
    volume = goog_list[i]['5. volume']
        

    engine.execute(f"""
    INSERT INTO stocks VALUES ('{date}','{symbol}',{open},{high},{low},{close},{volume});
    """)

### INSERTING TESLA  STOCKS INFO #########
tsla_list = list(tsla_data["Time Series (Daily)"].values())
for i in range(1):
    date = list(tsla_data["Time Series (Daily)"])[i]
    symbol = 'TSLA'
    open = tsla_list[i]['1. open']
    high = tsla_list[i]['2. high']
    low = tsla_list[i]['3. low']
    close = tsla_list[i]['4. close']
    volume = tsla_list[i]['5. volume']
        

    engine.execute(f"""
    INSERT INTO stocks VALUES ('{date}','{symbol}',{open},{high},{low},{close},{volume});
    """)


 ### INSERTING AMAZON  STOCKS INFO #########
amzn_list = list(amzn_data["Time Series (Daily)"].values())
for i in range(1):
    date = list(amzn_data["Time Series (Daily)"])[i]
    symbol = 'AMZN'
    open = amzn_list[i]['1. open']
    high = amzn_list[i]['2. high']
    low = amzn_list[i]['3. low']
    close = amzn_list[i]['4. close']
    volume = amzn_list[i]['5. volume']
        

    engine.execute(f"""
    INSERT INTO stocks VALUES ('{date}','{symbol}',{open},{high},{low},{close},{volume});
    """)


