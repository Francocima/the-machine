import anthropic
import sys
from pathlib import Path

client = anthropic.Anthropic()

SYSTEM_PROMPT_PATH = Path(__file__).parent / "system_prompt.md"


def run(input: str) -> str:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system=[
            {
                "type": "text",
                "text": SYSTEM_PROMPT_PATH.read_text(),
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": input}],
    )
    return response.content[0].text


if __name__ == "__main__":
    user_input = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
    print(run(user_input))
