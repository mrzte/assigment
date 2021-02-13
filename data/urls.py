from django.urls import path
from .views import DataDiriView,DataDiriDetailView

urlpatterns = [
    path('', DataDiriView.as_view(), name='data'),
    path('<int:pk>', DataDiriDetailView.as_view(), name='data-detail')
]