from django.contrib import admin
from .models import PersonalInfo, EducationalProgram, Management, Classmate

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'city', 'is_active')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('is_active', 'city')
    fieldsets = (
        ('Основная информация', {
            'fields': ('first_name', 'last_name', 'middle_name', 'photo', 'email', 'phone')
        }),
        ('Дополнительная информация', {
            'fields': ('birth_date', 'city', 'resume')
        }),
        ('Статус', {
            'fields': ('is_active',)
        }),
    )

@admin.register(EducationalProgram)
class EducationalProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'university', 'faculty', 'degree_level', 'start_year', 'end_year', 'is_active')
    search_fields = ('name', 'university', 'faculty')
    list_filter = ('degree_level', 'is_active', 'university')
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'university', 'faculty', 'program_url', 'degree_level')
        }),
        ('Период обучения', {
            'fields': ('duration', 'start_year', 'end_year')
        }),
        ('Описание программы', {
            'fields': ('what_i_study', 'what_i_learn', 'advantages', 'career_prospects')
        }),
        ('Статус', {
            'fields': ('is_active',)
        }),
    )

@admin.register(Management)
class ManagementAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'role', 'department', 'email', 'is_active')
    search_fields = ('first_name', 'last_name', 'email', 'department')
    list_filter = ('role', 'is_active', 'department')
    fieldsets = (
        ('Основная информация', {
            'fields': ('first_name', 'last_name', 'middle_name', 'photo', 'role')
        }),
        ('Контактная информация', {
            'fields': ('email', 'phone')
        }),
        ('Дополнительная информация', {
            'fields': ('department', 'academic_degree', 'bio', 'order')
        }),
        ('Статус', {
            'fields': ('is_active',)
        }),
    )

@admin.register(Classmate)
class ClassmateAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'group_number', 'city', 'email', 'is_close_friend', 'is_active')
    search_fields = ('first_name', 'last_name', 'email', 'group_number', 'city')
    list_filter = ('is_close_friend', 'is_active', 'city', 'group_number')
    fieldsets = (
        ('Основная информация', {
            'fields': ('first_name', 'last_name', 'middle_name', 'photo')
        }),
        ('Контактная информация', {
            'fields': ('email', 'phone', 'city', 'group_number')
        }),
        ('Дополнительная информация', {
            'fields': ('interests', 'is_close_friend')
        }),
        ('Социальные сети', {
            'fields': ('social_vk', 'social_telegram', 'social_instagram')
        }),
        ('Статус', {
            'fields': ('is_active',)
        }),
    )
