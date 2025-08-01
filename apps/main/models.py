from django.db import models

class OlympicsCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Mentor(models.Model):
    name = models.CharField(max_length=100)
    experience = models.IntegerField()
    achieved = models.TextField()

    def __str__(self):
        return self.name


class Olympics(models.Model):
    category = models.ForeignKey(OlympicsCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    info = models.TextField()
    mentors = models.ManyToManyField(Mentor)
    resources = models.TextField()


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['category']
        verbose_name_plural = 'Olympics'
        verbose_name = 'Olympics'

