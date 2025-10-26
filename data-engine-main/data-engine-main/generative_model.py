from transformers import pipeline

# Load the generative model (e.g., GPT-2)
generator = pipeline('text-generation', model='gpt2')

def generate_text(prompt):
    """Generate text based on the provided prompt."""
    response = generator(prompt, max_length=50, num_return_sequences=1)
    return response[0]['generated_text']
