from django.db.models import Q
from django.views import generic
from .models import Car


class IndexView(generic.ListView):
    model = Car
    paginate_by = 15

    def get_queryset(self):
        queryset = Car.objects.all()
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(number__icontains=keyword)| Q(area__name__icontains=keyword) | Q(insurance_period__end_time__icontains=keyword)
            )

        return queryset

class DetailView(generic.DetailView):
    model = Car