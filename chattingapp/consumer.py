from channels.generic.websocket import AsyncWebsocketConsumer
class TableData(AsyncWebsocketConsumer):
    async def connect(self):
        room_name = 'testing'
        self.group_name=room_name
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        pass

    async def receive(self, text_data):
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'randomFunction',
                'value': text_data,
            }
        )

    async def randomFunction(self, event):
            print(event['value'])
            await self.send(event['value'])


