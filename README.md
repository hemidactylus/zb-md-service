# ZeroBundle Metadata Service

Example post from the drivers:

```
curl -XPOST localhost:8000/get_bundle_data -d '{"zb_api_key": "000aaa"}' -H 'Content-Type: application/json' | jq
```

## Bundle string

It's about 7k chars as encoded.