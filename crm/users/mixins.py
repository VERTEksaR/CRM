from django.core.exceptions import PermissionDenied


class GroupRequiredMixin:
    """Mixin для проверки наличия у пользователя группы с правами"""
    group_required = None

    def dispatch(self, request, *args, **kwargs):
        """Метод для определения группы ролей у пользователя"""
        if not request.user.is_authenticated:
            raise PermissionDenied
        user_groups = []
        for group in request.user.groups.values_list('name', flat=True):
            user_groups.append(group)
        if len(set(user_groups).intersection(self.group_required)) <= 0:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
