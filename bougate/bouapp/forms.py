from django import forms
from datetime import datetime
from .models import *


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ['created_by', 'create_date', 'last_update_date', 'last_updated_by']
        fields = ['item_name', 'serial_number', 'type', 'person_name', 'created_by', 'create_date', 'last_update_date',
                  'last_updated_by']
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control'},),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'person_name': forms.Select(attrs={'class': 'form-control'}),
            'registered_by': forms.TextInput(attrs={'class': 'form-control'}),
            'create_date': forms.DateField(initial=datetime.date),
            'last_update_date': forms.DateField(initial=datetime.date),
            'last_updated_by': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'Item_name': 'Item Name:',
            'serial_number': 'Item Serial_number:',
            'type': 'Item Type',
            'person_name': 'Person Name',
            'created_by': 'Who registered it:',
            'create_date': 'Enter the create date:',
            'last_update_date': "last_update_date:",
            'last_updated_by': "last_updated_by:",

        }


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ['created_by', 'create_date', 'last_update_date', 'last_updated_by']
        fields = ['first_name', 'last_name', 'id_number', 'category', 'organisation', 'department', 'telephone', 'email',
                  'created_by', 'create_date', 'last_update_date', 'last_updated_by']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=category_select, attrs={'class': 'form-control'}),
            'organisation': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'created_by': forms.TextInput(attrs={'class': 'form-control'}),
            'create_date': forms.DateField(initial=datetime.date),
            'last_update_date': forms.DateField(initial=datetime.date),
            'last_updated_by': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name',
            'id_number': 'ID Number',
            'category': 'Category',
            'organisation': 'Organisation:',
            'department': 'Department:',
            'telephone': 'Telephone:',
            'email': 'Email:',
            'created_by': 'Who created this person:',
            'create_date': 'Enter the create date:',
            'last_update_date': "last_update_date:",
            'last_updated_by': "last_updated_by:",

        }


class BadgeForm(forms.ModelForm):
    class Meta:
        model = Badge
        exclude = ['time_out', 'created_by', 'create_date', 'last_update_date', 'last_updated_by']
        fields = ['item_name', 'person_name', 'location', 'item_owner', 'time_in', 'time_out',
                  'created_by', 'last_update_date', 'last_updated_by']
        widgets = {
            'item_name': forms.Select(attrs={'class': 'form-control'}),
            'person_name': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(choices=gate_select, attrs={'class': 'form-control'}),
            'item_owner': forms.Select(choices=item_owner, attrs={'class': 'form-control'}),
            'time_in': forms.TextInput(attrs={'class': 'form-control'}),
            'time_out': forms.TextInput(attrs={'class': 'form-control'}),
            'created_by': forms.TextInput(attrs={'class': 'form-control'}),
            'create_date': forms.DateField(initial=datetime.date),
            'last_update_date': forms.DateField(initial=datetime.date),
            'last_updated_by': forms.DateField(initial=datetime.date),
        }
        labels = {
            'item_name': 'Item Name:',
            'person_name': 'Person Name(Item Carrier)',
            'location': 'Gate used',
            'item_owner': 'Item owner',
            'time_in': 'Time in',
            'time_out': 'Time out',
            'created_by': 'Who registered it:',
            'create_date': 'Enter the create date:',
            'last_update_date': "last_update_date:",
            'last_updated_by': "last_updated_by:",
        }


# badging out form
class BadgeFormOut(forms.ModelForm):
    class Meta:
        model = Badge
        exclude = ['created_by', 'create_date', 'last_update_date', 'last_updated_by']
        fields = ['item_name', 'person_name', 'location', 'item_owner', 'time_in', 'time_out',
                  'created_by', 'last_update_date', 'last_updated_by']
        widgets = {
            'item_name': forms.Select(attrs={'class': 'form-control'}),
            'person_name': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(choices=gate_select, attrs={'class': 'form-control'}),
            'item_owner': forms.Select(choices=item_owner, attrs={'class': 'form-control'}),
            'time_in': forms.TextInput(attrs={'class': 'form-control'}),
            'time_out': forms.TextInput(attrs={'class': 'form-control'}),
            'created_by': forms.TextInput(attrs={'class': 'form-control'}),
            'create_date': forms.DateField(initial=datetime.date),
            'last_update_date': forms.DateField(initial=datetime.date),
            'last_updated_by': forms.DateField(initial=datetime.date),
        }
        labels = {
            'item_name': 'Item Name:',
            'person_name': 'Person Name(Item Carrier)',
            'location': 'Gate used',
            'item_owner': 'Item owner',
            'time_in': 'Time in',
            'time_out': 'Time out',
            'created_by': 'Who registered it:',
            'create_date': 'Enter the create date:',
            'last_update_date': "last_update_date:",
            'last_updated_by': "last_updated_by:",
        }
