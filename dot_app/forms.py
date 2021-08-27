from dot_app.models import *
from django.forms import ModelForm, widgets, DateInput

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class GiveBookForm(ModelForm):
    class Meta:
        model = GiveBook
        fields = '__all__'

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class CurriculumForm(ModelForm):
    class Meta:
        model = Curriculum
        fields = '__all__'
        

    

