# CrewCast

CrewCast is a lightweight, batteries-included toolkit for generating personalized podcast scripts using only the Python standard library. It blends configuration-driven episode design with a CLI that produces ready-to-record outlines in seconds.

---

## ✨ Highlights

- **Config-first workflow**: Define titles, hosts, tones, segments, and topics in JSON.
- **CLI-friendly**: Generate scripts from files or flags (`python -m crewcast`).
- **Deterministic output**: Ideal for pipelines, templates, and post-processing.
- **Pure standard library**: No dependencies required.

---

## Table of Contents

- [Quick Start](#quick-start)
- [Core Concepts](#core-concepts)
- [CLI Usage](#cli-usage)
- [Configuration Reference](#configuration-reference)
- [Output Format](#output-format)
- [Examples](#examples)
- [Development](#development)
- [Testing](#testing)
- [Roadmap](#roadmap)
- [FAQ](#faq)

---

## Quick Start

Generate a script directly from flags:

```bash
python -m crewcast \
  --title "CrewCast Daily" \
  --host "Alex" \
  --topics "AI" "space" \
  --tone "insightful"
```

Generate from a JSON configuration file:

```bash
python -m crewcast \
  --config examples/sample_config.json \
  --output episode.txt
```

---

## Core Concepts

CrewCast centers around a simple data model:

- **Episode**: Title, host name, tone, and a list of topics.
- **Segments**: Reusable sections (e.g., “Top story roundup”) that rotate through topics.
- **Script**: A single string assembled from a header, segments, and an outro.

This keeps the generator deterministic and easy to integrate into automation workflows.

---

## CLI Usage

```bash
python -m crewcast [--config PATH] [--title TITLE] [--host NAME] [--topics ...] [--tone TONE] [--output PATH]
```

| Flag | Description |
| --- | --- |
| `--config` | Path to a JSON configuration file. |
| `--title` | Episode title (default: `CrewCast Daily`). |
| `--host` | Host name (default: `CrewCast Host`). |
| `--topics` | One or more topics (default: `technology`, `culture`). |
| `--tone` | Narration style (default: `friendly`). |
| `--output` | Optional file path to save the script. |

---

## Configuration Reference

Use `examples/sample_config.json` as a template. All keys are optional.

```json
{
  "title": "The CrewCast Show",
  "host_name": "Jordan",
  "topics": ["climate", "robotics", "health"],
  "segments": [
    "Top story roundup",
    "Deep dive",
    "Listener question",
    "Closing thoughts"
  ],
  "tone": "friendly"
}
```

### Field details

| Field | Type | Default | Notes |
| --- | --- | --- | --- |
| `title` | string | `Untitled Episode` | Trimmed; falls back when blank. |
| `host_name` | string | `CrewCast Host` | The on-air host. |
| `topics` | array[string] | `technology` | Cycles through segments. |
| `segments` | array[string] | see defaults | Defines segment order. |
| `tone` | string | `friendly` | Drives the narration style. |

---

## Output Format

The script is a human-readable outline designed for live reading or post-editing:

```
Welcome to The CrewCast Show!
I'm Jordan, your friendly guide for today.
It is March 14, 2026, and we're covering: climate, robotics, health.

Segment 1: Top story roundup
Today's focus: climate.
Key points:
- Why climate matters right now.
- A quick story to make climate relatable.
- A takeaway you can share from this friendly discussion.

...

That's our show!
Thanks for listening to The CrewCast Show with Jordan.
Subscribe for more personalized episodes, and share this with a friend.
```

---

## Examples

### Minimal configuration via CLI

```bash
python -m crewcast --title "Signal Boost" --host "Nova" --topics "startups"
```

### Save output to a file

```bash
python -m crewcast --config examples/sample_config.json --output scripts/episode.txt
```

---

## Development

CrewCast is intentionally small and readable. Key modules:

- `crewcast/config.py` — configuration loading and validation.
- `crewcast/generator.py` — script generation logic.
- `crewcast/cli.py` — command-line interface.

To run locally, you only need Python 3.10+.

---

## Testing

Run the unit tests:

```bash
python -m unittest discover -s tests
```

---

## Roadmap

Potential upgrades for future iterations:

- Add templating support for custom segment text.
- Introduce speaker voices or multi-host scripts.
- Export to structured formats (Markdown, JSON, or SSML).
- Integrate LLM-generated segment details.

---

## FAQ

**Does CrewCast require external APIs?**
No. It runs entirely locally using the Python standard library.

**Can I customize the script structure?**
Yes—edit the `segments` list or extend the generator module for deeper changes.

**Is the output deterministic?**
Yes. Given the same inputs, CrewCast produces the same script text.
