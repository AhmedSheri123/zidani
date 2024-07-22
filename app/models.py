from django.db import models

class Message(models.Model):
    user = models.CharField(max_length=100)
    message = models.TextField(null=True, blank=True)
    pdf = models.FileField(upload_to='files/',null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
