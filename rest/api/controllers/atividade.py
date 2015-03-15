from flask.ext.restful import Resource
from api import api, request, abort
from api.models import Atividade
from api.serializers import AtividadeSerializer


class AtividadeListView(Resource):
    def get(self):
        atividades = Atividade.objects.all()
        return AtividadeSerializer(atividades, many=True).data

    def post(self):
        if not request.json:
            abort(400)
        atividade = Atividade(**request.json)
        atividade.save()
        return AtividadeSerializer(atividade).data, 201


class AtividadeView(Resource):
    def get(self, id):
        atividade = Atividade.objects.get_or_404(id=id)
        return AtividadeSerializer(atividade).data

    def put(self, id):
        if not request.json:
            abort(400)
        atividade = Atividade.objects.get_or_404(id=id)
        for key, element in request.json.items():
            atividade[key] = element
        atividade.save()
        return AtividadeSerializer(atividade).data, 200

    def delete(self, id):
        Atividade.objects.get_or_404(id=id).delete()
        return '', 200

api.add_resource(AtividadeListView, '/v1/atividades')
api.add_resource(AtividadeView, '/v1/atividades/<id>')
