from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Skill(models.Model):
    name = models.TextField(max_length=30)
    value = models.PositiveIntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)], default=1)
    
    def __str__(self) -> str:
        
        return f"{self.name} skill value is {self.value}"
    
    
class Education(models.Model):
    university_name = models.TextField(max_length=70)
    start_date = models.PositiveIntegerField(validators=[MaxValueValidator(2023), MinValueValidator(1900)])
    end_date = models.PositiveIntegerField(validators=[MaxValueValidator(2023), MinValueValidator(1900)])
    grade = models.TextField(max_length=30, blank=True, null=True)
    created_on=models.DateTimeField(auto_now=True)
    
    
    def __str__(self) -> str:
        return f"{self.university_name} university grade is {self.grade}"
    
class Experience(models.Model):
    position_name = models.TextField(max_length=100, blank=True, null=True)
    start_date = models.IntegerField(
        validators=[MaxValueValidator(2023), MinValueValidator(1900)])
    end_date = models.IntegerField(
        validators=[MaxValueValidator(2023), MinValueValidator(1900)])
    company_name = models.TextField(max_length=150)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.position_name} in {self. company_name}'   
    

# class SocialMedia(models.Model):
#     platform_name = models.TextField()
#     url = models.TextField()

#     def __str__(self) -> str:
#         return f"{self.platform_name} account"
    

# class Testimonial(models.Model):
#     name = models.TextField()
#     proffesion = models.TextField()
#     text = models.TextField()
#     image =models.ImageField()
    
#     def __str__(self) -> str:
#         return f"{self.name} - {self.proffesion}"
# class Testimonials(models.Model):
#     full_name = models.TextField(max_length=30)
#     position = models.TextField(max_length=70)
#     testimonial = models.TextField(max_length=300)
#     image = models.ImageField(upload_to='images/', null=True, blank=True)
#     link = models.URLField(blank=True, null=True)

    
    
class Service(models.Model):
    service_name = models.TextField()
    service_description = models.TextField()  
    
    def __str__(self) -> str:
        return f"{self.service_name} - {self.service_description}"
        
class Language(models.Model):
    name = models.CharField(max_length=20)
    level = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.level}"
    
    
    
class Courses(models.Model):
    program = models.TextField(max_length =100)
    program_name = models.TextField(max_length =100)
    cours_name = models.TextField(max_length =100)

    def __str__(self) -> str:
        return f'{self.cours_name}'
            

class PersonalInfo(models.Model):
    website = models.URLField(max_length = 200)
    phone = models.CharField(max_length=30)  
    city = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    degree = models.CharField(max_length=30)
    freelance = models.CharField(max_length=30)
    birthday = models.DateField()
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

