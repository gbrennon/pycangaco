from api.models import Praias, Atividades
from api.controllers.praia import PraiasSerializer
from tests.test_atividades import create_atividades
from base import BaseTestCase
import json


class PraiaTestCase(BaseTestCase):
    def setUp(self):
        self.surf_model = {
            'nome': 'Surf',
            'descricao': 'Surf e demais!'
        }
        self.sup_model = {
            'nome': 'Stand Up',
            'descricao': 'Stand Up e demais!'
        }
        sup = create_atividades(self.sup_model, 1)[0]['id']
        surf = create_atividades(self.surf_model, 1)[0]['id']
        self.model = {
            'nome': 'Porto da Barra',
            'descricao': 'Portao e sucesso!',
            'atividades': [str(surf), str(sup)]
        }

    def tearDown(self):
        Praias.drop_collection()
        Atividades.drop_collection()

    def test_get_an_empty_list_of_praias(self):
        response = self.client.get('/v1/praias')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['praias'], [])

    def test_post_an_invalid_praia(self):
        response = self.client.post('/v1/praias')
        self.assertEqual(response.status_code, 400)

    def test_post_a_praia(self):
        response = self.client.post('/v1/praias',
                                    data=json.dumps(self.model),
                                    content_type='application/json')
        response.json['praia'].pop('id')
        self.assertEqual(response.status_code, 201)
