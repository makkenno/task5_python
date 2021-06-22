import eel
import desktop
import pos_system

app_name="html"
end_point="index.html"
size=(700,600)

# オーダーインスタンスを作成
order = pos_system.init_order()

@ eel.expose
def add_order(product_code, quantity):
    order.add_item_order(product_code, quantity)
    item_name, subtotal = order.return_subtotal_per_item(product_code, quantity)
    return product_code, item_name, quantity, subtotal

@ eel.expose
def calculate_total_price():
    return order.calculate_total_price()

@ eel.expose
def settle_bill(amount_to_pay):
    return order.settle_bill(amount_to_pay)

desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)