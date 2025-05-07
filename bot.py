from core.client import PorypyClient

# Inicializando o bot
client = PorypyClient()

# Rodando o bot com o token do arquivo de configuração
client.run(client.token)