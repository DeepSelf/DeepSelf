# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Hobby, Value, Category, ConceptCategory, Concept, Project, Skill, Collaborator, ValueLevel, ExplorationDate, Role, Task, Candidacy, Company, SkillLevel, Personnality, PersonnalityLevel, UnderPersonnality, UnderPersonnalityLevel, UnderSkill, UnderSkillLevel

# Register your models here.

@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display   = ('name',)
    ordering       = ('id', )
    search_fields  = ('name',)


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    list_display   = ('name',)
    ordering       = ('id', )
    search_fields  = ('name',)

class UnderPersonnalityInline(admin.TabularInline):
    model = UnderPersonnality
    fieldsets = (
        (None, {"fields": ('name', 'color'),}),
    )
    
    extra = 0

@admin.register(Personnality)
class PersonnalityAdmin(admin.ModelAdmin):
    list_display   = ('name',)
    ordering       = ('id', )
    search_fields  = ('name',)
    inlines = (UnderPersonnalityInline,)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display   = ('name',)
    ordering       = ('id', )
    search_fields  = ('name',)


@admin.register(ConceptCategory)
class ConceptCategoryAdmin(admin.ModelAdmin):
    list_display   = ('name',)
    ordering       = ('id', )
    search_fields  = ('name',)


@admin.register(Concept)
class ConceptAdmin(admin.ModelAdmin):
    list_display   = ('name','description')
    ordering       = ('id', )
    search_fields  = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display   = ('name','description','state')
    ordering       = ('id', )
    search_fields  = ('name',)

class UnderSkillInline(admin.TabularInline):
    model = UnderSkill
    fieldsets = (
        (None, {"fields": ('name', 'color'),}),
    )
    
    extra = 0
    
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display   = ('name',)
    ordering       = ('id', )
    search_fields  = ('name',)
    inlines = (UnderSkillInline,)

class TaskInline(admin.TabularInline):
    model = Task
    fieldsets = (
        (None, {"fields": ('description',),}),
    )
    
    extra = 0

class RoleInline(admin.TabularInline):
    model = Role
    fieldsets = (
        (None, {"fields": ('role_name', 'project'),}),
    )
    
    extra = 0

class CandidacyInline(admin.TabularInline):
    model = Candidacy
    fieldsets = (
        (None, {"fields": ('role', 'description'),}),
    )
    
    extra = 0

class PersonnalityLevelInline(admin.TabularInline):
    model = PersonnalityLevel
    fieldsets = (
        (None, {"fields": ('personnality', 'personnality_level'),}),
    )
    readonly_fields = ('personnality',)
    
    extra = 0

class UnderPersonnalityLevelInline(admin.TabularInline):
    model = UnderPersonnalityLevel
    fieldsets = (
        (None, {"fields": ('underpersonnality', 'underpersonnality_level'),}),
    )
    
    extra = 0

class ValueLevelInline(admin.TabularInline):
    model = ValueLevel
    fieldsets = (
        (None, {"fields": ('value', 'value_level'),}),
    )
    
    extra = 0

class SkillLevelInline(admin.TabularInline):
    model = SkillLevel
    fieldsets = (
        (None, {"fields": ('skill', 'skill_level'),}),
    )
    
    extra = 0

class UnderSkillLevelInline(admin.TabularInline):
    model = UnderSkillLevel
    fieldsets = (
        (None, {"fields": ('underskill', 'underskill_level'),}),
    )
    
    extra = 0

class ExplorationDateInline(admin.TabularInline):
    model = ExplorationDate
    fieldsets = (
        (None, {"fields": ('concept', 'date'),}),
    )
    readonly_fields = ('concept','date')
    extra = 0


@admin.register(Collaborator)
class CollaboratorAdmin(admin.ModelAdmin):
    list_display   = ('user','job', )
    ordering       = ('user', )
    search_fields  = ('job',)
    inlines = (PersonnalityLevelInline,UnderPersonnalityLevelInline, ValueLevelInline, SkillLevelInline, UnderSkillLevelInline, RoleInline, CandidacyInline, ExplorationDateInline)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display   = ('description','role')
    ordering       = ('id',)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display   = ('name',)
    ordering       = ('id',)
    search_fields  = ('name',)

