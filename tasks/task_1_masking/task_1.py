from pathlib import Path

import polars as pl


def process_masking(src: Path) -> pl.DataFrame:
    """Загружает JSON и маскирует столбец email."""
    src = Path(src)
    if not src.exists():
        raise FileNotFoundError("Файл не найден!")

    if not src.suffix == ".json":
        raise ValueError(f"Файл в формате {src.suffix} не поддерживается")

    return pl.read_json(src).with_columns(pl.lit("!!!Masked!!!").alias("email"))
