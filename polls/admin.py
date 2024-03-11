from django.contrib import admin
from polls.models import Campus, Course, Member, ElectoralPosition, Party, Election, ElectionMember, CandidateElection

# Register your models here.
admin.site.register(Campus)
admin.site.register(Course)
admin.site.register(Member)
admin.site.register(ElectoralPosition)
admin.site.register(Party)
admin.site.register(Election)
admin.site.register(ElectionMember)
admin.site.register(CandidateElection)
