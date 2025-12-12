from openai import OpenAI

# Initialize the OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="Your API Key",
)

def generate_response(chat_history: str, sender_name="vedika") -> str:
    """
    Generates a one line response using OpenRouter API.
    in English if last message is from sender_name.
    """
    # Decide language
    lang_instruction = (
        "Write short responses in english." 
        if sender_name.lower() in chat_history.strip().split("/2025] ")[-1].lower()
        else "Write short responses in proper English."
    )

    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional
            "X-Title": "<YOUR_SITE_NAME>",      # Optional
        },
        model="openai/gpt-oss-20b:free",
        messages=[
            {
                "role": "system",
                "content": "You are a person named Bhuvan. You are from India, a coder, and you respond in a friendly, casual style."
            },
            {
                "role": "system",
                "content": lang_instruction
            },
            {"role": "user", "content": chat_history}
        ]
    )
    return completion.choices[0].message.content
