from django.contrib import admin
from .models import CompanyInformation, Book, Category, About, Contact
# Register your models here.
 
admin.site.register(CompanyInformation)
admin.site.register(Book) 
admin.site.register(Category) 
admin.site.register(About) 
admin.site.register(Contact) 


