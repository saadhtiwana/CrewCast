"""Episode script generation for CrewCast."""

from __future__ import annotations

from datetime import datetime

from crewcast.config import EpisodeConfig


def generate_episode(config: EpisodeConfig) -> str:
    """Generate a full episode script from configuration."""

    header = _generate_header(config)
    segments = generate_segments(config)
    outro = _generate_outro(config)
    return "\n\n".join([header, *segments, outro]).strip() + "\n"


def generate_segments(config: EpisodeConfig) -> list[str]:
    """Generate segment scripts for each segment title."""

    segments = []
    for index, segment_title in enumerate(config.segments, start=1):
        topic = config.topics[(index - 1) % len(config.topics)]
        segments.append(_render_segment(index, segment_title, topic, config))
    return segments


def _generate_header(config: EpisodeConfig) -> str:
    date = datetime.utcnow().strftime("%B %d, %Y")
    topics_line = ", ".join(config.topics)
    return (
        f"Welcome to {config.title}!\n"
        f"I'm {config.host_name}, your {config.tone} guide for today.\n"
        f"It is {date}, and we're covering: {topics_line}."
    )


def _render_segment(index: int, title: str, topic: str, config: EpisodeConfig) -> str:
    return (
        f"Segment {index}: {title}\n"
        f"Today's focus: {topic}.\n"
        "Key points:\n"
        f"- Why {topic} matters right now.\n"
        f"- A quick story to make {topic} relatable.\n"
        f"- A takeaway you can share from this {config.tone} discussion."
    )


def _generate_outro(config: EpisodeConfig) -> str:
    return (
        "That's our show!\n"
        f"Thanks for listening to {config.title} with {config.host_name}.\n"
        "Subscribe for more personalized episodes, and share this with a friend."
    )
