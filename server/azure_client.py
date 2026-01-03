import os
from pathlib import Path
from dotenv import load_dotenv
from openai import AzureOpenAI

# 🔹 Force-load .env from project root
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

class AzureLLMClient:
    def __init__(self):
        key = os.getenv("AZURE_OPENAI_API_KEY")
        endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        version = os.getenv("AZURE_OPENAI_API_VERSION")
        deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

        if not all([key, endpoint, version, deployment]):
            raise RuntimeError(
                f"Azure env vars not loaded:\n"
                f"KEY={bool(key)}\n"
                f"ENDPOINT={endpoint}\n"
                f"VERSION={version}\n"
                f"DEPLOYMENT={deployment}"
            )

        self.client = AzureOpenAI(
            api_key=key,
            azure_endpoint=endpoint,
            api_version=version,
        )
        self.deployment = deployment

    def summarize(self, text: str) -> str:
        response = self.client.chat.completions.create(
            model=self.deployment,
            messages=[
                {"role": "system", "content": "Summarize clearly."},
                {"role": "user", "content": text},
            ],
        )
        return response.choices[0].message.content

