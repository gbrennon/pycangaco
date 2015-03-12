from flask.ext.restful import Resource
from api import api, request, abort
from api.models import Praias, Atividades
from api.controllers.atividade import AtividadesSerializer
from marshmallow import Schema, fields


class PraiasSerializer(Schema):
    id = fields.String()
    atividades = fields.Nested(AtividadesSerializer, only=['nome'], many=True)

    class Meta:
        additional = ('nome', 'descricao')


class PraiasListView(Resource):
    def get(self):
        praias = Praias.objects.all()
        return {'praias': PraiasSerializer(praias, many=True).data}

    def post(self):
        if not request.json:
            abort(400)
        praia = Praias(**request.json)
        praia.save()
        return {'praia': PraiasSerializer(praia).data}, 201


class PraiaView(Resource):
    def get(self, id):
        praia = Praias.objects.get_or_404(id=id)
        return {'praia': PraiasSerializer(praia).data}


api.add_resource(PraiasListView, '/v1/praias')
api.add_resource(PraiaView, '/v1/praias/<id>')
