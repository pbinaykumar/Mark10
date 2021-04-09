from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Connection_Room
import json
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


class NewTableData(AsyncWebsocketConsumer):
    async def connect(self):
        room_name = self.scope['url_route']['kwargs']['id']
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
                'type': 'mychat',
                'value': text_data,
            }
        )

    async def mychat(self, event):
            print(event['value'])
            chats = await database_sync_to_async(self.chatset)(event['value'])
            print(chats)
            await self.send(chats)
    def chatset(self,chat):
        chats=Connection_Room.objects.get(connection_id=self.group_name)
        allchat = chats.chat
        if chat != 'undefined' and chat != '':
            allchat.append([chat, chat])
            chats.chat = allchat
            chats.save()
        chats = list(Connection_Room.objects.filter(connection_id=self.group_name).values('chat'))
        return json.dumps(chats)

