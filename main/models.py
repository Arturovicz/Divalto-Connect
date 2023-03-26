from django.db import models


class Articles(models.Model):
    article_id = models.IntegerField(primary_key=True)
    article_label = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.CharField(max_length=255)
    dimensions = models.DecimalField(max_digits=10, decimal_places=2)
    dimension_unit = models.CharField(max_length=5)
    fournisseur = models.CharField(max_length=60)
    stock = models.IntegerField()
    last_entry = models.DateField()

    def __str__(self):
        return self.article_label


class Plot(models.Model):
    article_id = models.IntegerField()
    stock = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.article_id} - {self.date}"


