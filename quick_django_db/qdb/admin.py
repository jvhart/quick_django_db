from django.contrib import admin
from quick_django_db.settings import REGISTERED_CLASSES

tbl_register_str = '''
from .models import {}
x = {}()
class {}Admin(admin.ModelAdmin):
      list_display = x.list_display()
admin.site.register({},{}Admin)
'''

for c in REGISTERED_CLASSES:
    exec(tbl_register_str.format(*5 * [c]))
