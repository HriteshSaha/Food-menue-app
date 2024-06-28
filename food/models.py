from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Items(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=50)
    item_desc = models.CharField(max_length=50)
    item_price = models.PositiveIntegerField()
    # Adding image field but not using ImageField function, here we create a CharField function to put the image url and to change the image we need to put the image address coppied from other website in this CharField.
    item_img = models.CharField(max_length=500, default='https://static.wixstatic.com/media/bf242e_6133b4ae6a104cc2b50d70179f35efea~mv2.jpg/v1/fill/w_500,h_374,al_c,lg_1,q_80,enc_auto/food-placeholder.jpg')

    def __str__(self):
        return self.item_name
    
    def get_absolute_url(self):
        return reverse("food:details", kwargs={"pk": self.pk})
    