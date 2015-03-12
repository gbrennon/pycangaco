from api import db


class Atividades(db.Document):
    nome = db.StringField(required=True)
    descricao = db.StringField(required=True)


class Praias(db.Document):
    nome = db.StringField(required=True)
    descricao = db.StringField(required=True)
    atividades = db.ListField(db.ReferenceField('Atividades'))

Praias.register_delete_rule(Atividades, 'praias', db.NULLIFY)
