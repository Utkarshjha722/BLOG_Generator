# download_models.py
import os

def download_model():
    model_path = "models"
    
    if not os.path.exists(model_path):
        os.makedirs(model_path)
        print("Created 'models' directory. Please place your llama-2-7b-chat.ggmlv3.q8_0.bin file here.")
    else:
        print("'models' directory already exists.")

if __name__ == "__main__":
    download_model()