import os
import json

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
BUNDLE_BASE_DIR = os.path.join(BASE_DIR, ".bundles")


def _load_ascii_from_config_key(bundle_dir, config, key, default):
    file_name = config.get(key, default)
    file_path = os.path.join(bundle_dir, file_name)
    return open(file_path).read()


def load_bundle_data(zb_api_key: str):
    """
    Returning None is explicit denial of access to caller
    (while other problems still arise as exceptions)
    """
    bundle_dir = os.path.join(BUNDLE_BASE_DIR, zb_api_key)
    if os.path.isdir(bundle_dir):
        config_data = _load_ascii_from_config_key(
            bundle_dir,
            {},
            '',
            './config.json',
        )
        config = json.loads(config_data)
        #
        ca_cert_data = _load_ascii_from_config_key(
            bundle_dir,
            config,
            "caCertLocation",
            "./ca.crt",
        )
        key_data = _load_ascii_from_config_key(
            bundle_dir,
            config,
            "keyLocation",
            "./key",
        )
        cert_data = _load_ascii_from_config_key(
            bundle_dir,
            config,
            "certLocation",
            "./cert",
        )
        #
        return {
            "config_data": config_data,
            "ca_cert_data": ca_cert_data,
            "key_data": key_data,
            "cert_data": cert_data,
        }
    else:
        return None