#!/bin/bash
# No dataset. Verify python and pytest are available.
python3 -c "import curses" || echo "WARN: curses unavailable, renderer rounds will need a fallback"
python3 -m pytest --version || pip install pytest
