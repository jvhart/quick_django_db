from django.db import models

# Create your models here.
# See link below for list of Django models, i.e. data types:
#  https://www.webforefront.com/django/modeldatatypesandvalidation.html

class ExampleTable(models.Model):
    first_name = models.CharField(max_length=32,null=True,blank=True)
    last_name = models.CharField(max_length=32,null=False,blank=False)
    person_id = models.IntegerField(null=False)
    person_active = models.BooleanField(null=False,blank=False)
    record_create_dt = models.DateTimeField(auto_now=True)
    record_modify_dt = models.DateTimeField(auto_now=False,null=True)

    class Meta:
        db_table = 'example_table'
        ordering = ["last_name","first_name"]
        verbose_name = 'Example Table Records'
        verbose_name_plural = 'Example Table Records'

    def admin_list_display(self):
        return ['last_name', 'first_name','record_create_dt']
