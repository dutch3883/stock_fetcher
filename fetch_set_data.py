import requests
import time
import json

# Define the list of stock symbols
# symbols = [
#     'ADVANC', 'AP', 'BCH', 'BCPG', 'CHG', 'CPF', 'EGCO', 'INTUCH', 'IVL', 'JMART',
#     'KKP', 'KTB', 'LH', 'ORI', 'PTT', 'PTTEP', 'RATCH', 'RCL', 'SAWAD', 'SIRI',
#     'SPALI', 'STA', 'STGT', 'TASCO', 'TCAP', 'THANI', 'TISCO', 'TTB', 'TU', 'WHA'
# ]

symbols = ['ADVANC']

# symbols = ["ACE", "ADVANC", "AH", "AMATA", "AOT", "AP", "ASW", "AWC", "BA", "BAFS", "BAM", "BANPU", "BBL", "BCH", "BCP", "BCPG", "BDMS", "BEM", "BGC", "BGRIM", "BLA", "BPP", "BRI", "BTS", "CBG", "CENTEL", "CK", "CKP", "COM7", "CPALL", "CPF", "CPN", "CRC", "DMT", "EA", "EGCO", "EPG", "ERW", "ETC", "GFPT", "GLOBAL", "GPSC", "GULF", "GUNKUL", "HANA", "HENG", "HMPRO", "HTC", "ICHI", "III", "ILM", "INTUCH", "IRPC", "IVL", "JTS", "KBANK", "KEX", "KKP", "KSL", "KTB", "KTC", "LH", "M-CHAI", "MAJOR", "MC", "MEGA", "MINT", "MTC", "NER", "NOBLE", "NRF", "NYT", "OR", "ORI", "OSP", "PLANB", "PR9", "PSH", "PSL", "PTT", "PTTEP", "PTTGC", "RATCH", "RBF", "RS", "S", "SABINA", "SAK", "SAPPE", "SAT", "SAWAD", "SC", "SCB", "SCC", "SCGP", "SHR", "SIRI", "SJWD", "SMPC", "SPALI", "STA", "STEC", "STGT", "SYNEX", "TCAP", "TFG", "THANI", "THCOM", "TISCO", "TOA", "TOG", "TOP", "TPIPL", "TQM", "TTA", "TTB", "TTW", "TVO", "VGI", "WHA", "WHAUP"]

# Function to fetch stock indicators for a single symbol
def fetch_stock_indicators(symbol, from_file = False):
    headers = {
        # 'authority': 'www.set.or.th',
        # 'accept': 'application/json, text/plain, */*',
        # 'accept-language': 'en,en-NZ;q=0.9,en-US;q=0.8,ja;q=0.7,th;q=0.6',
        # 'cache-control': 'no-cache',
        # 'dnt': '1',
        # 'pragma': 'no-cache',
        # 'referer': 'https://www.set.or.th/en/market/product/stock/quote/ADVANC/financial-statement/company-highlights',
        # 'sec-ch-ua': '"Not A Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        # 'sec-ch-ua-mobile': '?0',
        # 'sec-ch-ua-platform': '"macOS"',
        # 'sec-fetch-dest': 'empty',
        # 'sec-fetch-mode': 'cors',
        # 'sec-fetch-site': 'same-origin',
        # 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }

    status_headers =  headers = {
        # 'authority': 'www.set.or.th',
        # 'accept': 'application/json, text/plain, */*',
        # 'accept-language': 'en,en-NZ;q=0.9,en-US;q=0.8,ja;q=0.7,th;q=0.6',
        # 'cache-control': 'no-cache',
        'cookie': 'charlot=ad22719e-73a9-4c34-ae09-0c5d7b1a0cff; nlbi_2046605=NzuEK0P08lcHqKRhU9DvIwAAAADOJycTXvKhrxm6bE1+duAl; visid_incap_2046605=jVoySJTqRQGn6HnE4RlGehL52mUAAAAAQUIPAAAAAACnmRTW2Sc2XIbK0YGgE8Hf; incap_ses_1565_2046605=W7iBFu2UDk77lbS2zP+3FRP52mUAAAAAE42++l2RHNwZO1OhWSRoyQ==; incap_ses_1511_2046605=kHu7GlT8lEtLac4mSSf4FBP52mUAAAAApjKuoSjt3BmYRuL+c6wqbg==; _gcl_au=1.1.312300749.1708849429; _cbclose=1; _cbclose23453=1; _uid23453=2F086B38.1; _ctout23453=1; visid_incap_2771851=VaYdrz2JR4Guj/ZU/t2PdBX52mUAAAAAQUIPAAAAAABI+iwN61v6pX04Q7D2hfnW; incap_ses_1511_2771851=IcfjRn9PZh7la84mSSf4FBX52mUAAAAAluyBH5S7FfAUyY5UCNwHbg==; _fbp=fb.2.1708849430325.334330950; lightbox_exit_banner_timeout=1; _gid=GA1.3.370063838.1708849432; popup_timeout=1; exp_history={"go_expid":"GusVq2U2QG2l2p9tGb5KTQ","msgt":"lightbox_exit_banner","count":1}|{"go_expid":"5AD93i4KR9-ZVNOhL9Vr2w-V2","msgt":"popup","count":1}; api_call_counter=5; _ga_ET2H60H2CB=GS1.1.1708849432.1.1.1708851216.53.0.0; _ga_6WS2P0P25V=GS1.1.1708849432.1.1.1708851216.53.0.0; visit_time=256; landing_url=https://www.set.or.th/en/market/product/stock/quote/ADVANC/financial-statement/company-highlights; _ga=GA1.3.1065730672.1708849432; _gat_UA-426404-8=1',
        # 'dnt': '1',
        # 'pragma': 'no-cache',
        'referer': 'https://www.set.or.th/en/market/product/stock/quote/ADVANC/financial-statement/company-highlights',
        # 'sec-ch-ua': '"Not A Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        # 'sec-ch-ua-mobile': '?0',
        # 'sec-ch-ua-platform': '"macOS"',
        # 'sec-fetch-dest': 'empty',
        # 'sec-fetch-mode': 'cors',
        # 'sec-fetch-site': 'same-origin',
        # 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }
    
    # Initialize an empty dictionary to store indicators
    indicators = {}
    
    try:
        # Trading statistics URL
        if not from_file: 
            url_stats = f"https://www.set.or.th/api/set/stock/{symbol}/company-highlight/trading-stat?lang=en"
            response_stats = requests.get(url_stats, headers=headers)
            data_stats = response_stats.json()
            latest_stats = data_stats[-1]
            
            # Save trading stats to JSON file
            with open(f"data/{symbol}_trading_stats.json", "w") as file:
                json.dump(data_stats, file, indent=4)
        else:
            with open(f"data/{symbol}_trading_stats.json", "r") as file:
                # Load JSON data from the file
                data_stats = json.load(file)
                latest_stats = data_stats[-1]

        if not from_file:
            # Financial data URL
            url_financial = f"https://www.set.or.th/api/set/stock/{symbol}/company-highlight/financial-data?lang=en"
            response_financial = requests.get(url_financial, headers=headers)
            data_financial = response_financial.json()
            latest_financial = data_financial[-1]
            
            # Save financial data to JSON file
            with open(f"data/{symbol}_financial_data.json", "w") as file:
                json.dump(data_financial, file, indent=4)
        else:
            with open(f"data/{symbol}_financial_data.json", "r") as file:
                # Load JSON data from the file
                data_financial = json.load(file)
                latest_financial = data_financial[-1]
        
        # Extracting indicators
        indicators = {
            "Symbol": symbol,
            "Sector": latest_stats.get("sector"),
            "P/E": latest_stats.get("pe"),
            "P/BV": latest_stats.get("pbv"),
            "EPS": latest_financial.get("eps"),
            "GPM": latest_financial.get("grossProfitMargin"),
            "NPM": latest_financial.get("netProfitMargin"),
            "Current Ratio": latest_financial.get("currentRatio"),
            "D/E": latest_financial.get("deRatio"),
            "ROE": latest_financial.get("roe"),
            "ROA": latest_financial.get("roa"),
            "Yield": latest_stats.get("dividendYield"),
            "EBIT": latest_financial.get("ebit"),
            "EBITDA": latest_financial.get("ebitda")
        }
    except Exception as e:
        print(f"Failed to fetch data for {symbol}: {e}")
    
    return indicators

# Fetching and printing indicators for all symbols
headers_printed = False
for symbol in symbols:
    indicators = fetch_stock_indicators(symbol, from_file=False)
    if indicators:
        if not headers_printed:
            # Print the headers only once, separated by commas
            print(",".join(indicators.keys()))
            headers_printed = True
        # Print the values for each symbol, separated by commas
        print(",".join(str(value) for value in indicators.values()))
        time.sleep(0.1)  # sleep to avoid become suspicious