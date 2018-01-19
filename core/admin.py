#encoding: utf-8

from __future__ import unicode_literals
from django.contrib import admin
from .models import *

class TeacherAdmin(admin.ModelAdmin):
    list_display=('name', 'course', 'title', 'phone1', 'phone2', 'email', 'area', 'contract_type', 'active', 'effective',)
    search_fields=('name', 'course', 'title', 'area', 'contract_type', 'active', 'effective',)
    ordering=('name', 'course', 'title', 'area', 'contract_type', 'active', 'effective',)
    fields=('name', 'course', 'title', 'phone1', 'phone2', 'email', 'area', 'contract_type', 'active', 'effective',)

class AreaAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=('name',)
    ordering=('name',)
    fields=('name',)

class TitleAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=('name',)
    ordering=('name',)
    fields=('name',)

class DisciplineAdmin(admin.ModelAdmin):
    list_display=('name', 'short_name', 'grid', 'ementa', 'block', 'area', 'work_load',)
    search_fields=('name', 'short_name', 'grid', 'block', 'area',)
    ordering=('name', 'short_name', 'grid', 'block', 'area',)
    fields=('name', 'short_name', 'grid', 'ementa', 'block', 'area', 'work_load',)

class CourseGridAdmin(admin.ModelAdmin):
    list_display=('name', 'course', 'date_ini', 'date_term', 'active',)
    search_fields=('name', 'course', 'date_ini', 'date_term', 'active',)
    ordering=('name', 'course', 'date_ini', 'date_term', 'active',)
    fields=('name', 'course', 'date_ini', 'date_term', 'active',)

class CourseAdmin(admin.ModelAdmin):
    list_display=('name', 'short_name', 'campus', 'active',)
    search_fields=('name', 'short_name', 'campus', 'active',)
    ordering=('name', 'short_name', 'campus', 'active',)
    fields=('name', 'short_name', 'campus', 'active',)

class CampusAdmin(admin.ModelAdmin):
    list_display=('name', 'add_street', 'add_no', 'add_neighbor', 'add_city', 'add_uf', 'add_zip', 'phone1', 'phone2', 'email', 'site', 'active',)
    search_fields=('name', 'site', 'active',)
    ordering=('name', 'site', 'active',)
    fields=('name', 'add_street', 'add_no', 'add_neighbor', 'add_city', 'add_uf', 'add_zip', 'phone1', 'phone2', 'email', 'site', 'active',)

class UserAdmin(admin.ModelAdmin):
    list_display=('name', 'campus', 'course',)
    search_fields=('name', 'campus', 'course',)
    ordering=('name', 'campus', 'course',)
    fields=('name', 'campus', 'course',)

class ContractTypeAdmin(admin.ModelAdmin):
    list_display=('name', 'wk_teaching', 'wk_resext', 'wk_compl', 'active',)
    search_fields=('name', 'active',)
    ordering=('name', 'active',)
    fields=('name', 'wk_teaching', 'wk_resext', 'wk_compl', 'active',)

class ActivityTypeAdmin(admin.ModelAdmin):
    list_display=('name', 'wk_week', 'wk_limit', 'nature',)
    search_fields=('name', 'nature',)
    ordering=('name', 'nature',)
    fields=('name', 'wk_week', 'wk_limit', 'nature',)

class ActivityAdmin(admin.ModelAdmin):
    list_display=('teacher', 'act_type', 'quantity', 'date_ini', 'date_term', 'observations',)
    search_fields=('teacher', 'act_type', 'quantity', 'date_ini', 'date_term', 'observations',)
    ordering=('teacher', 'act_type', 'quantity', 'date_ini', 'date_term', 'observations',)
    fields=('teacher', 'act_type', 'quantity', 'date_ini', 'date_term', 'observations',)

class SemesterAdmin(admin.ModelAdmin):
    list_display=('name', 'date_ini', 'date_term',)
    search_fields=('name', 'date_ini', 'date_term',)
    ordering=('name', 'date_ini', 'date_term',)
    fields=('name', 'date_ini', 'date_term',)

class OfferAdmin(admin.ModelAdmin):
    list_display=('name', 'course', 'date_ini', 'date_term', 'semester',)
    search_fields=('name', 'course', 'date_ini', 'date_term', 'semester',)
    ordering=('name', 'course', 'date_ini', 'date_term', 'semester',)
    fields=('name', 'course', 'date_ini', 'date_term', 'semester',)

class EnrollmentAdmin(admin.ModelAdmin):
    list_display=('discipline', 'teacher', 'offer',)
    search_fields=('discipline', 'teacher', 'offer',)
    ordering=('discipline', 'teacher', 'offer',)
    fields=('discipline', 'teacher', 'offer',)

class NatureAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=('name',)
    ordering=('name',)
    fields=('name',)

admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Area,AreaAdmin)
admin.site.register(Title,TitleAdmin)
admin.site.register(Discipline,DisciplineAdmin)
admin.site.register(CourseGrid,CourseGridAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Campus,CampusAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(ContractType,ContractTypeAdmin)
admin.site.register(ActivityType,ActivityTypeAdmin)
admin.site.register(Activity,ActivityAdmin)
admin.site.register(Semester,SemesterAdmin)
admin.site.register(Offer,OfferAdmin)
admin.site.register(Enrollment,EnrollmentAdmin)
admin.site.register(Nature,NatureAdmin)
