from django.shortcuts import render
from asociados.models import Asociado
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView,UpdateView,CreateView
from asociados.forms import AsociadoForm
# Create your views here.
class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request,*args,**kwargs)

@method_decorator(login_required(),name='dispatch')
class AsociadosList(ListView):
    model = Asociado
    template_name = 'Asociados/listaAsociados.html'
    context_object_name = 'asociados'
    paginate_by = 10
    queryset = Asociado.objects.all()

@method_decorator(login_required(),name='dispatch')
class AsociadoCreate(CreateView):
    model = Asociado
    form_class = AsociadoForm
    template_name = 'Asociados/crearAsociado.html'
    success_url = reverse_lazy('Asociados:AsociadosAsociados')

@method_decorator(login_required(),name='dispatch')
class AsociadoEditar(UpdateView):
    model = Asociado
    form_class = AsociadoForm
    template_name = 'Asociados/editarAsociado.html'
    success_url = reverse_lazy('Asociados:AsociadosAsociados')