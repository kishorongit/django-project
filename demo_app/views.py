from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import TeacherForm
from .models import Teacher
# Create your views here.


def index_view(request):
    return render(request, "demo_app/index.html")


class TeacherCreateView(CreateView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('teacher-list')


class TeacherListView(ListView):
    model = Teacher
    paginate_by = 10

    def get_context_date(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = '__all__'
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('teacher-list')


class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teacher-list')
