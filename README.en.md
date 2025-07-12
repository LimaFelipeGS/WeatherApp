[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/LimaFelipeGS/WeatherApp/blob/main/README.md)

# WeatherApp

## Description

WeatherApp is a simple desktop application built with Python that allows users to check current weather information of any city using the OpenWeatherMap API. The application displays temperature and climate condition information - such as rain, drizzle or clear sky.

## Preview
<img width="449" height="517" alt="Image" src="https://github.com/user-attachments/assets/b81630b3-9d4a-4965-808b-65052fa14e76" />

## Technologies Employed

- Python
- PyQt5
- Requests
- API OpenWeatherMap

## Error Handling

The application displays comprehensive error messages for the following error types:

- Invalid city name
- Empty city input
- Connection error
- Invalid API Key
- Server errors
- Timeout error

## API Key

Use your own API Key to run the applicattion following these steps:
- Visit [OpenWeatherMap](https://openweathermap.org/)
- Create your account for free
- Copy the API Key that will be generated automatically (or create a new key)
- Replace the value in the "api_key" variable, located in the "get_weather" function

Note: The API Key takes a few hours to be activated, if your key isn't yet active the application will return the message that the key is invalid.

## Pre-Requisites

After installing the application, it is necessary to install PyQt5 and requests packages with the following terminal commands:

```bash
pip install PyQt5
```

```bash
pip install requests
```
