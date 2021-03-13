from django.contrib import admin
from django.core import serializers
from .models import Idea, Gallery, Learn, Motiv, IdeaComment, GalleryComment, LearnComment, MotivComment
from django.contrib.contenttypes.models import ContentType

#admin.site.register(ArticleAdmin)

admin.site.register(Idea)
admin.site.register(IdeaComment)
admin.site.register(Gallery)
admin.site.register(GalleryComment)
admin.site.register(Learn)
admin.site.register(LearnComment)
admin.site.register(Motiv)
admin.site.register(MotivComment)

