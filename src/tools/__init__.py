"""Tool definitions for the multi-agent orchestrator."""

from src.tools.calculator import calculate
from src.tools.search import scrape_url, web_search
from src.tools.text_processing import extract_key_points, summarize_text

__all__ = [
    "web_search",
    "scrape_url",
    "calculate",
    "summarize_text",
    "extract_key_points",
]
