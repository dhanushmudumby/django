from django.shortcuts import render,redirect
from django.http import request
from django.contrib.auth.models import User 
from django.contrib import auth,messages
from  . models import user_profile
from django.contrib.auth.decorators import login_required

# Create your views here.



def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['password1']
        user = auth.authenticate(username = uname,password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('/login')
    return render(request,'login.html')

def signin(request):
    if request.method  == 'POST':
        username = request.POST['uname']
        fname = request.POST['uname']
        lname = request.POST['uname']
        email = request.POST['mail']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,'username Taken')
                return redirect('/signin')
            elif User.objects.filter(email = email).exists():
                messages.info(request,'email Tacken')
                return redirect('/signin')
            else:
                user = User.objects.create_user(username = username,password = password1,first_name = fname,last_name = lname,email = email)
                user.save();
                print('form succesful')
                return redirect('/login')
        else:
            messages.info(request,"doesn't match")
            return redirect('/signin')

    else:
        print('form unsuccessful')
        return render(request,'Form.html')
    

def hello(request):
    return render(request,'hello.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='login')
def Profile(request):
    if request.method == 'POST':
    
        name = request.POST['Name']
        #Mail = request.POST['mail']
        mobile = request.POST['mobile']
        headline = request.POST['headline']
        bio = request.POST['bio']
        image = request.POST['image']
        certificates = request.POST['certification']
        skills = request.POST['skills']
        mobile = request.POST['mobile']
        social_git = request.POST['git']
        social_linkedin = request.POST['linkedin']
        social_website = request.POST['website']
        resume = request.POST['resume']

        
        profile = user_profile()
        profile.name = name
        profile.headline = headline
        profile.mobile = mobile
        profile.bio = bio
        profile.social_github = social_git
        profile.certificates = certificates
        profile.social_linkedin = social_linkedin
        profile.social_website = social_website
        profile.image = image
        profile.skills = skills

        profile.resume = resume
        profile.save()
        #print(User)

        return redirect('/account')
        

    print("form Failed")

    return render(request,'profile.html')

def account(request):
    #pk = user_profile.objects.get(id = pk)
    name = User.username
    pros = user_profile.objects.all()
    context = {'pros':pros}
    print(pros.values)
    
    return render(request,'account.html',context)
    