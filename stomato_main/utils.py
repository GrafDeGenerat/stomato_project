from django.views.generic.base import ContextMixin

top_menu = [
    {
        'title': 'Главное меню',
        'url': 'home'
    },
    {
        'title': 'Клиенты',
        'url': 'client_list'
    },
    {
        'title': 'Врачи',
        'url': 'doctor_list'
    },
    {
        'title': 'Записи',
        'url': 'visit_list'
    },

]


class RequiredMixin(ContextMixin):
    title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_menu'] = top_menu
        if self.title is not None:
            context['title'] = self.title
        return context
