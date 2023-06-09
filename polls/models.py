from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    

class post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    intro = models.TextField()
    body = models.TextField()    
    post_date = models.DateTimeField(auto_now_add=True)
    
    # models.pyにデータを記述しただけだからデータベースを連結させるコマンドを打つ
    # python manage.py makemigrationsと打つ