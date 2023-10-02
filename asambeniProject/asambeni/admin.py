from django.contrib import admin
from .models import CustomUser, Learner, Driver, AreaOfOperation, EndOfOperationArea

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Learner)
admin.site.register(Driver)
admin.site.register(AreaOfOperation)
admin.site.register(EndOfOperationArea)