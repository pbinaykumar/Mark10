import time

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import requests
from .models import Available_Format, Output_Format,All_Format,Document
from requests.auth import HTTPBasicAuth
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


    api_key = 'fd60c2a58929b90c57ad37f4feb484df05b1fa3b'
    endpoint = "https://sandbox.zamzar.com/v1/jobs"
    source_file = 'media/'+document.name
    target_format = selected_format
    file_content = {'source_file': open(source_file, 'rb')}
    data_content = {'target_format': target_format}
    res = requests.post(endpoint, data=data_content, files=file_content, auth=HTTPBasicAuth(api_key, ''))
    output1 = res.json()
    print('output1')
    print(output1)
    if 'id' in output1:
        id = output1['id']
        print(id)
        job_id = id
        time.sleep(4)
        print('enter to checking')
        outputfile=checking(job_id)
        print('out from checking')
        print(outputfile)
    elif "errors" in output1:
        error = output1['errors'][0]['message']
        if error == 'the size of file exceeds the maximum file size cap for the current plan':
            error = 'Sorry!Your file size is more then 1mb.'
        else:
            error = error
        outputfile='bkp'


    link='http://127.0.0.1:8000/media/'+document.name
    print(link,type(link))
    # input_file=Input_File(document=document)
    # input_file.save()
    outputfile='http://127.0.0.1:8000/'+str(outputfile)
    print(outputfile,type(outputfile))
    return JsonResponse({'link':outputfile,'name':document.name},safe=False)


def checking(job_id):
    outputfilename=None
    api_key = 'fd60c2a58929b90c57ad37f4feb484df05b1fa3b'
    endpoint = "https://sandbox.zamzar.com/v1/jobs/{}".format(job_id)
    response = requests.get(endpoint, auth=HTTPBasicAuth(api_key, ''))
    output2 = response.json()
    print('output2')
    print(output2)
    if 'successful' in output2.values():

        local_filename = output2["target_files"][0]["name"]
        outputfilename=local_filename
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
    # print(outputfilename,type(outputfilename))
    # outputfile="media/Output/"+ str(outputfilename)
    # print(outputfile)
    return file


