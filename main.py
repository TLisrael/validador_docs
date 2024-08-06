# pyinstaller --onefile validar_documentos.py || Arquivo dentro da pasta dist 

import re

def validar_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')
    
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    
def validar_docs(tipo_doc, valor_doc):
    if tipo_doc == 'cpf':
        return validar_cpf(valor_doc)
    
    elif tipo_doc == 'rg':
        return bool(re.match(r'^[0-9]{2}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}$', valor_doc))
    
    elif tipo_doc == 'cnh':
        return bool(re.match(r'^[0-9]{11}$', valor_doc))
    
    else:
        return False



def main():
    print('Validação de documentos')
    tipo_doc = input('Informe o tipo de documento (CPF, RG ou CNH)').strip().lower()
    num_doc = input('Informe o numero de documentos').strip()
    
    
    try:
        valido = validar_docs(tipo_doc, num_doc)
        if valido:
            print(f'O número {num_doc} é válido para o tipo de documento {tipo_doc.upper()}')
        else:
            print(f'O número {num_doc} não é válido para o tipo de documento {tipo_doc.upper()}')
    except Exception as e:
        print(f'Erro ao validar o documento: {str(e)}')

if __name__ == '__main__':
    main()