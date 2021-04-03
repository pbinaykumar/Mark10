import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Chat

@csrf_exempt
def set_chat(request):
    user=request.POST.get('user')
    print('user:',user)
    chat=request.POST.get('chat')
    print('chat')
    print(chat)
    chats=Chat.objects.get(path='bkp')
    allchat=chats.chat
    print(allchat)
    if chat!='undefined'and chat!='':
        allchat.append(chat)
        chats.chat=allchat
        chats.save()
    print(chats.chat,type(chats.chat))
    return JsonResponse(True,safe=False)
@csrf_exempt
def get_all_chat(request):
    chats=Chat.objects.get(path='bkp')
    allchat=chats.chat
    print(allchat)
    return JsonResponse(allchat,safe=False)