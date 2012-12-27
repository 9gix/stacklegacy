from django.contrib import admin
from stack.models import App, AppStack, Category
from ref.admin import ReferenceInline

class AppAdmin(admin.ModelAdmin):
    inlines = [ReferenceInline,]

class AppStackAdmin(admin.ModelAdmin):
    inlines = [ReferenceInline,]

admin.site.register(App, AppAdmin)
admin.site.register(AppStack, AppStackAdmin)
admin.site.register(Category)
