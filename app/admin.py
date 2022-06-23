
from django.contrib import admin
from .models import *
from django.contrib import admin

class QuestionAdmin(admin.ModelAdmin):
    list_display=('question_title','user')
    search_fields=('title','question')
admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(Upvote)
admin.site.register(Downvote)
admin.site.register(Post)
admin.site.register(Farmer)
admin.site.register(Officer)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Farm)
