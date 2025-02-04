# from django.http import HttpResponse
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.forms import UserCreationForm
#
# from django.shortcuts import render, redirect
#
#
# # Create your views here.
# # Our views page actually shows what the consumer is viewing
# # a pretty convienient name
# #Idk if I should use the 'gtMovies/index'or 'home/index' here,
# #so ima use gtMoives for now
#
# def index(request):
#     return render(request, 'gtMovies/index.html')
#
# def about(request):
#     return render(request, 'gtMovies/about.html')
#
#
# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')  # Redirect to login page after successful registration
#     else:
#         form = UserCreationForm()
#     return render(request, 'gtMovies/register.html', {'form': form})
#
# def user_login(request):
#     if request.method == "POST":
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('index')  # Redirect to home page after successful login
#     else:
#         form = AuthenticationForm()
#     return render(request, 'gtMovies/login.html', {'form': form})
#
#
# def logout_view(request):
#     logout(request)
#     return redirect('login')  # Redirect to login page