from django.http import HttpRequest
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from choice.models import ChoiceModel
from main.models import UserModel
from .models import ElectionModel
from .serializers import ElectionSerializerId, ElectionSerializer, CreateElectionSerializer
from main.error import HttpError


class ElectionViewSet(ViewSet):
    list_serializer_class = ElectionSerializer
    serializer_id_class = ElectionSerializerId
    create_serializer = CreateElectionSerializer
    
    @action(
        methods=['GET'],
        detail=False
    )
    def elections(self, request: HttpRequest):
        elections = ElectionModel.objects.all()
        serializer = self.list_serializer_class(elections, many=True)
        return Response(serializer.data)

    @action(
        methods=['GET'],
        detail=False
    )
    def get_election(self, request: HttpRequest) -> Response:
        serializer = self.serializer_id_class(data={'id': request.GET.get('id')})
        serializer.is_valid(raise_exception=True)
        election = serializer.validated_data['id']
        serializer = self.list_serializer_class(election, many=True)
        
        return Response({'response': serializer.data})

    @action(
        methods=['GET'],
        detail=False
    )
    def finish_election(self, request: HttpRequest) -> Response:
        serializer = self.serializer_id_class(data={'id': request.GET.get('id')})
        serializer.is_valid(raise_exception=True)
        election_id = serializer.validated_data['id'][0].id

        total_voters = UserModel.objects.filter(election_id=election_id).count()
        if total_voters == 0:
            raise HttpError(404, 'У голосования еще нет участников')

        choices = (
            ChoiceModel.objects
            .filter(election_id=election_id)
            .annotate(votes=Count('user'))
        )

        stats = [
            {
                'name': c.name,
                'votes': c.votes,
                'percentage': round(c.votes / total_voters * 100)
            }
            for c in choices
        ]

        max_pct = max(item['percentage'] for item in stats)
        winners = [item['name'] for item in stats if item['percentage'] == max_pct]

        if len(winners) > 1:
            result_msg = f'Ничья между {", ".join(winners)} с {max_pct}% голосов'
        else:
            result_msg = f'Победил выбор "{winners[0]}" с процентом {max_pct}%'

        response_data = {
            'message': 'Итоги голосования:',
            'statistic': [
                f"За ответ '{item['name']}' проголосовало {item['percentage']}% ({item['votes']} человек)"
                for item in stats
            ],
            'winner': result_msg
        }

        return Response({'response': response_data})
    
    @action(
        methods=['POST'],
        detail=False
    )
    def add_election(self, request: HttpRequest) -> Response:
        serializer = self.create_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({'response': f'Голосование "{serializer.validated_data['name']}" добавлено'}, status=201)
    
    @action(
        methods=['POST'],
        detail=False
    )
    def delete_election(self, request: HttpRequest):
        serializer = self.serializer_id_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        election = serializer.validated_data['id']
        election.delete()
        
        return Response({'response': 'Удаление прошло успешно! Все участники, выборы к голосованию и голосование, были удалены из базы данных'})