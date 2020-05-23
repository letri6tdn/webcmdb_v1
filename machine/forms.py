from django import forms

from .models import Machines

class MachineForm(forms.ModelForm):

    class Meta:
        model = Machines
        fields = (	'hostname', 
        			'last_known_location',
        			'ipv4',
        			'ipv6',
        			'operating_system',
        			'physical_virtual_machine',
        			'owner',
        			'administrator',
        			'u_of_a_tag_number',
        			'make_model',
        			'processor',
        			'ram_gb_field',
        			'storage_space_gb_field',
        			'gpu',
        			'serial_number',
        			'status',
        			'rack_number',
        			'srit_access',
        			'power_up',
        			'support_team',
        			'department',
        			'comments')
        widgets = {
            'hostname': forms.TextInput(attrs={'size':50}),
            'last_known_location': forms.TextInput(attrs={'size':50}),
            'ipv4': forms.TextInput(attrs={'size':50}),
            'ipv6': forms.TextInput(attrs={'size':50}),
            'operating_system': forms.TextInput(attrs={'size':50}),
            'physical_virtual_machine': forms.TextInput(attrs={'size':50}),
            'owner': forms.TextInput(attrs={'size':50}),
            'administrator': forms.TextInput(attrs={'size':50}),
            'u_of_a_tag_number': forms.TextInput(attrs={'size':50}),
            'make_model': forms.TextInput(attrs={'size':50}),
            'processor': forms.TextInput(attrs={'size':50}),
            'ram_gb_field': forms.TextInput(attrs={'size':50}),
            'storage_space_gb_field': forms.TextInput(attrs={'size':50}),
            'gpu': forms.TextInput(attrs={'size':50}),
            'serial_number': forms.TextInput(attrs={'size':50}),
            'status': forms.TextInput(attrs={'size':50}),
            'rack_number': forms.TextInput(attrs={'size':50}),
            'srit_access': forms.TextInput(attrs={'size':50}),
            'power_up': forms.TextInput(attrs={'size':50}),
            'support_team': forms.TextInput(attrs={'size':50}),
            'department': forms.TextInput(attrs={'size':50}),
            'comments': forms.TextInput(attrs={'size':50}),
        }