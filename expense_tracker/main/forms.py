from django import forms

from expense_tracker.main.models import Expense


class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class EditExpenseForm(CreateExpenseForm):
    pass


class DeleteExpenseForm(CreateExpenseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
