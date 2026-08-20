package main.java.com.weatherwardrobe.backend.client;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import java.util.List;

@JsonIgnoreProperties(ignoreUnknown = true)
public record OpenWeatherResponse (
    List<Weather> weather,
    Main main,
    Wind wind,
    Clouds clouds,
    long dt,
    Sys sys,
    String name
)
{

    @JsonIgnoreProperties(ignoreUnknown = true)
    public record Weather (String main, String description){}

    @JsonIgnoreProperties(ignoreUnknown = true)
    public record Main (
        double temp,
        @JsonProperty("feels_like") double feelsLike,
        @JsonProperty("temp_min") double tempMin,
        @JsonProperty("temp_max") double tempMax,
        int humidity
    ) {}

    @JsonIgnoreProperties(ignoreUnknown = true)
    public record Wind (double speed) {}

    @JsonIgnoreProperties(ignoreUnknown = true)
    public record Clouds (@JsonProperty("all") int coverage) {}

    @JsonIgnoreProperties(ignoreUnknown = true)
    public record Sys (String country) {}
    
}
