from django.db import models

# Create your models here.
class About(models.Model):
    short_description = models.Textfield()
    description = models.Textfield()
    image = models.ImageField(upload_to='about')

    class Meta:
        verbose_name='About me'
        verbose_name_plural = 'About me'
    
    def __str__(self):
        return 'About me'

#service model
class Service(models.Model):
    name =models.CharField(max_length=100, verbose_name='service name')
    description = models.TextField(verbose_name='About service')

    def __str__(self):
        return self.name

#recent work model
class RecentWork(models.Model):
    title = models.CharField(max_length=100,verbose_name='work title')
    image = models.ImageField(upload_to='works')

    def __str__(self):
        return self.title



#client model
class Client(models.Model):
    name = models.CharField(max_lenth=100, verbose_name='client name')
    description = models.TextField(verbose_name='client say')
    image = models.ImageField(upload_to='clients', default='default.png')

    def __str__(self):
        return self.name