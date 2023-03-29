from django.urls import path, re_path
from django.shortcuts import redirect

from analysis.views import IndexView, UploadLogFileView

urlpatterns = [
    path('', lambda req: redirect('records')),
    path('dashboard/', IndexView.as_view(), name='logs-index'),
    re_path(r'records/$', IndexView.as_view(), name='records'),
    # path('records/<title>/<section>/<log_id>/', IndexView.as_view(), name='records'),
    path('upload/', UploadLogFileView.as_view(), name='upload-file'),
]

