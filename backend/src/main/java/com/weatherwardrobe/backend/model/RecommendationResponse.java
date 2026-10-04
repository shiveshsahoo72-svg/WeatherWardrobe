package com.weatherwardrobe.backend.model;

public record RecommendationResponse(
    ClothingRequirements requirements,
    String explanation
){}
