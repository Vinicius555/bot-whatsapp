# Bot de Envio Automático de Mensagens no WhatsApp

## Visão Geral

Este script em Python automatiza o processo de envio de mensagens personalizadas no WhatsApp para clientes com base em informações armazenadas em uma planilha do Excel. O script utiliza a biblioteca openpyxl para manipulação de arquivos Excel, pyautogui para automatizar ações do mouse e teclado, e webbrowser para abrir a interface web do WhatsApp.

## Instruções de Uso
## Importando Bibliotecas

Certifique-se de ter as bibliotecas necessárias instaladas executando:

pip install openpyxl

pip install pyautogui

pip install pillow

## Autenticação no WhatsApp
Abra a interface web do WhatsApp visitando https://web.whatsapp.com/.

Execute o script e aguarde 30 segundos para permitir o carregamento do WhatsApp web.

## Lendo Planilha do Excel

Certifique-se de ter um arquivo Excel chamado clientes.xlsx com uma planilha chamada Sheet1.

A planilha deve conter informações do cliente com as colunas: Nome, Telefone e Vencimento.

## Enviando Mensagens no WhatsApp
O script lê as informações do cliente e gera mensagens personalizadas.

As mensagens incluem o nome do cliente e a data de vencimento do cartão com um link de pagamento.

## Tratamento de Erros
Se houver problemas no envio de mensagens, as informações de erro são registradas no arquivo erros.csv.

## Nota Importante
Certifique-se de ter o arquivo de imagem necessário (seta.png) para identificar a localização do botão de envio na interface do WhatsApp.

## Informações Adicionais

Autor: vinicius gabriel

Versão: 1.0

Contato: viniicius.dev@gmail.com
