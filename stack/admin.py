from django.contrib import admin
from stack.models import App, AppStack, Category, Architecture
from ref.admin import ReferenceInline

class ArchitectureInline(admin.TabularInline):
    model = Architecture

class ArchitectureAdmin(admin.ModelAdmin):
    inlines = [ReferenceInline,]

class AppAdmin(admin.ModelAdmin):
    inlines = [ArchitectureInline,]

class AppStackAdmin(admin.ModelAdmin):
    inlines = [ReferenceInline,]

admin.site.register(App, AppAdmin)
admin.site.register(AppStack, AppStackAdmin)
admin.site.register(Category)
admin.site.register(Architecture, ArchitectureAdmin)
