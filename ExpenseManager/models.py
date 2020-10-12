from django.db import models


class Expense(models.Model):
	expense_name = models.CharField(max_length=200)
	expense_money = models.IntegerField()
	expense_date = models.DateTimeField(auto_now=True)