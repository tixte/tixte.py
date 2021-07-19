import aiohttp

from .errors import NotImplementedError

from typing import (
    ClassVar,
    Any,
    Optional,
    Dict
)

class Route:
    """
    Route for the lib. Similar to how discord.py (https://github.com/Rapptz/discord.py/tree/master) does it,
    we'll use this for organizing any API calls.
    
    Parameters
    ----------
    method: :class:`str`
        The method you want to use.
    path: :class:`str`
        The additional path you want to use
    **parameters: Any
        Any params you want to add onto the url.
    """
    BASE: ClassVar[str] = ''
    
    def __init__(self, method: str, path: str, **parameters: Any) -> None:
        self.method: str = method
        self.path: str = path
        url = self.BASE + path
        if parameters:
            url += ''.join([f'{k}={v}' for k, v in parameters.items()])
        self.url = url
        
        
class HTTP:
    """
    The base HTTP class for the lib. This is where all operations will exist.
    
    Parameters
    ----------
    session: Optional[:class:aiohttp.ClientSession] = None
        The session used for requets. 
        We leave this optional because you can use a Discord bot's session instead of another one.
    """
    def __init__(self, session: Optional[aiohttp.ClientSession] = None) -> None:
        self.session = session or aiohttp.ClientSession()
        
    
    async def request(self, route: Route, **kwargs: Any) -> Dict:
        async with self.session.request(route.method, route.url, **kwargs) as resp:
            if resp.status != 200:
                raise NotImplementedError("API status was not 200, this hasn't been implemented yet.")
            
            # We're going to assume the API returns Dict for now.
            # We'll change this later as I get more info.
            return await resp.json()  
        