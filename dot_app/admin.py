from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Department, Teacher, Special, Book, Author,Student, GiveBook, Curriculum, BooksSection, BooksStructure

admin.site.register(Department)
admin.site.register(Teacher)
admin.site.register(Special)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Student)
admin.site.register(GiveBook)
admin.site.register(Curriculum)
admin.site.register(BooksSection)
admin.site.register(BooksStructure)