from django.db import models

#ORM-> Object Relationsl Mapper

# Create your models here.
class Campus(models.Model):
    campus_name = models.CharField(max_length=100)


class Course(models.Model):
    course_name = models.CharField(max_length=100)

class Member(models.Model):
    member_first_name = models.CharField(max_length=100)
    member_lastname = models.CharField(max_length=100)
    member_date_of_birth = models.DateField()
    member_contact = models.CharField(max_length=15)
    member_address = models.CharField(max_length=100)
    campus = models.ForeignKey(Campus,on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Dennis():
    pass
class Ivy():
    pass
