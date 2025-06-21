from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Demo")


@mcp.tool()
def addnum(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b
    





@mcp.resource("greeting://{name}")
def greeting(name: str):
    return f"Hello, {name}!"