from django.db import models
from django.db.models.deletion import CASCADE
import datetime
from django.utils import timezone

#lớp question kế thừa từ models
class Question(models.Model):

    question_text = models.CharField(max_length= 200)
    time_public = models.DateTimeField()
    def __str__(self):
        return self.question_text #thuận tiện cho việc xử lí ngôn ngữ

    def was_published_recently(self):
        return self.time_public >= timezone.now() - datetime.timedelta(days=1)

    

class choice(models.Model):
    #liên kết khóa ngoại đến lớp question
    question = models.ForeignKey(Question, on_delete= models.CASCADE)  # khi trl bị xóa đi thì câu hỏi cx bị xóa đi 
    choice_text = models.CharField(max_length= 100)
    vote = models.IntegerField(default= 0)
    def __str__(self):
        return self.choice_text

