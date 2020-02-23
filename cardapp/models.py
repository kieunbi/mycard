from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=200)
    card_name=models.TextField()
    pub_date=models.DateTimeField('data published')
    body=models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]   

class Card(models.Model):
    card_name=models.TextField()
    card_sort=models.TextField()

    card_price_min=models.IntegerField()

    card_movie = models.DecimalField(max_digits=8, decimal_places=2)
    card_bus = models.DecimalField(max_digits=8, decimal_places=2)
    card_coffee = models.DecimalField(max_digits=8, decimal_places=2)
    card_mart = models.DecimalField(max_digits=8, decimal_places=2)

    card_image=models.ImageField()


    def __str__(self):
        return self.card_name


