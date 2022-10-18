from django.shortcuts import render, redirect

from expense_tracker.main.models import Expense
from expense_tracker.profiles.forms import CreateProfileForm, EditProfileForm
from expense_tracker.profiles.models import Profile


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('snow_home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }
    return render(request, 'core/home-no-profile.html', context)


def show_profile(request):
    profile = Profile.objects.first()
    expenses = Expense.objects.all()
    # todo: refactor, remove duplication
    budget_left = profile.budget - sum([x.price for x in expenses])
    context = {
        'items': expenses.count(),
        'budget_left': budget_left,
        'profile': profile,
    }

    return render(request, 'profile/profile.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show_profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile/profile-edit.html', context=context)


def delete_profile(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        profile.delete()
        Expense.objects.all().delete()
        return redirect('snow_home')
    else:
        context = {
        }

        return render(request, 'profile/profile-delete.html', context)
