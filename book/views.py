from django.shortcuts import render,redirect
from book.models import Book
from book.forms import Bookcreate
from django.http import HttpResponse

# Create your views here.
def index(request):
    shelf=Book.objects.all()
    return render(request,'book/library.html',{'shelf':shelf}) 
def upload(request):
    upload=Bookcreate()
    if request.method=='POST':
        upload=Bookcreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('/')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request,'book/upload-form.html',{'upload': upload })
def update(request,pk):
    bookid=int(pk)
    try:
        booksel=Book.objects.get(id=bookid)
    except Book.DoesNotExist:
        return redirect('/')
    bookform=Bookcreate(request.POST or None, instance=booksel)
    if bookform.is_valid():
        bookform.save()
        return redirect('/')
    return render(request,'book/upload-form.html',{'upload': bookform })
def delete(request,pk):
    bookid=int(pk)
    try:
       book=Book.objects.get(id=bookid)
    except Book.DoesNotExist:
        return redirect('/')
    book.delete()
    return redirect('/')


