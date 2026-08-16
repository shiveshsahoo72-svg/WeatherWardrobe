# Weather Wardrobe

Weather-aware clothing recommendation system. Takes weather for a location, reasons about the combined conditions, and recommends an outfit from the user's actual wardrobe — with an explanation of why.

This is a rewrite of a working Python CLI prototype (v1) into a full-stack app. The owner is using this project to learn React/CSS, practice Python, apply Spring Boot experience, and build AI-engineering skills for internship interviews. Explain non-obvious choices; don't just emit code.

## Architecture

```
OpenWeatherMap
      |
Spring Boot     ingestion, normalization, persistence, orchestration
      |
Python service  interpretation -> clothing requirements -> wardrobe matching -> LLM explanation
      |
   React UI
```

## Layer rules (do not violate)

- **Java never makes clothing decisions.** No temperature thresholds, no warmth logic, no outfit rules in Spring Boot. If a conditional about weather values appears in Java, it belongs in Python.
- **Python never touches the database or the weather API.** It receives a normalized `WeatherSnapshot` plus the relevant wardrobe items in the request body, and returns a recommendation. Stateless, pure, testable without a DB or network.
- **Python never sees raw OpenWeatherMap JSON.** Spring Boot normalizes into our own `WeatherSnapshot` model first. Vendor quirks stop at that boundary.
- **Units are normalized once, at ingestion, in Spring Boot.** Every downstream value carries a known unit. (v1 bug to avoid: temp converted to F while temp_min/temp_max stayed C, then both handed to the LLM unlabeled.)
- **The LLM only phrases, never decides.** Python's deterministic logic picks valid items; the model turns the structured result into natural language. If the LLM call fails or is skipped, a template fallback produces a usable sentence and the app still works. Never on the critical path.

## Stack

- Backend: Java 17+, Spring Boot (Web, Lombok, Validation), WebClient, JPA + PostgreSQL
- Reasoning: Python 3.11+, FastAPI, Pydantic, pytest
- Frontend: React (Vite), plain CSS
- Weather: OpenWeatherMap classic free endpoints (current, 5-day/3-hour forecast, geocoding). NOT One Call 3.0/4.0 — that's pay-per-call and needs a card on file.

## Repo layout

```
/backend            Spring Boot
/reasoning-service  FastAPI + reasoning core
/frontend           React
```

## Domain model

`WeatherSnapshot` (owned by Spring Boot, mirrored as a Pydantic model in Python): temp, feels_like, humidity, wind_speed, precipitation_probability, condition, uv_index, cloud_cover, timestamp, plus a short array of upcoming hours for same-day change reasoning.

Clothing items store **attributes, not just names** — `warmth_level`, `waterproof`, `windproof`, `breathability`, `category`. Matching filters on attributes against structured clothing requirements. A row that only says "blue puffer jacket" is useless to the matching layer.

Tables: `users`, `clothing_items`, `recommendations`, `recommendation_items`.

## Reasoning engine (the core of the project)

Three distinct stages, kept separate:

1. **Interpretation** — pure functions classifying each dimension: comfort band from *feels-like* (not raw temp), precipitation risk, wind exposure, humidity, UV, and a same-day volatility flag.
2. **Clothing requirements** — compose the interpretations. Wind pushes toward more insulation even when temperature alone wouldn't. Rain requires a waterproof layer independent of temperature. Large same-day swings mean recommending layers, not one fixed outfit. Output is a structured requirements object (outerwear, layering, legwear, footwear, accessories) — not prose.
3. **Wardrobe matching** — score owned items against those requirements, fall back to generic categories when nothing matches.

Do not collapse these into one temperature-to-outfit lookup. The interaction between variables is the point of the project.

Required test case: 60°F windy and rainy must produce a visibly different recommendation from 60°F calm and sunny.

## Ported from v1

Working logic to preserve, not rewrite:

- `temp_catagories` / `wind_catagories` / `humidity_catagories` — the threshold bands are sound. Port into the interpretation layer, but return a named model instead of a positional list. (v1 returned a 9-element list read as `weather[0]`, `weather[3]`, `weather[8]` — brittle.)
- `findBestFit` scoring — port into wardrobe matching. **Known gap: it scores warmth, humidity, and wind but never precipitation**, so rain currently has no effect on recommendations. Closing that is a priority in the rewrite.
- `promptBuilder` — the structure was good. The prompt now receives already-decided requirements rather than deciding for itself.

## Scope

**Core (must ship):** weather ingestion + normalization, the three-stage reasoning engine with tests, wardrobe stored in Postgres with manual entry, LLM explanation with template fallback, React UI showing outfit + why.

**Stretch (cut first if time runs short):** MCP server exposing the reasoning core as a tool for AI agents, deployment, photo upload with a vision model to auto-populate clothing attributes (with a user confirmation step before saving — hence `attributes_confirmed`), multi-day/trip planning, feedback loop.

Four-week timeline, solo. A working, well-explained subset beats a broken complete system. Prefer incremental improvement over rewriting working components.

## Conventions

- API keys in environment variables, never committed. Verify `.gitignore` covers config files before the first commit.
- Reasoning logic gets unit tests. Tests must run without a database or network.
- Commit early and often; don't batch a week of work into one commit.
