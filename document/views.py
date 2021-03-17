from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Available_Format, Output_Format,All_Format,Document

from datetime import datetime

now = datetime.now()

@csrf_exempt
def format(request):
    print(request.POST)
    exe='pdf'
    exe=All_Format.objects.get(name=exe)
    ava=Available_Format.objects.get(input=exe)
    formarts=list(Output_Format.objects.filter(available_format=ava).values('output__name'))
    return JsonResponse(formarts,safe=False)

@csrf_exempt
def datasave(request):
    id = now.strftime("%d%m%Y%H%M%S")
    document=request.FILES.get('doc')
    data=Document(document=document,id=id)
    data.save()
    return JsonResponse({'id':id},safe=False)

@csrf_exempt
def convert(request):
    selected_format=request.POST.get('selected_format')
    documentid=request.POST.get('documentid')
    document=Document.objects.get(id=documentid).document
    print(document,type(document))

    filename=document.name[::-1]
    exe=filename[0:filename.index('.')][::-1]




    link='http://127.0.0.1:8000/media/'+document.name
    print(link)
    # input_file=Input_File(document=document)
    # input_file.save()
    return JsonResponse({'link':link,'name':document.name},safe=False)

