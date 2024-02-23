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
    member_avatar = models.CharField(max_length=200)
    member_campus = models.ForeignKey(Campus,on_delete=models.CASCADE)
    member_course = models.ForeignKey(Course, on_delete=models.CASCADE)

class ElectoralPosition(models.Model):
    electoral_position_name=models.CharField(max_length=100)

class Party(models.Model):
    party_name=models.CharField(max_length=100)

class Election(models.Model):
     election_date_created=models.DateField()
     election_closing_date=models.DateField()
     election_is_active=models.BooleanField()

class ElectionMember(models.Model):
    election_member_election=models.ForeignKey(Election,on_delete=models.CASCADE)
    election_member_member=models.ForeignKey(Member,on_delete=models.CASCADE)

class CandidateElection(models.Model):
    candidate_election_election=models.ForeignKey(Election,on_delete=models.CASCADE)
    candidate_election_member=models.ForeignKey(Member,on_delete=models.CASCADE)
    candidate_election_electoral_position=models.ForeignKey(ElectoralPosition,on_delete=models.CASCADE)
    candidate_election_party=models.ForeignKey(Party,on_delete=models.CASCADE)
    candidate_election_member_number_votes=models.IntegerField()
    


        