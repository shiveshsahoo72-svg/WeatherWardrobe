package com.weatherwardrobe.backend.service;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClient;

import com.weatherwardrobe.backend.model.ClothingRequirements;
import com.weatherwardrobe.backend.model.WeatherSnapshot;

import org.springframework.beans.factory.annotation.Value;

@Service 
public class RecommendationService {
    private final RestClient restClient;

    public RecommendationService(
        @Value("${reasoning.api.base-url}") String baseURL
    )
    {
        this.restClient = RestClient.builder().baseUrl(baseURL).build();
    }

    public ClothingRequirements getRecommendation(WeatherSnapshot snapshot){
        ClothingRequirements recommendation = this.restClient.post()
        .uri("/recommend")
        .body(snapshot)
        .retrieve()
        .body(ClothingRequirements.class);

        return recommendation;
    }
}
