from django.contrib import admin
from django.contrib.contenttypes import generic
from ref.models import Reference

class ReferenceInline(generic.GenericTabularInline):
    model = Reference
