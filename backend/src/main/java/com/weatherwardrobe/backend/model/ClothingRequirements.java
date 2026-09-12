package com.weatherwardrobe.backend.model;

import com.fasterxml.jackson.annotation.JsonProperty;

public record ClothingRequirements(
    @JsonProperty("insulation_level") int insulationLevel,
    @JsonProperty("waterproof_needed") boolean waterproofNeeded,
    @JsonProperty("windproof_needed") boolean windproofNeeded,
    String breathability,
    @JsonProperty("layering_recommended") boolean layeringRecommended)
    {}
