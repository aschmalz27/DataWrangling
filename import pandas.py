import pandas

stocks = pd.read_csv('C:/Users/Downloads/schma/stocks(1).csv')

stocks['date'].dtype

stocks['date'] = pandas.to_datetime(stocks['date'])

today = pd.Timestamp.today()

five_years_ago = today - pd.DateOffset(years=5)

stocks[stocks['date'] >= five_years_ago]

pd.Timestamp.now()

pd.Timestamp.now().timestamp()

pd.Timestamp(unix_time, unit="s")

pd.date_range(start="2020-01-01", end="2022-07-07", freq="D")

stocks[stocks['date'].isin(date_range)]

stocks['date'].dt.month
stocks['date'].dt.year