# `acli`

**Usage**:

```console
$ acli [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--version, -v`: Show the application's version and exit.
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `config`: Config commands.
* `system`: System commands.
* `personio`: Personio commands.
* `docker`: Docker commands.

# `acli system`

**Usage**:

```console
$ acli system [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `info`: Display system information.

## `acli system info`

Display system information.

**Usage**:

```console
$ acli system info [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

# `acli config`

**Usage**:

```console
$ acli config [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `init`: Initializes configuration files.
* `path`: Display full path of configuration files.
* `env`: Show environment variables.
* `show`: Show app configuration.

## `acli config init`

Initializes configuration files.

**Usage**:

```console
$ acli config init [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `acli config path`

Display full path of configuration files.

**Usage**:

```console
$ acli config path [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `acli config env`

Show environment variables.

**Usage**:

```console
$ acli config env [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `acli config show`

Show app configuration.

**Usage**:

```console
$ acli config show [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

# `acli personio`

**Usage**:

```console
$ acli personio [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `status`: Check Personio API status.
* `auth`: Authenticates with Personio API.
* `employee`: Get my infomration from Personio.
* `attendance`: Create a single-day attendance.

## `acli personio status`

Check Personio API status.

**Usage**:

```console
$ acli personio status [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `acli personio auth`

Authenticates with Personio API.

**Usage**:

```console
$ acli personio auth [OPTIONS]
```

**Options**:

* `-c, --client-id TEXT`: i.e.: papi-baaaaaad-c0de-fade-baad-00000000001d  [env var: ACLI_PERSONIO_CLIENT_ID; required]
* `-p, --client-secret TEXT`: i.e.: verY-Secret-p4ssw0rd  [env var: ACLI_PERSONIO_CLIENT_SECRET; required]
* `--help`: Show this message and exit.

## `acli personio employee`

Get my infomration from Personio.

**Usage**:

```console
$ acli personio employee [OPTIONS]
```

**Options**:

* `-c, --client-id TEXT`: i.e.: papi-baaaaaad-c0de-fade-baad-00000000001d  [env var: ACLI_PERSONIO_CLIENT_ID; required]
* `-p, --client-secret TEXT`: i.e.: verY-Secret-p4ssw0rd  [env var: ACLI_PERSONIO_CLIENT_SECRET; required]
* `-i, --employee-id TEXT`: i.e.: 123456  [env var: ACLI_PERSONIO_EMPLOYEE_ID; required]
* `--help`: Show this message and exit.

## `acli personio attendance`

Create a single-day attendance.

**Usage**:

```console
$ acli personio attendance [OPTIONS]
```

**Options**:

* `-c, --client-id TEXT`: i.e.: papi-baaaaaad-c0de-fade-baad-00000000001d  [env var: ACLI_PERSONIO_CLIENT_ID; required]
* `-p, --client-secret TEXT`: i.e.: verY-Secret-p4ssw0rd  [env var: ACLI_PERSONIO_CLIENT_SECRET; required]
* `-i, --employee-id TEXT`: i.e.: 123456  [env var: ACLI_PERSONIO_EMPLOYEE_ID; required]
* `-d, --attendance-date TEXT`: i.e.: 2006-01-02  [env var: ACLI_PERSONIO_ATTENDANCE_DATE]
* `-w, --attendance-weeks INTEGER`: i.e.: 4  [env var: ACLI_PERSONIO_ATTENDANCE_WEEKS; default: 0]
* `--help`: Show this message and exit.

# `acli docker`

**Usage**:

```console
$ acli docker [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `credentials`: Docker credentials commands.

## `acli docker credentials`

**Usage**:

```console
$ acli docker credentials [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `vault`: Show 1password vault information used by Docker.
* `get`: Show a credential from Docker credentials vault.
* `erase`: Erase a credential from Docker credentials vault.
* `list`: List all credentials from Docker credentials vault.
* `store`: Show a credential from Docker credentials vault.

### `acli docker credentials vault`

Show 1password vault information used by Docker.

**Usage**:

```console
$ acli docker credentials vault [OPTIONS]
```

**Options**:

* `--vault-name, -v TEXT`: i.e.: Docker  [env var: ACLI_DOCKER_VAULT_NAME; default: Docker]
* `--help`: Show this message and exit.

### `acli docker credentials get`

Show a credential from Docker credentials vault.

**Usage**:

```console
$ acli docker credentials get [OPTIONS]
```

**Options**:

* `--vault-name, -v TEXT`: i.e.: Docker  [env var: ACLI_DOCKER_VAULT_NAME; default: Docker]
* `--help`: Show this message and exit.

### `acli docker credentials erase`

Erase a credential from Docker credentials vault.

**Usage**:

```console
$ acli docker credentials erase [OPTIONS]
```

**Options**:

* `--vault-name, -v TEXT`: i.e.: Docker  [env var: ACLI_DOCKER_VAULT_NAME; default: Docker]
* `--help`: Show this message and exit.

### `acli docker credentials list`

List all credentials from Docker credentials vault.

**Usage**:

```console
$ acli docker credentials list [OPTIONS]
```

**Options**:

* `--vault-name, -v TEXT`: i.e.: Docker  [env var: ACLI_DOCKER_VAULT_NAME; default: Docker]
* `--help`: Show this message and exit.

### `acli docker credentials store`

Show a credential from Docker credentials vault.

**Usage**:

```console
$ acli docker credentials store [OPTIONS]
```

**Options**:

* `--vault-name, -v TEXT`: i.e.: Docker  [env var: ACLI_DOCKER_VAULT_NAME; default: Docker]
* `--help`: Show this message and exit.

