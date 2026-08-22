package com.weatherwardrobe.backend.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.weatherwardrobe.backend.model.WeatherSnapshot;
import com.weatherwardrobe.backend.service.WeatherService;

@RestController
public class WeatherController {
    
    private final WeatherService weatherService;

    public WeatherController(WeatherService weatherService){
        this.weatherService = weatherService;
    }

    @GetMapping("/api/weather")
    public WeatherSnapshot getWeather(@RequestParam String city, @RequestParam(required = false) String state, @RequestParam String country){
        return weatherService.getWeather(city, state, country);
    }
}
