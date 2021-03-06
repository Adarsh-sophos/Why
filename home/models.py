from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	explaination = models.CharField(max_length = 300 , default = '')
	text = models.CharField(max_length = 140)
	upvote = models.IntegerField(default = 0)
	downvote = models.IntegerField(default = 0)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	topic_choices = (
		('topic1' , 'topic1'),
		('topic2' , 'topic2'),
		)
	interests = models.CharField(max_length = 10 , default = '',choices = topic_choices)
	creation_date = models.DateTimeField(default = timezone.now())
	answer_count = models.IntegerField(default = 0)

	def __str__(self):
		return str(self.text)


class Vote_q(models.Model):
	user = models.ForeignKey(User , on_delete = models.CASCADE)
	question = models.ForeignKey(Question , on_delete = models.CASCADE)
	upvote = models.BooleanField(default = False)
	downvote = models.BooleanField(default = False)


class Answer(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	question = models.ForeignKey(Question , on_delete = models.CASCADE)
	text = models.CharField(max_length = 300)
	a_type = models.CharField(default = "text" , max_length = 10)
	path = models.CharField(max_length = 140 , default = "")
	upvote = models.IntegerField(default = 0)
	downvote = models.IntegerField(default = 0)
	creation_date = models.DateTimeField(default = timezone.now())

	def __str__(self):
		return str(self.text)
	class Meta:
		unique_together = ('user' , 'question',)

class Vote_a(models.Model):
	user = models.ForeignKey(User , on_delete = models.CASCADE)
	answer = models.ForeignKey(Answer , on_delete = models.CASCADE)
	upvote = models.BooleanField(default = False)
	downvote = models.BooleanField(default = False)


class Comment(models.Model):
	answer = models.ForeignKey(Answer, on_delete = models.CASCADE)
	user = models.ForeignKey(User , on_delete = models.CASCADE)
	comment = models.CharField(max_length = 50)



class up_notif_q(models.Model):
	user = models.ForeignKey(User , on_delete = models.CASCADE)
	voter = models.CharField(max_length = 50)
	question = models.ForeignKey(Question , on_delete = models.CASCADE)
	read = models.BooleanField(default = False)

class down_notif_q(models.Model):
	user = models.ForeignKey(User , on_delete = models.CASCADE)
	voter = models.CharField(max_length = 50)
	question = models.ForeignKey(Question , on_delete = models.CASCADE)
	read = models.BooleanField(default = False)

class up_notif_a(models.Model):
	user = models.ForeignKey(User , on_delete = models.CASCADE)
	voter = models.CharField(max_length = 50)
	answer = models.ForeignKey(Answer , on_delete = models.CASCADE)
	read = models.BooleanField(default = False)

class down_notif_a(models.Model):
	user = models.ForeignKey(User , on_delete = models.CASCADE)
	voter = models.CharField(max_length = 50)
	answer = models.ForeignKey(Answer , on_delete = models.CASCADE)
	read = models.BooleanField(default = False)

class answer_notif(models.Model):
	user = models.ForeignKey(User , on_delete = models.CASCADE)
	question = models.ForeignKey(Question , on_delete = models.CASCADE)
	answerer = models.CharField(max_length = 50)
	read = models.BooleanField(default = False)
