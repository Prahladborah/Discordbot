from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load pre-trained model and tokenizer
model_name = 'gpt2'  # You can also use 'gpt2-medium', 'gpt2-large', or 'gpt2-xl' for larger models
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

def generate_response(prompt):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

async def get_local_ai_response(prompt):
    try:
        response = generate_response(prompt)
        return response
    except Exception as e:
        return f"Error: {e}"
