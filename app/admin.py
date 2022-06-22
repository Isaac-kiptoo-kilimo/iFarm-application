from django.contrib import admin
from .models import *
from django.contrib import admin
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display=('question_title','user')
admin.site.register(Question,QuestionAdmin)
admin.site.register(Post)
admin.site.register(Farmer)
admin.site.register(Officer)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Farm)
