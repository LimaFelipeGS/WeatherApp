[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/LimaFelipeGS/WeatherApp/blob/main/README.en.md)

# WeatherApp

## Descrição
WeatherApp é uma aplicação simples para desktop desenvolvida em Python para mostrar informações de clima atual de uma cidade para o usuário utilizando a API OpenWeatherMap. A aplicação mostra informações de temperatura e condição climática - como chuva, névoa ou nublado. 

## Exemplo de Visualização
<img width="449" height="517" alt="Image" src="https://github.com/user-attachments/assets/b81630b3-9d4a-4965-808b-65052fa14e76" />

## Tecnologias Utilizadas

- Python
- PyQt5
- Requests
- API OpenWeatherMap

## Tratamento de Erros

A aplicação mostra mensagens de erro compreensivas para os seguintes tipos de erros:

- Nome de cidade inválido
- Nome de cidade vazio
- Falha de conexão a internet
- Chave da API inválida
- Erros de servidor
- Erros de timeout

## Chave da API

Utilize a sua própria chave da API para executar a aplicação, para isso:
- Visite [OpenWeatherMap](https://openweathermap.org/)
- Crie sua conta gratuitamente
- Copie a chave da API que será gerada automaticamente (ou crie uma nova chave)
- Substitua a chave na variável "api_key" na função "get_weather"

Obs: A ativação da chave da API pode levar algumas horas, caso sua chave não esteja ativa ainda a aplicação irá indicar que a chave fornecida é inválida

## Pré-Requisitos

Após instalação da aplicação, é necessário instalar os pacotes PyQt5 e requests no terminal com os seguintes comandos:

```bash
pip install PyQt5
```

```bash
pip install requests
```
