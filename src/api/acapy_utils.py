
async def acapy_admin_request(
        method: str,
        path: str,
        data: dict = None,
        text: bool = False,
        params: dict = None,
        headers: dict = None,
        tenant: bool = False,
    ) -> str:
    print(">>> called it!!!", method, path, data)
