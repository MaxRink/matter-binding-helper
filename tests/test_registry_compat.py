from types import SimpleNamespace

from custom_components.matter_binding_helper.matter.compat import iter_registry_devices


def test_iterates_legacy_registry_mapping_values():
    first = object()
    second = object()
    registry = SimpleNamespace(devices={"first": first, "second": second})
    assert list(iter_registry_devices(registry)) == [first, second]


def test_iterates_current_registry_collection_entries():
    first = object()
    second = object()
    registry = SimpleNamespace(devices=(first, second))
    assert list(iter_registry_devices(registry)) == [first, second]
