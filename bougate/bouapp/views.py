# import cv2
# import datetime
import datetime as dt
# from pyzbar import pyzbar
from django.db.models import Count
from django.db.models.functions import ExtractMonth
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ItemForm, PersonForm, BadgeForm, BadgeFormOut
from .models import *


import calendar
@login_required(login_url='login')
def home(request):
    username = request.GET['username']
    gate = request.GET['gate']
    badgein_nonstaff = Badge_nonstaff.objects.annotate(month=ExtractMonth('date_time_in')).values('month').annotate(count=Count('id')).values('month','count')
    badgeout_nonstaff =Badge_nonstaff.objects.filter(badgeout_status="out").annotate(month=ExtractMonth('date_time_in')).values('month').annotate(count=Count('id')).values('month','count')
    
    #data for month and count for badged in non staff
    monthNumber=[]
    count = []
    for d in badgein_nonstaff:
        monthNumber.append(calendar.month_name[d['month']])
        count.append(d['count'])
    #data for month and count of badged out non staff
    bo_monthNumber = []
    bo_count = []
    for d in badgeout_nonstaff:
        bo_monthNumber.append(calendar.month_name[d['month']])
        bo_count.append(d['count'])
    # return HttpResponse("Hello Uganda, Am John Paul")
    bin_nonstaff_results = Badge_nonstaff.objects.all()
    bout_nonstaff_results = Badge_nonstaff.objects.filter(badgeout_status="out")
    bin_nonstaff_count = bin_nonstaff_results.count()
    bout_nonstaff_count = bout_nonstaff_results.count()
    context = {
        'bin_nonstaff_count': bin_nonstaff_count,
        'bout_nonstaff_count': bout_nonstaff_count,
        'username': username,
        'gate':gate,
        'monthNumber':monthNumber,
        'count': count,
        'bo_monthNumber':bo_monthNumber,
        'bo_count': bo_count,
        
    }
    return render(request, "home.html", context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        gate = request.POST['gate']
        user = auth.authenticate(username=username, password=password)
        bin_nonstaff_results = Badge_nonstaff.objects.all()
        bout_nonstaff_results = Badge_nonstaff.objects.filter(badgeout_status="out")
        bin_nonstaff_count = bin_nonstaff_results.count()
        bout_nonstaff_count = bout_nonstaff_results.count()
        badgein_nonstaff = Badge_nonstaff.objects.annotate(month=ExtractMonth('date_time_in')).values('month').annotate(count=Count('id')).values('month','count')
        badgeout_nonstaff =Badge_nonstaff.objects.filter(badgeout_status="out").annotate(month=ExtractMonth('date_time_in')).values('month').annotate(count=Count('id')).values('month','count')
        monthNumber=[]
        count = []
        for d in badgein_nonstaff:
            monthNumber.append(calendar.month_name[d['month']])
            count.append(d['count'])
        bo_monthNumber = []
        bo_count = []
        for d in badgeout_nonstaff:
            bo_monthNumber.append(calendar.month_name[d['month']])
            bo_count.append(d['count'])
        
        if user is not None:
            # auth.login(request, user)
            # print('Login Successful!')
            request.session['username'] = username
            auth.login(request, user)
            return render(request,'home.html',{'bin_nonstaff_count': bin_nonstaff_count,'bout_nonstaff_count': bout_nonstaff_count,"username":username,"gate":gate, "monthNumber":monthNumber,"count":count,'bo_monthNumber':bo_monthNumber,'bo_count':bo_count})
            
            # return redirect('home',{"username":username})
        else:
            messages.error(request, 'Username or Password not correct,Try again')
            return redirect('login')
        
    else:
        return render(request, 'login.html')


@login_required(login_url='home')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        print('logged out from App..')
        return redirect('login')


# Creating, Validating and saving forms
@login_required(login_url='home')
def register_item(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('badge')
    else:
        form = ItemForm()
    context = {
        "form_item": form
    }
    return render(request, 'register_item.html', context)


@login_required(login_url='home')
def person(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('badge')
    else:
        form = PersonForm()
    context = {
        "form_person": form
    }
    return render(request, 'person.html', context)


@login_required(login_url='home')
def badge(request):
    form = BadgeForm()
    form_person = PersonForm()
    form_item = ItemForm()
    if request.method == 'POST':
        form = BadgeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BadgeForm()
    context = {
        "form_badge": form,
        "form_person": form_person,
        "form_item": form_item,
        "username": username
    }
    return render(request, 'badge.html', context)


# Creating Functions to Update data by the Users
def update_person(request, pk):
    person = Person.objects.get(id=pk)
    form = PersonForm(instance=person)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'update_person.html', context)


def update_item(request, pk):
    item = Item.objects.get(id=pk)
    form = ItemForm(instance=item)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'update_person.html', context)


def update_badgein_nonstaff(request, pk):
    badge = Badge_nonstaff.objects.get(id=pk)
    if request.method == 'POST':

        form = BadgeForm(request.POST, instance=badge)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'update_badge.html', context)


def update_badge_out(request, pk):
    badge_out = Badge.objects.get(id=pk)
    form = BadgeFormOut(instance=badge_out)
    if request.method == 'POST':

        form = BadgeFormOut(request.POST, instance=badge_out)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'update_badge_out.html', context)


def view_items(request):
    items_results = Item.objects.all()
    items_count = items_results.count()
    context = {
        'items_results': items_results,
        'items_count': items_count
    }
    return render(request, 'view_items.html', context)


def view_badge(request):
    badge_results = Badge.objects.all()
    return render(request, 'view_badge.html', {'badge_results': badge_results})


def view_person(request):
    person_results = Person.objects.all()
    return render(request, 'view_person.html', {'person_results': person_results})


# function for deleting person
def delete_bin_nonstaff(request, pk):
    username = request.GET['username']
    gate = request.GET['gate']
    results = Badge_nonstaff.objects.all()
    return render(request, 'badgedinnonstaff.html', {"username":username,"gate":gate,"results":results})
    


# function for deleting item
def delete_item(request, pk):
    item_delete = Item.objects.get(id=pk)
    item_delete.delete()
    return redirect('view_item')


# function for deleting badge
def delete_badge(request, pk):
    username = request.GET['username']
    gate = request.GET['gate']
    badge = Badge_nonstaff.objects.get(id=pk)
    badge.badgeout_status = "out"
    now = dt.datetime.now()
    badge.date_time_out=now.strftime("%Y-%m-%d %H:%M:%S")
    badge.save()
    results = Badge_nonstaff.objects.all()
    return render(request, 'badgeout_nonstaff.html', {"username":username,"gate":gate,"results":results})
    


# function to search in the data Person
def person_search_bar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            persons = Person.objects.filter(organisation__icontains=query)
            return render(request, 'person_search.html', {'persons': persons})
        else:
            print("No person to search from")
            return render(request, 'person_search.html', {})


# function to search in the data item
def item_search_bar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            items = Item.objects.filter(item_name__icontains = query)
            context = {
                'items': items
                       }
            return render(request, 'item_search.html', context)
        else:
            print("No Items to search from")
            return render(request, 'item_search.html', {})


# Function to search for badges or badged items
def badge_search_bar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            badges = Badge.objects.filter(location__icontains=query)

            context = {
                'badges': badges,
            }
            return render(request, 'badge_search.html', context)
        else:
            print("No Badge to search from")
            return render(request, 'badge_search.html', {})


# function for badge in staff
def badgeIn(request):
    if request.method == 'GET':
        username = request.GET['username']
        gate = request.GET['gate']
    return render(request, 'badgeIn.html', {"username":username,"gate":gate})

# function for badge out staff
def badgeout_staff(request):
    if request.method == 'GET':
        username = request.GET['username']
        gate = request.GET['gate']
    return render(request, 'badgeout_staff.html', {"username":username,"gate":gate})

#function for badge in non staff
def badgeIn_nonstaff(request):
    username = request.GET['username']
    gate = request.GET['gate']
    results = Badge_nonstaff.objects.only('visitor_ID')
    if request.method == 'POST':
        post = Badge_nonstaff()
        for result in results:
            if result.visitor_ID == request.POST['ID']:
                messages.error(request, 'ID is already taken')
                return render(request, 'badgeIn_nonstaff.html', {"username":username,"gate":gate})
        post.fullname = request.POST['NAME']
        post.dest_dept = request.POST['DEPARTMENT']
        post.visitor_ID = request.POST['ID']
        post.contact = request.POST['CONTACT']
        post.gadget_type = request.POST['GADGET']
        post.no_of_gadgets = request.POST['NO_GADGETS']
        post.gate = gate
        post.save()
        messages.error(request, 'Badge In successful')
        
    return render(request, 'badgeIn_nonstaff.html', {"username":username,"gate":gate})

# def scan(request):
#     if True:
#         url = "192.168.115.88:8080/video"
#         cap = cv2.VideoCapture(url)
#         while True:
#             ret,frame = cap.read()
#             frame = cv2.resize(frame,(0,0),fx=0.20,fy=0.20)
#             cv2.putText(frame,"Press q to exit scanner",(10,10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,100),1)
#             barcodes = pyzbar.decode(frame)
#             for barcode in barcodes:
#                 (x,y,w,h) = barcode.rect
#                 cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
#                 barcodeData = barcode.data.decode("utf-8")
#                 barcodeType = barcode.type
#                 text = "Barcode: {} Type:{}".format(barcodeData,barcodeType)
#                 cv2.putText(frame,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)
#             cv2.imshow("Scanner",frame)
#             if cv2.waitKey(1)==ord('q'):
#                 break
#         if text:
#             print(text)
#             return HttpResponse(barcodeData)
#         cap.release()
#         cv2.destroyAllWindows()
#     return render(request,"badgeIn_staff.html",{})

#function for badge out non staff
def badgeout_nonstaff(request):
    username = request.GET['username']
    gate = request.GET['gate']
    results = Badge_nonstaff.objects.filter(badgeout_status="none")
    return render(request, 'badgeout_nonstaff.html', {"username":username,"gate":gate,"results":results})

# function for badged in staff list
def badgedinstaff(request):
    if request.method == 'GET':
        username = request.GET['username']
        gate = request.GET['gate']
    return render(request, 'badgedinstaff.html', {"username":username,"gate":gate})

# function for badged out staff list
def badgedoutstaff(request):
    if request.method == 'GET':
        username = request.GET['username']
        gate = request.GET['gate']
    return render(request, 'badgedoutstaff.html', {"username":username,"gate":gate})

# function for badged in nonstaff list
def badgedinnonstaff(request):
    username = request.GET['username']
    gate = request.GET['gate']
    results = Badge_nonstaff.objects.all()
    return render(request, 'badgedinnonstaff.html', {"username":username,"gate":gate,"results":results})

# function for badged out non staff list
def badgedoutnonstaff(request):
    username = request.GET['username']
    gate = request.GET['gate']
    results = Badge_nonstaff.objects.filter(badgeout_status="out")
    
    return render(request, 'badgedoutnonstaff.html', {"username":username,"gate":gate,"results":results})




# import requests
# import cv2
# import numpy as np
# import imutils
  
# def connect(request):
#     if True:
#         url = "192.168.115.88:8080/video"
#         cap = cv2.VideoCapture(url)
#         while True:
#             ret,frame = cap.read()
#             frame = cv2.resize(frame,(0,0),fx=0.20,fy=0.20)
#             cv2.putText(frame,"Press q to exit scanner",(10,10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,100),1)
#             # barcodes = pyzbar.decode(frame)
#             for barcode in barcodes:
#                 (x,y,w,h) = barcode.rect
#                 cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
#                 text = ""
#                 cv2.putText(frame,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)
#             cv2.imshow("Scanner",frame)
#             if cv2.waitKey(1)==ord('q'):
#                 break
#         if text:
#             print(text)
#             return HttpResponse(barcodeData)
#         cap.release()
#         cv2.destroyAllWindows()
#     return render(request,"badgeIn_staff.html",{})