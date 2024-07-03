from django.db import models

# Create your models here.


class studentclinicfile(models.Model):
    full_name= models.CharField(max_length=255)
    matric_no= models.CharField(max_length=255)
    Department= models.CharField(max_length=255)
    courses= models.CharField(max_length=255)
    level= models.CharField(max_length=20)
    email= models.EmailField(max_length=255)
    phone_num= models.CharField(max_length=20)

    file_1 = models.FileField(null=True)
