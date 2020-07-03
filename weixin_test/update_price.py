import pandas as pd
import json

def update():
    df = pd.read_excel("prices.xls")
    update_data = {}
    for i in df.index.values:
        name = df.iloc[i]['探针名称']
        price = str(df.iloc[i]['收费'])
        update_data[name] = price + '元'
    f = open("prices.json", "w")
    f.write(json.dumps(update_data))
    f.close()


if __name__ == '__main__':
    update()


