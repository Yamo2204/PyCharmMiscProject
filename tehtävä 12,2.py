const axios = require('axios');
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const API_KEY = 'YOUR_API_KEY'; // Korvaa omalla OpenWeather API-avaimellasi
const BASE_URL = 'https://api.openweathermap.org/data/2.5/weather';

rl.question('Anna paikkakunnan nimi: ', async (city) => {
    try {
        const response = await axios.get(BASE_URL, {
            params: {
                q: city,
                appid: API_KEY,
                units: 'metric' // Celsius-asteina
            }
        });

        const weather = response.data.weather[0].description;
        const temperature = response.data.main.temp;

        console.log(`Säätila: ${weather}`);
        console.log(`Lämpötila: ${temperature} C`);
    } catch (error) {
        console.error('Virhe haettaessa säätietoja:', error.response ? error.response.data : error.message);
    } finally {
        rl.close();
    }
});

