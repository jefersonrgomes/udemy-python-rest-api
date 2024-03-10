from flask_restful import Resource, reqparse

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
    'hotel_id' : 'teste',
    'nome' : 'hotel 4',
    'estrelas' : '2',
    'diaria' : '200.00',
    'cidade' : 'cidade 4'
    }
    ]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}    

class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'message': 'Hotel não encontrado'}, 404

    def post(self, hotel_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome', type=str, required=True, help="The field 'nome' cannot be left blank")
        argumentos.add_argument('estrelas', type=float, required=True, help="The field 'estrelas' cannot be left blank")
        argumentos.add_argument('diaria', type=float, required=True, help="The field 'diaria' cannot be left blank")
        argumentos.add_argument('cidade', type=str, required=True, help="The field 'cidade' cannot be left blank")

        dados = argumentos.parse_args()
        
        novo_hotel = {
            'hotel_id' : hotel_id,
            'nome' : dados['nome'],
            'estrelas' : dados['estrelas'],
            'diaria' : dados['diaria'],
            'cidade' : dados['cidade']
        }
        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass