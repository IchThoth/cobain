import requests
import json
import pandas as pd

url = "https://public-api.birdeye.so/defi/tokenlist?sort_by=v24hChangePercent&sort_type=desc"
header = {"x-chain":"solana","X-API-KEY": "e3194f932e1846429558b16dc3ef19b4"}



response = requests.get(url,headers=header)

if response.status_code == 200:
    resp_data = response.json()
    tokens = resp_data.get('data',{}).get('tokens',[])
    df = pd.DataFrame(tokens)
    csv_fp = 'tokies.csv'
    
    min_vol = 10000
    f_data = [token for token in tokens if token.get('mc') and min_vol]
    df.to_csv(csv_fp,index=False)
    print(json.dumps(f_data, indent=4))
    #print(dataframe)
else:
    print("failed to retrieve data",response.status_code)
