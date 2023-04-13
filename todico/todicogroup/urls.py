from django.urls import path
from todicogroup.views import index,detail,product,card

urlpatterns = [
    path('', index, name='home'),
    path('<int:myid>', detail, name="detail"),
    path('<int:jyid>',product , name="product"),
    path('card /',card , name="card"),
]
