from transformers import pipeline

# Replace with your Hugging Face username
pipe = pipeline("text-generation", model="H4KAI/Answer-From-Vaathiyar")

result = pipe("Hello, AI!", max_length=50)
print(result[0]["generated_text"])
