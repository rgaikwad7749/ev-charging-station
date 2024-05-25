from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from urllib import request
# from .models import newuser,Sales

from django.shortcuts import render
from .models import newuser,Stations,Bookslots,Payment,Stationowner,Review,DeletedBooking,Offgrid_Stations,Hybrid_Stations
from django.shortcuts import render, redirect,get_object_or_404

def index(request):
    return render(request,'index.html')



def userlogin(request):
    if request.method== 'POST':
        try:
            Userdetailes=newuser.objects.get(Username=request.POST['Username'], pass1=request.POST['pass1'])
            print("Username=",Userdetailes)
            request.session['Username']=Userdetailes.Username
            messages.success(request,"successfully login")
            return redirect('userhome')
        except newuser.DoesNotExist as e:   
            messages.error(request,"Username/ Password Invalied...!")
   
    return render(request,'userlogin.html')


def userregistration(request):
    if request.method == 'POST':
        Username=request.POST['Username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if newuser.objects.filter(Username=Username).exists():
            messages.warning(request,'Username is already exists')
            return redirect('userregistration')
        else:
            newuser(Username=Username, fname=fname, lname=lname, email=email, pass1=pass1, pass2=pass2).save()
            messages.success(request, 'The new user '+request.POST['Username']+ " IS saved successfully..!")
            return redirect('userlogin')
    else:
         return render(request,'userregistration.html')


def logout(request):
    # logout(request)
    messages.success(request,"successfully logout..!")
    return redirect('index')


## Owner login
def owner_login(request):
    if request.method== 'POST':
        try:
            Userdetailes=Stationowner.objects.get(Username=request.POST['Username'], pass1=request.POST['pass1'])
            print("Username=",Userdetailes)
            request.session['Username']=Userdetailes.Username
            messages.success(request,"successfully login")
            return redirect('owner_home')
        except Stationowner.DoesNotExist as e:   
            messages.error(request,"Username/ Password Invalied...!")
   
    return render(request,'owner_login.html')



def owner_registrations(request):
    if request.method == 'POST':
        Username=request.POST['Username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if Stationowner.objects.filter(Username=Username).exists():
            messages.warning(request,'Username is already exists')
            return redirect('userregistration')
        else:
            Stationowner(Username=Username, fname=fname, lname=lname, email=email, pass1=pass1, pass2=pass2).save()
            messages.success(request, 'The new user '+request.POST['Username']+ " IS saved successfully..!")
            return redirect('owner_login')
    else:
         return render(request,'owner_registrations.html')


def owner_logout(request):
    # logout(request)
    messages.success(request,"successfully logout..!")
    return redirect('index')

def owner_home(request):
    return render(request, 'owner_home.html')


def userhome(request):
    return render(request, 'userhome.html')



def adminregistration(request):
    if request.method == 'POST':
        Username=request.POST['Username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1 !=pass2:
            messages.error(request,"password do not match")
            return redirect('user_registration')
        newuser(Username=Username, fname=fname, lname=lname, email=email, pass1=pass1, pass2=pass2).save()
        messages.success(request, 'The new user '+request.POST['Username']+ " IS saved successfully..!")
        return redirect('adminlogin')
    else:
        return render(request, 'adminregistration.html')


def adminlogin(request):
    if request.method== 'POST':
        try:
            Userdetailes=newuser.objects.get(Username=request.POST['Username'], pass1=request.POST['pass1'])
            print("Username=",Userdetailes)
            request.session['Username']=Userdetailes.Username
            messages.success(request,"successfully login")
            return redirect('admin_home')
        except newuser.DoesNotExist as e:   
            messages.error(request,"Username/ Password Invalied...!")
    return render(request, 'adminlogin.html')

def admin_home(request):
    return render(request, 'admin_home.html')


def admin_logout(request):
    messages.success(request,"successfully logout..!")
    return redirect('index')

def view_user(request):
    form=newuser.objects.all()
    return render(request,'view_user.html' , {'forms':form})


def add_stations(request):
    if request.method=='POST':
        sname=request.POST['sname']
        address=request.POST['address']
        area=request.POST['area']
        city=request.POST['city']
        phone=request.POST['phone']
        ctslot=request.POST['ctslot']
        details=request.POST['details']
        Location=request.POST['Location']
        station= Stations(sname=sname,address=address,area=area,city=city,phone=phone,ctslot=ctslot,details=details,Location=Location)
        station.save()    
        return redirect('add_stations')
    else:
        return render(request,'add_stations.html')


def search(request):
    query=request.GET['query']
    form=Stations.objects.filter(area__icontains=query)
    return render (request, 'search.html',{'forms':form})



# def book_slots(request):
#     if request.method=='POST':
#         oname=request.POST['oname']
#         vehicleno=request.POST['vehicleno']
#         mobileno=request.POST['mobileno']
#         city=request.POST['city']
#         area=request.POST['area']
#         time=request.POST['time']
        
#         book= Bookslots(oname=oname,vehicleno=vehicleno,mobileno=mobileno,city=city,area=area,time=time)
#         book.save()  
#         messages.error(request,"successfully done in payment and book slot")  
#         return redirect('payment')
#     else:
#         return render (request, 'book_slots.html')


# def book_slots(request):
#     if request.method == 'POST':
#         oname = request.POST['oname']
#         vehicleno = request.POST['vehicleno']
#         mobileno = request.POST['mobileno']
#         city = request.POST['city']
#         area = request.POST['area']
#         time = request.POST['time']
#         date = request.POST['date']

#         # Check if the slot already exists
#         if Bookslots.objects.filter(time=time).exists():
#             messages.error(request, f"Slot at {time} is already booked. Please choose another slot.")
#             return redirect('book_slots')
#         if Bookslots.objects.filter(time=time).exists():
#             messages.error(request, f"Slot at {time} is already booked. Please choose another slot.")
#             return redirect('book_slots')
      
#         else:
#             # Save the slot if it doesn't exist
#             book = Bookslots(oname=oname, vehicleno=vehicleno, mobileno=mobileno, city=city, area=area, time=time,date=date)
#             book.save()
#             messages.success(request, f"Slot at {time} booked successfully. Proceed to payment.")

#         return redirect('payment')

#     else:
#         return render(request, 'book_slots.html')

def book_slots(request):
    if request.method == 'POST':
        oname = request.POST['oname']
        vehicleno = request.POST['vehicleno']
        mobileno = request.POST['mobileno']
        city = request.POST['city']
        area = request.POST['area']
        time = request.POST['time']
        date = request.POST['date']
        hname=request.POST['hname']
        accountno=request.POST['accountno']
        ifsccode=request.POST['ifsccode']
        total=request.POST['total']

        # Check if the slot already exists
        if Bookslots.objects.filter(time=time, date=date).exists():
            messages.error(request, f"Slot at {time} on {date} is already booked. Please choose another slot.")
            return redirect('book_slots')
        
        else:
            # Save the slot if it doesn't exist
            
            book = Bookslots(oname=oname, vehicleno=vehicleno, mobileno=mobileno, city=city, area=area, time=time, date=date,hname=hname,accountno=accountno,ifsccode=ifsccode,total=total)
            book.save()
            
            messages.success(request, f"Slot at {time} on {date} booked successfully. Proceed to payment.")

        return redirect('user_review')

    else:
        booked_slots = Bookslots.objects.all()  # You may need to filter this based on your logic
        return render(request, 'book_slots.html',{'booked_slots': booked_slots})







def payment(request):
    if request.method=='POST':
        hname=request.POST['hname']
        accountno=request.POST['accountno']
        ifsccode=request.POST['ifsccode']
        total=request.POST['total']
        pays= Payment(hname=hname,accountno=accountno,ifsccode=ifsccode,total=total)
        pays.save() 
        messages.error(request,"successfully done in payment and book slot")  
        return redirect('user_review') 
    return render (request, 'payment.html')




def view_booking(request):
    form=Bookslots.objects.all()
    return render (request, 'View_booking.html',{'forms':form})


def view_slots(request):
    form=Stations.objects.all()
    return render (request, 'View_slots.html',{'forms':form})


def view_paymenthistory(request):
    form=Payment.objects.all()
    return render (request, 'View_paymenthistory.html',{'forms':form})


def user_review(request):
    if request.method=='POST':
        title=request.POST['title']
        rating=request.POST['rating']
        comment=request.POST['comment']
       
        rev= Review(title=title,rating=rating,comment=comment)
        rev.save() 
        messages.error(request,"successfully Added")  
        return redirect('userhome') 
    return render (request, 'user_review.html')




def contact(request):
    
    return render (request, 'contact.html')


def user_cancel(request):
    form=Bookslots.objects.all()
    return render (request,'user_cancelbooking.html',{'forms':form})


def cancel_booking(request, booking_id):
    booking = get_object_or_404(Bookslots, pk=booking_id)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Booking canceled successfully.")
        return redirect('user_cancel')  # Redirect to home page or any other page after canceling booking
    return render(request, 'user_cancelbooking.html')



def delete_data(request, id):
    booking = get_object_or_404(Bookslots, pk=id)

    if request.method == 'POST':
        # Create an instance of DeletedBooking model before deleting the booking
        deleted_booking = DeletedBooking(
            oname=booking.oname,
            vehicleno=booking.vehicleno,
            mobileno=booking.mobileno,
            city=booking.city,
            area=booking.area,
            time=booking.time,
            date=booking.date,
            hname=booking.hname,
            accountno=booking.accountno,
            ifsccode=booking.ifsccode,
            total=booking.total
        )
        deleted_booking.save()

        # Delete the booking
        booking.delete()
        messages.success(request, "Booking canceled successfully.")
        return redirect('user_cancel')

    return render(request, 'delete_booking.html', {'booking': booking})


def user_cancelbooking(request):
    form=DeletedBooking.objects.all()
    return render (request,'view_cancelbooking.html',{'forms':form})

def edit_data(request, id):
    booking = get_object_or_404(DeletedBooking, pk=id)
    if request.method == 'POST':
        booking.oname = request.POST['oname']
        booking.vehicleno = request.POST['vehicleno']
        booking.mobileno = request.POST['mobileno']
        booking.city = request.POST['city']
        booking.area = request.POST['area']
        booking.time = request.POST['time']
        booking.date = request.POST['date']
        booking.hname=request.POST['hname']
        booking.accountno=request.POST['accountno']
        booking.ifsccode=request.POST['ifsccode']
        booking.total=request.POST['total']
        booking.save()
        return redirect('admin_home')  # Redirect to booking detail page
    return render(request, 'edit_booking.html', {'booking': booking})






def offgrid_slot(request):
    form=Offgrid_Stations.objects.all()
    
    return render (request, 'offgrid.html',{'forms':form})



def hybrid_slot(request):
    form=Hybrid_Stations.objects.all()
    return render (request, 'hybrid.html',{'forms':form})



def add_hybridslot(request):
    if request.method=='POST':
        sname=request.POST['sname']
        address=request.POST['address']
        area=request.POST['area']
        sockets=request.POST['sockets']
        city=request.POST['city']
        phone=request.POST['phone']
        ctslot=request.POST['ctslot']
        details=request.POST['details']
        Location=request.POST['Location']
        station= Hybrid_Stations(sname=sname,address=address,area=area,sockets=sockets,city=city,phone=phone,ctslot=ctslot,details=details,Location=Location)
        station.save()    
        return redirect('add_hybridslot')
    else:
         return render (request, 'add_hybridstation.html')


def add_offgridslot(request):
    if request.method=='POST':
        sname=request.POST['sname']
        address=request.POST['address']
        area=request.POST['area']
        sockets=request.POST['sockets']
        city=request.POST['city']
        phone=request.POST['phone']
        ctslot=request.POST['ctslot']
        details=request.POST['details']
        Location=request.POST['Location']
        station= Offgrid_Stations(sname=sname,address=address,area=area,sockets=sockets,city=city,phone=phone,ctslot=ctslot,details=details,Location=Location)
        station.save()    
        return redirect('add_offgridslot')
    else:
    
        return render (request, 'add_offgridstations.html')