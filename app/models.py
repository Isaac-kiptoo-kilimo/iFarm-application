from django.db import models

from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Farm(models.Model):
    farm_name=models.CharField(max_length=100,blank=True,null=True)
    location=models.CharField(max_length=200,blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="farms",null=True,blank=True)
    farm_img=CloudinaryField('image',blank=True)
    admin=models.ForeignKey('Profile', on_delete=models.CASCADE, related_name="farms",null=True,blank=True)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts",null=True,blank=True)
    description=models.TextField(null=False)
    created_at=models.DateTimeField(auto_now_add=True,)

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def update_post(self,id,post):
        updated_post=Post.objects.filter(id=id).update(post)
        return updated_post


    def __str__(self):
        return self.title


class Location(models.Model):
    location_name=models.CharField(max_length=100,blank=True,null=True)
    place=models.CharField(max_length=100,blank=True,null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="locations",null=True,blank=True)
    farm_id=models.ForeignKey(Farm, on_delete=models.CASCADE, related_name="locations",null=True,blank=True)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self,id,location):
        updated_location=Location.objects.filter(id=id).update(location)
        return updated_location


    def __str__(self):
        return self.location_name

class Shop(models.Model):
    shop_name=models.CharField(max_length=100,blank=True,null=True)
    distance=models.IntegerField(blank=True,null=True)
    category=models.CharField(max_length=100,null=True,blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="shops",null=True,blank=True)
    
    def save_shop(self):
        self.save()

    def delete_shop(self):
        self.delete()

    def update_shop(self,id,shop):
        updated_shop=Shop.objects.filter(id=id).update(shop)
        return updated_shop


    def __str__(self):
        return self.shop_name

class Business(models.Model):
    business_name=models.CharField(max_length=100,blank=True,null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="users",null=True,blank=True)
    farm_id=models.ForeignKey(Farm, on_delete=models.CASCADE, related_name="farms",null=True,blank=True)
    business_logo=CloudinaryField('image',blank=True)
    business_email=models.EmailField(max_length=100,blank=True,null=True)
    contact=models.IntegerField(null=True,blank=True)

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def update_business(self,id,business):
        updated_business=Business.objects.filter(id=id).update(business)
        return updated_business


    def __str__(self):
        return self.business_name