from mcp.server.fastmcp import FastMCP
from server.azure_client import AzureLLMClient

mcp = FastMCP("Azure Smart Notes MCP Server")

_llm = None


def get_llm():
    global _llm
    if _llm is None:
        _llm = AzureLLMClient()
    return _llm


@mcp.tool()
def summarize_text(text: str) -> str:
    print("🛠 MCP tool summarize_text invoked")
    return get_llm().summarize(text)
