import tornado.ioloop
import tornado.web
import tornado.websocket
import json
import pymysql
import decimal
import time
from itertools import groupby
from websocketData import Tsujiri
from pathlib import Path

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    live_web_sockets = set()

    def check_origin(self, origin):  #允許外網連入
        return True
    def open(self):  #開啟時的動作
        self.live_web_sockets.add(self)
        print("WebSocket opened")

    def on_message(self, message):  #當訊息進入時，"觸發"
        message = json.loads(message)
        print ('Server receive:', message)

        data = {}
        if (message['action'] == '400'):
            # delete cart data if in step 2
            if message['step'] == '2':
                mysql = mysql_connection()
                connection = mysql['connection']
                cursor = mysql['cursor']

                sale_number = get_sale_number()
                sql = "DELETE carts, cart_products, cart_product_items FROM carts LEFT JOIN cart_products ON carts.id = cart_products.cart_id LEFT JOIN cart_product_items ON cart_products.id = cart_product_items.cart_product_id WHERE sale_number = %s"
                binds = (sale_number)
                delete_data(connection, cursor, sql, binds)

                close_connection(connection, cursor)

            language = get_language()
            language_id = language['id']
            language_code = language['code']

            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data": {
                    "language_id": language_id,
                    "language_code": language_code,
                    "redirect_to":"0",
                    "template":"tsujiri",
                    "languages":[
                        {
                            "id":"1",
                            "title":"English",
                            "code":"en"
                        },
                        {
                            "id":"2",
                            "title":"繁體中文",
                            "code":"zh-TW"
                        },
                        {
                            "id":"3",
                            "title":"简体中文",
                            "code":"zh-CN"
                        },
                        {
                            "id":"4",
                            "title":"日本語",
                            "code":"ja"
                        }
                    ]
                }
            }
        elif (message['action'] == '401'):
            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data": [
                    {
                        "banners" : [
                            {
                                'photo' : 'hero2.jpg',
                            },
                            {
                                'photo' : 'hero3.jpg'
                            }                            
                        ]
                    }   
                ]
            }
        elif (message['action'] == '403'):
            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data"    : []
            }
        elif (message['action'] == '404'):
            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data"    : []
            }
        elif (message['action'] == '405'):
            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data"    : []
            }
        elif (message['action'] == '406'):
            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data"    : []
            }            
        elif (message['action'] == '410'):
            mysql = mysql_connection()
            connection = mysql['connection']
            cursor = mysql['cursor']

            sql = "SELECT categories.id, contents.`name` AS title, categories.notice, contents.image AS photo FROM categories LEFT JOIN contents ON categories.id = contents.source_id AND contents.type = 3 AND contents.language_id = 26 WHERE categories.type = 3 AND client_id = %s ORDER BY categories.sort"
            binds = (25)
            categories = select_data(connection, cursor, sql, binds)
            # category_id = categories[0]['id']
            category_id = get_category_id()

            sql = """
                SELECT
                    products.id,
                    contents.NAME AS title,
                    product_sales.amount AS price,
                    contents.image AS photo 
                FROM
                    products
                    LEFT JOIN product_sales ON products.id = product_sales.product_id AND product_sales.sales_type_id = 1
                    LEFT JOIN contents ON products.id = contents.source_id AND contents.type = 4 AND language_id = 26
                    LEFT JOIN product_categories ON products.id = product_categories.product_id 
                WHERE
                    product_categories.category_id = %s
                    AND deleted_at IS NULL 
                ORDER BY
                    product_categories.sort"""
            binds = (category_id)
            products = select_data(connection, cursor, sql, binds)

            close_connection(connection, cursor)

            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data" : {
                    "category_id": category_id,
                    "categories": categories,
                    "products": products
                }
            }
            
        elif (message['action'] == '412'):
            mysql = mysql_connection()
            connection = mysql['connection']
            cursor = mysql['cursor']

            sql = """
                SELECT
                    products.id,
                    contents.NAME AS title,
                    product_sales.amount AS price,
                    contents.image AS photo 
                FROM
                    products
                    LEFT JOIN product_sales ON products.id = product_sales.product_id AND product_sales.sales_type_id = 1
                    LEFT JOIN contents ON products.id = contents.source_id AND contents.type = 4 AND language_id = 26
                    LEFT JOIN product_categories ON products.id = product_categories.product_id 
                WHERE
                    product_categories.category_id = %s
                    AND deleted_at IS NULL 
                ORDER BY
                    product_categories.sort"""
            binds = (message['category_id'])
            product = select_data(connection, cursor, sql, binds)

            close_connection(connection, cursor)
            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data"    : {
                    "products": product
                }
            }
        elif (message['action'] == '413'):
            mysql = mysql_connection()
            connection = mysql['connection']
            cursor = mysql['cursor']

            # select product
            sql = "SELECT products.id, products.title, products.volume, products.unit, products.order_type, contents.image AS photo, product_sales.amount AS price FROM products LEFT JOIN product_sales ON products.id = product_sales.product_id AND product_sales.sales_type_id = 1 LEFT JOIN contents ON products.id = contents.source_id AND contents.type = 4 AND contents.language_id = 26 WHERE products.id = %s"
            binds = (message['product_id'])
            product_data = select_data(connection, cursor, sql, binds)
            product = product_data[0]

            # select properties
            sql = "SELECT product_properties.id AS product_property_id, product_properties.property_id AS id, categories.title, contents.image AS photo, categories.private, product_properties.multiple, product_properties.quantity, product_properties.required FROM product_properties LEFT JOIN categories ON product_properties.property_id = categories.id LEFT JOIN contents ON categories.id = contents.source_id AND contents.type = 1 AND contents.language_id = 26 WHERE product_id = %s ORDER BY product_properties.sort"
            binds = (message['product_id'])
            properties = select_data(connection, cursor, sql, binds)

            for idx, property in enumerate(properties):
                # select property_items
                sql = "SELECT categories.id, contents.name AS title, product_property_items.`default`, product_property_items.online, product_property_items.sort, product_property_items.plus_price AS price, product_property_items.volume, contents.image AS photo FROM product_property_items LEFT JOIN categories ON product_property_items.item_id = categories.id LEFT JOIN contents ON categories.id = contents.source_id AND contents.type = 2 AND contents.language_id = 26 WHERE product_property_id = %s ORDER BY product_property_items.sort"
                binds = (property['product_property_id'])
                item_data = select_data(connection, cursor, sql, binds)
                properties[idx]['items'] = item_data

            # select categories
            sql = "SELECT id, title, private FROM categories WHERE EXISTS (SELECT * FROM product_categories WHERE categories.id = product_categories.category_id AND product_id = %s) AND type = 3 AND categories.deleted_at IS NULL"
            binds = (message['product_id'])
            categories = select_data(connection, cursor, sql, binds)

            close_connection(connection, cursor)

            data = {
                "success": True,
                "action":"413",
                "code":0,
                "message":"",
                "datetime":"2020-10-12 17:54:42:2174",
                "data":{
                    "product": product,
                    "properties": properties,
                    "categories": categories,
                }
            }
        elif (message['action'] == '416'):
            category_id = message['category_id']
            change_category_id(category_id)

            data = {
                "success": True,
                "action":"416",
                "code":0,
                "message":"",
                "data":[]
            }
        # 420 商品加入購物車 
        elif (message['action'] == '420'):
            mysql = mysql_connection()
            connection = mysql['connection']
            cursor = mysql['cursor']

            sale_number = get_sale_number()
            payment_id = 1

            product_id = message['product_id']
            items = [des["item_id"] for des in message["items"]]
            items_str = ','.join(str(x) for x in items)

            # product data (with product_sales)
            sql = "SELECT products.id, product_sales.amount, products.title, products.order_type FROM product_sales LEFT JOIN products ON product_sales.product_id = products.id WHERE product_id = %s AND sales_type_id = 1"
            binds = (product_id)
            product_data = select_data(connection, cursor, sql, binds)
            product = product_data[0]

            # property item data
            sql = "SELECT * FROM product_property_items LEFT JOIN product_properties ON product_property_items.product_property_id = product_properties.id WHERE product_properties.product_id = %s AND product_property_items.item_id IN (" + items_str + ")"
            binds = (product_id)
            item_data = select_data(connection, cursor, sql, binds)

            # is drink
            order_type = product['order_type']
            property_count = len(item_data)
            is_drink = order_type == 1 and property_count > 0

            # 商品價格 + 屬性價格
            sub_total = decimal.Decimal(product['amount'])
            if is_drink:
                for item in item_data:
                    sub_total += item['plus_price']

            # 購物車總金額: (商品價格 + 屬性價格) * 數量
            sale_total = sub_total * decimal.Decimal(message["quantity"])

            # select carts data
            sql = "SELECT * FROM carts WHERE sale_number = %s"
            binds = (sale_number)
            cart_data = select_data(connection, cursor, sql, binds)

            if len(cart_data):
                cart_id = cart_data[0]['id']
                new_sale_total = decimal.Decimal(cart_data[0]['sale_total']) + sale_total
                # update sale_total
                sql = "UPDATE carts SET sale_total = %s WHERE id = %s"
                binds = (new_sale_total, cart_id)
                update_data(connection, cursor, sql, binds)
            else:
                # insert into `carts`
                sql = "INSERT INTO carts (client_id, payment_id, sale_number, sale_total, created_at) VALUES (25, %s, %s, %s, now())"
                binds = (payment_id, sale_number, sale_total)
                cart_id = insert_data(connection, cursor, sql, binds)

            # insert into `cart_products`
            sql = "INSERT INTO cart_products (cart_id, product_id, qty, sub_total, sale_price) VALUES (%s, %s, %s, %s, %s)"
            binds = (cart_id, product_id, message["quantity"], sub_total, product['amount'])
            cart_product_id = insert_data(connection, cursor, sql, binds)

            # insert into `cart_product_items`
            for item in item_data:
                sql = "INSERT INTO cart_product_items (cart_product_id, property_id, item_id, sale_price, qty, sub_total) VALUES (%s, %s, %s, %s, %s, %s)"
                binds = (cart_product_id, item['property_id'], item['item_id'], item['plus_price'], 1, item['plus_price'])
                cart_product_item_id = insert_data(connection, cursor, sql, binds)

            ## get carts data
            order = get_cart_data(connection, cursor, cart_id)

            close_connection(connection, cursor)

            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data"    : {
                    "order": order
                }
            }
        elif (message['action'] == '421'):
            mysql = mysql_connection()
            connection = mysql['connection']
            cursor = mysql['cursor']

            sale_number = get_sale_number()
            cart_product_id = message['id']

            # delete `cart_product_items` data
            sql = "DELETE FROM cart_product_items WHERE cart_product_id = %s"
            binds = (cart_product_id)
            delete_data(connection, cursor, sql, binds)

            # delete `cart_products` data
            sql = "DELETE FROM cart_products WHERE id = %s"
            binds = (cart_product_id)
            delete_data(connection, cursor, sql, binds)

            # update `carts` sale_total
            sql = "SELECT * FROM carts WHERE sale_number = %s"
            binds = (sale_number)
            carts = select_data(connection, cursor, sql, binds)

            cart_id = 0
            if len(carts):
                cart_id = carts[0]['id']
            update_carts_sale_total(connection, cursor, cart_id)

            ## get carts data
            order = get_cart_data(connection, cursor, cart_id)

            close_connection(connection, cursor)

            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data"    : {
                    "order": order
                }
            }
        elif (message['action'] == '422'):
            mysql = mysql_connection()
            connection = mysql['connection']
            cursor = mysql['cursor']

            cart_id = message['order_id']
            cart_product_id = message['id']
            qty = message['qty']

            # udpate `cart_products` qty
            sql = "UPDATE cart_products SET qty = %s WHERE cart_id = %s AND id = %s"
            binds = (qty, cart_id, cart_product_id)
            update_data(connection, cursor, sql, binds)

            # update `carts` sale_total
            update_carts_sale_total(connection, cursor, cart_id)

            ## get carts data
            order = get_cart_data(connection, cursor, cart_id)

            close_connection(connection, cursor)

            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data"    : {
                    "order": order
                }
            }
        # 423 取得購物清單
        elif (message['action'] == '423'):
            sale_number = get_sale_number()
            mysql = mysql_connection()
            connection = mysql['connection']
            cursor = mysql['cursor']

            sql = "SELECT * FROM carts WHERE sale_number = %s"
            binds = (sale_number)
            carts = select_data(connection, cursor, sql, binds)

            cart_id = 0
            if len(carts):
                cart_id = carts[0]['id']

            order = get_cart_data(connection, cursor, cart_id)

            close_connection(connection, cursor)

            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data"    : {
                    "order": order
                }
            }
        elif (message['action'] == '424'):
            mysql = mysql_connection()
            connection = mysql['connection']
            cursor = mysql['cursor']

            sale_number = get_sale_number()

            sql = "DELETE carts, cart_products, cart_product_items FROM carts LEFT JOIN cart_products ON carts.id = cart_products.cart_id LEFT JOIN cart_product_items ON cart_products.id = cart_product_items.cart_product_id WHERE carts.sale_number = %s"
            binds = (sale_number)
            delete_data(connection, cursor, sql, binds)

            close_connection(connection, cursor)

            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data"    : []
            }
        elif (message['action'] == '440'):
            mysql = mysql_connection()
            connection = mysql['connection']
            cursor = mysql['cursor']

            sale_number = get_sale_number()

            sql = "SELECT * FROM carts WHERE sale_number = %s"
            binds = (sale_number)
            carts = select_data(connection, cursor, sql, binds)

            cart_id = 0
            if len(carts):
                cart_id = carts[0]['id']

            order = get_cart_data(connection, cursor, cart_id)

            close_connection(connection, cursor)

            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data"    : {
                    "order": order
                }
            }
        elif (message['action'] == '441'):
            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data"    : []
            }
        elif (message['action'] == '442'):
            return False
        # test feedback Active Send Data 402
        elif (message['action'] == '4020'):
            data = {
                "action"      : message['action'],
                "redirect_to" : "0"
            }            
        # test feedback Active Send Data 442
        elif (message['action'] == '4420'):
            # Server do something
            data = {
                "action"  : message['action'],
                "payment" :{
                        "total"  : "560",
                        "paid"   : "500",
                        "unpaid" : "60",
                        "change" : "0"
                }
            }
        # test feedback Active Send Data 443
        elif (message['action'] == '4430'):
            # Server do something
            data = {
                "action"  : message['action'],
            }
        # test feedback Active Send Data 499
        elif (message['action'] == '4990'):
            data = {
                "action"  : message['action'],
                "message" : "系統交班中, 暫時停止服務"
            }
        elif (message['action'] == '530'):
            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data"    : {
                    "raffle_id" : "1",
                    "game_times" : "2",
                    "gifts" : [
                        {
                            "gift_id" : "1",
                            "product_id" : "70",
                            "number" : "9",
                            "quantity" : "1",
                            "title" : "500分",
                            "image" : "a.png"
                        },
                        {
                            "gift_id" : "2",
                            "product_id" : "76",
                            "number" : "4",
                            "quantity" : "1",
                            "title" : "3,000分",
                            "image" : "b.png"
                        },
                        {
                            "gift_id" : "3",
                            "product_id" : "70",
                            "number" : "10",
                            "quantity" : "1",
                            "title" : "500分",
                            "image" : "c.png"
                        },
                        {
                            "gift_id" : "4",
                            "product_id" : "84",
                            "number" : "5",
                            "quantity" : "1",
                            "title" : "2,000分",
                            "image" : "b.png"
                        },
                        {
                            "gift_id" : "5",
                            "product_id" : "85",
                            "number" : "3",
                            "quantity" : "1",
                            "title" : "3,000分",
                            "image" : "b.png"
                        },
                        {
                            "gift_id" : "6",
                            "product_id" : "0",
                            "number" : "16",
                            "quantity" : "0",
                            "title" : "200分",
                            "image" : "b.png"
                        },
                        {
                            "gift_id" : "7",
                            "product_id" : "86",
                            "number" : "1",
                            "quantity" : "1",
                            "title" : "10,000分",
                            "image" : "b.png"
                        },
                        {
                            "gift_id" : "8",
                            "product_id" : "87",
                            "number" : "11",
                            "quantity" : "1",
                            "title" : "500分",
                            "image" : "b.png"
                        },
                        {
                            "gift_id" : "9",
                            "product_id" : "70",
                            "number" : "14",
                            "quantity" : "1",
                            "title" : "200分",
                            "image" : "b.png"
                        },
                        {
                            "gift_id" : "10",
                            "product_id" : "88",
                            "number" : "2",
                            "quantity" : "1",
                            "title" : "5,000分",
                            "image" : "b.png"
                        },
                        {
                            "gift_id" : "11",
                            "product_id" : "70",
                            "number" : "15",
                            "quantity" : "1",
                            "title" : "200分",
                            "image" : "b.png"
                        },
                        {
                            "gift_id" : "12",
                            "product_id" : "89",
                            "number" : "6",
                            "quantity" : "1",
                            "title" : "2,000分",
                            "image" : "b.png"
                        },
                        {
                            "gift_id" : "73",
                            "product_id" : "70",
                            "number" : "8",
                            "quantity" : "1",
                            "title" : "1,000分",
                            "image" : "b.png"
                        },
                        {
                            "gift_id" : "14",
                            "product_id" : "70",
                            "number" : "13",
                            "quantity" : "1",
                            "title" : "200分",
                            "image" : "b.png"
                        },
                        {
                            "gift_id" : "15",
                            "product_id" : "70",
                            "number" : "7",
                            "quantity" : "1",
                            "title" : "1,000分",
                            "image" : "b.png"
                        },
                        {
                            "gift_id" : "16",
                            "product_id" : "70",
                            "number" : "12",
                            "quantity" : "1",
                            "title" : "200分",
                            "image" : "b.png"
                        },
                    ]
                }
            }
        elif (message['action'] == '531'):
            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data"    : {
                    "device_uuid" : None,
                    "raffle_id" : "1",
                    "serial_number" : "202010310004",
                    "gift_id" : "1",
                    "device_gift_assign_id" : "5",
                    "chance_index" : "4",
                    "title" : "代幣 40枚",
                    "quantity" : "1",
                    "token" : "40",
                    "gift_level" : "3",
                    "gift_number" : "0",
                    "datetime" : "2020-10-31 11:19:01",
                    "left" : "1",
                }
            }
        elif (message['action'] == '532'):
            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data"    : []
            }
        elif (message['action'] == '533'):
            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data"    : []
            }
        elif (message['action'] == '010'):
            language_id = message['language_id']
            change_language(language_id)

            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data"    : []
            }
        else:
            data = {
                "success" : False,
                "code"    : 1,
                "message" : "Error message"
            }

        response = json.dumps(data, cls=DecimalEncoder)
        print ("response", response)
        self.write_message(response)

    def on_close(self):   #當連線中斷時，"觸發"
        print("WebSocket closed")

    @classmethod
    def send_message(cls, message):
        removable = set()
        for ws in cls.live_web_sockets:
            if not ws.ws_connection or not ws.ws_connection.stream.socket:
                removable.add(ws)
            else:
                ws.write_message(message)
        for ws in removable:
            cls.live_web_sockets.remove(ws)

# Test : Active Send Data Through URL with parameter
class TestHandler(tornado.web.RequestHandler):
    def get(self):
        # example: http://localhost:8887/test?action=4020

        action = self.get_arguments("action")
        server = tornado.ioloop.IOLoop.current()
        data = {}
        # redirect to page 1
        if action == ['4024']:
            data = {
                "action": "402",
                "redirect_to": "4"
            }
        if action == ['4027']:
            data = {
                "action": "402",
                "redirect_to": "7"
            }               
        if action == ['4028']:
            data = {
                "action": "402",
                "redirect_to": "8"
            }            
        # qrcode success
        if action == ['4050']:
            data = {
                "success" : True,
                "action"  : "405",
                "code"    : 0,
                "message" : "",
                "data"    : []
            }
        # qrcode error
        if action == ['4051']:
            data = {
                "success" : False,
                "action"  : "405",
                "code"    : 1,
                "message" : "找不到訂單",
                "data"    : []
            }
        # keep send Payment
        elif action == ['4420']:
            data = {
                "action":"442",
                "payment":{
                    "total":"1560",
                    "paid":"1500",
                    "unpaid":"60",
                    "change":"0"
                }
            }
        #response complete pay
        elif action == ['4430']:
            data = {
                "action" : "443"
            }
        #response error
        elif action == ['4990']:
            data = {
                "action" : "499",
                "message" : "系統交班中, 暫時停止服務"
            }

        response = json.dumps(data)
        print ("send", response)
        server.add_callback(WebSocketHandler.send_message, response)
        self.set_status(200)
        self.finish()


# mysql connection
def mysql_connection():
    db_settings = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "",
        "db": "tsujirihq_test",
        "charset": "utf8"
    }

    connection = pymysql.connect(**db_settings)
    cursor = connection.cursor()
    return {
        "connection": connection,
        "cursor": cursor
    }

def close_connection(connection, cursor):
    cursor.close()
    connection.close()

def sql_handler(connection, cursor, type, sql, binds = None):
    result = []
    field_name = []
    success = True

    try:
        if type == 'select':
            if binds:
                cursor.execute(sql, binds)
            else:
                cursor.execute(sql)
            result = cursor.fetchall()
            # print(result)
            field_name = [des[0] for des in cursor.description]

        else:
            cursor.execute(sql, binds)
            connection.commit()
            result.append({"id": cursor.lastrowid})
        # 提交到数据库执行
        connection.commit()
    except:
        # 如果发生错误则回滚
        connection.rollback()
        success = False

    return {
        'success': success,
        'type': type,
        'result': result,
        'field_name': field_name
    }

def get_format_data(response):
    result = response['result']
    field_name = response['field_name']
    data = format_data_from_mysql(result, field_name)
    return data

def format_data_from_mysql(result, field_name):
    data = []
    for idx, name in enumerate(result):
        bb = {}
        for key in range(len(name)):
            bb[field_name[key]] = name[key]
        data.append(bb)
    return data

def select_data(connection, cursor, sql, binds = None):
    response = sql_handler(connection, cursor, 'select', sql, binds)
    data = get_format_data(response)
    return data

def insert_data(connection, cursor, sql, binds):
    response = sql_handler(connection, cursor, 'insert', sql, binds)
    id = response['result'][0]['id']
    return id

def update_data(connection, cursor, sql, binds):
    response = sql_handler(connection, cursor, 'update', sql, binds)

def delete_data(connection, cursor, sql, binds):
    response = sql_handler(connection, cursor, 'delete', sql, binds)
# /.mysql connection

# define a function for key
def key_func(k):
    return k['property_id']

# get_cart_data: get cart data by cart_id
def get_cart_data(connection, cursor, cart_id):
    # cart products
    sql = "SELECT carts.id, carts.payment_id, carts.sale_number, carts.sale_total, cart_products.product_id, cart_products.qty AS quantity, cart_products.sub_total, cart_products.sale_price, products.title, products.unit, products.volume, products.order_type, contents.image AS photo, cart_products.id AS cart_product_id FROM carts LEFT JOIN cart_products ON carts.id = cart_products.cart_id LEFT JOIN products ON cart_products.product_id = products.id LEFT JOIN contents on products.id = contents.source_id AND contents.type = 4 AND contents.language_id = 26 WHERE carts.id = %s ORDER BY cart_product_id DESC"
    binds = (cart_id)
    cart_products = select_data(connection, cursor, sql, binds)

    order = {
        "order_id": cart_id,
        "sale_number": '',
        "order_total": 0,
        "payment_id": 0,
        "products": [],
    }

    if len(cart_products):
        order["sale_number"] = cart_products[0]['sale_number']
        order["order_total"] = cart_products[0]['sale_total']
        order["payment_id"] = cart_products[0]['payment_id']

        for cart_product in cart_products:
            if cart_product['cart_product_id']:
                product = {
                    "id": cart_product['cart_product_id'],
                    "product_id": cart_product['product_id'],
                    "product_title": cart_product['title'],
                    "quantity": cart_product['quantity'],
                    "sale_price": cart_product['sale_price'],
                    "sub_total": cart_product['quantity'] * cart_product['sub_total'],
                    "photo": cart_product['photo'],
                    "remark": "",
                    "unit": cart_product['unit'],
                    "volume": cart_product['volume'],
                    "order_type": cart_product['order_type'],
                    "properties": [],
                    "categories": []
                }

                # properties
                sql = """
                    SELECT
                        cart_product_items.property_id, property_content.`name` AS property_title, property_content.image AS property_photo, cart_product_items.item_id, property_item_content.`name` AS item_title, cart_product_items.qty AS quantity, cart_product_items.sale_price, cart_product_items.sub_total, property_item_content.image AS item_photo
                    FROM
                        cart_product_items
                        LEFT JOIN categories AS property ON cart_product_items.property_id = property.id
                        LEFT JOIN contents AS property_content ON property.id = property_content.source_id AND property_content.type = 1 AND property_content.language_id = 26 
                        LEFT JOIN categories AS property_item ON cart_product_items.item_id = property_item.id
                        LEFT JOIN contents AS property_item_content ON property_item.id = property_item_content.source_id AND property_item_content.type = 2 AND property_item_content.language_id = 26
                    WHERE
                        cart_product_items.cart_product_id = %s"""
                binds = (cart_product['cart_product_id'])
                property_items = select_data(connection, cursor, sql, binds)

                product_remark = []
                if len(property_items):
                    # sort by property_id
                    property_items = sorted(property_items, key=key_func)

                    for key, value in groupby(property_items, key_func):
                        property_item_list = list(value)
                        property = {
                            "id": property_item_list[0]['property_id'],
                            "title": property_item_list[0]['property_title'],
                            "photo": property_item_list[0]['property_photo'],
                            "items":[]
                        }

                        for property_item in property_item_list:
                            item = {
                                "id": property_item['item_id'], "title": property_item['item_title'], "quantity": property_item['quantity'],
                                "sale_price": property_item['sale_price'], "sub_total": property_item['sub_total'], "photo": property_item['item_photo']
                            }
                            remark = property_item['item_title']
                            product_remark.append(remark)

                            property['items'].append(item)
                        product["properties"].append(property)

                product["remark"] = ','.join(str(x) for x in product_remark)

                # categories
                sql = "SELECT categories.id, contents.name AS title, categories.private, contents.image AS photo FROM categories LEFT JOIN contents ON categories.id = contents.source_id AND contents.type = 3 AND contents.language_id = 26 WHERE EXISTS (SELECT * FROM product_categories WHERE product_categories.category_id = categories.id AND product_categories.product_id = %s)"
                binds = (cart_product['product_id'])
                categories = select_data(connection, cursor, sql, binds)
                product["categories"] = categories
                order['products'].append(product)

    return order
# /.get_cart_data

# update carts sale_total
def update_carts_sale_total(connection, cursor, cart_id):
    # select all cart product data
    sql = "SELECT * FROM cart_products WHERE cart_id = %s"
    binds = (cart_id)
    cart_products = select_data(connection, cursor, sql, binds)

    sale_total = 0
    for cart_product in cart_products:
        sale_total += decimal.Decimal(cart_product['sub_total']) * cart_product['qty']

    # update `carts` sale_total
    sql = "UPDATE carts SET sale_total = %s WHERE id = %s"
    binds = (sale_total, cart_id)
    update_data(connection, cursor, sql, binds)
# /.update carts sale_total

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)

# sale_number
def gen_sale_number():
    date = time.strftime("%Y%m%d", time.localtime())
    return date + "00001"

def get_sale_number(config = None):
    if (config == None):
        config = get_config()
    return config['sale_number']
# /.sale_number

# config
def get_config_path():
    return "C:\www\\food_dev\\templates\\default\config.json"

def get_config():
    file_path = get_config_path()
    sale_number = gen_sale_number()
    config = {
        "language": { "id": 1, "code": "en" },
        "sale_number": sale_number,
        "category_id": 171
    }

    try:
        data = Path(file_path).read_text()
        config = json.loads(data)
    except:
        print('file doesn\'t exist')
        # Path(file_path).touch(exist_ok=True)
        data = json.dumps(config)
        Path(file_path).write_text(data)

    return config

def get_category_id(config = None):
    if (config == None):
        config = get_config()
    return config['category_id']

def change_category_id(category_id):
    config = get_config()
    file_path = get_config_path()
    config['category_id'] = category_id
    data = json.dumps(config)
    Path(file_path).write_text(data)

def get_language(config = None):
    if (config == None):
        config = get_config()
    return config['language']

def change_language(language_id):
    config = get_config()
    language_id = str(language_id)
    language = get_language(config)
    if language_id == '1':
        language['id'] = 1
        language['code'] = 'en'
    else:
        language['id'] = 2
        language['code'] = 'zh-TW'

    file_path = get_config_path()
    config['language'] = language
    data = json.dumps(config)
    Path(file_path).write_text(data)
# /.config

def my_app():  #url對映
    return tornado.web.Application([
        (r"/test", TestHandler),
        # (r"/image/jpg/(.*)",tornado.web.StaticFileHandler,{"path": "assets/img"}),
        (r"/", WebSocketHandler),
    ])

def main():
    global port
    port = 8888

    app = my_app()
    app.listen(port)
    print("歡迎使用tornado，您的連線port為:{0} ".format(port))
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()