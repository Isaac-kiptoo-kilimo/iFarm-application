from django.db import models
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import transaction
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_farmer = models.BooleanField(default=False)
    is_officer = models.BooleanField(default=False)


class Farmer(models.Model):
    resignation=models.CharField(max_length=100,null=True,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,related_name='farmer')
    # posts = models.ManyToManyField('Post',primary_key=True,related_name='officer', through='post')
   

    @transaction.atomic
    def save_farmer(self):
        user=super().save(commit=False)
        user.is_farmer = True
        user.save()
        farmer = Farmer.objects.create(user=user)
        return user

class Officer(models.Model):
    resignation=models.CharField(max_length=100,null=True,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,related_name='Officer')
    # posts = models.ManyToManyField('Post',primary_key=True,related_name='officer', through='post')

class Farm(models.Model):
    farm_name=models.CharField(max_length=100,blank=True,null=True)
    location=models.CharField(max_length=200,blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="farms",null=True,blank=True)
    farm_img=CloudinaryField('image',blank=True)
    admin=models.ForeignKey('Profile', on_delete=models.CASCADE, related_name="farmers",null=True,blank=True)
    Agricultural_helpline=models.CharField(max_length=200,blank=True,null=True)
    description=models.TextField(null=False,blank=True)


    def save_farm(self):
        self.save()

    def update_farm(self):
        self.update()

    def delete_farm(self):
        self.delete()
        
    @classmethod
    def find_farm(cls,farm_id):
        new_farm = cls.objects.filter(farm_id=farm_id)
        return new_farm

    def __str__(self):
        return str(self.farm_name)


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    fullname=models.CharField(max_length=100,blank=True,null=True)
    username=models.CharField(max_length=100,blank=True,null=True)
    farm=models.ForeignKey(Farm,on_delete=models.SET_NULL, null=True, related_name='members', blank=True)
    email=models.EmailField(max_length=100,blank=True,null=True)
    proc_img=CloudinaryField('image',blank=True)
    bio=models.TextField(blank=True,null=True)
    contacts=models.CharField(max_length=200)
    locations=models.CharField(max_length=200)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self,id,profile):
        updated_profile=Profile.objects.filter(id=id).update(profile)
        return updated_profile

    def __str__(self):
        return str(self.fullname)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            instance.profile.save()

        post_save.connect(Profile, sender=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        Profile.objects.get_or_create(user=instance)
        instance.profile.save()


class Post(models.Model):
    title=models.CharField(max_length=100,null=True,blank=True)
    post_img=CloudinaryField('post_img',blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post",null=True,blank=True)
    description=models.TextField(null=False)
    created_at=models.DateTimeField(auto_now_add=True,)
    price=models.CharField(max_length=100,null=True,blank=True)
    shop=models.CharField(max_length=100,blank=True,null=True)
    category=models.CharField(max_length=100,null=True,blank=True)
    location=models.CharField(max_length=100,blank=True,null=True)
    

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def update_post(self,id,post):
        updated_post=Post.objects.filter(id=id).update(post)
        return updated_post


    def __str__(self):
        return self.title
    
    
class Question(models.Model):
    question_title=models.CharField(max_length=100,blank=True,null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions",null=True,blank=True)
    question=models.TextField(null=True,blank=True)
    post_at=models.DateTimeField(auto_now_add=True,)

    def save_question(self):
        self.save()

    def delete_question(self):
        self.delete()

    def update_question(self,id,question):
        updated_question=Question.objects.filter(id=id).update(question)
        return updated_question


    def __str__(self):
        return self.question

class Answer(models.Model):
    answer_title=models.CharField(max_length=100,blank=True,null=True)
    question=models.ForeignKey(User, on_delete=models.CASCADE, related_name="answers",null=True,blank=True)
    answer=models.TextField(null=True,blank=True)
    posted_at=models.DateTimeField(auto_now_add=True,)

    def save_answer(self):
        self.save()

    def delete_answer(self):
        self.delete()

    def update_answer(self,id,answer):
        updated_answer=Question.objects.filter(id=id).update(answer)
        return updated_answer


    def __str__(self):
        return self.answer
