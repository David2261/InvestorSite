import datetime
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.core import serializers

class Idea(models.Model):
	idea_title = models.CharField('Название идеи', max_length = 120)
	idea_text = models.TextField('Текст идеи')
	idea_views = models.IntegerField('Просмотры', default=0)
	idea_image = models.ImageField(null = True, blank=True, upload_to='Blog', help_text='150x150px', verbose_name='Изображение')
	idea_pub_date = models.DateTimeField('Дата публикации', auto_now_add = True)

	def __str__(self):
		return self.article_title

	def was_published_recently(self):
		return self.idea_pub_date >= (timezone.now() - datetime.timedelta(days = 7))
	    
	class Meta:
				verbose_name = 'Идея'
				verbose_name_plural = 'Идеи'
				ordering = ["-id"]


"""			
def make_published(self, request, queryset):
	rows_updated = queryset.update(status='p')
	if rows_updated == 1:
		message_bit = "1 story was"
	else:
		message_bit = "%s stories were" % rows_updated

	self.message_user(request, "%s successfully marked as published." % message_bit)
"""

class IdeaComment(models.Model):
	idea = models.ForeignKey(Idea, on_delete = models.CASCADE)
	idea_author_name = models.CharField('Имя автора', max_length = 50)
	idea_comment_text = models.CharField('Текст комментария', max_length = 200)

	class Meta:
			verbose_name = 'Комментарий'
			verbose_name_plural = 'Комментарии'

	def __str__(self):
		return self.idea_author_name

class Gallery(models.Model):
	gallery_title = models.CharField("Название картинки", max_length = 120)
	gallery_text = models.TextField("Текст картинки")
	gallery_views = models.IntegerField("Просмотры", default=0)
	gallery_image = models.ImageField(null = True, blank=True, upload_to='Gallery', help_text='150x150px', verbose_name='Изображение')
	gallery_pub_date = models.DateTimeField('Дата публикации', auto_now_add = True)

	def __str__(self):
		return self.gallery_title

	def was_published_recently(self):
		return self.gallery_pub_date >= (timezone.now() - datetime.timedelta(days = 7))

	class Meta:
				verbose_name = 'Галерея'
				verbose_name_plural = 'Галереи'
				ordering = ["-id"]

class GalleryComment(models.Model):
	gallery_title = models.ForeignKey(Gallery, on_delete = models.CASCADE)
	gallery_author_name = models.CharField('Имя автора', max_length = 50)
	gallery_comment_text = models.CharField('Текст комментария', max_length = 200)

	class Meta:
			verbose_name = 'Комментарий'
			verbose_name_plural = 'Комментарии'

	def __str__(self):
		return self.gallery_author_name

class Learn(models.Model):
	learn_title = models.CharField("Название статьи", max_length = 150)
	learn_text = models.TextField("Текст статьи")
	learn_views = models.IntegerField("Просмотры", default=0)
	learn_image = models.ImageField(null = True, blank=True, upload_to='Learn', help_text='150x150px', verbose_name='Обучение')
	learn_pub_date = models.DateTimeField('Дата публикации', auto_now_add = True)
	
	def __str__(self):
		return self.learn_title

	def was_published_recently(self):
		return self.learn_pub_date >= (timezone.now() - datetime.timedelta(days = 7))

class LearnComment(models.Model):
	learn_title = models.ForeignKey(Learn, on_delete = models.CASCADE)
	learn_author_name = models.CharField('Имя автора', max_length = 50)
	learn_comment_text = models.CharField('Текст комментария', max_length = 200)

	class Meta:
			verbose_name = 'Комментарий'
			verbose_name_plural = 'Комментарии'

	def __str__(self):
		return self.learn_author_name


class Motiv(models.Model):
	motiv_title = models.CharField("Название мотивации", max_length = 120)
	motiv_text = models.TextField("Текст мотивации")
	motiv_views = models.IntegerField("Просмотры", default=0)
	motiv_image = models.ImageField(null = True, blank=True, upload_to='Motiv', help_text='150x150px', verbose_name='Изображение')
	motiv_pub_date = models.DateTimeField('Дата публикации', auto_now_add = True)

	def __str__(self):
		return self.motiv_title

	def was_published_recently(self):
		return self.motiv_pub_date >= (timezone.now() - datetime.timedelta(days = 7))

	class Meta:
				verbose_name = 'Мотивация'
				verbose_name_plural = 'Мотивации'
				ordering = ["-id"]

class MotivComment(models.Model):
	motiv_title = models.ForeignKey(Motiv, on_delete = models.CASCADE)
	motiv_author_name = models.CharField('Имя автора', max_length = 50)
	motiv_comment_text = models.CharField('Текст комментария', max_length = 200)

	class Meta:
			verbose_name = 'Комментарий'
			verbose_name_plural = 'Комментарии'

	def __str__(self):
		return self.motiv_author_name