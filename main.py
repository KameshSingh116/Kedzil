import google.generativeai as genai

genai.configure(api_key="your_gemini_api_key")

def chat_with_gemini(prompt):
    model = genai.GenerativeModel("gemini-1.5-pro-latest")  # ✅ Use an available model
    response = model.generate_content(prompt)
    return response.text

print("Kedzil: Hello! Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Kedzil: Radhe Radhe :)")
        break
    response = chat_with_gemini(user_input)
    print("Kedzil:", response)
