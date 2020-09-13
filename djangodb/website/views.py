from django.shortcuts import render, redirect ##
from .models import Member #step 14 from location, import class
from .forms import MemberForm #step 19
from django.contrib import messages ##

def home(request): #step 8
    all_members = Member.objects.all #from inside our member model, pull all the data and store into variable
    return render(request, 'home.html', {'all':all_members}) #use dictionary. pass in the variable (information) and reference on page as 'all'

#step 9, migrate
#step 10, create super user

#step 16

def join(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None) #if user posted info, put that into our form save that info into a variable called form.
        if form.is_valid():
            form.save()
        else: #instead of erasing and redirecting, we can keep the POSTed info saved
            fname = request.POST['fname']
            lname = request.POST['lname']
            age = request.POST['age']
            email = request.POST['email']
            passwd = request.POST['passwd']
            messages.success(request, ('There was an error in your form, Please try again'))
            #return redirect('join')
            return render(request, 'join.html', {'fname':fname, 'lname':lname, 'age':age, 'email':email, 'passwd':passwd})
        messages.success(request, ('Your Form Has Been Submitted Successfully!'))
        return redirect('home')
    else:
        return render(request, 'join.html', {})



