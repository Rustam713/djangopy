from django.db import models

# Create your models here.
class New(models.Model):
    name = models.CharField(max_length=2222)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Новый'
        verbose_name_plural = 'Новые'
        ordering = ('id',)