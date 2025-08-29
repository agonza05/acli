#!/usr/bin/env bash

OLD_VERSION=$(uvx --from=toml-cli toml get --toml-path=pyproject.toml project.version)
NEW_VERSION=$(echo $OLD_VERSION | awk -F. -v OFS=. '{$(NF-1)++; $NF=0; print}')
uvx --from=toml-cli toml set --toml-path=pyproject.toml project.version $NEW_VERSION
uvx --from=toml-cli toml set --toml-path=pyproject.toml metadata.version $NEW_VERSION
sed -i "" -E "s|__version__.*|__version__ = \"$NEW_VERSION\"|g" acli/__init__.py
