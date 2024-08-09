from django.db import models

# Create your models here.

from datetime import date



# Create your models here.
    
# from django.db import models

class Event(models.Model):
    # event_name = models.CharField(max_length=100)
    # start_date = models.DateField()
    # end_date = models.DateField()
    location = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, default='Not specified')
    price_range = models.CharField(max_length=50)
#     # created_at = models.DateTimeField(auto_now_add=True)
   

    # def __str__(self):
    #     return self.event_name  # 管理画面などでオブジェクトを表示する際の文字列
    # some_field_name  # 'title' フィールドがあると仮定

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)  # 必要に応じて default 値を削除または設定
    genre = models.CharField(max_length=100, default='Not specified')
    category = models.CharField(max_length=50, blank=True, null=True)
    price_range = models.CharField(max_length=50, blank=True, null=True)
    
    google_maps = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='restaurants/', blank=True, null=True)
    # date_added = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.name
    
class Photo(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='restaurant_photos/')
    # created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Photo of {self.restaurant.name}"        
        # return f"{self.restaurant.name} - {self.caption[:20]}"       




# class Post(models.Model):
#     # 既存のフィールド
#     title = models.CharField(max_length=100)
#     content = models.TextField()
    
    # 追加するフィールド
    # created_at = models.DateTimeField(auto_now_add=True)

# class Comment(models.Model):
#     # 既存のフィールド
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     content = models.TextField()

    # 追加するフィールド
    # created_at = models.DateTimeField(auto_now_add=True)


