import django_filters
from .models import Project, Category
from django import forms

categories = Category.objects.all()
#CATEGORIES_CHOICE = ((category.id, category.name) for category in categories)
CATEGORIES_CHOICE = (
    (1, 'innovation'),
    (2, 'qualité de vie'),
    (3, 'sociétal'),
    (4, 'opérationnel')
)




class CategoryFilter(django_filters.FilterSet):

    #id = django_filters.MultipleChoiceFilter(choices=CATEGORIES_CHOICE)
    #category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())
    id = django_filters.BooleanFilter(field_name='name')

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('hey')
        #print(kwargs)
        '''for category in kwargs['queryset']:
            self.fields = django_filters.BooleanFilter(field_name='name')'''
        for k in self.__dict__.keys():
            print(str(k) + ' : ' + str(self.__dict__[k]))
    

    class Meta:
        model = Category
        fields = ['name']

class CategoryFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for category in categories:
            self.fields['category'+str(category.id)] = forms.BooleanField(widget=forms.CheckboxInput, label=category.name, required=False)
    


class ProjectForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, label="nom du projet")
    description = forms.CharField(max_length=2000, required=True, widget=forms.Textarea, label="description")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for category in categories:
            self.fields['category'+str(category.id)] = forms.BooleanField(widget=forms.CheckboxInput, label=category.name, required=False)
        
