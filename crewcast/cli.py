"""Command-line interface for CrewCast."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from crewcast.config import EpisodeConfig, load_config
from crewcast.generator import generate_episode


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate a personalized podcast script.")
    parser.add_argument("--config", type=Path, help="Path to a JSON config file.")
    parser.add_argument("--title", help="Episode title.")
    parser.add_argument("--host", dest="host_name", help="Host name.")
    parser.add_argument("--topics", nargs="*", help="Topics to cover in the episode.")
    parser.add_argument("--tone", default="friendly", help="Tone for the host narration.")
    parser.add_argument("--output", type=Path, help="Write the episode script to a file.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.config:
        config = load_config(args.config)
    else:
        config = EpisodeConfig.from_mapping(
            {
                "title": args.title or "CrewCast Daily",
                "host_name": args.host_name or "CrewCast Host",
                "topics": args.topics or ["technology", "culture"],
                "tone": args.tone,
            }
        )

    script = generate_episode(config)

    if args.output:
        args.output.write_text(script, encoding="utf-8")
    else:
        print(script)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
