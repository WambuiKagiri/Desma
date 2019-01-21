from django.contrib import admin
from .models import subscriber
from .models import listings_waiting_list
from .models import customer
from .models import properties
from .models import booked_viewings
from .models import property_admin
# Register your models here.

admin.site.register(subscriber)
admin.site.register(listings_waiting_list)
admin.site.register(customer)
admin.site.register(booked_viewings)
admin.site.register(properties,property_admin)


class property_admin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(property_admin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield