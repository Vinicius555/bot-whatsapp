# Importando Bibliotecas
import openpyxl
import pyautogui
import webbrowser
from time import sleep
from urllib.parse import quote

# Autenticando whatsaap

webbrowser.open('https://web.whatsapp.com/')
sleep(30)

# Ler planilha e guardar informações

wordbook = openpyxl.load_workbook('clientes.xlsx')
pagina_clientes = wordbook['Sheet1']

for linha in pagina_clientes.iter_rows(min_row=2):
    # lendo nome,telefone,vencimento
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value

# Criar links personalizados do whatsapp e enviar mensagens para cada cliente

    mensagem = f"Olá {nome}, seu cartão vence no dia {vencimento.strftime('%d/%m/%y')}. Favor pagar no link: https://www.google.com"

    try:
        link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'

    # Abrindo navegador

        webbrowser.open(link_mensagem_whatsapp)
        sleep(10)
    # Enviando mensagem
        seta = pyautogui.locateCenterOnScreen('seta.png')
        sleep(5)
        pyautogui.click(seta[0], seta[1])
        sleep(10)
        pyautogui.hotkey('crtl', 'w')
        sleep(5)
    except:
        # Criando arquivos de erros
        print(f"Não foi possivel enviar mensagem para {nome}")
        with open('erros.csv', 'a', newline='', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome},{telefone}')
