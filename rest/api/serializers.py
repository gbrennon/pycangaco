from marshmallow import Schema, fields


class AtividadeSerializer(Schema):
    id = fields.String()

    class Meta:
        additional = ('nome', 'descricao')


class PraiaSerializer(Schema):
    id = fields.String()
    atividades = fields.Nested(AtividadeSerializer, many=True)

    class Meta:
        additional = ('nome', 'descricao')
