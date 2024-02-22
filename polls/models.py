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

class Electoral_Position(models.Model):
    electoral_position_name=models.CharField(max_length=100)

class Party(models.Model):
    party_name=models.CharField(max_length=100)
class Election(models.Model):
     election_date_created=models.DateField()
     election_closing_date=models.DateField()
     election_is_active=models.BooleanField()
class Election_Member(models.Model):
    election=models.ForeignKey(Election,on_delete=models.CASCADE)
    election=models.ForeignKey(Member,on_delete=models.CASCADE)
class Candidate_Election(models.Model):
    candidate_election=models.ForeignKey(Election,on_delete=models.CASCADE)
    candidate_election=models.ForeignKey(Member,on_delete=models.CASCADE)
    candidate_election=models.ForeignKey(Electoral_Position,on_delete=models.CASCADE)
    candidate_election=models.ForeignKey(Party,on_delete=models.CASCADE)
    


        