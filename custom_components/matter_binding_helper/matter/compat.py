"""Compatibility helpers for Home Assistant registry collection APIs."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any


def iter_registry_devices(registry: Any) -> Iterable[Any]:
    """Iterate registry entries across old mappings and current collections."""
    devices = registry.devices
    if isinstance(devices, Mapping):
        return devices.values()
    return devices
