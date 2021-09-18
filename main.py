import pandas as pd
from twilio.rest import Client

# Seu SID de conta da twilio.com/console
account_sid = "AC86df5550c4069d3c3b28afbbe283d807"
# Seu Auth Token de twilio.com/console
auth_token  = "68381f20287af6c5cbc5526d86a5687f"
client = Client(account_sid, auth_token)


# Abrir os 6 arquivos em exel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx') # f {valor} faz um luping
    if (tabela_vendas['Vendas'] > 55000).any(): # verifica apenas a coluna vendas | any() para verificar se TEM algum valor maior que 55000
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'no mes {mes} alguem bateu a meta. Vendedor: {vendedor}, vendas: {vendas}')
        message = client.messages.create(
            to="+552187890765", 
            from_="+19563406789",
            body=f'no mes {mes} alguem bateu a meta. Vendedor: {vendedor}, vendas: {vendas}')

        print(message.sid)




      
# Para cada arquivo:

# Verificar e algum valor na coluna vendas daquele arquivo é maior que 55.000 mil

# Se for maior do que 55.000 mil -> Envia um SMS com o Nome, o Mes e as vendas do vendedor

# Caso não seja maioor que 55.000, não irei fazer nada.


