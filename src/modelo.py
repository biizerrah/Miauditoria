
class Gatinho:

    def __init__(self, nome: str, cor: str, sexo: str):

        self.nome = nome.strip().lower()
        self.cor = cor.strip().lower()

        sexo_formatado = sexo.strip().lower()
        if sexo_formatado not in ('f', 'm'):
            raise ValueError(f"Entrada Inválida: {sexo_formatado}. Digite [f] para femea ou [m] para macho.")
        self.sexo = sexo_formatado
        
        
        

    def __repr__(self):

        return f"Gatinho(Nome: {self.nome}, Cor: {self.cor}, Sexo: {self.sexo})"


    def __str__(self):

        identificar_sexo = 'Fêmea' if self.sexo == 'f' else 'Macho'
        return f"(Nome: {self.nome.title()} | Cor: {self.cor.title()} | Sexo: {identificar_sexo})"


    def to_dict(self):

        return {

            'nome': self.nome,
            'cor': self.cor,
            'sexo': self.sexo
        }

    @staticmethod
    def to_obj(data: dict):

        return Gatinho(

            nome = data['nome'],
            cor = data['cor'],
            sexo = data['sexo']
        )




    