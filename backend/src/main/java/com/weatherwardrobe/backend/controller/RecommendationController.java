package com.weatherwardrobe.backend.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.weatherwardrobe.backend.model.ClothingRequirements;
import com.weatherwardrobe.backend.model.WeatherSnapshot;
import com.weatherwardrobe.backend.service.RecommendationService;
import com.weatherwardrobe.backend.service.WeatherService;

@RestController 
public class RecommendationController {
    
    private final WeatherService weatherService;
    private final RecommendationService recommendationService;

    public RecommendationController(WeatherService weatherService, RecommendationService recommendationService){
        this.weatherService = weatherService;
        this.recommendationService = recommendationService;
    }

    @GetMapping("/api/recommendation")
    public ClothingRequirements getRecommendation(
        @RequestParam String city, 
        @RequestParam(required = false) String state, 
        @RequestParam String country)
        {
            WeatherSnapshot snapshot = weatherService.getWeather(city, state, country);
            return recommendationService.getRecommendation(snapshot);
        }
}
