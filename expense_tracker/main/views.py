from django.shortcuts import render, redirect

from expense_tracker.main.forms import CreateExpenseForm, EditExpenseForm, DeleteExpenseForm
from expense_tracker.main.models import Expense
from expense_tracker.profiles.models import Profile


def show_home(request):
    is_registered = True if Profile.objects.all().count() > 0 else False
    if is_registered:
        profile = Profile.objects.first()
        expenses = Expense.objects.all()
        budget_left = profile.budget - sum([x.price for x in expenses])
        context = {
            'budget': profile.budget,
            'expenses': expenses,
            'budget_left': budget_left,
        }
        return render(request, 'core/home-with-profile.html', context)
    else:
        return redirect('create_profile')


def create_expense(request):
    if request.method == 'POST':
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('snow_home')
    else:
        form = CreateExpenseForm()

    context = {
        'form': form,
    }

    return render(request, 'expense/expense-create.html', context=context)


def edit_expense(request, expense_id):
    expense = Expense.objects.get(pk=expense_id)

    if request.method == 'POST':
        form = EditExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('snow_home')
    else:
        form = EditExpenseForm(instance=expense)

    context = {
        'expense': expense,
        'form': form,
    }

    return render(request, 'expense/expense-edit.html', context)


def delete_expense(request, expense_id):
    expense = Expense.objects.get(pk=expense_id)

    if request.method == 'POST':
        expense.delete()
        return redirect('snow_home')
    else:
        form = DeleteExpenseForm(instance=expense)

    context = {
        'expense': expense,
        'form': form,
    }

    return render(request, 'expense/expense-delete.html', context)

