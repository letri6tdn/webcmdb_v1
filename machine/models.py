# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Machines(models.Model):
    id_machine = models.TextField(db_column='ID', primary_key=True,blank=True, null=False)  # Field name made lowercase.
    hostname = models.TextField(db_column='Hostname', blank=True, null=True)  # Field name made lowercase.
    last_known_location = models.TextField(db_column='Last Known Location', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ipv4 = models.TextField(db_column='IPv4', blank=True, null=True)  # Field name made lowercase.
    ipv6 = models.TextField(db_column='IPv6', blank=True, null=True)  # Field name made lowercase.
    operating_system = models.TextField(db_column='Operating System', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    physical_virtual_machine = models.TextField(db_column='Physical/Virtual Machine', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    owner = models.TextField(db_column='Owner', blank=True, null=True)  # Field name made lowercase.
    administrator = models.TextField(db_column='Administrator', blank=True, null=True)  # Field name made lowercase.
    u_of_a_tag_number = models.TextField(db_column='U of A Tag Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    make_model = models.TextField(db_column='Make/Model', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    processor = models.TextField(db_column='Processor', blank=True, null=True)  # Field name made lowercase.
    ram_gb_field = models.TextField(db_column='RAM (GB)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    storage_space_gb_field = models.TextField(db_column='Storage Space (GB)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    gpu = models.TextField(db_column='GPU', blank=True, null=True)  # Field name made lowercase.
    serial_number = models.TextField(db_column='Serial Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    rack_number = models.TextField(db_column='Rack Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    srit_access = models.TextField(db_column='SRIT Access', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    power_up = models.TextField(db_column='Power Up', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    support_team = models.TextField(db_column='Support Team', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    department = models.TextField(db_column='Department', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'machines'
        verbose_name_plural = 'machines'
