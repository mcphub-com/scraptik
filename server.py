import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/scraptik-api-scraptik-api-default/api/scraptik'

mcp = FastMCP('scraptik')

@mcp.tool()
def get_user_info(username: Annotated[str, Field(description='')]) -> dict: 
    '''Get user info by username.'''
    url = 'https://scraptik.p.rapidapi.com/web/get-user'
    headers = {'x-rapidapi-host': 'scraptik.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def video_without_watermark(aweme_id: Annotated[str, Field(description='')]) -> dict: 
    '''Get video URL without watermark by aweme_id.'''
    url = 'https://scraptik.p.rapidapi.com/video-without-watermark'
    headers = {'x-rapidapi-host': 'scraptik.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'aweme_id': aweme_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def username_to_id(username: Annotated[str, Field(description='')]) -> dict: 
    '''Get user id from username'''
    url = 'https://scraptik.p.rapidapi.com/username-to-id'
    headers = {'x-rapidapi-host': 'scraptik.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
