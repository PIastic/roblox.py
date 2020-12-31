import aiohttp

class Http:
    def __init__(self,cookies=None,headers=None):
        self.cookies = cookies
        self.headers = headers
    async def __aenter__(self):
        self._session = aiohttp.ClientSession(cookies=self.cookies)
        return self

    async def __aexit__(self, *err):
        await self._session.close()
        self._session = None
    @property
    def fetch(self):
        return self._session