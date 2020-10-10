# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Hobby, Value, Category, ConceptCategory, Concept, Project, Skill, Collaborator, ValueLevel, ExplorationDate, Role, Task, Candidacy, Company

# Register your models here.

@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display   = ('name',)
    ordering       = ('id', )
    search_fields  = ('name',)


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    list_display   = ('name','level')
    ordering       = ('id', )
    search_fields  = ('name',)


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

    
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display   = ('name',)
    ordering       = ('id', )
    search_fields  = ('name',)


@admin.register(Collaborator)
class CollaboratorAdmin(admin.ModelAdmin):
    list_display   = ('user','job', )
    ordering       = ('user', )
    search_fields  = ('job',)


@admin.register(ValueLevel)
class ValueLevelAdmin(admin.ModelAdmin):
    list_display   = ('collaborator',)
    ordering       = ('id', )

@admin.register(ExplorationDate)
class ExplorationDateAdmin(admin.ModelAdmin):
    list_display   = ('collaborator','concept', 'date')
    ordering       = ('id', )

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display   = ('collaborator','role_name', 'project')
    ordering       = ('id', )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display   = ('description','role')
    ordering       = ('id', )


@admin.register(Candidacy)
class CandidacyAdmin(admin.ModelAdmin):
    list_display   = ('role','collaborator', 'description')
    ordering       = ('id', )


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display   = ('name',)
    ordering       = ('id', )
    search_fields  = ('name',)

