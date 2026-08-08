# L01 Simple APIs

- **Certificate:** IBM Data Engineering Professional Certificate
- **Course:** C02 Python for Data Science, AI & Development
- **Module:** M05 APIs and Data Collections
- **Date studied:** 2026-06-14

---

## Table of Contents

- [Overview](#overview)
- [What is an API?](#what-is-an-api)
- [REST APIs](#rest-apis)
- [PyCoinGecko — REST API Example](#pycoingecko--rest-api-example)
- [Applications of APIs](#applications-of-apis)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

This lesson introduces APIs as the mechanism by which software communicates via defined inputs and outputs, using pandas as a familiar first example. It then focuses on REST APIs specifically — the client/resource/endpoint/request/response cycle over HTTP and JSON — and walks through PyCoinGecko as a hands-on wrapper-library example, before surveying the range of domains (social media, e-commerce, weather, payments) that rely on APIs.

---

## What is an API?

An **API (Application Programming Interface)** lets two pieces of software talk to each other. Like a function, you only need to know its inputs and outputs — not how it works internally.

**Example — Pandas as an API:**

When you use pandas, you're actually using an API to communicate with underlying software components (some not even written in Python).

```python
# Creating a DataFrame — passing data to the pandas API (this is called an "instance")
import pandas as pd

data = {'Name': ['Alice', 'Bob'], 'Score': [90, 85]}
df = pd.DataFrame(data)

df.head()   # communicates with the API to display the first few rows
df.mean()   # asks the API to compute and return the mean values
```

---

## REST APIs

**REST (Representational State Transfer)** APIs allow programs to communicate over the internet, enabling access to external storage, data, and AI algorithms.

| Term | Description |
|------|-------------|
| **Client** | Your program / code making the request |
| **Resource** | The web service you communicate with |
| **Endpoint** | The URL address where the service is found |
| **Request** | What the client sends to the resource (usually HTTP + JSON) |
| **Response** | What the resource returns to the client (usually JSON) |

**How the cycle works:**
1. Client sends an **HTTP message** (containing a JSON file with instructions) to the endpoint
2. The web service performs the requested operation
3. The web service returns an **HTTP response** (usually as a JSON file)
4. The client receives and processes the data

---

## PyCoinGecko — REST API Example

**PyCoinGecko** is a Python wrapper for the CoinGecko API (updated every minute). Cryptocurrency data is ideal for API use because it changes constantly and is critical for trading decisions.

```python
# Install the library
# pip install pycoingecko

from pycoingecko import CoinGeckoAPI
import pandas as pd

cg = CoinGeckoAPI()
```

```python
# Fetch Bitcoin price data in USD for the past 30 days
data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)

# Response is a dict with keys: 'prices', 'market_caps', 'total_volumes'
# Each value is a nested list of [unix_timestamp, value]
price_data = data['prices']
```

```python
# Convert nested list to a DataFrame with readable datetime
df = pd.DataFrame(price_data, columns=['timestamp', 'price'])
df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
```

```python
# Build daily candlestick (OHLC) data by grouping by date
candlestick = df.groupby('date')['price'].agg(
    Open='first',
    High='max',
    Low='min',
    Close='last'
).reset_index()
```

```python
# Plot the candlestick chart using Plotly and export as HTML
import plotly.graph_objects as go

fig = go.Figure(data=[go.Candlestick(
    x=candlestick['date'],
    open=candlestick['Open'],
    high=candlestick['High'],
    low=candlestick['Low'],
    close=candlestick['Close']
)])
fig.write_html('bitcoin_candlestick.html')
# Open the .html file → click "Trust HTML" in the top-left of the tab to view the chart
```

---

## Applications of APIs

| Domain | Examples | What the API provides |
|--------|----------|-----------------------|
| Social media | Facebook, Twitter, Instagram | Access to posts, user data, feeds |
| E-commerce | Amazon, eBay | Product catalogs, orders, inventory |
| Weather | AccuWeather, The Weather Channel | Real-time and forecast weather data |
| Maps & Navigation | Google Maps, Waze | Location, directions, traffic data |
| Payment gateways | PayPal, Stripe | Secure payment processing |
| Messaging | WhatsApp, Facebook Messenger | Sending/receiving messages |

---

## 📖 Key Terms & Glossary

| Term | Definition |
|------|------------|
| API | A set of rules that allows two software systems to communicate via defined inputs and outputs |
| REST API | An API that communicates over the internet using HTTP and typically exchanges data as JSON |
| Client | The program or code that sends a request to a web service |
| Resource | The web service or server that the client is communicating with |
| Endpoint | The specific URL where a web service can be accessed |
| Request | The message sent from the client to the web service (usually HTTP + JSON) |
| Response | The data returned from the web service to the client (usually JSON) |
| JSON | JavaScript Object Notation — a text format for structured data, maps to Python dict/list |
| Wrapper | A Python library that wraps a REST API into easy-to-call Python functions |
| UNIX timestamp | The number of seconds (or milliseconds) elapsed since Jan 1, 1970 |
| OHLC | Open, High, Low, Close — four price points used to describe price movement in a time period |
| Candlestick chart | A financial chart showing OHLC data for a series of time periods |
| Instance | In API terms, the object created when you initialise an API client (e.g. `cg = CoinGeckoAPI()`) |

---

## ❓ My Questions & Gaps

- [ ] What is the difference between GET, POST, PUT, and DELETE HTTP methods — when is each used?
- [ ] How do you handle API authentication (API keys, Bearer tokens, OAuth)?
- [ ] What happens when an API rate limit is hit — how do you handle retries?
- [ ] When should you use a wrapper library vs. calling the REST API directly with `requests`?

---

## 🔗 Resources

- [IBM Data Engineering Professional Certificate](https://www.coursera.org/professional-certificates/ibm-data-engineer)
- [CoinGecko API Documentation](https://www.coingecko.com/en/api)
- [PyCoinGecko on PyPI](https://pypi.org/project/pycoingecko/)
- [Plotly Candlestick Chart Docs](https://plotly.com/python/candlestick-charts/)
