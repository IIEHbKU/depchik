import json
from typing import Dict, Any

import aiohttp


async def generate_analysis(
        model: str,
        prompt: str,
        stream: bool
) -> Dict[str, Any]:
    api_url = "http://127.0.0.1:11434/api/generate",
    body = {
        "model": model,
        "prompt": prompt,
        "stream": stream
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(
            url=api_url,
            headers={"Content-Type": "application/json"},
            json=body
        ) as response:
            response_text = await response.text()
            response.raise_for_status()
            response_data = json.loads(response_text)
            return response_data
