from django.db import models

# Create your models here.
class QuestionManager(model.Manager)
    
    # returns last added question
    def new():
        pass
    # returns questions sorted by rating
    def popular():
        pass
      
class Question(models.Model):
    objects = QuestionManager()
  
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    author = models.OneToOneField(User)
    likes = models.ManyToMany(User, related_name='question_like')
    
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question)
    author = models.OneToOneField(User)
    
