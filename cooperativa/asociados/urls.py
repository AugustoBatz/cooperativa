from django.urls import path
from asociados.views import AsociadosList,AsociadoCreate,AsociadoEditar

urlpatterns=[
    path('asociadoslist/',AsociadosList.as_view(),name='AsociadosAsociados'),
    path('asociadoscreate/',AsociadoCreate.as_view(),name='CrearAsociado'),
    path('editarasociado/<int:pk>',AsociadoEditar.as_view(),name='EditarAsociado')

]