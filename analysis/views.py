from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView

from analysis.filter import Filter
from analysis.forms import NewLogForm, FilterForm
from analysis.models import Analysis
from utils.file_processor import FileProcessor


class IndexView(ListView):
    model = Analysis
    template_name = 'analysis/index.html'
    context_object_name = 'logs'
    extra_context = {'form': NewLogForm(), 'filter_form': FilterForm()}
    paginate_by = 5

    def get_queryset(self):
        title = self.request.GET.get("title")
        section = self.request.GET.get("section")
        log_id = self.request.GET.get("log_id")

        queryset = Analysis.objects.filter(user_id=self.request.user.id)
        if title or section or log_id:
            print("Time to filter")
            return queryset.filter(Q(title__icontains=title) | Q(section=section.upper()) | Q(log_id=log_id))
        else:
            return queryset


class UploadLogFileView(View):
    http_method_names = ["post", "get"]  # let's allow only post request.
    form_class = NewLogForm
    success_url = reverse_lazy('records')
    template_name = 'analysis/index.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            FileProcessor(form, request.user)  # send file for processing

            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})
