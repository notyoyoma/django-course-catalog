from django.core.urlresolvers import reverse_lazy
from django.views import generic
from courses.models import Course, CourseForm


class IndexView(generic.ListView):
    model = Course


class DetailView(generic.DetailView):
    model = Course


class CreateView(generic.CreateView):
    model = Course
    success_url = reverse_lazy('index')
    form_class = CourseForm


class UpdateView(generic.UpdateView):
    model = Course
    success_url = reverse_lazy('index')
    form_class = CourseForm
    template_name_suffix = '_update_form'


