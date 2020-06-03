from django.db import models


# Create your models here.

class Category(models.Model):
    post_type = models.CharField(max_length=20)

    class Meta:
        verbose_name = "categorie"

    def __str__(self):
        return self.post_type


class Post(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return '%s, %s' % (self.titre, self.contenu)


class Comment(models.Model):
    autheur = models.CharField(max_length=60)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return '%s, %s' % (self.autheur, self.contenu)
