def shopping(shop_file):
    shop_dict = {} # 생성할 사전 객체

    with open("data/"+ shop_file) as f:
      for line in f:
        if line != "\n":
          name, price = line.strip().split()
          if name != "#쇼핑몰":
            shop_dict[name] = price

    return shop_dict

def item_price(shop_file, item):
    return shopping(shop_file)[item]
