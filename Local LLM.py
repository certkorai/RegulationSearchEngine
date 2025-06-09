# llm_handler.py

import requests
import os

def call_open_llm(prompt: str, model: str = "gemma:7b", endpoint: str = "http://localhost:11434/api/generate"):
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(endpoint, json=payload)
    return response.json().get("response", "") if response.status_code == 200 else response.text


def call_hf_llm(prompt: str, model_id: str, hf_token: str):
    headers = {"Authorization": f"Bearer {hf_token}"}
    data = {"inputs": prompt, "parameters": {"max_new_tokens": 1200}}
    response = requests.post(f"https://api-inference.huggingface.co/models/{model_id}", headers=headers, json=data)
    return response.json()[0]['generated_text'] if isinstance(response.json(), list) else str(response.json())


def query_llm(prompt, mode="auto", model_id="google/gemma-1.1-7b-it", hf_token=None, local_endpoint=None):
    """
    mode = "hf", "local", or "auto"
    """
    if mode == "hf":
        if not hf_token:
            raise ValueError("Hugging Face token required for mode=hf.")
        return call_hf_llm(prompt, model_id, hf_token)

    elif mode == "local":
        return call_open_llm(prompt, model=model_id, endpoint=local_endpoint)

    elif mode == "auto":
        if hf_token:
            return call_hf_llm(prompt, model_id, hf_token)
        elif local_endpoint:
            return call_open_llm(prompt, model=model_id, endpoint=local_endpoint)
        else:
            raise ValueError("Neither HF token nor local endpoint provided.")

    else:
        raise ValueError("Invalid mode. Choose 'hf', 'local', or 'auto'.")
