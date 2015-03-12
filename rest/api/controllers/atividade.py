from flask.ext.restful import Resource
from api import api, request, abort
from api.models import Atividades
from marshmallow import Schema, fields


class AtividadesSerializer(Schema):
    id = fields.String()

    class Meta:
        additional = ('nome', 'descricao')


class AtividadesListView(Resource):
    def get(self):
        atividades = Atividades.objects.all()
        return {'atividades': AtividadesSerializer(atividades, many=True).data}

    def post(self):
        if not request.json:
            abort(400)
        atividade = Atividades(**request.json)
        atividade.save()
        return {'atividade': AtividadesSerializer(atividade).data}, 201


class AtividadesView(Resource):
    def get(self, id):
        atividade = Atividades.objects.get_or_404(id=id)
        return {'atividade': AtividadesSerializer(atividade).data}

api.add_resource(AtividadesListView, '/v1/atividades')
api.add_resource(AtividadesView, '/v1/atividades/<id>')
