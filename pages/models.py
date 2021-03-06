from django.db import models


# Create your models here.


class Feedback(models.Model):
    prenom = models.CharField(max_length=200)
    nom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Feedback"

    def __str__(self):
        return '%s, %s' % (self.prenom, self.email)


class Membership(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=100)
    areacode = models.IntegerField()
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=100, unique=True)
    profession = models.CharField(max_length=400)
    country = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s, %s' % (self.firstname, self.email)

