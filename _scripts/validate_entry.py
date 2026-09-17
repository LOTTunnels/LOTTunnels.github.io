"""Validate _lottunnels/Binaries/<name>.md front matter against the entry schema.

Usage:
    python validate_entry.py <file> [<file> ...]

Exits non-zero if any file fails to parse as YAML or fails schema validation.
"""

import sys
from datetime import date
from pathlib import Path as FilePath

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError


class Command(BaseModel):
    model_config = ConfigDict(extra="forbid")

    Command: str = Field(min_length=1)
    Description: str = Field(min_length=1)
    Usecase: str = Field(min_length=1)
    Category: str = Field(min_length=1)
    Privileges: str = Field(min_length=1)
    OperatingSystem: str = Field(min_length=1)


class FullPathEntry(BaseModel):
    model_config = ConfigDict(extra="forbid")

    Path: str | None = Field(default=None, min_length=1)
    Filename: str | None = Field(default=None, min_length=1)


class DetectionEntry(BaseModel):
    model_config = ConfigDict(extra="forbid")

    Domain: str | None = Field(default=None, min_length=1)
    Command: str | None = Field(default=None, min_length=1)
    URL: str | None = Field(default=None, min_length=1)
    Sigma: str | None = Field(default=None, min_length=1)


class ResourceEntry(BaseModel):
    model_config = ConfigDict(extra="forbid")

    Link: str = Field(min_length=1)


class AcknowledgementEntry(BaseModel):
    model_config = ConfigDict(extra="forbid")

    Person: str = Field(min_length=1)
    Handle: str | None = Field(default=None, min_length=1)


class BinaryEntry(BaseModel):
    model_config = ConfigDict(extra="forbid")

    Name: str = Field(min_length=1)
    Description: str = Field(min_length=1)
    Author: str = Field(min_length=1)
    Created: date
    Commands: list[Command] = Field(min_length=1)
    Custom_Domain_Supported: bool | None = None
    Full_Path: list[FullPathEntry] | None = Field(default=None, min_length=1)
    Detection: list[DetectionEntry] = Field(min_length=1)
    Resources: list[ResourceEntry] | None = Field(default=None, min_length=1)
    Acknowledgement: list[AcknowledgementEntry] | None = Field(default=None, min_length=1)


def load_front_matter(path: FilePath) -> dict:
    raw = path.read_text(encoding="utf-8")
    stripped = raw.strip()
    if not stripped.startswith("---"):
        raise ValueError("file does not start with a '---' YAML front matter block")

    documents = [doc for doc in yaml.safe_load_all(stripped.strip("-")) if doc is not None]
    if not documents:
        raise ValueError("no YAML front matter found")
    return documents[0]


def validate_file(path: FilePath) -> list[str]:
    try:
        data = load_front_matter(path)
    except yaml.YAMLError as exc:
        return [f"YAML parse error: {exc}"]
    except ValueError as exc:
        return [str(exc)]

    try:
        BinaryEntry.model_validate(data)
    except ValidationError as exc:
        errors = []
        for error in exc.errors():
            location = " -> ".join(str(part) for part in error["loc"])
            errors.append(f"{location}: {error['msg']}")
        return errors

    return []


def main(argv: list[str]) -> int:
    if not argv:
        print("usage: validate_entry.py <file> [<file> ...]", file=sys.stderr)
        return 2

    exit_code = 0
    for arg in argv:
        path = FilePath(arg)
        errors = validate_file(path)
        if errors:
            exit_code = 1
            print(f"::error file={path}::Schema validation failed")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK: {path}")

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
