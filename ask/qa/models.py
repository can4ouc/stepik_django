from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255, null=False)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(
        User,
        related_name='question_author',
        on_delete=models.DO_NOTHING,
    )
    likes = models.ManyToManyField(User, related_name='question_like_user')


    class Meta:
        ordering = ('-added_at',)

    def __str__(self):
        return self.title

    def get_url(self):
        return "/question/{}/".format(self.id)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(
        Question,
        related_name='question_answer',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        related_name='answer_author',
        on_delete=models.DO_NOTHING,
    )


    class Meta:
        ordering = ('added_at',)

