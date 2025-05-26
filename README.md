# Minimal MCP Approval Demo

This is a minimal working example of the MCP permission approval system using stdio transport.

## Files

- `approval_server.py` - The approval server that controls permissions
- `demo_server.py` - Demo server with two tools: one approved, one denied
- `mcp-servers.json` - MCP configuration for stdio transport


## Setup

1. Make sure you have the required dependencies:
```bash
pip install mcp 
```


## How It Works

The demo includes two simple tools:

1. **safe_operation** - This tool will be APPROVED by the approval server
2. **dangerous_operation** - This tool will be DENIED by the approval server

The approval server checks the tool name and decides:
- If tool contains "safe_operation" → **ALLOW**
- If tool contains "dangerous_operation" → **DENY**
- Any other tool → **DENY** (default)

## Testing

### Test 1: Approved Operation
```bash
claude -p "run the safe operation" \
  --mcp-config mcp-servers.json \
  --permission-prompt-tool mcp__approval-server__permissions__approve \
  --output-format stream-json \
  --verbose \
  --debug
```
Expected: The operation executes successfully

### Test 2: Denied Operation
```bash
claude -p "run the dangerous operation" \
  --mcp-config mcp-servers.json \
  --permission-prompt-tool mcp__approval-server__permissions__approve \
  --output-format stream-json \
  --verbose \
  --debug
```
Expected: The operation is denied with message "This operation is not allowed for security reasons"
