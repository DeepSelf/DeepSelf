# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Hobby(models.Model):
    name = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = _("Hobby")
        verbose_name_plural = _("Hobbies")

    def __str__(self):
        return self.name

class Value(models.Model):
    
    name = models.CharField(max_length=100)
    level = models.FloatField(default=0.0)

    class Meta:
        verbose_name = _("Valeur")
        verbose_name_plural = _("Valeurs")

    def __str__(self):
        return self.name

class Category(models.Model):
    
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = _("Categorie")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class ConceptCategory(models.Model):
    
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = _("Catégorie de concepts")
        verbose_name_plural = _("Catégories de concepts")

    def __str__(self):
        return self.name

class Company(models.Model):
    
    name = models.CharField(max_length=100)
    competencies_score = models.FloatField(default=0.0)
    life_quality_score = models.FloatField(default=0.0)

    class Meta:
        verbose_name = _("Entreprise")
        verbose_name_plural = _("Entreprises")

    def __str__(self):
        return self.name


class Concept(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    proxim_concepts = models.ManyToManyField("self")
    categories = models.ManyToManyField(ConceptCategory, related_name="contains")

    class Meta:
        verbose_name = _("Concept")
        verbose_name_plural = _("Concepts")

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    state = models.CharField(max_length=50, default="starting")
    values = models.ManyToManyField(Value, related_name="needs")
    category = models.ManyToManyField(Category, related_name="contains")
    company = models.ForeignKey(Company, null=True, related_name="projects", on_delete=models.CASCADE)  

    class Meta:
        verbose_name = _("Projet")
        verbose_name_plural = _("Projets")

    def __str__(self):
        return self.name


class Skill(models.Model):
    
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Compétence")
        verbose_name_plural = _("Compétences")

    def __str__(self):
        return self.name


class Collaborator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    picture = models.ImageField(upload_to="profile_pictures")
    job = models.CharField(null=True, max_length=200)
    arrival_date = models.DateField(auto_now=True)
    hobbies = models.ManyToManyField(Hobby, related_name="hobbies")
    projects = models.ManyToManyField(Project, related_name="members", through="Role")
    value_level = models.ManyToManyField(Value, related_name="owner", through="ValueLevel")
    skills = models.ManyToManyField(Skill, related_name="can")
    extroversion = models.FloatField(default=0.0)
    conscientiousness = models.FloatField(default=0.0)
    neurotism = models.FloatField(default=0.0)
    opening = models.FloatField(default=0.0)
    pleasantness = models.FloatField(default=0.0)
    visited_concepts_list = models.ManyToManyField(Concept, related_name="explorers", through="ExplorationDate")
    recommended_concepts = models.ManyToManyField(Concept, related_name="pretenders")
    company = models.ForeignKey(Company, null=True, related_name="employees", on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = _("Collaborateur")
        verbose_name_plural = _("Collaborateurs")

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name



class ValueLevel(models.Model):
    value_level = models.FloatField(default=0.0)
    value = models.ForeignKey(Value, on_delete=models.CASCADE)
    collaborator = models.ForeignKey(Collaborator, on_delete=models.CASCADE)    

    class Meta:
        verbose_name = _("ValueLevel")
        verbose_name_plural = _("ValueLevels")

    def __str__(self):
        return "{0} {1} a {2}% de {3}".format(self.collaborator.user.first_name, self.collaborator.user.last_name, self.value_level, self.value.name)


class ExplorationDate(models.Model):

    date = models.DateField(auto_now=True)
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE)
    collaborator = models.ForeignKey(Collaborator, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Date d'exploration")
        verbose_name_plural = _("Dates d'exploration")

    def __str__(self):
        return "{0} {1} a vu {2} le {3}".format(self.collaborator.user.first_name, self.collaborator.user.last_name, self.concept.name, self.date)




class Role(models.Model):
    role_name = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    collaborator = models.ForeignKey(Collaborator, null=True, on_delete=models.SET_NULL)
    

    class Meta:
        verbose_name = _("Role")
        verbose_name_plural = _("Roles")

    def __str__(self):
        return "rôle de {0} dans le projet {1}".format(self.role_name, self.project.name)


class Task(models.Model):
    description = models.TextField(max_length=2000)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Tâche")
        verbose_name_plural = _("Tâches")

    def __str__(self):
        return self.description

    
class Candidacy(models.Model):
    
    role = models.ForeignKey(Role, related_name="candidacies", on_delete=models.CASCADE)
    collaborator = models.ForeignKey(Collaborator, related_name="candidates_for", on_delete=models.CASCADE)
    description = models.TextField(max_length=5000)

    class Meta:
        verbose_name = _("Candidature")
        verbose_name_plural = _("Candidatures")

    def __str__(self):
        return "{0} {1} candidate pour le rôle de {2} dans le projet {3}".format(self.collaborator.user.first_name, self.collaborator.user.last_name, self.role.role_name, self.role.project.name)









