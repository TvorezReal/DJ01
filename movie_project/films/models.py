from django.db import models

class News_post(models.Model):
	title = models.CharField('Название фильма', max_length=50)
	short_description = models.CharField('Краткое описание фильма', max_length=200)
	feedback = models.TextField('Отзыв о фильме')
	pub_date = models.DateTimeField('Дата публикации')


	class Meta:
		verbose_name = 'Фильм'
		verbose_name_plural = 'Фильмы'

	def __str__(self):
		return self.title



# Create your models here.
