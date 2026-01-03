from server.azure_client import AzureLLMClient

if __name__ == "__main__":
    llm = AzureLLMClient()

    text = """
    Today we discussed project timelines, delivery risks, and action items.
    The backend team will deliver APIs by Friday.
    Frontend will start integration next week.
    """

    summary = llm.summarize(text)

    print("\n===== SUMMARY =====\n")
    print(summary)
