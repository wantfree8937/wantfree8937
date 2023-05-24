from pathlib import Path

data_path = Path() / "data"
data_path.mkdir(parents=True, exist_ok=True)

code_path = Path() / "codes"
code_path.mkdir(parents=True, exist_ok=True)

def shopping(shop_file):
    shop_dict = {} # 생성할 사전 객체

    with open(data_path / shop_file, mode='r', encoding='utf-8') as f:    
      for line in f:
        price_of_goods = line.strip().split() 
        if price_of_goods != []:      
          goods, price = price_of_goods 
        if price != shop_file[4]:
          shop_dict[goods] = int(price.rstrip('원'))

    return shop_dict

def item_price(shop_file, item):
    return shopping(shop_file)[item]
