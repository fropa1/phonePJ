from .models import Telephone, Employees, Clients, Models, Feedback
from django.forms import ModelForm, TextInput, Textarea, EmailInput, NumberInput
class ClientForm15(ModelForm):
    class Meta:
        model = Clients
        fields=['name', 'numb', 'mail', 'color', 'count', 'empl','telephonemod']

        widgets = {
            'name': TextInput(attrs={
                'class': 'FIO',
                'placeholder': 'ФИО'
            }),
            'numb': NumberInput(attrs={
                'class': 'number',
                'placeholder': 'Номер телефона +7'
            }),
            'mail': EmailInput(attrs={
                'class': 'mail',
                'placeholder': 'Почта'
            }),
            'color': TextInput(attrs={
                'class': 'color',
                'placeholder': 'Цвет'
            }),
            'count': TextInput(attrs={
                'class': 'value',
                'placeholder': 'Количество'
            }),
            'empl': TextInput(attrs={
                'class': 'FIO-sot',
                'placeholder': 'ФИО Сотрудника(опционально)',
            }),
            'telephonemod': TextInput(attrs={
                'class': 'telephonemod',
                'value': 'Iphone 15',
                'readonly': 'readonly'
            })
        }
class ClientForm14(ModelForm):
    class Meta:
        model = Clients
        fields=['name', 'numb', 'mail', 'color', 'count', 'empl','telephonemod']

        widgets = {
            'name': TextInput(attrs={
                'class': 'FIO',
                'placeholder': 'ФИО'
            }),
            'numb': NumberInput(attrs={
                'class': 'number',
                'placeholder': 'Номер телефона в формате +7'
            }),
            'mail': EmailInput(attrs={
                'class': 'mail',
                'placeholder': 'Почта'
            }),
            'color': TextInput(attrs={
                'class': 'color',
                'placeholder': 'Цвет'
            }),
            'count': TextInput(attrs={
                'class': 'value',
                'placeholder': 'Количество'
            }),
            'empl': TextInput(attrs={
                'class': 'FIO-sot',
                'placeholder': 'ФИО Сотрудника(опционально)',
            }),
            'telephonemod': TextInput(attrs={
                'class': 'telephonemod',
                'value': 'Iphone 14',
                'readonly': 'readonly'
            })
        }
class ClientForm13(ModelForm):
    class Meta:
        model = Clients
        fields=['name', 'numb', 'mail', 'color', 'count', 'empl','telephonemod']

        widgets = {
            'name': TextInput(attrs={
                'class': 'FIO',
                'placeholder': 'ФИО'
            }),
            'numb': NumberInput(attrs={
                'class': 'number',
                'placeholder': 'Номер телефона в формате +7'
            }),
            'mail': EmailInput(attrs={
                'class': 'mail',
                'placeholder': 'Почта'
            }),
            'color': TextInput(attrs={
                'class': 'color',
                'placeholder': 'Цвет'
            }),
            'count': TextInput(attrs={
                'class': 'value',
                'placeholder': 'Количество'
            }),
            'empl': TextInput(attrs={
                'class': 'FIO-sot',
                'placeholder': 'ФИО Сотрудника(опционально)',
            }),
            'telephonemod': TextInput(attrs={
                'class': 'telephonemod',
                'value': 'Iphone 13 PRO MAX',
                'readonly': 'readonly'
            })
        }
class ClientForm11(ModelForm):
    class Meta:
        model = Clients
        fields=['name', 'numb', 'mail', 'color', 'count', 'empl','telephonemod']

        widgets = {
            'name': TextInput(attrs={
                'class': 'FIO',
                'placeholder': 'ФИО'
            }),
            'numb': NumberInput(attrs={
                'class': 'number',
                'placeholder': 'Номер телефона в формате +7'
            }),
            'mail': EmailInput(attrs={
                'class': 'mail',
                'placeholder': 'Почта'
            }),
            'color': TextInput(attrs={
                'class': 'color',
                'placeholder': 'Цвет'
            }),
            'count': TextInput(attrs={
                'class': 'value',
                'placeholder': 'Количество'
            }),
            'empl': TextInput(attrs={
                'class': 'FIO-sot',
                'placeholder': 'ФИО Сотрудника(опционально)',
            }),
            'telephonemod': TextInput(attrs={
                'class': 'telephonemod',
                'value': 'Iphone 11 PRO MAX',
                'readonly': 'readonly'
            })
        }
class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields=['fio', 'feed']

        widgets = {
            'fio': TextInput(attrs={
                'class': 'iname',
                'placeholder': 'Ваше Имя Фамилия'
            }),
            'feed': Textarea(attrs={
                'class': 'itext',
                'placeholder': 'Текст отзыва'
            })

        }
