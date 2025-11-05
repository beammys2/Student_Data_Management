from django.shortcuts import render
from app.app_forms import Stud
from app.models import Stud as S
from app.app_forms import Delete
from app.app_forms import Update
from app.app_forms import Search

# Create your views here.
def index(request):
    num = S.objects.all().count()
    n1 = S.objects.filter(Class='1').count()
    n2 = S.objects.filter(Class='2').count()
    n3 = S.objects.filter(Class='3').count()
    n4 = S.objects.filter(Class='4').count()
    n5 = S.objects.filter(Class='5').count()
    n6 = S.objects.filter(Class='6').count()
    n7 = S.objects.filter(Class='7').count()
    n8 = S.objects.filter(Class='8').count()
    n9 = S.objects.filter(Class='9').count()
    n10 = S.objects.filter(Class='10').count()
    context = {
        'num': num,
        'n1': n1,
        'n2': n2,
        'n3': n3,
        'n4': n4,
        'n5': n5,
        'n6': n6,
        'n7': n7,
        'n8': n8,
        'n9': n9,
        'n10': n10,
    }
    return render(request, 'app/base.html', context=context)
def insert(request):
   ack=""
   stud=Stud()
   if request.method=='POST':
       stud=Stud(request.POST)
       if stud.is_valid():
           r=stud.cleaned_data['reg']
           n=stud.cleaned_data['name']
           cla=stud.cleaned_data['clas']
           sec=stud.cleaned_data['section']
           roll=stud.cleaned_data['rollno']
           per=stud.cleaned_data['percentage']
           gen=stud.cleaned_data['gender']
           phone=stud.cleaned_data['phone']
           add=stud.cleaned_data['address']
           p=S(Reg=r,Name=n,Class=cla,Section=sec,Rollno=roll,Percentage=per,Gender=gen,Phone=phone,Address=add)
           p.save()
           ack="Inserted Successfully!!!"
           return render(request,'app/messages.html',{'text':ack})
       
   return render(request,'app/insert.html',{'form':stud})

def delete(request):
    d=Delete(request.POST or None)
    if d.is_valid():
        item=d.cleaned_data['reg']
        try:
            queryset=S.objects.filter(Reg=item)
            queryset.delete()
            return render(request,'app/messages.html',{"text":"Deleted Succesfully"})
        except S.DoesNotExist:
           queryset=None
        if queryset==None:
            ack="Sorry! No Such Registration Number Found!"
            return render(request,'app/messages.html',{'text':ack})
    return render(request,'app/delete.html',{'form':d})


def update(request):
    stud=Update(request.POST or None)
    if stud.is_valid():
        r=stud.cleaned_data['reg']
        n=stud.cleaned_data['name']
        cla=stud.cleaned_data['clas']
        sec=stud.cleaned_data['section']
        roll=stud.cleaned_data['rollno']
        per=stud.cleaned_data['percentage']
        gen=stud.cleaned_data['gender']
        phone=stud.cleaned_data['phone']
        add=stud.cleaned_data['address']
        try:
            queryset=S.objects.get(Reg=r)

            queryset.name=n
            queryset.clas=cla
            queryset.section=sec
            queryset.rollno=roll
            queryset.percentage=per
            queryset.gender=gen
            queryset.phone=phone
            queryset.address=add
            queryset.save()
            x=S.objects.filter(Reg=r)
            context={
                "Set":x
            }
            return render(request,'app/existing.html',context)
        except S.DoesNotExist:
           queryset=None
        if queryset==None:
            ack="Sorry! No Such Registration Number Found!"
            return render(request,'app/messages.html',{'text':ack})
        
    return render(request,"app/update.html",{"form":stud})

def search(request):
    t=Search(request.POST or None)
    if t.is_valid():
        q=t.cleaned_data['name']
        q1=S.objects.filter(Name=q)
        if len(q1)==0:
            return render(request,'app/messages.html',{"text":"NOT FOUND!!"})
        context={
            "Set":q1,
        }
        return render(request,'app/existing.html',context)
    return render(request,'app/search.html',{'form':t})

def display(request):
    q=S.objects.all()
    context={
        "Set":q
    }
    return render(request,'app/existing.html',context)
