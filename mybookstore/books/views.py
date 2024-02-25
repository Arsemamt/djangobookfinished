from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import  CompanyInformation,Book, Category, About, Contact

def home(request):
    info = CompanyInformation.objects.first()
    Books = Book.objects.all()

    data ={
        'info': info,
        'Books': Books
    }

    return render(request,'home.html',data) 

def about(request):
    about_info = About.objects.first()
    return render(request,'about.html', {'about_info': about_info}) 

def book(request):
    category_filter = request.GET.get('Category')
    if category_filter:
        category = Category.objects.get(name=category_filter)
        Books = Book.objects.filter(category=category)
    else:
        Books = Book.objects.all()
    return render(request, 'book.html', {'Books': Books})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact_info = Contact.objects.create(name=name, email=email, message=message)
        messages.success(request, "Form submitted successfully!")
        return redirect('contact')
    else:
        messages.info(request, "Please use the form to submit your message.")

        contact_info = None

        return render(request, 'contact.html',{"message": "Please use the form to submit your message.", "contact_info": contact_info})

