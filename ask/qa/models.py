from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Question(models.Model):
    title = models.CharField(max_length=255, null=False)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name="question_author",
    )
    likes = models.ManyToManyField(User, related_name="question_like")


    class Meta:
        ordering = ('-added_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/question/{}/".format(self.id)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
    )


    class Meta:
        ordering = ('added_at',)

