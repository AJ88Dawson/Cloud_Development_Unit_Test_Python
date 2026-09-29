"""Makes `tests` a package and puts `src/` on the import path.

Without this, `from exercise1.calculator import Calculator` below would fail, because
`src/` is not a folder Python searches by default. The pytest version of this
project did the same job with a `pythonpath = src` line in `pytest.ini`.
`unittest` has no configuration file, so the three lines below do it instead.

You do not need to change anything in this file.
"""

import os
import sys

sys.path.insert(
    0, os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "src")
)
