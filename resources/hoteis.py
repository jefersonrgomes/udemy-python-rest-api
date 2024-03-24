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

class HotelModel:
    def __init__(self, hotel_id, nome, estrelas, diaria, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade
    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade
        }
        

class Hoteis(Resource):
    
   
    #GET ALL
    def get(self):
        return {'hoteis': hoteis}    

    def findHotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None    
class Hotel(Resource):
     #ARGUMENTS
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="The field 'nome' cannot be left blank")
    argumentos.add_argument('estrelas', type=float, required=True, help="The field 'estrelas' cannot be left blank")
    argumentos.add_argument('diaria', type=float, required=True, help="The field 'diaria' cannot be left blank")
    argumentos.add_argument('cidade', type=str, required=True, help="The field 'cidade' cannot be left blank")
    
    #GET BY ID
    def get(self, hotel_id):
        hotel = Hoteis.findHotel(hotel_id)
        if hotel:
            return hotel
        return {'message': 'Hotel não encontrado'}, 404
    
    #POST
    def post(self, hotel_id):
        dados = Hotel.argumentos.parse_args()       
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()        
        hoteis.append(novo_hotel)
        return novo_hotel, 200

    #PUT
    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        hotel = Hoteis.findHotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200
        hoteis.append(novo_hotel)
        return novo_hotel, 201
    
    #DELETE
    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message': 'Hotel deleted.'}, 200

        