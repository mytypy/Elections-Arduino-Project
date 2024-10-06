from rest_framework.generics import ListAPIView
from .models import ElectionModel
from .serializers import ElectionSerializer


class Election(ListAPIView):
    serializer_class = ElectionSerializer
    
    def get_queryset(self):
        return ElectionModel.objects.filter(pk=self.kwargs['pk'])