import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("BusinessAPI")

API_BASE = "http://localhost:3001"

@mcp.tool()
def get_product_info(product_id: str) -> dict:
 response = httpx.get(f"{API_BASE}/products/{product_id}")
 if response.status_code == 404:
  return {"error": f"Product {product_id} not found"}
 return response.json()

@mcp.tool()
def get_stock_level(product_id: str) -> dict:
 response = httpx.get(f"{API_BASE}/stock/{product_id}")
 if response.status_code == 404:
  return {"error": f"Product {product_id} not found"}
 data = response.json()
 data["status"] = "rupture" if data["quantity"] == 0 else "bas" if data["quantity"] < 10 else "normal"
 return data

@mcp.tool()
def search_orders(client: str = None, status: str = None) -> list:
 params = {}
 if client: params["client"] = client
 if status: params["status"] = status
 response = httpx.get(f"{API_BASE}/orders", params=params)
 return response.json()

if __name__ == "__main__":
 mcp.run(transport="stdio")