import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, 
                            QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Digite o nome da cidade:  ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Buscar", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App") # Nome da janela
        self.setWindowIcon(QIcon("images/cloud.png")) # Ícone da janela

        # Gerenciador de layout vertical
        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        # Alinhamento dos objetos
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        # Objetos nomeados para aplicação de CSS
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        # Aplicação de CSS
        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input{
                font-size: 40px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 75px;
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather) # Conectar o clique do botão a função get_weather

    # Conexão com a API
    def get_weather(self):
        api_key = "7264e793bd8c1afb846670edd33d42eb"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=pt_br"

        try:
            response = requests.get(url)
            response.raise_for_status() # Raises an exception if there is any HTTPErrors
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)
        # Tratamento de erros
        except requests.exceptions.HTTPError as http_error: # Erros de HTTP
            match response.status_code:
                case 400:
                    self.display_error("Bad Request:\nRevise o nome da cidade")
                case 401:
                    self.display_error("Unauthorized:\nChave API invalida")
                case 403:
                    self.display_error("Forbidden:\nAcesso Negado")
                case 404:
                    self.display_error("Not Found:\nCidade nao encontrada")
                case 500:
                    self.display_error("Internal Server Error:\nTente novamente mais tarde")
                case 502:
                    self.display_error("Bad Gateway:\nResposta invalida do servidor")
                case 503:
                    self.display_error("Service Unavailable:\nServidor fora do ar")
                case 504:
                    self.display_error("Gateway Timeout:\nSem resposta do servidor")
                case _:
                    self.display_error(f"HTTP Error:\n{http_error}")

        except requests.exceptions.ConnectionError: # Erro de conexão
            self.display_error("Conection Error:\nVerifique sua conexão de internet")

        except requests.exceptions.Timeout: # Erro de timeout
            self.display_error("Timeout Error:\nO sistema nao retornou uma resposta no tempo limite")

        except requests.exceptions.TooManyRedirects: # Muitos redirecionamentos
            self.display_error("Too many Redirects:\nVerifique o URL")

        except requests.exceptions.RequestException as req_error: # Outros erros possíveis
            self.display_error(f"Request Error: {req_error}")

    # Atualiza o erro na janela
    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    # Atualiza as informações da cidade pesquisada
    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 75px;")

        temperature_kelvin = data["main"]["temp"]
        temperature_celsius = temperature_kelvin - 273.15 # Converter a temperatura para Celsius

        weather_id = data["weather"][0]["id"]

        weather_description = data["weather"][0]["description"]
        
        self.temperature_label.setText(f"{temperature_celsius:.0f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(f"{weather_description}")

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232: # Tempestade
            return "⛈️​"
        elif 300 <= weather_id <= 321: # Garoa
            return "🌦️​"
        elif 500 <= weather_id <= 531: # Chuva
            return "🌧️​"
        elif 600 <= weather_id <= 622: # Neve
            return "❄️​"
        elif 701 <= weather_id <= 741: # Névoa
            return "🌫️​​"
        elif weather_id == 762: # Névoa vulcânica
            return "🌋​​"
        elif weather_id == 771: # Ventos fortes
            return "💨​​​"
        elif weather_id == 781: # Tornado
            return "🌪️​​​​"
        elif weather_id == 800: # Céu limpo
            return "☀️​​​​​"
        elif 801 <= weather_id <= 804: # Nublado
            return "☁️​​​​​​"
        else:
            return ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
