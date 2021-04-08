import time

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import requests
from .models import Available_Format, Output_Format,All_Format,Document
from requests.auth import HTTPBasicAuth
from datetime import datetime

now = datetime.now()

# @csrf_exempt
# def format(request):
#     print(request.POST)
#     exe='pdf'
#     exee=All_Format.objects.get(name=exe)
#     ava=Available_Format.objects.get(input=exee)
#     formarts=list(Output_Format.objects.filter(available_format=ava).values('output__name'))
#     return JsonResponse(formarts,safe=False)

@csrf_exempt
def datasave(request):
    print(request.FILES,request.POST)
    exe = request.POST.get('ext')
    try:
        exe = All_Format.objects.get(name=exe)
        ava = Available_Format.objects.get(input=exe)
        formarts = list(Output_Format.objects.filter(available_format=ava).values('output__name'))
        id = now.strftime("%d%m%Y%H%M%S")
        document = request.FILES.get('doc')
        data = Document(document=document, id=id)
        data.save()
    except:
        print('error')
        id=404
        formarts='not found'
    return JsonResponse({'id':id,'formarts':formarts},safe=False)

@csrf_exempt
def convert(request):
    print(request.POST)
    selected_format=request.POST.get('selected_format')
    documentid=request.POST.get('documentid')
    document=Document.objects.get(id=documentid).document
    print(document.name,type(document.name))


    api_key = 'fd60c2a58929b90c57ad37f4feb484df05b1fa3b'
    endpoint = "https://sandbox.zamzar.com/v1/jobs"
    source_file = 'media/'+document.name
    target_format = selected_format
    file_content = {'source_file': open(source_file, 'rb')}
    data_content = {'target_format': target_format}
    res = requests.post(endpoint, data=data_content, files=file_content, auth=HTTPBasicAuth(api_key, ''))
    output1 = res.json()

    if 'id' in output1:
        id = output1['id']
        print(id)
        job_id = id
        time.sleep(4)
        print('enter to checking')
        outputfile=checking(job_id)
        print('out from checking')
        print(outputfile)
        # output_link='http://127.0.0.1:8000/media/'+document.name
        inputfilename = request.POST.get('inputfilename')
        outputfilename = inputfilename[0:inputfilename.rindex('.') + 1] + selected_format
        output_link = str(outputfile)
    elif "errors" in output1:
        error = output1['errors'][0]['message']
        if error == 'the size of file exceeds the maximum file size cap for the current plan':
            error = 'Sorry!Your file size is more then 1mb.'
        else:
            error = error
        outputfilename = error
        output_link = 'error'
    return JsonResponse({'link':output_link,'name':outputfilename},safe=False)


def checking(job_id):
    api_key = 'fd60c2a58929b90c57ad37f4feb484df05b1fa3b'
    endpoint = "https://sandbox.zamzar.com/v1/jobs/{}".format(job_id)
    response = requests.get(endpoint, auth=HTTPBasicAuth(api_key, ''))
    output2 = response.json()
    print('output2')
    print(output2)
    if 'successful' in output2.values():
        local_filename = output2["target_files"][0]["name"]
        file_id = output2["target_files"][0]["id"]
        endpoint = "https://sandbox.zamzar.com/v1/files/{}/content".format(file_id)

        response = requests.get(endpoint, stream=True, auth=HTTPBasicAuth(api_key, ''))
        try:
            with open("media/Output//" + local_filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                print("File downloaded")
                print(local_filename)
                if local_filename is not None:
                    file="media/Output/" +local_filename
                    print(file)
                return file

        except IOError:
            print("Error")
    else:
        time.sleep(2)
        file=checking(job_id)
    # outputfile="media/Output/"+ str(outputfilename)
    return file


def massaddformat(request):
    # data=['csv','djvu','doc','docx','eml','eps','key','mpp','msg','numbers','odp','ods','odt','pages','pdf','pps','ppsx','ppt','pptx','ps','pub','rtf','txt','vsd','vsdx','wks','wpd','wps','xlr','xls','xlsx','xps']
    # for formatt in data:
    #     newf=All_Format(name=formatt)
    #     newf.save()
    return JsonResponse('Finished',safe=False)



