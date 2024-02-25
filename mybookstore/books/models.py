from django.db import models
from django.utils import timezone


class CompanyInformation(models.Model):
   name  = models.CharField(max_length=100)
   description = models.TextField()
   
   def __str__(self) -> str:
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
  
class Book(models.Model):
    image = models.ImageField(null=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    description = models.TextField()
    price = models.FloatField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')

    def __str__(self) -> str:
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.name} - {self.email}'


class About(models.Model):
    OurStory_title = models.CharField(max_length=100)
    OurStory_content = models.TextField()
    OurMission_title = models.CharField(max_length=100)
    OurMission_content = models.TextField()
    OurVision_title = models.CharField(max_length=100)
    OurVision_content = models.TextField()
    TeamMember_name = models.CharField(max_length=100)
    TeamMember_position = models.CharField(max_length=100)
    TeamMember_position1 = models.CharField(max_length=100)
    ContactAbout_title = models.CharField(max_length=100)
    ContactAbout_content = models.TextField()
    ContactAbout_email = models.EmailField()

    def __str__(self) -> str:
        return self.OurStory_title

