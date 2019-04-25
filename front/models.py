from django.db import models

class Level(models.Model):
    name = models.CharField(max_length = 120)

    def __str__(self):
        return self.name

class Kid(models.Model):
    name = models.CharField(max_length = 120)
    surname = models.CharField(max_length = 120)
    birthday = models.DateField()
    mail = models.EmailField(blank = True)
    phone = models.CharField(max_length = 20, blank = True)
    school_lvl = models.ForeignKey('Level', on_delete = models.CASCADE)
    root = models.ForeignKey('Parent', on_delete = models.CASCADE)

    def __str__(self):
        return self.name.title() + ' ' + self.surname.title()

class Parent(models.Model):
    name = models.CharField(max_length = 120)
    surname = models.CharField(max_length = 120)
    address = models.CharField(max_length = 255)
    zip_code = models.PositiveIntegerField()
    city = models.CharField(max_length = 255)
    mail = models.EmailField()
    phone = models.CharField(max_length = 20, blank = True)
    kids = models.ManyToManyField('Kid')

    def __str__(self):
        return self.name.title() + ' ' + self.surname.title()

class Plan(models.Model):
    name = models.CharField(max_length = 120)
    duration = models.DurationField()
    price = models.FloatField()

    def __str__(self):
        return self.name + '@' + str(self.price)

    class Meta:
        ordering = ['duration']

class Topic(models.Model):
    name = models.CharField(max_length = 120)
    img = models.ImageField()

    def __str__(self):
        return self.name
