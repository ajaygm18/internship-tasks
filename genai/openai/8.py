client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": "generate a c atchy restaurant slogan for italian"}],
  max_completion_tokens=100
)

print(response.choices[0].message.content)