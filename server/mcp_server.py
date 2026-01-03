from dotenv import load_dotenv
load_dotenv()   # 🔑 load env FIRST

from server.tools import mcp

def main():
    print("🚀 MCP Azure Smart Notes Server running")
    mcp.run()

if __name__ == "__main__":
    main()
