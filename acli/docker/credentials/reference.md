## Generic Docker credentials tool

### Store

```
$ docker-credential-1password store <<EOF
{
  "ServerURL": "https://example.com",
  "Username": "myusername",
  "Secret": "averylongpassword"
}
EOF
```

### List

```
$ docker-credential-1password list
{
  "https://example.com": "myusername"
}
```

### Get

```
$ docker-credential-1password get <<< example.com
{"ServerURL": "https://example.com", "Username": "myusername", "Secret": "averylongpassword"}
```

### Erase

```
$ docker-credential-1password erase <<< example.com
```
