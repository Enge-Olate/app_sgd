import os

class Dirs:
    def __init__(self, nome_pasta, get_path='c:/Users/marci/Documentos', pastas=['TESTE', 'PDF', 'DIELETRCO']):
        
        
        self.get_path = get_path
        self.pastas = pastas
        self.nome_pasta = nome_pasta
        self.mensagem = f'A pasta {self.nome_pasta} já existe.'
        
    def criar_pastas(self):
        try:
            if self.get_path:
                print(f'Tentando mudar para o diretório: {self.get_path}')
                os.chdir(self.get_path)
            else:  
                raise FileNotFoundError('Diretório não encontrado!')

            print(f'Tentando criar a pasta: {self.nome_pasta}')
            if not os.path.exists(self.nome_pasta):
                os.makedirs(os.path.join(self.get_path, self.nome_pasta))
                print(f'Tentando mudar para o diretório: {self.nome_pasta}')    
                os.chdir(self.nome_pasta)
                for pasta in self.pastas:
                    print(f'Tentando criar às subpastas: {pasta}')
                    if not os.path.exists(pasta):
                        os.makedirs(pasta)
                print(f'Pasta {self.nome_pasta} criada com sucesso!')
                return True
            else:
                raise FileExistsError(self.mensagem)
            
        except FileExistsError:
            print(f'Erro: {self.mensagem}')
        except FileNotFoundError as e:
            print('Erro: Diretório não encontrado!{e}')
            raise e
        finally:
            print('Fim do programa!')