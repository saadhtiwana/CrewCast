"""Configuration models and loaders for CrewCast."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


DEFAULT_SEGMENTS = (
    "Top story roundup",
    "Deep dive",
    "Listener question",
    "Closing thoughts",
)


@dataclass(frozen=True)
class EpisodeConfig:
    """Configuration for a single episode generation run."""

    title: str
    host_name: str
    topics: tuple[str, ...]
    segments: tuple[str, ...] = field(default_factory=lambda: tuple(DEFAULT_SEGMENTS))
    tone: str = "friendly"

    @staticmethod
    def from_mapping(data: dict) -> "EpisodeConfig":
        title = str(data.get("title", "Untitled Episode")).strip() or "Untitled Episode"
        host_name = str(data.get("host_name", "CrewCast Host")).strip() or "CrewCast Host"
        tone = str(data.get("tone", "friendly")).strip() or "friendly"

        topics_raw = data.get("topics", [])
        topics = tuple(str(topic).strip() for topic in _coerce_iterable(topics_raw))
        topics = tuple(topic for topic in topics if topic) or ("technology",)

        segments_raw = data.get("segments", DEFAULT_SEGMENTS)
        segments = tuple(str(segment).strip() for segment in _coerce_iterable(segments_raw))
        segments = tuple(segment for segment in segments if segment) or tuple(DEFAULT_SEGMENTS)

        return EpisodeConfig(
            title=title,
            host_name=host_name,
            topics=topics,
            segments=segments,
            tone=tone,
        )


def load_config(path: Path) -> EpisodeConfig:
    """Load episode configuration from a JSON file."""

    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("Config file must contain a JSON object at the root.")
    return EpisodeConfig.from_mapping(payload)


def _coerce_iterable(value: object) -> Iterable:
    if value is None:
        return ()
    if isinstance(value, (list, tuple)):
        return value
    return (value,)
