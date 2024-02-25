from django.contrib import admin
from django.urls import path
from books.views import home,about,contact,book
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('book/', book, name='book'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


