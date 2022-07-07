from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


class RegisterView(View):

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to Log in.')
            return redirect('user-login')
        return render(request, 'users/register.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})


class ProfileView(View):

    def get(self, request, *args, **kwargs):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, 'users/profile.html', context)

    def post(self, request, *args, **kwargs):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('user-profile')




