from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Factory, Unit, Equipment
from .serializers import FactorySerializer, UnitSerializer, EquipmentSerializer
from .utils import get_all_parents, get_all_children

# DRF ViewSets (без изменений)
class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.select_related('factory').all()
    serializer_class = UnitSerializer

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.prefetch_related('units__factory').all()
    serializer_class = EquipmentSerializer

# HTML-views

def index(request):
    factories = Factory.objects.prefetch_related('units__equipment').all()
    units = Unit.objects.select_related('factory').all()
    equipment = Equipment.objects.prefetch_related('units__factory').all()

    equipment_data = []
    for e in equipment:
        us = list(e.units.all())
        # собираем уникальные фабрики с id и name
        seen = set()
        fs = []
        for u in us:
            f = u.factory
            if f.id not in seen:
                seen.add(f.id)
                fs.append({'id': f.id, 'name': f.name})
        # юниты тоже переводим в упрощенный формат
        uds = [{'id': u.id, 'name': u.name} for u in us]
        equipment_data.append({
            'id':          e.id,
            'name':        e.name,
            'units':       uds,
            'factories':   fs
        })

    return render(request, 'core/index.html', {
        'factories':      factories,
        'units':          units,
        'equipment_data': equipment_data
    })


def hierarchy(request, model, pk):
    model_map = {'factory': Factory, 'unit': Unit, 'equipment': Equipment}
    Model = model_map[model]
    obj = get_object_or_404(Model, pk=pk)
    return render(request, 'core/hierarchy.html', {
        'object':   obj,
        'model':    model.capitalize(),
        'parents':  get_all_parents(obj),
        'children': get_all_children(obj),
    })
