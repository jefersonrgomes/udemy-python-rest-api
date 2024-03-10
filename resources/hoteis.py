from flask_restful import Resource

hoteis = [
    {
    'hotel_id' : '1',
    'nome' : 'hotel 1',
    'estrelas' : '5',
    'diaria' : '500.00',
    'cidade' : 'cidade 1'
    },
    {
    'hotel_id' : '2',
    'nome' : 'hotel 2',
    'estrelas' : '4',
    'diaria' : '400.00',
    'cidade' : 'cidade 2'
    },
    {
    'hotel_id' : '3',
    'nome' : 'hotel 3',
    'estrelas' : '3',
    'diaria' : '300.00',
    'cidade' : 'cidade 3'
    },
    {
    'hotel_id' : '4',
    'nome' : 'hotel 4',
    'estrelas' : '2',
    'diaria' : '200.00',
    'cidade' : 'cidade 4'
    }
    ]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}    