from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# from .models import JobDescription, Resume
from .models import HRmanagerID, HRUser, Resume


# Create your views here.
def loginPage(request):
    # if user is loggedin they cant goto login page
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User Doesnot Exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('upload')
        else:
            messages.error(request, 'Username or password doesnot exist')
    context ={}
    return render(request, 'base/login.html',context)


#@login_required(Login_url= 'login')
def logoutUser(request):
    logout(request)
    return redirect('home')


def signupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        if password and confirmPassword and password != confirmPassword:
            messages.error(request,"Passwords do not match.")
            return redirect('signup')
        else:
            user = User.objects.filter(username = username)
            if user.exists():
                messages.error(request, 'Username already taken')
                return redirect('signup')

            user = User.objects.create_user(username,email,password)
            user.set_password(password)
            user.save()
            messages.info(request, 'Account created successfully')
            login(request,user)
            return redirect('upload')
    return render(request, 'base/signup.html')

# def signupPage(request):
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             messages.error(request,"Passwords do not match.")
            
#     else:
#         form=CreateUserForm()
#     context = {'form':form}
#     return render(request, 'base/signup.html',context)




# METHOD ORIGINAL


# @login_required(login_url= 'login')
# def upload(request):
#     if request.method == 'POST':
#         user = request.user  # Get the currently logged-in user

#         # Your other form processing logic

#         job_description_instance = JobDescription.objects.create(
#             user=user,
#             jobdescription=request.FILES.get('jobdescription'),
#             skills=request.POST['skills'],
#             education=request.POST['education'],
#             age=request.POST['age'],
#             experience=request.POST['experience']
#         ) 
#         resume_files = request.FILES.getlist('resumes')
#         count = request.POST['count']
        

#         for  resume_file in resume_files:
#             Resume.objects.create(user= user,resumes=resume_file,count=count)
                  
#         messages.success(request, 'Files uploaded successfully.')
#         return redirect('home') 
#     return render(request, 'base/upload.html')


def home(request):
    return render(request, 'base/home.html')

def aboutus(request):
    return render(request, 'base/aboutus.html')

def contactus(request):
    return render(request, 'base/contactus.html')

# METHOD3


# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .forms import JobDescriptionForm, ResumeForm

# @login_required
# def upload_job_description(request):
#     if request.method == 'POST':
#         form = JobDescriptionForm(request.POST, request.FILES)
#         if form.is_valid():
#             job_description = form.save(commit=False)
#             job_description.user = request.user
#             job_description.save()
#             return redirect('success_url')  # Redirect to a success page
#     else:
#         form = JobDescriptionForm()
#     return render(request, 'upload.html', {'form': form})

# @login_required
# def upload_resume(request):
#     if request.method == 'POST':
#         form = ResumeForm(request.POST, request.FILES)
#         if form.is_valid():
#             resume = form.save(commit=False)
#             resume.user = request.user
#             resume.save()
#             return redirect('success_url')  # Redirect to a success page
#     else:
#         form = ResumeForm()
#     return render(request, 'upload.html', {'form': form})

#METHOD 4

@login_required(login_url= 'login')
def upload(request):
    if request.method == 'POST':
        user = request.user  # Get the currently logged-in user

        # Assuming you have a form with 'jobdescription', 'skills', 'education', 'age', 'experience', 'resumes', and 'count' fields
        hr_manager_id_instance = HRmanagerID.objects.create(HR_id=request.POST['HR_id'])

        hr_user_instance = HRUser.objects.create(
            user=user,
            HR_id=hr_manager_id_instance,
            jobdescription=request.FILES.get('jobdescription'),
            skills=request.POST['skills'],
            education=request.POST['education'],
            age=request.POST['age'],
            experience=request.POST['experience'],
            count = request.POST['count']
        )
        
        resume_files = request.FILES.getlist('resumes')

        for resume_file in resume_files:
            # Create a Resume object associated with the HRUser instance
            resume_obj = Resume.objects.create(user=user, file=resume_file)
            hr_user_instance.resumes.add(resume_obj) 
        hr_user_instance.save()

        messages.success(request, 'Files uploaded successfully.')
        return redirect('home')

    return render(request, 'base/upload.html')



@login_required(login_url='login')
def view_resumes(request):
    user = request.user
    hr_user_instance = HRUser.objects.get(user=user)
    resumes = hr_user_instance.resumes.all()
    return render(request, 'base/view_resumes.html', {'resumes': resumes})
