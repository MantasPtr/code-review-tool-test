import openai
from openai import OpenAI
import os
import argparse

# Set your OpenAI API key
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main(system_prompt_file, user_request_file):
    # Read the contents of the files
    system_prompt = read_file(system_prompt_file)
    user_request = read_file(user_request_file)

    # Prepare the messages for the API
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_request}
    ]

    try:
        # Send the request to the API
        completions = client.chat.completions.create(
            model="gpt-4-turbo",  # You can specify the model you want to use
            # model="gpt-4",  # You can specify the model you want to use
            messages=messages,
            temperature=0,
            seed=1234
        )
        # Print the response from the API
        print(completions.choices[0].message.content)
    except openai.OpenAIError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Send prompts to OpenAI GPT API.')
    parser.add_argument(
        '-s', '--system_prompt_file',
        type=str,
        default='/Users/mape/code-review-tool-test/gpt_system_prompt.txt',
        help='File path for the system prompt (default: /Users/mape/code-review-tool-test/gpt_system_prompt.txt)'
    )
    parser.add_argument(
        '-u', '--user_request_file',
        type=str,
        default='user_request.txt',
        help='File path for the user request prompt (default: user_request.txt)'
    )

    args = parser.parse_args()

    # Run the main function with the provided arguments
    main(args.system_prompt_file, args.user_request_file)
