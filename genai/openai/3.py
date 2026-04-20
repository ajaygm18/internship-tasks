client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
  # Specify the model
  model="gpt-4o-mini",
  messages=[
    # Assign the correct role
    {"role": "user", 
     "content": "Announce my new AI Engineer role on LinkedIn."}]
)

print(response.choices[0].message.content)