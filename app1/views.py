from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':15,'b':10}
    return render(request,'conditions.html',context=d)

def if_else(request):
    d={'a':15,'b':10}
    return render(request,'if_else.html',context=d)

def if_elif(request):
    d={'a':15,'b':10,'c':12}
    return render(request,'if_elif.html',context=d)



def for_loop(request):
    d={'name':'Kanchana','age':22,'hobbies':['cooking','Craft','Listening music']}
    return render(request,'for_loop.html',context=d)
