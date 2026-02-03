import unittest

from crewcast.config import EpisodeConfig
from crewcast.generator import generate_episode


class GeneratorTests(unittest.TestCase):
    def test_generate_episode_contains_segments_and_host(self):
        config = EpisodeConfig.from_mapping(
            {
                "title": "Space Briefing",
                "host_name": "Nova",
                "topics": ["rockets", "telescopes"],
                "segments": ["News", "Deep dive"],
                "tone": "curious",
            }
        )

        script = generate_episode(config)

        self.assertIn("Space Briefing", script)
        self.assertIn("Nova", script)
        self.assertIn("Segment 1: News", script)
        self.assertIn("Segment 2: Deep dive", script)


if __name__ == "__main__":
    unittest.main()
