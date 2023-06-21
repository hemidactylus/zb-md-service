# ZeroBundle Metadata Service

## Setup

Get an Astra SCB. Then:

```
mkdir -p .bundles/000aaa
cd .bundles/000aaa
unzip FULL_PATH_TO_SCB
cd ../../
```

Also install all of `requirements.txt` (note  you need the modified Cassandra drivers).

Start with

```
uvicorn api:app
```

## Mini example setup

`cd sample_client`.

Adjust keyspace name and tables, etc in the "sample client" dummy code.

In that dir, `cp .env.template .env`, edit and then source the `.env`.

Post to run just once to get the value for `ASTRA_ZB_STRING` in the `.env`:

```
curl -XPOST localhost:8000/get_bundle_string -d '{"zb_api_key": "000aaa"}' -H 'Content-Type: application/json' | jq
```

(it should be about 7k characters).

## "Usage"

### With the mini app

```
cd sample_client
. .env
python testconn.py astra_db   # sanity check

python testconn.py astra_zb_key     # requires the API running

python testconn.py astra_zb_string  # no API required
```

### Test

Example post from the drivers:

```
curl -XPOST localhost:8000/get_bundle_data -d '{"zb_api_key": "000aaa"}' -H 'Content-Type: application/json' | jq
```
