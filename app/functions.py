from flujo.models import InstanciaFlujo


def merge_flujo_acciones(instanciaflujo):
    historia = []
    last_h = None
    for h in instanciaflujo.historia.all():
        if (last_h is None
                or last_h['accion'].estado_final != h.accion.estado_final):
            if last_h is not None:
                historia.append(last_h)
            last_h = {
                'pk': h.pk,
                'accion': h.accion,
                'updated_at': h.updated_at,
                'historia_detalle': [],
            }
        if last_h['updated_at'] < h.updated_at:
            last_h['updated_at'] = h.updated_at
        for hd in h.historia_detalle.all():
            last_h['historia_detalle'].append(hd)
    if last_h is not None:
        historia.append(last_h)
    return historia
