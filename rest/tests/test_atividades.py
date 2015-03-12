from api.models import Atividades
from base import BaseTestCase
import json


def create_atividades(model, qnty):
    return Atividades.objects.insert([Atividades(**model)
                                     for x in range(qnty)])


class AtividadesTestCase(BaseTestCase):
    def setUp(self):
        self.model = {
            'nome': 'Surf',
            'descricao': 'E um esporte muito radical!'
        }

    def tearDown(self):
        Atividades.drop_collection()

    def test_get_an_empty_list_of_atividades(self):
        response = self.client.get('/v1/atividades')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['atividades'], [])

    def test_post_an_atividade(self):
        response = self.client.post('/v1/atividades',
                                    data=json.dumps(Atividades(**self.model).
                                                    __dict__['_data']),
                                    content_type='application/json')
        response.json['atividade'].pop('id')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['atividade'], self.model)

    def test_get_an_atividade(self):
        ativ = create_atividades(self.model, 1)[0]
        response = self.client.get('/v1/atividades/' + str(ativ['id']))
        response.json['atividade'].pop('id')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['atividade'], self.model)
