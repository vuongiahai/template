# consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json
import time

 

class activate_function(AsyncWebsocketConsumer):  
    
    async def connect(self):  
        time.sleep(1)                         
        await self.accept()    
        message ="hello connect from PC "             
        await self.send(text_data=json.dumps(message))   
        self.device_group_name = 'group1'
        await self.channel_layer.group_add(
            self.device_group_name,
            self.channel_name
        )    
              
    async def disconnect(self,text_data):
        await self.channel_layer.group_discard(
            self.device_group_name,
            self.channel_name
        )
        pass
    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
        except:
            data={'command':'stand'}
        command = data['command']   

        if command == 'tien':
            await self.send_control_command('tien')
        elif command == 'lui':
            await self.send_control_command('lui')
        elif command == 'trai':
            await self.send_control_command('trai')
        elif command == 'phai':
            await self.send_control_command('phai')
        elif command == 'stop':
            await self.send_control_command('stop')
        else:
            await self.send_error_message("Invalid command")
        
        pass
    async def control_device(self, event):
             # Send control command to the device (e.g., ESP8266)
        command = event.get('command')
        # Kiểm tra xác thực, có thể sử dụng các thông tin trong event để xác thực
        # Thực hiện điều khiển thiết bị và gửi kết quả lại cho client
        await self.send(text_data=json.dumps({            
            'message':command
        }))
        # Send control command to the device (e.g., ESP8266)
        pass 
    async def send_control_command(self, command):
        # Gửi lệnh điều khiển đến thiết bị thông qua giao thức (ví dụ: MQTT, HTTP, ...)
        # Đây là ví dụ giả sử, bạn cần thay đổi phù hợp với giao thức và thiết bị thực tế
        await self.channel_layer.group_send(
            self.device_group_name,
            {
                'type': 'control_device',
                'command': command
            }
        )
    async def send_error_message(self, message):
        # Gửi thông báo lỗi đến client
        await self.send(text_data=json.dumps({
            'status': 'error',
            'message': message
        }))