from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class HomePage(TemplateView):
    template_name = 'flash/homepage.html'
    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['post'] = Post.objects.all()
        context['pro'] = Projects.objects.all()
        return context

class PostPage(TemplateView):
    template_name = 'post.html'

    def get_context_data(self, **kwargs):
        context = super(PostPage, self).get_context_data(**kwargs)
        context['post'] = Post.objects.all()
        return context


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

# class Contact(TemplateView):
#   template_name = "flash/contact.html"


class Contact(CreateView):
    model = Contact
    template_name = "flash/contact.html"
    # form_class=""
    form_class = ContactForm
    def get_success_url(self):
        return reverse_lazy('Contact')

    def form_valid(self,ContactForm):
        ContactForm.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, ContactForm):
        return self.render_to_response(self.get_context_data(ContactForm=ContactForm))

class ProjectsPage(TemplateView):
    template_name = 'flash/projects.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectsPage, self).get_context_data(**kwargs)
        context['pro'] = Projects.objects.all()
        return context
