import tornado.ioloop
import tornado.web
import tornado.websocket
import json
from websocketData import Tsujiri

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
        if (message['event']== 'request:ping' ):
            data = {
                    'event' : 'response:ping',
                    'success' : True,
                    'code' : 0,
                    'message' : "",
                    'data'  : {}
            }
        elif (message['action'] == '7000'):
            data = {
                "event" : "response:api",
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "init",
                "data"    : {
                    "init":"success"
                }
            }
        elif (message['action'] == '0101'):
            data = {
                "event" : "response:api",
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "Login failed.",
                "data"    : {
                    "id" : 12,
                    "name" : "Eddie"
                }
            }
        elif (message['action'] == '0102'):
            data = {
                "event" : "response:api",
                "success": True,
                "action"  : message['action'],
                "code":0,  
                "message":"No machine found",  
                "data": {
                    "pcbs":[ 
                        {
                            "id":1,
                            "title":"SLOT"
                        },
                        {
                            "id":2,
                            "title":"EAGLE"
                        },
                        {
                            "id":3, 
                            "title":"ARISTOCRAT"
                        }
                    ]
                }
            }
        elif (message['action'] == '0103'):
            if(message['data']['current_page'] == 0):
                data = {
                    "event" : "response:api",
                    "action":message['action'],
                    "success":True,
                    "code":0,
                    "message":"No matching records found.",
                    "data":{
                        "pagination":{ 
                            # "current_page":"0",
                            # "max_page":"0",
                            # "page_count":"15",
                            # "record_count":"0"
                            "current_page":"0",
                            "max_page":"2",
                            "page_count":"15",
                            "record_count":"100"
                        },
                        "machines":[ 
                            {
                                "id":1,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":None,
                                # // 以下欄位 有配對才有資料
                                "device_id":1,
                                "device_uuid":"47656a73-fd0d-4cf0-8bf3-0b5ac4990661",
                                "device_title":"TS-001",
                                "device_serial":"TS-001",
                                "connect_status":1
                            },
                            {
                                "id":2,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":2, 
                            },
                            {
                                "id":4,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":4,
                                # // 以下欄位 有配對才有資料
                                "device_id":8,
                                "device_uuid":"47656a73-fd0d-4cf0-8bf3-0b5ac4990661",
                                "device_title":"TS-008",
                                "device_serial":"TS-008",
                                "connect_status":0
                            },
                            {
                                "id":7,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":7, 
                                "device_id":13, 
                                "device_uuid":"5d8fff31-f818-40ba-a7b1-b51476c10b13",
                                "device_title":"TS-013",
                                "device_serial":"TS-013",
                                "connect_status":1
                            },
                            {
                                "id":12,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":12,
                                # // 以下欄位 有配對才有資料
                                "device_id":18,
                                "device_uuid":"47656a73-fd0d-4cf0-8bf3-0b5ac4990661",
                                "device_title":"TS-018",
                                "device_serial":"TS-018",
                                "connect_status":0
                            },
                            {
                                "id":19,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":19, 
                            },
                            {
                                "id":23,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":23,
                                # // 以下欄位 有配對才有資料
                                "device_id":34,
                                "device_uuid":"47656a73-fd0d-4cf0-8bf3-0b5ac4990661",
                                "device_title":"TS-034",
                                "device_serial":"TS-034",
                                "connect_status":1
                            },
                            {
                                "id":28,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":28, 
                            },
                            {
                                "id":31,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":31,
                                # // 以下欄位 有配對才有資料
                                "device_id":41,
                                "device_uuid":"47656a73-fd0d-4cf0-8bf3-0b5ac4990661",
                                "device_title":"TS-041",
                                "device_serial":"TS-041",
                                "connect_status":0
                            },
                            {
                                "id":36,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":36, 
                                "device_id":43, 
                                "device_uuid":"5d8fff31-f818-40ba-a7b1-b51476c10b13",
                                "device_title":"TS-043",
                                "device_serial":"TS-043",
                                "connect_status":1
                            },
                            {
                                "id":47,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":47,
                            },
                            {
                                "id":52,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":52, 
                                "device_id":66, 
                                "device_uuid":"5d8fff31-f818-40ba-a7b1-b51476c10b13",
                                "device_title":"TS-066",
                                "device_serial":"TS-066",
                                "connect_status":1
                            },
                            {
                                "id":55,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":55,
                                # // 以下欄位 有配對才有資料
                                "device_id":68,
                                "device_uuid":"47656a73-fd0d-4cf0-8bf3-0b5ac4990661",
                                "device_title":"TS-068",
                                "device_serial":"TS-068",
                                "connect_status":0
                            },
                            {
                                "id":59,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":59, 
                                "device_id":71, 
                                "device_uuid":"5d8fff31-f818-40ba-a7b1-b51476c10b13",
                                "device_title":"TS-071",
                                "device_serial":"TS-071",
                                "connect_status":1
                            },
                            {
                                "id":62,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":62,
                            }
                        ]
                    }
                }
            if(message['data']['current_page'] == 1):
                data={
                    "event" : "response:api",
                    "action":message['action'],
                    "success":True,
                    "code":0,
                    "message":"No matching records found.",
                    "data":{
                        "pagination":{ 
                            "current_page":"1",
                            "max_page":"2",
                            "page_count":"15",
                            "record_count":"100"
                        },
                        "machines":[ 
                            {
                                "id":2,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":2,
                                # // 以下欄位 有配對才有資料
                                "device_id":2,
                                "device_uuid":"47656a73-fd0d-4cf0-8bf3-0b5ac4990661",
                                "device_title":"TS-002",
                                "device_serial":"TS-002",
                                "connect_status":1
                            },
                            {
                                "id":2,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":2, 
                            },
                            {
                                "id":4,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":4,
                                # // 以下欄位 有配對才有資料
                                "device_id":8,
                                "device_uuid":"47656a73-fd0d-4cf0-8bf3-0b5ac4990661",
                                "device_title":"TS-008",
                                "device_serial":"TS-008",
                                "connect_status":0
                            },
                            {
                                "id":7,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":7, 
                                "device_id":13, 
                                "device_uuid":"5d8fff31-f818-40ba-a7b1-b51476c10b13",
                                "device_title":"TS-013",
                                "device_serial":"TS-013",
                                "connect_status":1
                            },
                            {
                                "id":12,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":12,
                                # // 以下欄位 有配對才有資料
                                "device_id":18,
                                "device_uuid":"47656a73-fd0d-4cf0-8bf3-0b5ac4990661",
                                "device_title":"TS-018",
                                "device_serial":"TS-018",
                                "connect_status":0
                            },
                            {
                                "id":19,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":19, 
                            },
                            {
                                "id":23,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":23,
                                # // 以下欄位 有配對才有資料
                                "device_id":34,
                                "device_uuid":"47656a73-fd0d-4cf0-8bf3-0b5ac4990661",
                                "device_title":"TS-034",
                                "device_serial":"TS-034",
                                "connect_status":0
                            },
                            {
                                "id":28,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":28, 
                            },
                            {
                                "id":31,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":31,
                                # // 以下欄位 有配對才有資料
                                "device_id":41,
                                "device_uuid":"47656a73-fd0d-4cf0-8bf3-0b5ac4990661",
                                "device_title":"TS-041",
                                "device_serial":"TS-041",
                                "connect_status":0
                            },
                            {
                                "id":36,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":36, 
                                "device_id":43, 
                                "device_uuid":"5d8fff31-f818-40ba-a7b1-b51476c10b13",
                                "device_title":"TS-043",
                                "device_serial":"TS-043",
                                "connect_status":1
                            },
                            {
                                "id":47,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":47,
                            },
                            {
                                "id":52,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":52, 
                                "device_id":66, 
                                "device_uuid":"5d8fff31-f818-40ba-a7b1-b51476c10b13",
                                "device_title":"TS-066",
                                "device_serial":"TS-066",
                                "connect_status":1
                            },
                            {
                                "id":55,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":55,
                                # // 以下欄位 有配對才有資料
                                "device_id":68,
                                "device_uuid":"47656a73-fd0d-4cf0-8bf3-0b5ac4990661",
                                "device_title":"TS-068",
                                "device_serial":"TS-068",
                                "connect_status":0
                            },
                            {
                                "id":59,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":59, 
                                "device_id":71, 
                                "device_uuid":"5d8fff31-f818-40ba-a7b1-b51476c10b13",
                                "device_title":"TS-071",
                                "device_serial":"TS-071",
                                "connect_status":1
                            },
                            {
                                "id":62,
                                "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title":"打地鼠",
                                "serial_number":"",
                                "station_no":62,
                            }
                        ]
                    }
                }
            if(message['data']['pcb_id'] == '2'):
                data = {
                    "event" : "response:api",
                    "success": True,
                    "action"  : message['action'],
                    "code":0,  
                    "message":"No Tasi found",  
                    "data": {
                        "pagination":{ 
                            "current_page":"0",
                            "max_page":"0",
                            "page_count":"15",
                            "record_count":"0"
                        },
                        "machines": []
                    }
                }
        elif (message['action'] == '0104'):
            if(message['data']['current_page'] == 0):
                data = {
                    "event" : "response:api",
                    "success": True,
                    "action"  : message['action'],
                    "code":0,
                    "message":"No Tasi found",
                    "data": {
                        "pagination":{
                            "current_page":"0",
                            "max_page":"2",
                            "page_count":"15",
                            "record_count":"100"
                        },
                        "devices": [
                            {
                                "id": 1,
                                "uuid": "47656a73-fd0d-4cf0-8bf3-0b5ac4990661",
                                "title": "TS-001",
                                "serial_number": "TS-001",
                                "machine_id": 1,
                                "machine_uuid": "f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title": "打地鼠",
                                "machine_serial": "",
                                "station_no": None,
                                "connect_status":1
                            },
                            {
                                "id": 2,
                                "uuid": "5d8fff31-f818-40ba-a7b1-b51476c10b13",
                                "title": "TS-002",
                                "serial_number": "TS-002",
                            },
                            {
                                "id": 6,
                                "uuid": "5d8fff31-f818-40ba-a7b1-b51476c10b13",
                                "title": "TS-006",
                                "serial_number": "TS-006",
                                "machine_id": 6,
                                "machine_uuid": "f653089d-8b85-4cf5-a685-d16f6f6c3bc6",
                                "machine_title": "打地鼠",
                                "machine_serial": "",
                                "station_no": 6,
                                "connect_status":1
                            },
                            {
                                "id": 8,
                                "uuid": "5d8fff31-f818-40ba-a7b1-b51476c10b13",
                                "title": "TS-008",
                                "serial_number": "TS-008",
                                "machine_id": 8,
                                "machine_uuid": "f853089d-8b85-4cf5-a685-d16f6f8c3bc8",
                                "machine_title": "打地鼠",
                                "machine_serial": "",
                                "station_no": 8,
                                "connect_status":1
                            },
                            {
                                "id": 1,
                                "uuid": "47656a73-fd0d-4cf0-8bf3-0b5ac4990661",
                                "title": "TS-001",
                                "serial_number": "TS-001",
                                "machine_id": 1,
                                "machine_uuid": "f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title": "打地鼠",
                                "machine_serial": "",
                                "station_no": 1,
                                "connect_status":1
                            },
                            {
                                "id": 2,
                                "uuid": "5d8fff31-f818-40ba-a7b1-b51476c10b13",
                                "title": "TS-002",
                                "serial_number": "TS-002",
                            },
                            {
                                "id": 6,
                                "uuid": "5d8fff31-f818-40ba-a7b1-b51476c10b13",
                                "title": "TS-006",
                                "serial_number": "TS-006",
                                "machine_id": 6,
                                "machine_uuid": "f653089d-8b85-4cf5-a685-d16f6f6c3bc6",
                                "machine_title": "打地鼠",
                                "machine_serial": "",
                                "station_no": 6,
                                "connect_status":1
                            },
                            {
                                "id": 8,
                                "uuid": "5d8fff31-f818-40ba-a7b1-b51476c10b13",
                                "title": "TS-008",
                                "serial_number": "TS-008",
                                "machine_id": 8,
                                "machine_uuid": "f853089d-8b85-4cf5-a685-d16f6f8c3bc8",
                                "machine_title": "打地鼠",
                                "machine_serial": "",
                                "station_no": 8,
                                "connect_status":1
                            },
                            {
                                "id": 1,
                                "uuid": "47656a73-fd0d-4cf0-8bf3-0b5ac4990661",
                                "title": "TS-001",
                                "serial_number": "TS-001",
                                "machine_id": 1,
                                "machine_uuid": "f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                                "machine_title": "打地鼠",
                                "machine_serial": "",
                                "station_no": 1,
                                "connect_status":1
                            },
                            {
                                "id": 2,
                                "uuid": "5d8fff31-f818-40ba-a7b1-b51476c10b13",
                                "title": "TS-002",
                                "serial_number": "TS-002",
                            },
                            {
                                "id": 6,
                                "uuid": "5d8fff31-f818-40ba-a7b1-b51476c10b13",
                                "title": "TS-006",
                                "serial_number": "TS-006",
                                "machine_id": 6,
                                "machine_uuid": "f653089d-8b85-4cf5-a685-d16f6f6c3bc6",
                                "machine_title": "打地鼠",
                                "machine_serial": "",
                                "station_no": 6,
                                "connect_status":1
                            },
                            {
                                "id": 8,
                                "uuid": "5d8fff31-f818-40ba-a7b1-b51476c10b13",
                                "title": "TS-008",
                                "serial_number": "TS-008",
                                "machine_id": 8,
                                "machine_uuid": "f853089d-8b85-4cf5-a685-d16f6f8c3bc8",
                                "machine_title": "打地鼠",
                                "machine_serial": "",
                                "station_no": 8,
                                "connect_status":1
                            }
                        ]
                    }
                }
            if(message['data']['current_page'] == 1):
                data = {
                "event" : "response:api",
                "success": True,
                "action"  : message['action'],
                "code":0,  
                "message":"No Tasi found",  
                "data": {
                    "pagination":{ 
                        "current_page":"1",
                        "max_page":"2",
                        "page_count":"15",
                        "record_count":"100"
                    },
                    "devices": [
                        {
                            "id": 2,
                            "uuid": "47656a73-fd0d-4cf0-8bf3-0b5ac4990661",
                            "title": "TS-002",
                            "serial_number": "TS-002",
                            "machine_id": 3,
                            "machine_uuid": "f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                            "machine_title": "打地鼠",
                            "machine_serial": "",
                            "station_no": 3,
                            "connect_status":1
                        },
                        {
                            "id": 2,
                            "uuid": "5d8fff31-f818-40ba-a7b1-b51476c10b13",
                            "title": "TS-002",
                            "serial_number": "TS-002",
                        },
                        {
                            "id": 6,
                            "uuid": "5d8fff31-f818-40ba-a7b1-b51476c10b13",
                            "title": "TS-006",
                            "serial_number": "TS-006",
                            "machine_id": 6,
                            "machine_uuid": "f653089d-8b85-4cf5-a685-d16f6f6c3bc6",
                            "machine_title": "打地鼠",
                            "machine_serial": "",
                            "station_no": 6,
                            "connect_status":1
                        },
                        {
                            "id": 8,
                            "uuid": "5d8fff31-f818-40ba-a7b1-b51476c10b13",
                            "title": "TS-008",
                            "serial_number": "TS-008",
                            "machine_id": 8,
                            "machine_uuid": "f853089d-8b85-4cf5-a685-d16f6f8c3bc8",
                            "machine_title": "打地鼠",
                            "machine_serial": "",
                            "station_no": 8,
                            "connect_status":1
                        },
                        {
                            "id": 1,
                            "uuid": "47656a73-fd0d-4cf0-8bf3-0b5ac4990661",
                            "title": "TS-001",
                            "serial_number": "TS-001",
                            "machine_id": 1,
                            "machine_uuid": "f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                            "machine_title": "打地鼠",
                            "machine_serial": "",
                            "station_no": 1,
                            "connect_status":1
                        },
                        {
                            "id": 2,
                            "uuid": "5d8fff31-f818-40ba-a7b1-b51476c10b13",
                            "title": "TS-002",
                            "serial_number": "TS-002",
                        },
                        {
                            "id": 6,
                            "uuid": "5d8fff31-f818-40ba-a7b1-b51476c10b13",
                            "title": "TS-006",
                            "serial_number": "TS-006",
                            "machine_id": 6,
                            "machine_uuid": "f653089d-8b85-4cf5-a685-d16f6f6c3bc6",
                            "machine_title": "打地鼠",
                            "machine_serial": "",
                            "station_no": 6,
                            "connect_status":1
                        },
                        {
                            "id": 8,
                            "uuid": "5d8fff31-f818-40ba-a7b1-b51476c10b13",
                            "title": "TS-008",
                            "serial_number": "TS-008",
                            "machine_id": 8,
                            "machine_uuid": "f853089d-8b85-4cf5-a685-d16f6f8c3bc8",
                            "machine_title": "打地鼠",
                            "machine_serial": "",
                            "station_no": 8,
                            "connect_status":1
                        },
                        {
                            "id": 1,
                            "uuid": "47656a73-fd0d-4cf0-8bf3-0b5ac4990661",
                            "title": "TS-001",
                            "serial_number": "TS-001",
                            "machine_id": 1,
                            "machine_uuid": "f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                            "machine_title": "打地鼠",
                            "machine_serial": "",
                            "station_no": 1,
                            "connect_status":1
                        },
                        {
                            "id": 2,
                            "uuid": "5d8fff31-f818-40ba-a7b1-b51476c10b13",
                            "title": "TS-002",
                            "serial_number": "TS-002",
                        },
                        {
                            "id": 6,
                            "uuid": "5d8fff31-f818-40ba-a7b1-b51476c10b13",
                            "title": "TS-006",
                            "serial_number": "TS-006",
                            "machine_id": 6,
                            "machine_uuid": "f653089d-8b85-4cf5-a685-d16f6f6c3bc6",
                            "machine_title": "打地鼠",
                            "machine_serial": "",
                            "station_no": 6,
                            "connect_status":1
                        },
                        {
                            "id": 8,
                            "uuid": "5d8fff31-f818-40ba-a7b1-b51476c10b13",
                            "title": "TS-008",
                            "serial_number": "TS-008",
                            "machine_id": 8,
                            "machine_uuid": "f853089d-8b85-4cf5-a685-d16f6f8c3bc8",
                            "machine_title": "打地鼠",
                            "machine_serial": "",
                            "station_no": 8,
                            "connect_status":1
                        }
                    ]
                }
            }
            if(message['data']['current_page'] >= 2):
                data = {
                    "event" : "response:api",
                    "success": True,
                    "action"  : message['action'],
                    "code":0,  
                    "message":"No Tasi found",  
                    "data": {
                        "pagination":{ 
                            "current_page":"2",
                            "max_page":"2",
                            "page_count":"15",
                            "record_count":"100"
                        },
                        "devices": []
                    }
                }
        elif (message['action'] == '0105'):
            data = {
                "event" : "response:api",
                "success": True,
                "action"  : message['action'],
                "code":0,  
                "message":"No matching records found.",  
                "data": {
                    "devices":[
                        {
                            "id":1,
                            "uuid":"47656a73-fd0d-4cf0-8bf3-0b5ac4990661",
                            "title":"TS-001",
                            "serial_number":"TS-001",
                            "machine_id":1,
                            "machine_uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                            "machine_title":"打地鼠",
                            "machine_serial":"",
                            "station_no":1,
                            "connect_status":1
                        },
                        {
                            "id":2,
                            "uuid":"5d8fff31-f818-40ba-a7b1-b51476c10b13",
                            "title":"TS-002", 
                            "serial_number":"TS-002",
                            "machine_id":2,
                            "machine_uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                            "machine_title":"打地鼠",
                            "machine_serial":"",
                            "station_no":2,
                            "connect_status":0
                        },
                        {
                            "id":3,
                            "uuid":"5d8fff31-f818-40ba-a7b1-b51476c10b13",
                            "title":"TS-003", 
                            "serial_number":"TS-003",
                            "machine_id":7,
                            "machine_uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                            "machine_title":"打地鼠",
                            "machine_serial":"",
                            "station_no":7,
                            "connect_status":0
                        }
                    ]
                }
            }
        elif (message['action'] == '0106'):
            data = {
                "event" : "response:api",
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "Pair failed.",
                "data": {
                    "machine":{
                        "id":1,
                        "uuid":"f253089d-8b85-4cf5-a685-d16f6f2c3bc2",
                        "machine_title":"打地鼠",
                        "serial_number":"",
                        "station_no":1,
                        "device_id":25,
                        "device_uuid":"47656a73-fd0d-4cf0-8bf3-0b5ac4990661",
                        "device_title":"TS-025",
                        "device_serial":"TS-025"
                    },
                    "machine_stations":{
                        "id":10,
                        "machine_id":1,
                        "station_no":1,
                        "device_id":1,
                        "online":1
                    }
                }
            }
        elif (message['action'] == '0107'):
            data = {
                "event" : "response:api",
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "No parameter found",
                "data": {
                    "parameters":[
                        {
                            "id":1,
                            "title":"Debounce Time",
                            "options":[
                                {
                                    "id":11,
                                    "title":"1 Bytes",
                                    "value":1,
                                    "default":1
                                },
                                {
                                    "id":12, 
                                    "title":"2 Bytes", 
                                    "value":2, 
                                    "default":0 
                                }
                            ]
                        },
                        {
                            "id":2, 
                            "title":"Transmission Delay Time", 
                            "options":[
                                {
                                    "id":21, 
                                    "title":"1 Bytes",
                                    "value":1,
                                    "default":1
                                },
                                {
                                    "id":22,  
                                    "title":"2 Bytes", 
                                    "value":2, 
                                    "default":0 
                                }
                            ]
                        }
                    ],
                    "reader_parameters":[
                        # {
                        #     "parameter_id":1,
                        #     "option_id":11
                        # },
                        # {
                        #     "parameter_id":2, 
                        #     "option_id":22 
                        # }
                    ]
                } 
            }
        elif (message['action'] == '0108'):
            data = {
                "event" : "response:api",
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "parameter change failed",
                "data": message['data']
            }
        elif (message['action'] == '0109'):
            data = {
                "event" : "response:api",
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "Default failed.",
                "data": {
                    "parameters":[
                        {
                            "id":1,
                            "title":"Debounce Time",
                            "options":[
                                {
                                    "id":11,
                                    "title":"1 Bytes",
                                    "value":1,
                                    "default":1
                                },
                                {
                                    "id":12, 
                                    "title":"2 Bytes", 
                                    "value":2, 
                                    "default":0
                                }
                            ]
                        },
                        {
                            "id":2, 
                            "title":"Transmission Delay Time", 
                            "options":[
                                {
                                    "id":21, 
                                    "title":"1 Bytes",
                                    "value":1,
                                    "default":1
                                },
                                {
                                    "id":22,  
                                    "title":"2 Bytes", 
                                    "value":2, 
                                    "default":0
                                }
                            ]
                        }
                    ],
                }
            }
        elif (message['action'] == '0110'):
            data = {
                "event" : "response:api",
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "Switch mode failed.",
                "data": {}
            }
        elif (message['action'] == '0111'):
            data = {
                "event" : "response:api",
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "Error Message.",
                "data": {
                    "machine_id":1,
                    "station_no":1,
                    "tasi_id":1,
                    "tasi_number":"TS-001",
                    "mode":2
                }
            }
        elif (message['action'] == '0112'):
            data = {
                "event" : "response:api",
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "Restart failed",
                "data": {}
            }
        elif (message['action'] == '400'):
            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data": {
                    "language_id":1,
                    "language_code":"en",
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
            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data" : {
                    "categories":[
                        {
                            "id":182,
                            "title":"Tea",
                            "photo":"1.png"
                        },
                        {
                            "id":171,
                            "title":"O-Matcha",
                            "photo":"1.png"
                        },
                        {
                            "id":183,
                            "title":"Ice Blended",
                            "photo":"2.png"
                        },
                        {
                            "id":184,
                            "title":"Latte",
                            "photo":"3.png"
                        },
                        {
                            "id":185,
                            "title":"Float",
                            "photo":"3.png"
                        },
                        {
                            "id":186,
                            "title":"Soft Ice Cream",
                            "photo":"3.png"
                        },
                        {
                            "id":187,
                            "title":"Sundae",
                            "photo":"3.png"
                        },
                        {
                            "id":188,
                            "title":"Shaved Ice",
                            "photo":"3.png"
                        },
                    ],
                    "products":[
                        {
                            "id":"27",
                            "title":"Sencha",
                            "price" : 115,
                            "photo":"1_20201808105300000.png"
                        },
                        {
                            "id":"28",
                            "title":"Genmaicha",
                            "price" : 115,
                            "photo":"1_20201808105419000.png"
                        },
                        {
                            "id":"29",
                            "title":"Yuzu Citron Tea",
                            "price" : 130,
                            "photo":"1_20201808105720000.png"
                        },
                        {
                            "id":"30",
                            "title":"Yuzu Sencha",
                            "price" : 130,
                            "photo":"1_20201808105818000.png"
                        },
                        {
                            "id":"31",
                            "title":"Yuzu Houjicha",
                            "price" : 130,
                            "photo":"1_20201808111700000.png"
                        },
                        {
                            "id":"66",
                            "title":"Houjicha",
                            "price" : 115,
                            "photo":"1_20202008155411000.png"
                        },
                    ]
                }
            }
        elif (message['action'] == '412'):
            product = {}
            product[182] = [
                { "id":"27", "title":"Sencha", "photo":"1_20201808105300000.png", "price":"115", "volume":None, 'unit':None },
                { "id":"28", "title":"Genmaicha", "photo":"1_20201808105419000.png", "price":"115", "volume":None, 'unit':None },
                { "id":"29", "title":"Yuzu Citron Tea", "photo":"1_20201808105720000.png", "price":"130", "volume":None, 'unit':None },
                { "id":"30", "title":"Yuzu Sencha", "photo":"1_20201808105818000.png", "price":"130", "volume":None, 'unit':None },
                { "id":"31", "title":"Yuzu Houjicha", "photo":"1_20201808111700000.png", "price":"130", "volume":None, 'unit':None },
                { "id":"66", "title":"Houjicha", "photo":"1_20202008155411000.png", "price":"115", "volume":None, 'unit':None },
            ]

            product[171] = [
                { "id":"26", "title":"Yuzu O-Matcha", "photo":"1_20201808100017000.png", "price":"145", "volume":None, 'unit':None },
                { "id":"64", "title":"O-Matcha", "photo":"1_20202008155144000.png", "price":"130", "volume":None, 'unit':None },
                { "id":"65", "title":"O-Matcha Cappuccino", "photo":"1_20202008155255000.png", "price":"140", "volume":None, 'unit':None },
            ]

            product[183] = [
                { "id":"40", "title":"TSUJIRI Ice Blended", "photo":"1_20201808150733000.png", "price":"155", "volume":None, 'unit':None },
                { "id":"41", "title":"TSUJIRI Milk", "photo":"1_20201808150838000.png", "price":"170", "volume":None, 'unit':None },
                { "id":"42", "title":"Houjicha", "photo":"1_20201808151048000.png", "price":"150", "volume":None, 'unit':None },
                { "id":"43", "title":"Houjicha Milk", "photo":"1_20201808151309000.png", "price":"165", "volume":None, 'unit':None },
                { "id":"44", "title":"Yuzu Citron", "photo":"1_20201808151359000.png", "price":"165", "volume":None, 'unit':None },
                { "id":"45", "title":"Red Bean", "photo":"1_20201808153015000.png", "price":"160", "volume":None, 'unit':None },
                { "id":"46", "title":"Chocolate", "photo":"1_20201808153113000.png", "price":"160", "volume":None, 'unit':None },
            ]

            product[184] = [
                { "id":"32", "title":"TSUJIRI", "photo":"1_20201808111819000.png", "price":"155", "volume":None, 'unit':None },
                { "id":"33", "title":"TSUJIRI + Kinako Kuromitsu", "photo":"1_20201808111916000.png", "price":"165", "volume":None, 'unit':None },
                { "id":"34", "title":"TSUJIRI + Whipped Cream", "photo":"1_20201808112017000.png", "price":"170", "volume":None, 'unit':None },
                { "id":"35", "title":"Houjicha + Whipped Cream", "photo":"1_20201808112111000.png", "price":"160", "volume":None, 'unit':None },
                { "id":"36", "title":"Houjicha", "photo":"1_20201808150301000.png", "price":"145", "volume":None, 'unit':None },
                { "id":"37", "title":"Chocolate", "photo":"1_20201808150427000.png", "price":"140", "volume":None, 'unit':None },
                { "id":"38", "title":"Chocolate + Whipped Cream", "photo":"1_20201808150540000.png", "price":"155", "volume":None, 'unit':None },
                { "id":"39", "title":"Chocolate + O-Matcha", "photo":"1_20201808150643000.png", "price":"175", "volume":None, 'unit':None },
                # { "id":"64", "title":"O-Matcha", "photo":"1_20202008155144000.png", "price":"130", "volume":None, 'unit':None },
            ]

            product[185] = [
                { "id":"47", "title":"TSUJIRI Float", "photo":"1_20201808153201000.png", "price":"170", "volume":None, 'unit':None },
                { "id":"48", "title":"TSUJIRI Milk", "photo":"1_20201808153253000.png", "price":"185", "volume":None, 'unit':None },
                { "id":"49", "title":"Houjicha", "photo":"1_20201808153346000.png", "price":"160", "volume":None, 'unit':None },
                { "id":"50", "title":"Houjicha Milk", "photo":"1_20201808153526000.png", "price":"175", "volume":None, 'unit':None },
                { "id":"51", "title":"Yuzu Citron", "photo":"1_20201808153612000.png", "price":"180", "volume":None, 'unit':None },
                { "id":"52", "title":"Red Bean", "photo":"1_20201808153702000.png", "price":"170", "volume":None, 'unit':None },
                { "id":"53", "title":"Chocolate", "photo":"1_20201808153807000.png", "price":"170", "volume":None, 'unit':None },
            ]

            product[186] = [
                { "id":"68", "title":"TSUJIRI O-Matcha Soft Ice Cream", "photo":"1_20202008155702000.png", "price":"150", "volume":None, 'unit':None },
                { "id":"69", "title":"TSUJIRI Vanilla Soft Ice Cream", "photo":"1_20202008155747000.png", "price":"110", "volume":None, 'unit':None },
            ]

            product[187] = [
                { "id":"58", "title":"Shiratama Sundae", "photo":"1_20201808154743000.png", "price":"225", "volume":None, 'unit':None },
                { "id":"59", "title":"Chiffon Cake Parfait Sundae", "photo":"1_20201808154922000.png", "price":"225", "volume":None, 'unit':None },
            ]

            product[188] = [
                { "id":"60", "title":"TSUJIRI Shaved Ice", "photo":"1_20201808155029000.png", "price":"275", "volume":None, 'unit':None },
                { "id":"61", "title":"Uji Kintoki", "photo":"1_20201808155257000.png", "price":"200", "volume":None, 'unit':None },
                { "id":"62", "title":"Uji Sunrise", "photo":"1_20201808155340000.png", "price":"275", "volume":None, 'unit':None },
                { "id":"63", "title":"Yuzu Citron Shaved Ice", "photo":"1_20201808155439000.png", "price":"220", "volume":None, 'unit':None },
                { "id":"67", "title":"Uji Sunset", "photo":"1_20202008155550000.png", "price":"275", "volume":None, 'unit':None },
            ]

            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data"    : {
                    "products":product[message['category_id']]
                }
            }

            # if (message['category_id'] == 1):
            #     data = {
            #         "success" : True,
            #         "action"  : message['action'],
            #         "code"    : 0,
            #         "message" : "",
            #         "data"    : {
            #             "products":[
            #                 {
            #                     "id":"1",
            #                     "title":"商品一",
            #                     "photo":"1_20201808105300000.png",
            #                     "price":"10"
            #                 },
            #                 {
            #                     "id":"2",
            #                     "title":"商品二",
            #                     "photo":"1_20201808105419000.png",
            #                     "price":"10"
            #                 },
            #                 {
            #                     "id":"3",
            #                     "title":"商品三",
            #                     "photo":"1_20201808105720000.png",
            #                     "price":"10"
            #                 }
            #             ]
            #         }
            #     }
            # elif (message['category_id'] == 2):
            #     data = {
            #         "success" : True,
            #         "action"  : message['action'],
            #         "code"    : 0,
            #         "message" : "",
            #         "data"    : {
            #             "products":[

            #             ]
            #         }
            #     }
            # if (message['category_id'] == 3):
            #     data = {
            #         "success" : True,
            #         "action"  : message['action'],
            #         "code"    : 0,
            #         "message" : "",
            #         "data"    : {
            #             "products":[
            #                 {
            #                     "id":"182",
            #                     "title":"商品一",
            #                     "photo":"3_20200608134659000.jpg",
            #                     "price":"10"
            #                 },
            #                 {
            #                     "id":"2",
            #                     "title":"商品二",
            #                     "photo":"3_20200608134804000.jpg",
            #                     "price":"10"
            #                 },
            #                 {
            #                     "id":"3",
            #                     "title":"商品三",
            #                     "photo":"3_20200608134822000.jpg",
            #                     "price":"10"
            #                 }
            #             ]
            #         }
            #     }
        elif (message['action'] == '413'):
            product = {}
            property = []
            category = []
            products = Tsujiri.get_products()
            properties = Tsujiri.get_properties()
            categories = Tsujiri.get_categories()

            product = products[int(message['product_id'])]
            
            if (int(message['product_id']) >= 27 and int(message['product_id']) <= 31) or int(message['product_id']) == 66:
                property = properties[27]
                category = categories[182]

            elif (int(message['product_id']) >= 64 and int(message['product_id']) <= 65) or int(message['product_id']) == 26:
                property = properties[26]
                category = categories[171]

            elif (int(message['product_id']) >= 40 and int(message['product_id']) <= 46):
                category = categories[183]

            elif (int(message['product_id']) >= 32 and int(message['product_id']) <= 39):
                category = categories[184]

            elif (int(message['product_id']) >= 47 and int(message['product_id']) <= 53):
                category = categories[185]

            elif (int(message['product_id']) >= 68 and int(message['product_id']) <= 69):
                category = categories[186]

            elif (int(message['product_id']) >= 58 and int(message['product_id']) <= 59):
                category = categories[187]

            elif (int(message['product_id']) >= 60 and int(message['product_id']) <= 67):
                category = categories[188]

            data = {
                "success": True,
                "action":"413",
                "code":0,
                "message":"",
                "datetime":"2020-10-12 17:54:42:2174",
                "data":{
                    "product":product,
                    "properties":property,
                    "categories":category,

                    # "product":{
                    #     "id":"28",
                    #     "title":"Genmaicha",
                    #     "photo":"1_20201808105419000.png",
                    #     "price":"115"
                    # },
                    # "properties":[
                    #     {
                    #         "id":"90",
                    #         "title":"Hot / Cold",
                    #         "multiple":"0",
                    #         "quantity":"1",
                    #         "required":"1",
                    #         "items":[
                    #             {
                    #                 "id":"150",
                    #                 "title":"Cold",
                    #                 "price":"0.00",
                    #                 "default":"0"
                    #             },
                    #             {
                    #                 "id":"151",
                    #                 "title":"Hot",
                    #                 "price":"0.00",
                    #                 "default":"0"
                    #             }
                    #         ]
                    #     },
                    #     {
                    #         "property_id":"2",
                    #         "title":"Size",
                    #         "multiple":"0",
                    #         "quantity":"1",
                    #         "required":"1",
                    #         "items":[
                    #             {
                    #                 "item_id":"3",
                    #                 "title":"Large",
                    #                 "price":"10",
                    #                 "default":"1"
                    #             },
                    #             {
                    #                 "item_id":"4",
                    #                 "title":"Small",
                    #                 "price":"0",
                    #                 "default":"0"
                    #             }
                    #         ]
                    #     },
                    #     {
                    #         "property_id":"3",
                    #         "title":"配料",
                    #         "multiple":"1",
                    #         "quantity":"2",
                    #         "required":"0",
                    #         "items":[
                    #             {
                    #                 "item_id":"5",
                    #                 "title":"紅豆",
                    #                 "price":"0",
                    #                 "default":"1"
                    #             },
                    #             {
                    #                 "item_id":"6",
                    #                 "title":"白玉",
                    #                 "price":"15",
                    #                 "default":"0"
                    #             },
                    #             {
                    #                 "item_id":"7",
                    #                 "title":"綠豆",
                    #                 "price":"0",
                    #                 "default":"1"
                    #             },
                    #             {
                    #                 "item_id":"8",
                    #                 "title":"芋頭",
                    #                 "price":"0",
                    #                 "default":"1"
                    #             }
                    #         ]
                    #     }
                    # ]
                }
            }
            # data = {
            #     "success": True,
            #     "action":"413",
            #     "code":0,
            #     "message":"",
            #     "datetime":"2020-10-12 16:29:06:3878",
            #     "data":{
            #         "product":
            #             {
            #                 "id":"30",
            #                 "title":"Yuzu Sencha",
            #                 "photo":"1_20201808105818000.png",
            #                 "price":"130"
            #             }
            #         ,
            #         "properties":[

            #         ]
            #     }
            # }
            # data = {
            #     "success" : True,
            #     "action"  : message['action'],
            #     "code"    : 0,
            #     "message" : "",
            #     "data"    : {
            #         "product":{
            #             "id":"1",
            #             "title":"商品一",
            #             "photo":"1.jpg",
            #             "price":"10"
            #         },
            #         "properties":[
            #             {
            #                 "property_id":"1",
            #                 "title":"冷熱",
            #                 "multiple":"0",
            #                 "quantity":"1",
            #                 "required":"1",
            #                 "items":[
            #                     {
            #                         "item_id":"1",
            #                         "title":"冷",
            #                         "price":"0",
            #                         "defaults":"1"
            #                     },
            #                     {
            #                         "item_id":"2",
            #                         "title":"熱",
            #                         "price":"10",
            #                         "defaults":"0"
            #                     }
            #                 ]
            #             },
            #             {
            #                 "property_id":"2",
            #                 "title":"大小",
            #                 "multiple":"0",
            #                 "quantity":"1",
            #                 "required":"1",
            #                 "items":[
            #                     {
            #                         "item_id":"3",
            #                         "title":"大",
            #                         "price":"10",
            #                         "defaults":"1"
            #                     },
            #                     {
            #                         "item_id":"4",
            #                         "title":"小",
            #                         "price":"0",
            #                         "defaults":"0"
            #                     }
            #                 ]
            #             },
            #             {
            #             "property_id":"3",
            #             "title":"配料",
            #             "multiple":"1",
            #             "quantity":"2",
            #             "required":"0",
            #             "items":[
            #                 {
            #                     "item_id":"5",
            #                     "title":"紅豆",
            #                     "price":"0",
            #                     "defaults":"1"
            #                 },
            #                 {
            #                     "item_id":"6",
            #                     "title":"白玉",
            #                     "price":"15",
            #                     "defaults":"0"
            #                 },
            #                 {
            #                     "item_id":"7",
            #                     "title":"綠豆",
            #                     "price":"0",
            #                     "defaults":"1"
            #                 },
            #                 {
            #                     "item_id":"8",
            #                     "title":"芋頭",
            #                     "price":"0",
            #                     "defaults":"1"
            #                 }
            #             ]
            #             }
            #         ]
            #     }
            # }
        elif (message['action'] == '421'):
            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data"    : {
                    "order":{
                        "order_id":21,
                        "sale_number":"20200819000005",
                        "order_total":"795",
                        "payment_id":1,
                        "products":[
                            {
                                "id":"68",
                                "product_id":"68",
                                "product_title":"TSUJIRI O-Matcha Soft Ice Cream",
                                "quantity":"2",
                                "sale_price":"150",
                                "sub_total":"300",
                                "photo":"1_20202008155702000.png",
                                "remark":"",
                                "properties":[]
                            },
                            {
                                "id":"26",
                                "product_id":"26",
                                "product_title":"Yuzu O-Matcha",
                                "quantity":"3",
                                "sale_price":"165",
                                "sub_total":"495",
                                "photo":"1_20201808100017000.png",
                                "remark":"Cold, Large",
                                "properties":[
                                    {
                                        "id":"189",
                                        "title":"Hot / Cold",
                                        "items":[
                                            {
                                                "id":"193",
                                                "title":"Cold",
                                                "quantity":"1",
                                                "sale_price":"0",
                                                "sub_total":"0"
                                            }
                                        ]
                                    },
                                    {
                                        "id":"191",
                                        "title":"Size",
                                        "items":[
                                            {
                                                "id":"197",
                                                "title":"Large",
                                                "quantity":"1",
                                                "sale_price":"20",
                                                "sub_total":"20"
                                            }
                                        ]
                                    }
                                ]
                            },
                        ]
                    }
                }
            }
        elif (message['action'] == '422'):
            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data"    : {
                    "order":{
                        "order_id":21,
                        "sale_number":"20201124000001",
                        "order_total":"1295",
                        "payment_id":1,
                        "products":[
                            {
                                "id":"316",
                                "product_id":"28",
                                "product_title":"Genmaicha",
                                "quantity":"4",
                                "sale_price":"125",
                                "sub_total":"500",
                                "photo":"1_20201808105419000.png",
                                "remark":"Cold, Medium",
                                "properties":[
                                    {
                                        "id":"75",
                                        "title":"Hot / Cold",
                                        "items":[
                                            {
                                                "id":"79",
                                                "title":"Cold",
                                                "quantity":"1",
                                                "sale_price":"0",
                                                "sub_total":"0"
                                            }
                                        ]
                                    },
                                    {
                                        "id":"77",
                                        "title":"Size",
                                        "items":[
                                            {
                                                "id":"82",
                                                "title":"Medium",
                                                "quantity":"1",
                                                "sale_price":"10",
                                                "sub_total":"10"
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "id":"68",
                                "product_id":"68",
                                "product_title":"TSUJIRI O-Matcha Soft Ice Cream",
                                "quantity":"2",
                                "sale_price":"150",
                                "sub_total":"300",
                                "photo":"1_20202008155702000.png",
                                "remark":"",
                                "properties":[]
                            },
                            {
                                "id":"26",
                                "product_id":"26",
                                "product_title":"Yuzu O-Matcha",
                                "quantity":"3",
                                "sale_price":"165",
                                "sub_total":"495",
                                "photo":"1_20201808100017000.png",
                                "remark":"Cold, Large",
                                "properties":[
                                    {
                                        "id":"189",
                                        "title":"Hot / Cold",
                                        "items":[
                                            {
                                                "id":"193",
                                                "title":"Cold",
                                                "quantity":"1",
                                                "sale_price":"0",
                                                "sub_total":"0"
                                            }
                                        ]
                                    },
                                    {
                                        "id":"191",
                                        "title":"Size",
                                        "items":[
                                            {
                                                "id":"197",
                                                "title":"Large",
                                                "quantity":"1",
                                                "sale_price":"20",
                                                "sub_total":"20"
                                            }
                                        ]
                                    }
                                ]
                            },
                        ]
                    }
                }
            }
        # 劇本一
        # 420 商品加入購物車 、 421 刪除商品 、 423 購物清單
        elif (message['action'] == '420' or message['action'] == '421' or message['action'] == '423'):
            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data"    : {
                    "order":{
                        "order_id":21,
                        "sale_number":"20210108000003",
                        "order_total":"1170",
                        "payment_id":2,
                        "products":[
                            {
                                "id":"316",
                                "product_id":"28",
                                "product_title":"Genmaicha",
                                "quantity":"3",
                                "sale_price":"125",
                                "sub_total":"375",
                                "photo":"1_20201808105419000.png",
                                "remark":"Cold, Medium",
                                "properties":[
                                    {
                                        "id":"75",
                                        "title":"Hot / Cold",
                                        "items":[
                                            {
                                                "id":"79",
                                                "title":"Cold",
                                                "quantity":"1",
                                                "sale_price":"0",
                                                "sub_total":"0"
                                            }
                                        ]
                                    },
                                    {
                                        "id":"77",
                                        "title":"Size",
                                        "items":[
                                            {
                                                "id":"82",
                                                "title":"Medium",
                                                "quantity":"1",
                                                "sale_price":"10",
                                                "sub_total":"10"
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "id":"68",
                                "product_id":"68",
                                "product_title":"TSUJIRI O-Matcha Soft Ice Cream",
                                "quantity":"2",
                                "sale_price":"150",
                                "sub_total":"300",
                                "photo":"1_20202008155702000.png",
                                "remark":"",
                                "properties":[]
                            },
                            {
                                "id":"26",
                                "product_id":"26",
                                "product_title":"Yuzu O-Matcha",
                                "quantity":"3",
                                "sale_price":"165",
                                "sub_total":"495",
                                "photo":"1_20201808100017000.png",
                                "remark":"Cold, Large",
                                "properties":[
                                    {
                                        "id":"189",
                                        "title":"Hot / Cold",
                                        "items":[
                                            {
                                                "id":"193",
                                                "title":"Cold",
                                                "quantity":"1",
                                                "sale_price":"0",
                                                "sub_total":"0"
                                            }
                                        ]
                                    },
                                    {
                                        "id":"191",
                                        "title":"Size",
                                        "items":[
                                            {
                                                "id":"197",
                                                "title":"Large",
                                                "quantity":"1",
                                                "sale_price":"20",
                                                "sub_total":"20"
                                            }
                                        ]
                                    }
                                ]
                            },
                        ]
                    }
                }
            }
        # 劇本二
        # elif (message['action'] == '420' or message['action'] == '421' or message['action'] == '423'):
        #     data = {
        #         "success" : True,
        #         "action"  : message['action'],
        #         "code"    : 0,
        #         "message" : "",
        #         "data"    : {
        #             "order":{
        #                 "order_id": 230,
        #                 "sale_number":"20201123000003",
        #                 "order_total":"345",
        #                 "payment_id": 2,
        #                 "products":[
        #                     {
        #                         "id":"330",
        #                         "product_id":"28",
        #                         "product_title":"Genmaicha",
        #                         "quantity":"3",
        #                         "sale_price":"115",
        #                         "sub_total":"345",
        #                         "photo":"1_20201808105419000.png",
        #                         "remark":"冷",
        #                         "properties":[
        #                             {
        #                                 "id":"75",
        #                                 "title":"Hot / Cold",
        #                                 "items":[
        #                                     {
        #                                         "id":"79",
        #                                         "title":"Cold",
        #                                         "quantity":"1",
        #                                         "sale_price":"0",
        #                                         "sub_total":"0"
        #                                     }
        #                                 ]
        #                             }                                 
        #                         ]
        #                     }
        #                 ]
        #             }
        #         }
        #     }
        elif (message['action'] == '440'):
            data = {
                "success" : True,
                "action"  : message['action'],
                "code"    : 0,
                "message" : "",
                "data"    : []
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


        response = json.dumps(data)
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
                    "total":"1295",
                    "paid":"1200",
                    "unpaid":"95",
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