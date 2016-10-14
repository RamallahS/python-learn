from django.contrib import admin

from polls.models import Question, Animal

admin.site.register(Question)
admin.site.register(Animal)
