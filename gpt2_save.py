from transformers import AutoTokenizer, AutoModelForCausalLM

# Load GPT-2 model
model_name = "openai-community/gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Save model and tokenizer locally
model.save_pretrained("my_model")
tokenizer.save_pretrained("my_model")

print("Model saved successfully!")

