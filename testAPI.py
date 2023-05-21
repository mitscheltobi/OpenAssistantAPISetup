import sys
from text_generation import Client


def main():
    client = Client("http://127.0.0.1:8080")
    if len(sys.argv) < 1:
        prompt = f"<|prompter|>{sys.argv[1]}<|endoftext|><|assistant|>"
    else:
        prompt = f"<|prompter|>What are some interesting facts about dogs?<|endoftext|><|assistant|>"

    text = ""
    for response in client.generate_stream(prompt):
        if not response.token.special:
            print(response.token.text, end="\r")
            text += response.token.text
    print("\n Generated Answer: " + text)


if __name__ == "__main__":
    main()
