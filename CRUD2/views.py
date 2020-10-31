from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import  INFO
from django.contrib.auth.models import User, auth 
from django.contrib.auth import authenticate, login

# Create your views here.

def employee_list(request):
	context =  {'employee_list':INFO.objects.all()}
	return render(request, 'html/employee_list.html', context)

def employee_form(request, id=0):
	if request.method == "GET":
		if id == 0:
			form = EmployeeForm()
		else:
			employee = INFO.objects.get(pk=id)
			form = EmployeeForm(instance=employee)
		return render(request, 'html/employee_form.html',{'form':form})
	else:
		if id == 0:
			form = EmployeeForm(request.POST)
		else:
			employee = INFO.objects.get(pk=id)
			form = EmployeeForm(request.POST,instance=employee)	
		if form.is_valid():
			form.save()
		return redirect('/employee/list')	

def employee_delete(request, id):
	employee = INFO.objects.get(pk=id)
	employee.delete()
	return redirect('/employee/list')	



def home(request):s
	return render(request, 'html/home.html')






def login1(request):
	if request.method =="POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username= username, password=password)
		if user:
			login(request, user)
			return redirect('/employee/home')
			
		else:
			error = "Sorry error username and password"
			return render(request, 'html/login.html',{'error':error})		


	else:
		return render(request, 'html/login.html')	





def signup(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if password1 == password2 :
			if User.objects.filter(username=username).exists():
				print("Username is already taken")
				return render(request, 'html/register.html')
			elif User.objects.filter(email=email).exists():
				print("Email is already taken")
				return render(request, 'html/register')
			else:
				user = User.objects.create_user(
											first_name=first_name,
											last_name=last_name,
											email=email,
											username=username,
											password= password1
												)		
			user.save();
			print('User Created')
			return redirect('home')

			

	else:
		return render(request, 'html/register.html')






	
