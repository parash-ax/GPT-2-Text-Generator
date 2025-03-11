# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="openai-community/gpt2")  # Load model directly

# Load tokenizer and model manually
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2")
model = AutoModelForCausalLM.from_pretrained("openai-community/gpt2")

# Test pipeline method
result = pipe("Hello, AI!", max_length=50)
print("Pipeline Output:\n", result[0]["generated_text"])

# Test manual method
import torch

input_text = "Hello, AI!"
inputs = tokenizer(input_text, return_tensors="pt")

# Generate text
output = model.generate(**inputs, max_length=50)

# Decode and print
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print("\nManual Model Output:\n", generated_text)
