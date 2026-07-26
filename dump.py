#!/usr/bin/env python3
"""
dump_project.py
================
یک اسکریپت مستقل پایتون که کل ساختار پوشه‌ها و محتوای فایل‌های یک پروژه‌ی کد رو
در یک فایل خروجی تمیز (Markdown یا txt) جمع می‌کنه، آماده برای دادن به هوش مصنوعی.

استفاده:
    python dump_project.py /path/to/project
    python dump_project.py /path/to/project -o output.md
    python dump_project.py /path/to/project -o output.txt --format txt
    python dump_project.py /path/to/project --max-size 300000
    python dump_project.py /path/to/project --exclude node_modules --exclude .venv

پیش‌فرض‌ها:
    - خروجی: <project_name>_dump.md در همون پوشه‌ای که اسکریپت اجرا می‌شه
    - فرمت: markdown
    - فایل‌های باینری/شناخته‌نشده رد می‌شن (فقط اسمشون توی درخت میاد)
    - پوشه‌های رایج (git، venv، node_modules، cache، ...) به‌صورت پیش‌فرض حذف می‌شن
    - فایل‌های خیلی بزرگ (پیش‌فرض > 500KB) کامل درج نمی‌شن، فقط اعلام می‌شه که رد شدن
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# پوشه‌هایی که همیشه باید نادیده گرفته بشن (مگر کاربر صراحتاً بخواد)
DEFAULT_EXCLUDE_DIRS = {
    ".git", ".hg", ".svn",
    "__pycache__", ".mypy_cache", ".pytest_cache", ".ruff_cache",
    "node_modules", ".venv", "venv", "env", ".env_dir",
    "dist", "build", ".next", ".nuxt",
    ".idea", ".vscode",
    "site-packages", "egg-info",
}

# پسوند فایل‌هایی که به‌عنوان کد/متن در نظر گرفته می‌شن و محتواشون درج می‌شه
TEXT_EXTENSIONS = {
    ".py", ".pyi", ".pyx",
    ".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs",
    ".json", ".yaml", ".yml", ".toml", ".ini", ".cfg",
    ".md", ".rst", ".txt",
    ".html", ".htm", ".css", ".scss", ".sass",
    ".sql",
    ".sh", ".bash", ".zsh",
    ".env", ".env.example",
    ".dockerfile", "Dockerfile",
    ".gitignore", ".gitattributes",
    ".xml", ".csv",
    ".java", ".go", ".rs", ".rb", ".php", ".c", ".cpp", ".h", ".hpp",
    ".vue", ".svelte",
    ".graphql", ".proto",
    ".makefile", "Makefile",
}

# نگاشت پسوند به زبان، برای syntax highlighting در بلوک کد مارک‌داون
LANG_MAP = {
    ".py": "python", ".pyi": "python", ".pyx": "python",
    ".js": "javascript", ".jsx": "jsx", ".ts": "typescript", ".tsx": "tsx",
    ".mjs": "javascript", ".cjs": "javascript",
    ".json": "json", ".yaml": "yaml", ".yml": "yaml",
    ".toml": "toml", ".ini": "ini", ".cfg": "ini",
    ".md": "markdown", ".rst": "rst", ".txt": "text",
    ".html": "html", ".htm": "html", ".css": "css",
    ".scss": "scss", ".sass": "sass",
    ".sql": "sql",
    ".sh": "bash", ".bash": "bash", ".zsh": "bash",
    ".xml": "xml", ".csv": "csv",
    ".java": "java", ".go": "go", ".rs": "rust", ".rb": "ruby",
    ".php": "php", ".c": "c", ".cpp": "cpp", ".h": "c", ".hpp": "cpp",
    ".vue": "vue", ".svelte": "svelte",
    ".graphql": "graphql", ".proto": "protobuf",
}


def is_probably_text_file(path: Path) -> bool:
    """تشخیص می‌ده که آیا فایل رو باید به‌عنوان متن/کد در نظر گرفت."""
    if path.name in TEXT_EXTENSIONS:
        return True
    if path.suffix.lower() in TEXT_EXTENSIONS:
        return True
    # فایل‌های بدون پسوند رایج مثل Dockerfile, Makefile
    if path.suffix == "" and path.name in {"Dockerfile", "Makefile", "LICENSE"}:
        return True
    return False


def read_file_safely(path: Path, max_size: int) -> tuple[str | None, str | None]:
    """
    محتوای فایل رو می‌خونه.
    خروجی: (محتوا یا None, پیام خطا/رد شدن یا None)
    """
    try:
        size = path.stat().st_size
    except OSError as exc:
        return None, f"[خطا در خواندن اندازه‌ی فایل: {exc}]"

    if size > max_size:
        return None, f"[رد شد: حجم فایل {size:,} بایت بیشتر از حد مجاز {max_size:,} بایت است]"

    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None, "[رد شد: فایل باینری یا انکودینگ غیر UTF-8 تشخیص داده شد]"
    except OSError as exc:
        return None, f"[خطا در خواندن فایل: {exc}]"

    return content, None


def build_tree_lines(root: Path, exclude_dirs: set[str]) -> list[str]:
    """ساخت نمای درختی ساختار پوشه‌ها/فایل‌ها به شکل متنی."""
    lines: list[str] = [f"{root.name}/"]

    def walk(dir_path: Path, prefix: str) -> None:
        try:
            entries = sorted(
                dir_path.iterdir(),
                key=lambda p: (p.is_file(), p.name.lower()),
            )
        except OSError:
            return

        entries = [
            e for e in entries
            if not (e.is_dir() and e.name in exclude_dirs)
            and not e.name.startswith(".DS_Store")
        ]

        for i, entry in enumerate(entries):
            is_last = i == len(entries) - 1
            connector = "└── " if is_last else "├── "
            suffix = "/" if entry.is_dir() else ""
            lines.append(f"{prefix}{connector}{entry.name}{suffix}")

            if entry.is_dir():
                extension = "    " if is_last else "│   "
                walk(entry, prefix + extension)

    walk(root, "")
    return lines


def collect_files(root: Path, exclude_dirs: set[str]) -> list[Path]:
    """جمع‌آوری تمام فایل‌ها به ترتیب مرتب، با رد کردن پوشه‌های حذف‌شده."""
    files: list[Path] = []

    def walk(dir_path: Path) -> None:
        try:
            entries = sorted(dir_path.iterdir(), key=lambda p: p.name.lower())
        except OSError:
            return
        for entry in entries:
            if entry.is_dir():
                if entry.name in exclude_dirs:
                    continue
                walk(entry)
            elif entry.is_file():
                files.append(entry)

    walk(root)
    return files


def dump_markdown(
    root: Path,
    files: list[Path],
    tree_lines: list[str],
    max_size: int,
) -> str:
    parts: list[str] = []
    parts.append(f"# دامپ پروژه: {root.name}\n")
    parts.append(f"مسیر مبدا: `{root}`\n")
    parts.append(f"تعداد کل فایل‌ها: {len(files)}\n")

    parts.append("\n## ساختار پوشه‌ها و فایل‌ها\n")
    parts.append("```")
    parts.extend(tree_lines)
    parts.append("```")

    parts.append("\n## محتوای فایل‌ها\n")

    for path in files:
        rel_path = path.relative_to(root)
        parts.append(f"\n### `{rel_path}`\n")

        if not is_probably_text_file(path):
            parts.append("_[این فایل باینری/غیرمتنی تشخیص داده شد و محتوایش درج نشد]_\n")
            continue

        content, note = read_file_safely(path, max_size)
        if content is None:
            parts.append(f"_{note}_\n")
            continue

        lang = LANG_MAP.get(path.suffix.lower(), "")
        parts.append(f"```{lang}")
        parts.append(content.rstrip("\n"))
        parts.append("```")

    return "\n".join(parts) + "\n"


def dump_txt(
    root: Path,
    files: list[Path],
    tree_lines: list[str],
    max_size: int,
) -> str:
    parts: list[str] = []
    sep = "=" * 70

    parts.append(sep)
    parts.append(f"دامپ پروژه: {root.name}")
    parts.append(f"مسیر مبدا: {root}")
    parts.append(f"تعداد کل فایل‌ها: {len(files)}")
    parts.append(sep)

    parts.append("\nساختار پوشه‌ها و فایل‌ها:\n")
    parts.extend(tree_lines)

    parts.append("\n" + sep)
    parts.append("محتوای فایل‌ها")
    parts.append(sep)

    for path in files:
        rel_path = path.relative_to(root)
        parts.append(f"\n----- FILE: {rel_path} -----")

        if not is_probably_text_file(path):
            parts.append("[این فایل باینری/غیرمتنی تشخیص داده شد و محتوایش درج نشد]")
            continue

        content, note = read_file_safely(path, max_size)
        if content is None:
            parts.append(note or "[نامشخص]")
            continue

        parts.append(content.rstrip("\n"))

    return "\n".join(parts) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="کل ساختار و محتوای یک پروژه‌ی کد رو در یک فایل تمیز جمع می‌کند، آماده برای دادن به هوش مصنوعی."
    )
    parser.add_argument(
        "project_path", type=str, nargs="?", default=None,
        help="مسیر پوشه‌ی پروژه (اگر ندهید، پوشه‌ای که خود اسکریپت در آن قرار دارد استفاده می‌شود)"
    )
    parser.add_argument(
        "-o", "--output", type=str, default=None,
        help="مسیر فایل خروجی (پیش‌فرض: <project_name>_dump.<ext> در پوشه‌ی فعلی)"
    )
    parser.add_argument(
        "--format", choices=["md", "markdown", "txt"], default="md",
        help="فرمت خروجی (پیش‌فرض: md)"
    )
    parser.add_argument(
        "--max-size", type=int, default=500_000,
        help="حداکثر حجم هر فایل بر حسب بایت که کامل درج می‌شود (پیش‌فرض: 500000)"
    )
    parser.add_argument(
        "--exclude", action="append", default=[],
        help="نام پوشه‌ی اضافی برای حذف کردن (قابل تکرار، مثلا --exclude tests --exclude data)"
    )
    parser.add_argument(
        "--no-default-exclude", action="store_true",
        help="پوشه‌های پیش‌فرض حذف‌شده (git, venv, node_modules, ...) را حذف نکن"
    )

    args = parser.parse_args()

    if args.project_path:
        root = Path(args.project_path).expanduser().resolve()
    else:
        # هیچ مسیری داده نشده: پوشه‌ای که خود اسکریپت در آن قرار دارد استفاده می‌شود
        root = Path(__file__).resolve().parent
        print(f"هیچ مسیری داده نشد؛ پوشه‌ی خود اسکریپت به‌عنوان پروژه در نظر گرفته شد: {root}")

    if not root.exists() or not root.is_dir():
        print(f"خطا: مسیر '{root}' پیدا نشد یا یک پوشه نیست.", file=sys.stderr)
        sys.exit(1)

    exclude_dirs = set() if args.no_default_exclude else set(DEFAULT_EXCLUDE_DIRS)
    exclude_dirs.update(args.exclude)

    fmt = "markdown" if args.format in ("md", "markdown") else "txt"
    ext = "md" if fmt == "markdown" else "txt"

    if args.output:
        output_path = Path(args.output).expanduser().resolve()
    else:
        output_path = root / f"{root.name}_dump.{ext}"

    script_path = Path(__file__).resolve()

    print(f"در حال اسکن پروژه: {root}")
    tree_lines = build_tree_lines(root, exclude_dirs)
    files = collect_files(root, exclude_dirs)

    # خود اسکریپت و فایل خروجی قبلی را از دامپ حذف کن (اگر داخل همان پروژه باشند)
    skip_names = {"dump_project.py", "dump.py", output_path.name}
    files = [f for f in files if f.resolve() != script_path and f.name not in skip_names]

    print(f"تعداد فایل پیدا شده: {len(files)}")

    if fmt == "markdown":
        result = dump_markdown(root, files, tree_lines, args.max_size)
    else:
        result = dump_txt(root, files, tree_lines, args.max_size)

    output_path.write_text(result, encoding="utf-8")
    print(f"فایل خروجی نوشته شد: {output_path}")
    print(f"حجم فایل خروجی: {output_path.stat().st_size:,} بایت")


if __name__ == "__main__":
    main()