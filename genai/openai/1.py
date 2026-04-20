response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_completion_tokens=100,
  
    # Enter your prompt
    messages=[{"role": "user", "content": "Why is OpenAPI valuable for developers"}]
)

print(response.choices[0].message.content)