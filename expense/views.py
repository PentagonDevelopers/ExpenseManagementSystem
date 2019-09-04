from django.shortcuts import render
from .models import Expense
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)

total_amount = 0


def home(request):
    return render(request, 'expense/home.html')


@login_required
def dashboard(request):
    expenses = Expense.objects.all()
    global total_amount
    total_amount = 0
    for expense in expenses:
        total_amount += expense.amount

    return render(request, 'expense/dashboard.html', {'data': expenses, 'total_amount': total_amount, 'div_show': True})


class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    fields = ['expense_for', 'amount', 'description']

    def form_valid(self, form):
        form.instance.by_whom = self.request.user
        return super().form_valid(form)
