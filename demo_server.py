#!/usr/bin/env python3
"""
Minimal demo server with tools that need approval
"""

from mcp.server.fastmcp import FastMCP
import datetime

# Create MCP server
mcp = FastMCP("demo-server")

@mcp.tool()
async def safe_operation() -> dict:
    """This operation will be APPROVED"""
    return {
        "status": "success",
        "message": "This safe operation was executed successfully",
        "timestamp": datetime.datetime.now().isoformat()
    }

@mcp.tool()
async def dangerous_operation() -> dict:
    """This operation will be DENIED"""
    return {
        "status": "success", 
        "message": "This dangerous operation should never execute",
        "timestamp": datetime.datetime.now().isoformat()
    }

if __name__ == "__main__":
    # Run as stdio server
    import asyncio
    asyncio.run(mcp.run())