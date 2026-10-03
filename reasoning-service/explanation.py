import os
from groq import Groq


client = Groq(api_key=os.environ["GROQ_API_KEY"])

_INSULATION_PHRASES = {
    5: "heavy insulation",
    4: "a warm coat",
    3: "a mid-weight layer",
    2: "a light layer",
    1: "something light and comfortable",
}

def explain(requirements, snapshot) -> str:
    try:
        prompt = build_prompt(requirements, snapshot)
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
    except Exception as e:
        return build_template_explanation(requirements, snapshot)

def build_prompt(requirements, snapshot) -> str:
    prompt = f"""Your job is to plainly explain clothing recommendation that is weather appropriate based on weather details.
    
    The Weather in {snapshot.city}, {snapshot.country} is {snapshot.temperature} degrees Celsius. It feels like {snapshot.feelsLike} degrees Celsius with 
    a condition labeled as {snapshot.condition} and the description as {snapshot.conditionDescription}. The system has already determined that the user needs the following:
    Waterproof: {requirements.waterproof_needed}, Windproof: {requirements.windproof_needed}, Layering: {requirements.layering_recommended}, 
    Breathability: {requirements.breathability}, Insulation Level: {_INSULATION_PHRASES[requirements.insulation_level]}

    Keep the response to 2 sentences.
    Keep the tone friendly and practical.
    Do not contradict requirements.
    Return only the explanation.
     
    """

    return prompt



def build_template_explanation(requirements, snapshot) -> str:
    weather = (
        f"It's {snapshot.temperature:.0f}°C in {snapshot.city}, "
        f"feeling like {snapshot.feelsLike:.0f}°C with {snapshot.conditionDescription}."
    )

    parts = [_INSULATION_PHRASES[requirements.insulation_level]]

    if requirements.waterproof_needed:
        parts.append("a waterproof outer layer")
    if requirements.windproof_needed:
        parts.append("something that blocks the wind")
    if requirements.layering_recommended:
        parts.append("layers you can take off indoors")
    if requirements.breathability == "high":
        parts.append("breathable fabric")

    if len(parts) == 1:
        clothing = f"You'll want {parts[0]}."
    else:
        clothing = f"You'll want {', '.join(parts[:-1])}, and {parts[-1]}."

    return f"{weather} {clothing}"