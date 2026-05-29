

# Register your models here.
from django.contrib import admin
from .models import Question,Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Question)
admin.site.register(Choice)
