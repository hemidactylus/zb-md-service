import os
from dotenv import find_dotenv, load_dotenv
from cassandra.cluster import (
    Cluster,
)
from cassandra.auth import PlainTextAuthProvider

# this will climb the directory tree looking for the file
dotenv_file = find_dotenv('.env')
load_dotenv(dotenv_file)

ASTRA_DB_CLIENT_ID = "token"
ASTRA_DB_APPLICATION_TOKEN = os.environ["ASTRA_DB_APPLICATION_TOKEN"]

def getCQLSession(mode='astra_db'):
    if mode == 'astra_db':
        ASTRA_DB_SECURE_BUNDLE_PATH = os.environ["ASTRA_DB_SECURE_BUNDLE_PATH"]
        cluster = Cluster(
            cloud={
                "secure_connect_bundle": ASTRA_DB_SECURE_BUNDLE_PATH,
            },
            auth_provider=PlainTextAuthProvider(
                ASTRA_DB_CLIENT_ID,
                ASTRA_DB_APPLICATION_TOKEN,
            ),
        )
        astraSession = cluster.connect()
        return astraSession
    elif mode == 'astra_zb_key':
        ASTRA_ZB_API_KEY = os.environ["ASTRA_ZB_API_KEY"]
        cluster = Cluster(
            cloud={
                "zb_api_key": ASTRA_ZB_API_KEY,
            },
            auth_provider=PlainTextAuthProvider(
                ASTRA_DB_CLIENT_ID,
                ASTRA_DB_APPLICATION_TOKEN,
            ),
        )
        astraSession = cluster.connect()
        return astraSession
    elif mode == 'astra_zb_string':
        ASTRA_ZB_STRING = os.environ["ASTRA_ZB_STRING"]
        cluster = Cluster(
            cloud={
                "zb_string": ASTRA_ZB_STRING,
            },
            auth_provider=PlainTextAuthProvider(
                ASTRA_DB_CLIENT_ID,
                ASTRA_DB_APPLICATION_TOKEN,
            ),
        )
        astraSession = cluster.connect()
        return astraSession
    elif mode == 'local':
        cluster = Cluster(['172.17.0.2'])
        localSession = cluster.connect()
        return localSession
    else:
        raise ValueError('Unknown CQL Session mode')
