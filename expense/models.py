from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Expense(models.Model):
    expense_for = models.CharField(max_length=40, null=False)
    amount = models.FloatField(max_length=6, default=0)
    description = models.TextField()
    date_of_expense = models.DateTimeField(default=timezone.now)
    by_whom = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'expense for {} by {}'.format(self.expense_for, self.by_whom)

    def get_absolute_url(self):
        return reverse('dashboard')
