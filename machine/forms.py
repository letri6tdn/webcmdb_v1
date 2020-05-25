from django import forms

from .models import Machines

class MachineForm(forms.ModelForm):

    class Meta:
        model = Machines

        fields = [	'hostname', 
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
        			'comments']
        widgets = {
            'hostname': forms.TextInput(attrs={'size':40}),
            'last_known_location': forms.TextInput(attrs={'size':40}),
            'ipv4': forms.TextInput(attrs={'size':40}),
            'ipv6': forms.TextInput(attrs={'size':40}),
            'operating_system': forms.TextInput(attrs={'size':40}),
            'physical_virtual_machine': forms.TextInput(attrs={'size':40}),
            'owner': forms.TextInput(attrs={'size':40}),
            'administrator': forms.TextInput(attrs={'size':40}),
            'u_of_a_tag_number': forms.TextInput(attrs={'size':40}),
            'make_model': forms.TextInput(attrs={'size':40}),
            'processor': forms.TextInput(attrs={'size':40}),
            'ram_gb_field': forms.TextInput(attrs={'size':40}),
            'storage_space_gb_field': forms.TextInput(attrs={'size':40}),
            'gpu': forms.TextInput(attrs={'size':40}),
            'serial_number': forms.TextInput(attrs={'size':40}),
            'status': forms.TextInput(attrs={'size':40}),
            'rack_number': forms.TextInput(attrs={'size':40}),
            'srit_access': forms.TextInput(attrs={'size':40}),
            'power_up': forms.TextInput(attrs={'size':40}),
            'support_team': forms.TextInput(attrs={'size':40}),
            'department': forms.TextInput(attrs={'size':40}),
            'comments': forms.Textarea(),
        }