"""Repository-wide integrity checks for generated-source contamination."""

from __future__ import annotations

import ast
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_all_python_files_parse():
    for path in ROOT.rglob("*.py"):
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


def test_no_shell_heredoc_fragments_in_source():
    banned = ("cat >", "<<'PY'", '<<"PY"', "\nEOF\n")
    for path in [*ROOT.rglob("*.py"), *ROOT.rglob("*.sql")]:
        if path == Path(__file__):
            continue
        text = path.read_text(encoding="utf-8")
        assert not any(token in text for token in banned), path


def test_every_yaml_file_is_a_mapping():
    for path in ROOT.rglob("*.yaml"):
        assert isinstance(yaml.safe_load(path.read_text(encoding="utf-8")), dict), path


def test_required_runtime_directories_exist():
    assert (ROOT / "apps/admin/templates").is_dir()
    assert (ROOT / "apps/admin/static").is_dir()
    assert (ROOT / "migrations").is_dir()