from django.conf.urls import include, url
from .views import HomePageView, Paragens_dataset, c6_dataset, c9_dataset

urlpatterns = [
url(r'^$', HomePageView.as_view(), name = 'home'),
url(r'^Paragens_data$', Paragens_dataset, name = 'Paragens'),
url(r'^c6_data$', c6_dataset, name = 'c6y'),
url(r'^c9_data$', c9_dataset, name = 'c9y'),

]
