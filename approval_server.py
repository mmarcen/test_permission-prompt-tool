#!/usr/bin/env python3
"""
Minimal MCP approval server using stdio transport
"""

from mcp.server.fastmcp import FastMCP
import datetime
import json

# Create MCP server
mcp = FastMCP("approval-server")

def log_to_file(message):
    """Simple file logging to verify the approval function is called"""
    with open("approval_log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {message}\n")

@mcp.tool()
async def permissions__approve(tool_name: str, input: dict, reason: str = "") -> dict:
    """
    Approve or deny permission requests from Claude.
    
    Returns dict with behavior:"allow"/"deny"
    """
    # Log that we were called
    log_to_file(f"CALLED with tool_name={tool_name}, input={json.dumps(input)}")
    
    # APPROVE safe_operation
    if "safe_operation" in tool_name:
        log_to_file(f"APPROVED: {tool_name}")
        return {
            "behavior": "allow",
            "updatedInput": input
        }
    
    # DENY dangerous_operation
    if "dangerous_operation" in tool_name:
        log_to_file(f"DENIED: {tool_name}")
        return {
            "behavior": "deny",
            "message": "This operation is not allowed for security reasons"
        }
    
    # Default: deny unknown operations
    log_to_file(f"DENIED (unknown): {tool_name}")
    return {
        "behavior": "deny",
        "message": f"Unknown operation: {tool_name}"
    }

if __name__ == "__main__":
    # Run as stdio server
    import asyncio
    asyncio.run(mcp.run())