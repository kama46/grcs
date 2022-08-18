from django.db import models
from datetime import timezone, datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

category_select = (
    ('Employee', 'Employee'),
    ('Visitor', 'Visitor')
)


# creating Person/Item carrier model
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    id_number = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=category_select, default="In")
    organisation = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    last_update_date = models.DateTimeField(default=datetime.now, blank=True)

    last_updated_by = models.CharField(default='admin', max_length=20)

    def __str__(self):
        return self.first_name

# creating the modal for employees and gadgets assigned to them
class Employee_Data(models.Model):
    employee_ID = models.CharField(max_length=50)
    employee_name = models.CharField(max_length=100)
    employee_dept = models.CharField(max_length=50)
    gadget_ID = models.CharField(max_length=50)
    gadget_type = models.CharField(max_length=50)

    def __str__(self):
        return self.employee_ID


# creating Item model
class Item(models.Model):
    item_name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=20)
    person_name = models.ForeignKey(Person, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    last_update_date = models.DateTimeField(default=datetime.now, blank=True)

    last_updated_by = models.CharField(default='admin', max_length=20)

    def __str__(self):
        return self.item_name


# declaring the gates of BOU in form of tuples
gate_select = (
    ('shimoni', 'Shimoni'),
    ('kampala road gate', 'KAMPALA ROAD GATE'),
    ('plot 45', 'Plot 45')
)
# creating ownership choices
item_owner = (
    ('Bank of Uganda', 'BANK OF UGANDA'),
    ('Personal', 'PERSONAL')
)
badgein_status = (
    ('In', 'In'),
)
badgeout_status = (
    ('Out', 'Out'),
)


# creating badge in and out model
class Badge(models.Model):
    item_name = models.ForeignKey(Item, on_delete=models.CASCADE)
    person_name = models.ForeignKey(Person, on_delete=models.CASCADE)
    location = models.CharField(max_length=20, choices=gate_select, default='main gate')
    item_owner = models.CharField(max_length=20, choices=item_owner, default='Bank of Uganda')
    status = models.CharField(max_length=20, choices=badgein_status, default="In")
    create_date = models.DateTimeField(default=datetime.now, blank=False)
    time_in = models.DateTimeField(default=datetime.now, blank=False)
    time_out = models.DateTimeField(default=datetime.now, blank=False)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    last_update_date = models.DateTimeField(auto_now=True)
    # last_updated_by = models.CharField(default='admin', max_length=20)

    def __str__(self):
        return f"{self.item_name} badged in at {self.time_in}"

# modal for badge staff
class Badge_staff(models.Model):
    employee_ID = models.ForeignKey(Employee_Data, on_delete=models.CASCADE)
    personal_gadget_type = models.CharField(max_length=50)
    no_of_gadgets = models.IntegerField(blank=True, null=True)
    date_time = models.DateTimeField(default=datetime.now, blank=False)
    gate = models.CharField(max_length=20, choices=gate_select, default='main gate')
    badgein_status = models.CharField(max_length=20, choices=badgein_status, default="In")
    
    def __str__(self):
        return self.employee_ID


# modal for badge nonstaff
class Badge_nonstaff(models.Model):
    fullname = models.CharField(max_length=100)
    dest_dept = models.CharField(max_length=50)
    visitor_ID = models.CharField(max_length=255,default="000")
    contact = models.CharField(max_length=20)
    gadget_type = models.CharField(max_length=50)
    no_of_gadgets = models.IntegerField(blank=True, null=True)
    date_time_in = models.DateTimeField(default=datetime.now, blank=False)
    date_time_out = models.DateTimeField(default=datetime.now, blank=False)
    gate = models.CharField(max_length=20, choices=gate_select, default='main gate')
    badgein_status = models.CharField(max_length=20, choices=badgein_status, default="In")
    badgeout_status = models.CharField(max_length=20, choices=badgeout_status, default="none")

    def __str__(self):
        return self.fullname

