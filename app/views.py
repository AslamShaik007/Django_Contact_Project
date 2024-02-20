from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# def home(request):
#     context = {
#         "contact": Contact.objects.all()
#     }
#     return render(request, 'index.html', context)

# def details(request, id):
#     context = {
#         "contact": get_object_or_404(Contact, pk=id)
#     }
#     return render(request, 'detail.html', context)


class HomePageView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = Contact
    context_object_name = 'contact'

    def get_queryset(self):
        contacts = super().get_queryset()
        return contacts.filter(manager = self.request.user)
        


class DetailPageView(LoginRequiredMixin, DetailView):
    template_name = 'detail.html'
    model = Contact
    context_object_name = 'contact'

@login_required
def search(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_result = Contact.objects.filter(
            Q(name__icontains = search_term) |
            Q(info__iexact = search_term) |
            Q(phone__iexact = search_term)
        )
        context = {
            'search_term': search_term,
            'contact': search_result.filter(manager = request.user)
        }
        return render(request, 'search.html', context)
    else:
        return redirect('home-page')
    
class ContactCreateview(LoginRequiredMixin, CreateView):
    model = Contact
    template_name = 'create.html'
    fields = ['name', 'email', 'phone', 'info', 'gender', 'image']
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        messages.success(self.request, 'Your Contact Has Been Successfully Created')
        return redirect('home-page')


class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = Contact
    template_name = 'update.html'
    fields = ['name', 'email', 'phone', 'info', 'gender', 'image']
    success_url = reverse_lazy('home-page')
    
    def form_valid(self, form):
        instance = form.save()
        messages.success(self.request, 'Your Contact Has Been Successfully Updated')
        return redirect('detail', instance.pk)

class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = 'delete.html'
    success_url = reverse_lazy('home-page')

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request, 'Your Contact Has Been Successfully Deleted')
        return super().delete(self, request, *args, **kwargs)


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home-page')