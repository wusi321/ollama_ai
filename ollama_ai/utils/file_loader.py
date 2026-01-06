from pathlib import Path

def read_file(path: str) -> str:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"{path} not found")
    return path.read_text(encoding="utf-8", errors="ignore")


def read_project(root: str, suffix=(".c", ".h", ".py")) -> str:
    root = Path(root)
    if not root.exists():
        raise FileNotFoundError(f"{root} not found")

    contents = []
    for file in root.rglob("*"):
        if file.suffix in suffix:
            contents.append(
                f"\n// ===== FILE: {file} =====\n"
                + file.read_text(errors="ignore")
            )
    return "\n".join(contents)