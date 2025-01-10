from mcp.server.fastmcp import FastMCP
from datetime import datetime

mcp = FastMCP("Demo")

@mcp.resource("date://current")
def get_current_date() -> str:
    """Return the current date as a string."""
    current_date = datetime.now().strftime("%Y-%m-%d")
    return f"The current date is {current_date}"

@mcp.resource("time://current")
def get_current_time() -> str:
    """Return the current time as a string."""
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"The current time is: {current_time}")

