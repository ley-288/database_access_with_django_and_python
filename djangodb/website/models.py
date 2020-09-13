from django.db import models

#step 11
class Member(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    passwd = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.fname + ' ' + self.lname #admin display and homepage
