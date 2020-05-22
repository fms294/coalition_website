from django.db import models

# Create your models here.


class Feedback(models.Model):
    firstname = models.CharField(max_length=200)
    lastname= models.CharField(max_length=100)
    areacode = models.IntegerField()
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=100)
    may_contact = models.BooleanField()
    feedback=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural= "Feedback"

    def __str__(self):
        return self.firstname + "-" + self.email


class Membership(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=100)
    areacode = models.IntegerField()
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=100)
    profession=models.CharField(max_length=200)
    country= models.CharField(max_length=50)

    def __str__(self):
        return  self.firstname + "-" + self.email

