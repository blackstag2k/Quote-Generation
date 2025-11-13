import pandas as pd
import google.genai as genai

client = genai.Client(api_key="ENTER_API_KEY")

template_prompt = """You are an expert quotes writer
Write one quote each for the topic provided below:

topic: {topic}

Make the quotes beautiful and impactful"""

df = pd.read_csv("Quotes.csv")

quotes = []

for _, row in df.iterrows():
    prompt = template_prompt.format(
        topic=row['topic']
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    quotes.append(response.text.strip())

df["quotes"] = quotes
df.to_csv("Quotes_output.csv", index=False)
print("quotes are generated and saved to Quotes_output.csv")