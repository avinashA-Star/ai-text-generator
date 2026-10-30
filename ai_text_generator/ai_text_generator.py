"""
AI Text Generator (simple base project)
---------------------------------------
Uses a pre-trained GPT-2 model from Hugging Face to continue any prompt you type.

Setup:
    pip install transformers torch

Run:
    python ai_text_generator.py
"""

from transformers import pipeline, set_seed


def load_generator(model_name: str = "gpt2"):
    """Load the text-generation pipeline (downloads the model on first run)."""
    print(f"Loading model '{model_name}' ... (first run may take a minute)")
    return pipeline("text-generation", model=model_name)


def generate_text(generator, prompt: str, max_length: int = 100,
                  num_results: int = 1, temperature: float = 0.8):
    """Generate text continuing from the given prompt."""
    outputs = generator(
        prompt,
        max_length=max_length,
        num_return_sequences=num_results,
        temperature=temperature,   # higher = more creative, lower = more focused
        top_k=50,
        top_p=0.95,
        do_sample=True,
        truncation=True,
        pad_token_id=50256,        # GPT-2 end-of-text token
    )
    return [o["generated_text"] for o in outputs]


def main():
    set_seed(42)  # remove this line for different results every run
    generator = load_generator()

    print("\n=== AI Text Generator ===")
    print("Type a prompt and press Enter. Type 'quit' to exit.\n")

    while True:
        prompt = input("Prompt > ").strip()
        if prompt.lower() in {"quit", "exit", "q"}:
            print("Goodbye!")
            break
        if not prompt:
            continue

        try:
            length = int(input("Max length (default 100) > ") or 100)
        except ValueError:
            length = 100

        results = generate_text(generator, prompt, max_length=length)
        for i, text in enumerate(results, 1):
            print(f"\n--- Result {i} ---\n{text}\n")


if __name__ == "__main__":
    main()
