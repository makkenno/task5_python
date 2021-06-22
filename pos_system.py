import pandas as pd
import datetime

### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price,quantity=0):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
        self.quantity=quantity
    
    def get_price(self):
        return self.price

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_quantity_list=[]
        self.item_master=item_master
        self.set_datetime()

    
    def set_datetime(self):
        self.datetime=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    def get_item_data(self,item_code):
        for m in self.item_master:
            if item_code == m.item_code:
                return m.item_name, m.price

    def take_order(self):
        while True:
            item_code = ""
            input_text=input("商品コードを入力してください。終了する場合はendと入力してください：")
            if input_text == "end":
                break
            for row in self.item_master:
                if row.item_code == input_text:
                    item_code = input_text
            if not item_code:
                print('登録されている商品コードを入力してください')
                continue
            item_quantity=input("個数を入力してください:")
            self.add_item_order(item_code,item_quantity)

    
    def add_item_order(self,item_code,item_quantity):
        self.item_order_list.append(item_code)
        self.item_quantity_list.append(item_quantity)

    def return_subtotal_per_item(self,item_code,item_quantity):
        item_name, item_price = self.get_item_data(item_code)
        subtotal = item_price * int(item_quantity)
        return item_name, subtotal

    def view_item_list(self):
        for item in self.item_order_list:
            print("商品コード:{}".format(item))

    def calculate_total_price(self):
        self.total_price=0
        for row in self.item_master:
            for item_code,item_quantity in zip(self.item_order_list,self.item_quantity_list):
                if row.item_code == item_code:
                    price=row.price*int(item_quantity) 
                    self.total_price+=price
        return self.total_price

    def pay_off(self):
        if len(self.item_order_list)>=1:
            while True:
                amount_to_pay=input("お支払い金額を入力してください：")
                change_money=int(amount_to_pay)-self.total_price
                if change_money>=0:
                    self.receipt(f"お支払い金額：{amount_to_pay}円")
                    self.receipt(f"お釣り：{change_money}円")
                    break
                else:
                    print(f"{abs(change_money)}円不足しています。再度入力してください")
            print("ありがとうございました。")

    def settle_bill(self, amount_to_pay):
        return int(amount_to_pay) - self.total_price


    def receipt(self,text):
        print(text)
        with open("./receipt/" + self.receipt_file_name,mode="a",encoding="utf-8_sig") as f:
            f.write(text+"\n") 


    
def add_item_master_from_csv(csv_path):
    # マスタ登録
    item_master=[]
    item_master_df = pd.read_csv(csv_path, dtype={"code":object})
    for row in item_master_df.itertuples():
        item_master.append(Item(row.code,row.name,row.price))
    return item_master
    
def init_order():
    item_master = add_item_master_from_csv('./item_master.csv')
    # オーダー登録
    order=Order(item_master)
    return order
    # order.take_order()
    
    # # オーダー表示
    # order.view_item_list()
    # order.view_order_list()
    
    # # 精算
    # order.pay_off()
    
# if __name__ == "__main__":
#     main()