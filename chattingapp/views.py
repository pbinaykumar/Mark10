import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Chat

@csrf_exempt
def set_chat(request):
    print('setttttttt')
    user=request.POST.get('user')
    print('user:',user)
    chat=request.POST.get('chat')
    print('chat')
    print(chat)
    room = request.POST.get('room')
    print(room)
    chats=Chat.objects.get(room=room)
    allchat=chats.chat
    print(allchat)
    if chat!='undefined'and chat!='':
        allchat.append([user,chat])
        chats.chat=allchat
        chats.save()
    print(chats.chat,type(chats.chat))
    return JsonResponse(True,safe=False)
@csrf_exempt
def get_all_chat(request):
    print('gettttttttttt')
    room=request.POST.get('room')
    print(room)
    try:
         chats=Chat.objects.get(room=room)
         print(chats)
    except:
        new_room=Chat(room=room)
        new_room.save()
        chats=new_room
    allchat = chats.chat
    print(allchat)
    return JsonResponse(allchat,safe=False)