from django.contrib import admin
from products.models import ProductTable,Order_history,Payment_history
# Register your models here.
admin.site.register(ProductTable)
admin.site.register(Order_history)
admin.site.register(Payment_history)
