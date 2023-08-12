from django.db import models

class icf_event(models.Model):
    title=models.CharField(max_length=100,null=True)
    description=models.TextField(max_length=1000,null=True)
    video=models.FileField(upload_to='videos/',blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class icf_quote(models.Model):
    title=models.CharField(max_length=100,null=True)
    description=models.TextField(max_length=1000,null=True)
    photo=models.ImageField(upload_to='photos/',blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class frequent_ask(models.Model):
    question_one=models.CharField(max_length=100,null=True)
    question_two=models.CharField(max_length=100,null=True)
    question_three=models.CharField(max_length=100,null=True)
    question_four=models.CharField(max_length=100,null=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.updated_at)


class faq_qn01(models.Model):
    question_one=models.CharField(max_length=100,null=True)
    answer_one=models.CharField(max_length=500,null=True)
    description=models.TextField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return self.question_one

class faq_qn02(models.Model):
    question_two=models.CharField(max_length=100,null=True)
    answer_two=models.CharField(max_length=500,null=True)
    description=models.TextField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return self.question_two

class faq_qn03(models.Model):
    question_three=models.CharField(max_length=100,null=True)
    answer_three=models.CharField(max_length=500,null=True)
    description=models.TextField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return self.question_three

class faq_qn04(models.Model):
    question_four=models.CharField(max_length=100,null=True)
    answer_one=models.CharField(max_length=500,null=True)
    description=models.TextField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return self.question_four
    
