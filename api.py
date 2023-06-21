import json

from fastapi import FastAPI, Response, status

from bundle_lib import load_bundle_data
from models import BundleRequest
from encoding import encode

app = FastAPI()


@app.post("/get_bundle_data")
async def get_bundle_data(bundle_request: BundleRequest, response: Response):
    bundle_data = load_bundle_data(zb_api_key=bundle_request.zb_api_key)
    if bundle_data is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return None
    else:
        return bundle_data

@app.post("/get_bundle_string")
async def get_bundle_string(bundle_request: BundleRequest, response: Response):
    bundle_data = load_bundle_data(zb_api_key=bundle_request.zb_api_key)
    if bundle_data is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return None
    else:
        encoded = encode(json.dumps(bundle_data))
        return {'bundle_string': encoded}
