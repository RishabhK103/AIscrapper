import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()


client = Groq(api_key=os.getenv("GROQ_API_KEY"))

system_prompt = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully:\n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}.\n"
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response.\n"
    "3. **Empty Response:** If no information matches the description, return an empty string ('').\n"
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

def parse_with_groq(dom_chunks, parse_description, model="llama-3.1-8b-instant"):
    parsed_result = []

    for i, chunk in enumerate(dom_chunks, start=1):
        prompt = system_prompt.format(dom_content=chunk, parse_description=parse_description)

        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a precise extraction assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
        )

        print(f"parsed batch {i} of {len(dom_chunks)}")

        parsed_result.append(response.choices[0].message.content.strip())

    return "\n".join(parsed_result)

