# `acli`

**Usage**:

```console
$ acli [OPTIONS]
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
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

* `show`: Show app configuration.
* `env`: Show envrionment variables.
* `path`: Display full path of configuration files.
* `set`: Set app configuration.

## `acli config show`

Show app configuration.

**Usage**:

```console
$ acli config show [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `acli config env`

Show envrionment variables.

**Usage**:

```console
$ acli config env [OPTIONS]
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

## `acli config set`

Set app configuration.

**Usage**:

```console
$ acli config set [OPTIONS]
```

**Options**:

* `-p, --key-path TEXT`: i.e.: section.subsection.key  [required]
* `-v, --key-value TEXT`: i.e.: new_value  [required]
* `--help`: Show this message and exit.

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

* `up`: Upgrade brew packages.
* `info`: Display system information.

## `acli system up`

Upgrade brew packages.

**Usage**:

```console
$ acli system up [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `acli system info`

Display system information.

**Usage**:

```console
$ acli system info [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

# `acli project`

**Usage**:

```console
$ acli project [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `direnv`: Create a new direnv file in the current...
* `gitemail`: Set the git user email address.

## `acli project direnv`

Create a new direnv file in the current directory.

**Usage**:

```console
$ acli project direnv [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `acli project gitemail`

Set the git user email address.

**Usage**:

```console
$ acli project gitemail [OPTIONS]
```

**Options**:

* `-w, --work-email`: i.e.: user@company.com  [env var: ACLI_PROJECT_WORK_EMAIL]
* `-p, --personal-email`: i.e.: user@personal.com  [env var: ACLI_PROJECT_PERSONAL_EMAIL]
* `--help`: Show this message and exit.

# `acli personio`

Global options for personio commands.

**Usage**:

```console
$ acli personio [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-c, --client-id TEXT`: i.e.: papi-baaaaaad-c0de-fade-baad-00000000001d  [env var: ACLI_PERSONIO_CLIENT_ID; required]
* `-p, --client-secret TEXT`: i.e.: verY-Secret-p4ssw0rd  [env var: ACLI_PERSONIO_CLIENT_SECRET; required]
* `-i, --employee-id TEXT`: i.e.: 123456  [env var: ACLI_PERSONIO_EMPLOYEE_ID; required]
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `status`: Check Personio API status.
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

## `acli personio employee`

Get my infomration from Personio.

**Usage**:

```console
$ acli personio employee [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `acli personio attendance`

Create a single-day attendance.

**Usage**:

```console
$ acli personio attendance [OPTIONS]
```

**Options**:

* `-d, --attendance-date TEXT`: i.e.: 2006-01-02  [env var: ACLI_PERSONIO_ATTENDANCE_DATE]
* `-w, --attendance-weeks INTEGER`: i.e.: 4  [env var: ACLI_PERSONIO_ATTENDANCE_WEEKS; default: 0]
* `--help`: Show this message and exit.

# `acli docker`

**Usage**:

```console
$ acli docker [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `credentials`: Docker credentials commands.

## `acli docker credentials`

Docker credentials commands.

**Usage**:

```console
$ acli docker credentials [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `vault`: Show 1password vault information used by...
* `get`: Show a credential from Docker credentials...
* `erase`: Erase a credential from Docker credentials...
* `list`: List all credentials from Docker...
* `store`: Show a credential from Docker credentials...

### `acli docker credentials vault`

Show 1password vault information used by Docker.

**Usage**:

```console
$ acli docker credentials vault [OPTIONS]
```

**Options**:

* `-v, --vault-name TEXT`: i.e.: Docker  [env var: ACLI_DOCKER_VAULT_NAME; default: Docker]
* `--help`: Show this message and exit.

### `acli docker credentials get`

Show a credential from Docker credentials vault.

**Usage**:

```console
$ acli docker credentials get [OPTIONS]
```

**Options**:

* `-v, --vault-name TEXT`: i.e.: Docker  [env var: ACLI_DOCKER_VAULT_NAME; default: Docker]
* `--help`: Show this message and exit.

### `acli docker credentials erase`

Erase a credential from Docker credentials vault.

**Usage**:

```console
$ acli docker credentials erase [OPTIONS]
```

**Options**:

* `-v, --vault-name TEXT`: i.e.: Docker  [env var: ACLI_DOCKER_VAULT_NAME; default: Docker]
* `--help`: Show this message and exit.

### `acli docker credentials list`

List all credentials from Docker credentials vault.

**Usage**:

```console
$ acli docker credentials list [OPTIONS]
```

**Options**:

* `-v, --vault-name TEXT`: i.e.: Docker  [env var: ACLI_DOCKER_VAULT_NAME; default: Docker]
* `--help`: Show this message and exit.

### `acli docker credentials store`

Show a credential from Docker credentials vault.

**Usage**:

```console
$ acli docker credentials store [OPTIONS]
```

**Options**:

* `-v, --vault-name TEXT`: i.e.: Docker  [env var: ACLI_DOCKER_VAULT_NAME; default: Docker]
* `--help`: Show this message and exit.

# `acli docker credentials`

**Usage**:

```console
$ acli docker credentials [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `vault`: Show 1password vault information used by...
* `get`: Show a credential from Docker credentials...
* `erase`: Erase a credential from Docker credentials...
* `list`: List all credentials from Docker...
* `store`: Show a credential from Docker credentials...

## `acli docker credentials vault`

Show 1password vault information used by Docker.

**Usage**:

```console
$ acli docker credentials vault [OPTIONS]
```

**Options**:

* `-v, --vault-name TEXT`: i.e.: Docker  [env var: ACLI_DOCKER_VAULT_NAME; default: Docker]
* `--help`: Show this message and exit.

## `acli docker credentials get`

Show a credential from Docker credentials vault.

**Usage**:

```console
$ acli docker credentials get [OPTIONS]
```

**Options**:

* `-v, --vault-name TEXT`: i.e.: Docker  [env var: ACLI_DOCKER_VAULT_NAME; default: Docker]
* `--help`: Show this message and exit.

## `acli docker credentials erase`

Erase a credential from Docker credentials vault.

**Usage**:

```console
$ acli docker credentials erase [OPTIONS]
```

**Options**:

* `-v, --vault-name TEXT`: i.e.: Docker  [env var: ACLI_DOCKER_VAULT_NAME; default: Docker]
* `--help`: Show this message and exit.

## `acli docker credentials list`

List all credentials from Docker credentials vault.

**Usage**:

```console
$ acli docker credentials list [OPTIONS]
```

**Options**:

* `-v, --vault-name TEXT`: i.e.: Docker  [env var: ACLI_DOCKER_VAULT_NAME; default: Docker]
* `--help`: Show this message and exit.

## `acli docker credentials store`

Show a credential from Docker credentials vault.

**Usage**:

```console
$ acli docker credentials store [OPTIONS]
```

**Options**:

* `-v, --vault-name TEXT`: i.e.: Docker  [env var: ACLI_DOCKER_VAULT_NAME; default: Docker]
* `--help`: Show this message and exit.

