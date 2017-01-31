from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuestionManager(models.Manager):
    
    # returns last added question
    def new(self):
        return self.order_by('-pk')
    # returns questions sorted by rating
    def popular(self):
        return self.order_by('-rating')
      
class Question(models.Model):
    objects = QuestionManager()
  
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank = True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name = 'question_like')

    def get_url(self):
        return '/question/'+str(pk)+'/'

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank = True, auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

    def get_by_id(self,id):
        Answer.obgects.filter(question__pk=id)
