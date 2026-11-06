from pathlib import Path

import polars as pl


def process_truncation(src: Path) -> pl.DataFrame:
    """Загружает JSON и оставляет максимум 2 элемента в массивах столбца skills."""
    src = Path(src)
    if not src.exists():
        raise FileNotFoundError("Файл не найден!")

    if not src.suffix == ".json":
        raise ValueError(f"Файл в формате {src.suffix} не поддерживается")

    return pl.read_json(src).with_columns(pl.col("skills").list.head(2))
