# MCP Calculator Server

This project is a simple Model Context Protocol (MCP) server that evaluates mathematical expressions sent by MCP clients. It can be used with the official MCP Python client or the VSCode MCP extension.

---

## Features
- Evaluate math expressions using Python's `math` module (e.g., `sqrt(25) + 2**3`).
- Secure evaluation: only math functions/constants are available.
- Exposes a `calculate` tool via the MCP protocol.
- Compatible with the [Model Context Protocol VSCode extension](https://marketplace.visualstudio.com/items?itemName=modelcontextprotocol.mcp).

---

## Setup

1. **Clone the repository and enter the directory:**
   ```bash
   git clone <your-repo-url>
   cd calculator-mcp
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the MCP Server

Start the server (by default, it listens on all interfaces at port 8500, root path):

```bash
python app.py
```

You should see:
```
MCP server running on 0.0.0.0:8500 (root path)
```

---

## Using the Python Client

The provided `client.py` can be used to test the server:

```bash
python client.py
```

This will send the expression `sqrt(25) + 2**3` to the server and print the result.

You can modify `client.py` to send other expressions.

---

## Using the MCP Server in VSCode

1. **Install the MCP Extension:**
   - Open VSCode.
   - Go to Extensions (`Ctrl+Shift+X` or `Cmd+Shift+X`).
   - Search for `Model Context Protocol` or `MCP` and install the official extension.

2. **Start the MCP server:**
   - Make sure `python app.py` is running.

3. **Connect VSCode to the MCP Server:**
   - Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`).
   - Type `MCP: Add Server` or `MCP: Connect to Server`.
   - Enter the server URL:
     ```
     http://127.0.0.1:8500/
     ```
   - Give it a name (e.g., "Calculator MCP").

4. **Use the MCP Tools in VSCode:**
   - Open the MCP sidebar (look for the MCP icon).
   - Select your server.
   - You should see the `calculate` tool.
   - Run the tool, enter a math expression, and see the result in VSCode.

---

## Security Note
- Only math functions/constants are available to evaluated expressions.
- No access to Python built-ins or the file system.

---

## License
MIT 