from __future__ import annotations

from rich.console import ConsoleOptions, Console, RenderResult
from rich.segment import Segment
from rich.style import Style

from ..color import Color


class Blank:
    """Draw solid background color."""

    def __init__(self, color: Color | str = "transparent") -> None:
        background = color if isinstance(color, Color) else Color.parse(color)
        self._style = (
            Style()
            if background.is_transparent
            else Style.from_color(None, background.rich_color)
        )

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        width = options.max_width
        height = options.height or options.max_height

        segment = Segment(" " * width, self._style)
        line = Segment.line()
        for _ in range(height):
            yield segment
            yield line


if __name__ == "__main__":
    from rich import print

    print(Blank("red"))