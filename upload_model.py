from huggingface_hub import HfApi # type: ignore

# Replace with your Hugging Face username
repo_id = "H4KAI/Answer-From-Vaathiyar"

api = HfApi()
api.create_repo(repo_id, exist_ok=True)  # Create repo if not exists

# Upload all files in the "my_model" folder
api.upload_folder(folder_path="my_model", repo_id=repo_id)

print(f"Model uploaded to https://huggingface.co/{repo_id}")
