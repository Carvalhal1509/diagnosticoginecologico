# Importação do Módulo
import modulo_execucao


# Mensagens da Aplicação
def títulos(msg):
    print('+=' * 40)
    print(f'\033[1:35m{msg:^80}\033[m')
    print('+=' * 40)


def grim60():
    print(f'=> \033[0:31mVocê está com {modulo_execucao.dados["idade"]} anos, portanto, '
          f'está em grupo de risco pela idade e deve procurar um medico.\033[m')


def gri():
    print(f'=> \033[0:32mVocê está com {modulo_execucao.dados["idade"]} anos, portanto, '
          f'não está em grupo de risco pela idade.\033[m')


def msganemias():
    print(f'=> \033[0:31mVocê é anemica, isso agrava o seu quadro ginecologico!\033[m')


def msganemian():
    print(f'=> \033[0:32mVocê não é anemica. Parabéns! Isso pode não agravar seu quadro ginecologico!\033[m')
    
def msgmiomas():
    print(f'=> \033[0:31mVocê pode ter um Mioma, isso agrava o seu quadro ginecologico!\033[m')
    
def msgmioman():
    print(f'=> \033[0:32mVocê não tem um mioma.Parabéns! Isso pode não agravar seu quadro ginecologico!\033[m')


def msgdoencass():
    print(f'=> \033[0:31mSeu quadro de doenças pré-existentes que podem agravar o fator '
          f'de risco: \033[m')
    print(f'    => \033[0:31m{modulo_execucao.doenças}\033[m')


def msgdoencasn():
    print(f'=> \033[0:32mVocê não possui quadro prévio, portanto, não terá o '
          f'risco agravado.\033[m')

def msgsintomasmenosgraves():
    print(f'=> \033[1:31mVocê apresenta sérios sintomas que podem indicar Vulvovaginite. \n'
          f'    Procure imediatamente um ponto de atendimento e relate seus sintomas. \n'
          f'    Cuide-se, pois, o seu quadro pode se agravar rapidamente!\033[m')

def msgsintomasgraves():
    print(f'=> \033[1:32mVocê apresenta sérios sintomas que podem indicar Mioma Uterino. \n'
          f'    Procure imediatamente um ponto de atendimento e relate seus sintomas. \n'
          f'    Cuide-se, pois, o seu quadro pode se agravar rapidamente!\033[m')

def msgsintomasendo():
    print(f'=> \033[1:31mVocê apresenta sérios sintomas que podem indicar Endometriose. \n'
          f'    Procure imediatamente um ponto de atendimento e relate seus sintomas. \n'
          f'    Cuide-se, pois, o seu quadro pode se agravar rapidamente!\033[m')



def msgsintomasleves():
    print(f'=> \033[0:33mVocê apresenta sintomas leves que podem significar Candidiase. \n'
          f'    Se apresentar quadro de colica intensa, procure o sistema de \n'
          f'    saúde imediatamente relatando os sintomas apresentados.\033[m')


def msgsemsintomas():
    print(f'=> \033[0:32mVocê não possui nenhum sintoma de doenca,que pode significar Vulvite. \n'
          f'    Caso o quadro nao melhore, procure o sistema de saúde.\033[m')


def cabeçalhorel():
    print(f'\033[0:32m{modulo_execucao.dados["nome"]}\033[m, segue o relatório baseado '
          f'em suas respostas:')


# Tratamento de Erros
def errodado():
    print(f'\033[0:31m=> Dado inválido, tente novamente!\033[m')


def errogenerico():
    print(f'\033[0:31m=> Houve um erro geral no Sistema!\033[m')