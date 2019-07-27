from django.contrib import admin

# Register your models here.
from Questions.models import Questions, QuestionsType

admin.site.register(Questions)
admin.site.register(QuestionsType)
