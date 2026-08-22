package com.weatherwardrobe.backend.service;

import org.springframework.stereotype.Service;

import java.time.Instant;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.client.RestClient;

import com.weatherwardrobe.backend.client.OpenWeatherResponse;
import com.weatherwardrobe.backend.model.WeatherSnapshot;

@Service
public class WeatherService {
    
    private final RestClient restClient;
    private final String apiKey;

    public WeatherService(
            @Value("${openweather.api.base-url}") String baseUrl,
            @Value("${openweather.api.key}") String apiKey) {
        this.restClient = RestClient.builder().baseUrl(baseUrl).build();
        this.apiKey = apiKey;
    }

    public WeatherSnapshot getWeather(String city, String state, String country){
        String q = buildQuery(city, state, country);
        OpenWeatherResponse apiResponse = restClient.get()
            .uri(uriBuilder -> uriBuilder.path("/weather")
            .queryParam("q", q)
            .queryParam("appid", apiKey)
            .queryParam("units", "metric")
            .build())
            .retrieve()
            .body(OpenWeatherResponse.class);
        
        return toSnapshot(apiResponse);
    }

    private WeatherSnapshot toSnapshot(OpenWeatherResponse apiResponse){
        WeatherSnapshot weatherSnapshot = new WeatherSnapshot(
            apiResponse.name(),
            apiResponse.sys().country(),
            apiResponse.main().temp(),
            apiResponse.main().feelsLike(),
            apiResponse.main().tempMin(),
            apiResponse.main().tempMax(),
            apiResponse.main().humidity(),
            apiResponse.wind().speed(),
            apiResponse.weather().get(0).main(),
            apiResponse.weather().get(0).description(),
            apiResponse.clouds().coverage(),
            Instant.ofEpochSecond(apiResponse.dt())
        );

        return weatherSnapshot;
    }

    private String buildQuery(String city, String state, String country){
        if (state != null && !state.isBlank()){
            return city + ", " + state + ", " + country;
        }
        return city + ", " + country;
    }
}
