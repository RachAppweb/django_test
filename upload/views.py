from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .forms import *
from .models import *
import re
# this function perform uploading and verefying the type and storing the content of the file
def goes(request):
    if request.method == 'POST' :
        # schema=['trans_id','merchant','country','city','amount','currency']
        form=UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
           file=request.FILES['file']
           if str(file).endswith('.csv')or str(file).endswith('.txt'): 
              with open (str(file),'wb+')as destination:
                 for chunk in file.chunks():
                    #  auth_id
                    fileo=str(file)
                    destination.write(chunk)
                    with open(str(fileo),'r') as fil:
                         for line in fil:
                                if 'auth_id'  in line:
                                    return HttpResponse('this file should be in mongodb database')
                                else:  
                                    trying=line.split(',')
                                    trans_id=''.join(trying[0])
                                    merchant=','.join(trying[1:3])
                                    country=''.join(trying[4])
                                    city=''.join(trying[5])
                                    amount=''.join(trying[3:4])
                                    currency=''.join(trying[6])
                                    originalo=original.objects.create(trans_id=trans_id,merchant=merchant,
                                                                    country=country,city=city,amount=amount,currency=currency)
                                    originalo.save()
           else:
               return HttpResponse('the file shuld be either csv or txt')
              
    else:
        form=UploadFileForm()



    return render(request,'index.html',{'form':form})
# getting all the files uploded
def allfiles(request):
    allfiles=original.objects.all()
    return render(request,'index.html',{'allfiles':allfiles})
# modify the file and display its done if evrythings goes fine
def modify(request,id):
    theonefile=original.objects.get(id=id)
    if request.method== 'POST':
    #    getting the availabel content the POST request
       form=editfilecontent(request.POST,instance=theonefile)
       if form.is_valid():
           
        trans_id=form.cleaned_data['trans_id']
        merchant=form.cleaned_data['merchant']
        country=form.cleaned_data['country']
        city=form.cleaned_data['city']
        amount=form.cleaned_data['amount']
        currency=form.cleaned_data['currency']

        
        theonefile.trans_id=trans_id
        theonefile.merchant=merchant
        theonefile.country=country
        theonefile.city=city
        theonefile.amount=amount
        theonefile.currency=currency
        theonefile.save()
        return HttpResponse('its done')
    else:
        # if there is no post request we should let the previous content
        form=editfilecontent(instance=theonefile)

        
    context={'theonefile':theonefile,
              'form':form
              }



    return render (request,'changin.html',context)

