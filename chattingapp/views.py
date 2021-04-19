import json
from datetime import datetime
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Chat,Connection_Room
from django.db import IntegrityError
@csrf_exempt
def set_chat(request):
    user=request.POST.get('user')
    chat=request.POST.get('chat')
    room = request.POST.get('room')
    chats=Chat.objects.get(room=room)
    allchat=chats.chat
    if chat!='undefined'and chat!='':
        allchat.append([user,chat])
        chats.chat=allchat
        chats.save()
    return JsonResponse(True,safe=False)
@csrf_exempt
def get_all_chat(request):
    room=request.POST.get('room')
    try:
         chats=Chat.objects.get(room=room)
    except:
        new_room=Chat(room=room)
        new_room.save()
        chats=new_room
    allchat = chats.chat
    return JsonResponse(allchat,safe=False)


@csrf_exempt
def signup(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    # try:
    user_idd=unique_user_id()
    print('user_id')
    print(user_idd)
    user = User.objects.create_user(id=202,username=username, password=password,first_name=first_name,last_name=last_name)
    user.save()
    print('user_id')
    print(user.id)
    output='success'
    # except IntegrityError:
    #     output='this user is alredy exist'
    return JsonResponse({'output': output},safe=False)

@csrf_exempt
def signin(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    if User.objects.filter(username=username).exists():
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            status=True
            print(user.id)
            log={"username":user.username,'first_name':user.first_name,'last_name':user.last_name,'user_id':user.id}
        else:
            status=False
            log='wrong password'
    else:
        status=False
        log="User Doesn't exists"
    return JsonResponse({"status": status, "log": log}, safe=False)


@csrf_exempt
def unique_connection_id():
    connection_id=Connection_Room.objects.all().values('connection_id').last()
    if connection_id == None or int(connection_id['connection_id'][1:9]) != int(datetime.now().strftime("%Y%m%d")):
        count=1
    else:
        count=int(connection_id['connection_id'][9:])+1
    new_connection_id = 'B'+datetime.now().strftime("%Y%m%d")+str('%03d' % count)
    return new_connection_id

@csrf_exempt
def new_connection(request):
    user1_id=request.POST.get('user1_id')
    user2_id=request.POST.get('user2_id')
    user1=User.objects.get(username=user1_id)
    try:
        user2=User.objects.get(username=user2_id)
    except:
        return JsonResponse("user does't exist", safe=False)
    check1=Connection_Room.objects.filter(user1=user1,user2=user2)
    check2=Connection_Room.objects.filter(user1=user2,user2=user1)
    if len(check1)==0 and len(check2)==0:
        connection_id=unique_connection_id()
        new_conn=Connection_Room(user1=user1,user2=user2,connection_id=connection_id)
        new_conn.save()
        status='success'
    else:
        status='alredy exist'
    return JsonResponse(status,safe=False)

@csrf_exempt
def my_friends(request):
    user_id = request.POST.get('user1_id')
    user = User.objects.get(username=user_id)
    flist1 = list(Connection_Room.objects.filter(user1=user).values('user2__first_name','connection_id'))
    flist2 = list(Connection_Room.objects.filter(user2=user).values('user1__first_name','connection_id'))
    flists=[flist1,flist2]
    return JsonResponse({'flists':flists},safe=False)

@csrf_exempt
def chats(request):
    connection_id=request.POST.get('connection_id')
    chat=Connection_Room.objects.get(connection_id=connection_id).chat
    return JsonResponse(chat,safe=False)

@csrf_exempt
def unique_user_id():
    now = datetime.now()
    id = now.strftime("%Y%m%d%H%M%S")
    return id