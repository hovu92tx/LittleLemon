from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta, date, time
# Create your models here.
def is_valid_time(check_datetime):
    # Define start and end times
    start_time = time(14, 0)  # 2 PM
    end_times = {
        0: time(21, 0),  # Sunday
        1: time(22, 0),  # Monday
        2: time(22, 0),  # Tuesday
        3: time(22, 0),  # Wednesday
        4: time(22, 0),  # Thursday
        5: time(22, 0),  # Friday
        6: time(23, 0),  # Saturday
    }
    day_of_week = date.today().weekday()
    end_time = end_times[day_of_week]
    if not start_time <= check_datetime <= end_time:
        raise ValidationError("The date and time must not be earlier than current time. Open Time: Mon - Fri: 2pm - 10pm, Sat: 2pm - 11pm, Sun: 2pm - 9pm.")

def validate_min_datetime(value):
    min_datetime = date.today()
    formatted_min_datetime = min_datetime.strftime('%Y-%m-%d')
    if value < min_datetime:
        raise ValidationError(f"The date and time must not be earlier than {formatted_min_datetime}")

class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField(validators=[validate_min_datetime], default=timezone.now)
    reservation_time = models.TimeField(validators=[is_valid_time], default=time(14, 0))  # 2 PM as default

    def __str__(self):
        return self.first_name + ' '+ str(self.reservation_date) +' '+ str(self.reservation_time)
   
   

class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    def __str__(self):
        return self.title

class Menu(models.Model):
   name = models.CharField(max_length=255,db_index=True)
   price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
   description = models.TextField(max_length=1000, default='')
   featured = models.BooleanField(db_index=True, default = False)
   category = models.ForeignKey(Category, on_delete=models.PROTECT, default =1)

   def __str__(self):
      return self.name
      

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem_id =  models.SmallIntegerField()
    rating = models.SmallIntegerField()
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('menuitem', 'user')


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="delivery_crew", null=True)
    status = models.BooleanField(default=0, db_index=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    date = models.DateField(db_index=True)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order')
    menuitem = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('order', 'menuitem')