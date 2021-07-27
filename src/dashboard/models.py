from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class ReportProblem(models.Model):
    email = models.EmailField(max_length=200)
    issue = models.CharField(max_length=100)
    description = models.TextField(null=False)
    
    def __str__(self):
        return self.issue


class Tips(models.Model):
    tips = models.CharField(max_length=250)
    
    def __str__(self):
        return self.tips

class Package(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    seats = models.IntegerField()
    date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to="packages/")
    org = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Book(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.package.title+' booked by '+ self.user.email