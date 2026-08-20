package main.java.com.weatherwardrobe.backend.model;

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
    java.time.Instant timestamp
) {}
