from django.db import models


class Articles(models.Model):
    order_id = models.IntegerField(primary_key=True)
    prod_label = models.CharField(max_length=255)
    prod_ref = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    order_number = models.IntegerField()
    order_date = models.DateField()
    order_quantity = models.IntegerField()
    order_price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_number = models.IntegerField()
    delivery_quantity = models.IntegerField()
    delivery_date = models.DateField()

    def __str__(self):
        return self.prod_label

    class Meta:
        db_table = 'main_articles'


"""
<form class="d-flex mb-3" method="get">
        <div class="form-group me-3">

          <label for="search">Search by name:</label>
          <input type="text" id="search" name="q" value="{{ request.GET.q }}" class="form-control">
        </div>
        <button type="submit" class="btn btn-warning">Search</button>
      </form>
"""
