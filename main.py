import requests

API_KEY = "f3cd99e18f67e8099e260474815596d4"

# Obtenha os dados meteorológicos de uma cidade
def get_weather_data(city, state):
    # Formate a consulta para a API
    query = f"{city},{state},US"
    # Faça a solicitação à API
    response = requests.get("http://apiadvisor.climatempo.com.br/api/v1/climate/temperature/locale/3477?token=412d1fcab0f8946eddf24094753b089a")
    # Verifique se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Retorne os dados meteorológicos
        return response.json()
    else:
        # Caso contrário, retorne None
        return None

# Peça ao usuário o nome da cidade e do estado
city = input("Digite o nome da cidade: ")
state = input("Digite o nome do estado: ")

# Obtenha os dados meteorológicos da cidade
data = get_weather_data(city, state)

# Verifique se os dados foram obtidos com sucesso
if data is not None:
    # Extraia a descrição do clima e a temperatura atual
    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    # Imprima os dados na tela
    print(f"O clima em {name}, {state} é {description} com temperatura de {temperature}°C")
else:
    # Caso contrário, informe que não foi possível obter os dados
    print("Não foi possível obter os dados meteorológicos para essa localidade.")
