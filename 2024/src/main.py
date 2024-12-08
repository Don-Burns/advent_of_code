import importlib
import logging
from pathlib import Path
from types import ModuleType

from aoc.logger import logger

INPUT_DIR = Path(__file__).parent.parent / "input"


def main() -> int:
    """
    Main function
    """
    for day in sorted(INPUT_DIR.glob("*.txt")):
        logger.info("Running %s", day.stem)
        day_input = day.read_text()
        day_module: ModuleType = importlib.import_module(f"aoc.days.{day.stem}")
        try:
            logger.info("Part 1 Answer: %s", day_module.part_1(day_input))
        except AttributeError:
            logger.exception("Part 1 not found")
        try:
            logger.info("Part 2 Answer: %s", day_module.part_2(day_input))
        except AttributeError:
            logger.exception("Part 2 not found")

    return 0


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    raise SystemExit(main())
