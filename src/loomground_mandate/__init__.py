# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 flxk1
"""loomground-mandate — Did this run serve the purpose it was given?

One narrow problem. See :mod:`loomground_mandate.divergence` for the reasoning;
this module only re-exports it and the version.
"""

from ._version import __version__
from .divergence import (
    Mandate,
    TrajectoryStep,
    Divergence,
    detect,
    fold_divergences,
    KINDS,
)

__all__ = [
    "__version__",
    "Mandate",
    "TrajectoryStep",
    "Divergence",
    "detect",
    "fold_divergences",
    "KINDS",
]
