package com.weatherwardrobe.backend.model;

import java.time.Instant;

public record WeatherSnapshot(
    String city,
    String country,
    double temperature,
    double feelsLike,
    double tempMin,
    double tempMax,
    int humidity,
    double windSpeed,
    String condition,
    String conditionDescription,
    int cloudCover,
    Instant timestamp
) {}
