# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from colorfield.fields import ColorField
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

class Value(models.Model):
    
    name = models.CharField(max_length=100)
    color = ColorField(default='#FF0000')

    class Meta:
        verbose_name = _("Valeur")
        verbose_name_plural = _("Valeurs")

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


class Personnality(models.Model):
    
    name = models.CharField(max_length=100)
    color = ColorField(default='#FF0000')

    class Meta:
        verbose_name = _("Trait de personnalité")
        verbose_name_plural = _("Traits de personnalité")

    def __str__(self):
        return self.name


class UnderPersonnality(models.Model):
    
    name = models.CharField(max_length=100)
    color = ColorField(default='#FF0000')
    mother_personnality = models.ForeignKey(Personnality, related_name="under_personnalities", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Sous-trait de personnalité")
        verbose_name_plural = _("Sous-traits de personnalité")

    def __str__(self):
        return self.name


class Skill(models.Model):
    
    name = models.CharField(max_length=100)
    color = ColorField(default='#FF0000')

    class Meta:
        verbose_name = _("Compétence")
        verbose_name_plural = _("Compétences")

    def __str__(self):
        return self.name


class UnderSkill(models.Model):
    
    name = models.CharField(max_length=100)
    color = ColorField(default='#FF0000')
    mother_skill = models.ForeignKey(Skill, related_name="under_skills", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Sous-compétence")
        verbose_name_plural = _("Sous-compétences")

    def __str__(self):
        return self.name


class Collaborator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    picture = models.ImageField(upload_to="profile_pictures", default=None, null=True)
    job = models.CharField(null=True, max_length=200)
    arrival_date = models.DateField(auto_now=True)
    hobbies = models.ManyToManyField(Hobby, related_name="hobbies")
    projects = models.ManyToManyField(Project, related_name="members", through="Role")
    personnality_level = models.ManyToManyField(Personnality, related_name="is_caracterised_by", through="PersonnalityLevel")
    underpersonnality_level = models.ManyToManyField(UnderPersonnality, related_name="precisely_caracterised_by", through="UnderPersonnalityLevel")
    value_level = models.ManyToManyField(Value, related_name="owner", through="ValueLevel")
    skill_level = models.ManyToManyField(Skill, related_name="can", through="SkillLevel")
    underskill_level = models.ManyToManyField(UnderSkill, related_name="precisely_can", through="UnderSkillLevel")
    visited_concepts_list = models.ManyToManyField(Concept, related_name="explorers", through="ExplorationDate")
    recommended_concepts = models.ManyToManyField(Concept, related_name="pretenders")
    deepself_score = models.FloatField(default=0.0)
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
        verbose_name = _("Niveau de Valeur")
        verbose_name_plural = _("Niveaux de Valeurs")

    def __str__(self):
        return "{0} {1} a {2}% de {3}".format(self.collaborator.user.first_name, self.collaborator.user.last_name, self.value_level, self.value.name)


class SkillLevel(models.Model):
    skill_level = models.FloatField(default=0.0)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    collaborator = models.ForeignKey(Collaborator, on_delete=models.CASCADE)    

    class Meta:
        verbose_name = _("Niveau de Compétence")
        verbose_name_plural = _("Niveaux de Compétences")

    def __str__(self):
        return "{0} {1} a {2}% de {3}".format(self.collaborator.user.first_name, self.collaborator.user.last_name, self.skill_level, self.skill.name)


class UnderSkillLevel(models.Model):
    underskill_level = models.FloatField(default=0.0)
    underskill = models.ForeignKey(UnderSkill, related_name='levels', on_delete=models.CASCADE)
    collaborator = models.ForeignKey(Collaborator, on_delete=models.CASCADE)    

    class Meta:
        verbose_name = _("Niveau de Sous-compétence")
        verbose_name_plural = _("Niveaux de Sous-compétences")

    def __str__(self):
        return "{0} {1} a {2}% de {3}".format(self.collaborator.user.first_name, self.collaborator.user.last_name, self.underskill_level, self.underskill.name)

class UnderPersonnalityLevel(models.Model):
    underpersonnality_level = models.FloatField(default=0.0)
    underpersonnality = models.ForeignKey(UnderPersonnality, on_delete=models.CASCADE)
    collaborator = models.ForeignKey(Collaborator, on_delete=models.CASCADE)    

    class Meta:
        verbose_name = _("Niveau de Sous-trait de personnalité")
        verbose_name_plural = _("Niveaux de Sous-traits de personnalité")

    def __str__(self):
        return "{0} {1} a {2}% de {3}".format(self.collaborator.user.first_name, self.collaborator.user.last_name, self.underpersonnality_level, self.underpersonnality.name)


class PersonnalityLevel(models.Model):
    personnality_level = models.FloatField(default=0.0)
    personnality = models.ForeignKey(Personnality, on_delete=models.CASCADE)
    collaborator = models.ForeignKey(Collaborator, on_delete=models.CASCADE)    

    class Meta:
        verbose_name = _("Niveau de Trait de personnalité")
        verbose_name_plural = _("Niveaux de Traits de personnalité")

    def underLevels(self):
        return UnderPersonnalityLevel.objects.filter(underpersonnality__in = self.personnality.under_personnalities.all(), collaborator=self.collaborator)

    def __str__(self):
        return "{0} {1} a {2}% de {3}".format(self.collaborator.user.first_name, self.collaborator.user.last_name, self.personnality_level, self.personnality.name)


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









