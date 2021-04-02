import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Chat

@csrf_exempt
def chat(request):
    chat=request.POST.get('chat')
    print('chat')
    print(chat)
    chats=Chat.objects.get(path='bkp')
    allchat=chats.chat
    if chat!='undefined':
        allchat.append(chat)
        chats.chat=allchat
        chats.save()
    print(chats.chat,type(chats.chat))
    return JsonResponse(allchat,safe=False)
