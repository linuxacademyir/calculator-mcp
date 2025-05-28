# app.py
from mcp.server.fastmcp import FastMCP
import math

def evaluate_expression(expr: str) -> str:
    try:
        safe_dict = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
        safe_dict.update({"__builtins__": {}})
        return str(eval(expr, safe_dict))
    except Exception as e:
        return f"Error: {e}"

class CalculatorMCP(FastMCP):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_tool(self.calculate)

    def calculate(self, payload: str) -> str:
        return evaluate_expression(payload)

if __name__ == "__main__":
    server = CalculatorMCP(host="0.0.0.0", port=8500, streamable_http_path="/")
    print("MCP server running on 0.0.0.0:8500 (root path)")
    server.run(transport="streamable-http")
