import os

class Dirs:
    def __init__(
            self, 
            nome_pasta, 
            get_path_tc='c:/Users/Public/Documents/TC',
            get_path_tp='c:/Users/Public/Documents/TP',
            pastas=['TESTE', 'PDF', 'DIELETRICO']):
        
        self.get_path_tc = get_path_tc
        self.get_path_tp = get_path_tp
        self.pastas = pastas
        self.nome_pasta = nome_pasta
        self.mensagem = f'A pasta {self.nome_pasta} já existe.'
        
    def criar_pastas_tc(self):
        try:
            if self.get_path_tc:
                print(f'Tentando mudar para o diretório: {self.get_path_tc}')
                os.chdir(self.get_path_tc)
            else:  
                raise FileNotFoundError('Diretório TC não encontrado!')

            print(f'Tentando criar a pasta: {self.nome_pasta}')
            if not os.path.exists(self.nome_pasta):
                os.makedirs(os.path.join(self.get_path_tc, self.nome_pasta))
                print(f'Tentando mudar para o diretório: {self.nome_pasta}')    
                os.chdir(self.nome_pasta)
                for pasta in self.pastas:
                    print(f'Tentando criar as subpastas: {pasta}')
                    if not os.path.exists(pasta):
                        os.makedirs(pasta)
                print(f'Pasta {self.nome_pasta} criada com sucesso!')
                return True
            else:
                raise FileExistsError(self.mensagem)
            
        except FileExistsError:
            print(f'Erro: {self.mensagem}')
        except FileNotFoundError as e:
            print(f'Erro: Diretório não encontrado! {e}')
            raise e
        finally:
            print('Fim do programa!')

    def criar_pastas_tp(self):
        try:
            if self.get_path_tp:
                print(f'Tentando mudar para o diretório: {self.get_path_tp}')
                os.chdir(self.get_path_tp)
            else:  
                raise FileNotFoundError('Diretório TP não encontrado!')

            print(f'Tentando criar a pasta: {self.nome_pasta}')
            if not os.path.exists(self.nome_pasta):
                os.makedirs(os.path.join(self.get_path_tp, self.nome_pasta))
                print(f'Tentando mudar para o diretório: {self.nome_pasta}')    
                os.chdir(self.nome_pasta)
                for pasta in self.pastas:
                    print(f'Tentando criar as subpastas: {pasta}')
                    if not os.path.exists(pasta):
                        os.makedirs(pasta)
                print(f'Pasta {self.nome_pasta} criada com sucesso!')
                return True
            else:
                raise FileExistsError(self.mensagem)
            
        except FileExistsError:
            print(f'Erro: {self.mensagem}')
        except FileNotFoundError as e:
            print(f'Erro: Diretório não encontrado! {e}')
            raise e
        finally:
            print('Fim do programa!')