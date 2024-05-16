def get_param(request, param, default=None):
    value = request.GET.get(param)
    return value


def get_param_int(request, param, default=None):
    try:
        value = int(request.GET.get(param))
    except (TypeError, ValueError):
        return default
    return value
