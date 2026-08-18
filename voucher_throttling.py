"""Voucher distribution throttling logic."""

from typing import Iterable, List, Sequence


COOLDOWN_SECONDS = 5


def rejected_citizen_ids(requests: Iterable[Sequence[int]]) -> List[int]:
    """Return citizen IDs for requests rejected by 5-second per-citizen throttling.

    A citizen request is approved if no approved request exists for that citizen in the
    5-second cooldown window. Rejected requests do not extend cooldown.
    """
    next_allowed_at = {}
    rejected: List[int] = []

    for citizen_id, timestamp in requests:
        allowed_at = next_allowed_at.get(citizen_id)
        if allowed_at is not None and timestamp < allowed_at:
            rejected.append(citizen_id)
            continue

        next_allowed_at[citizen_id] = timestamp + COOLDOWN_SECONDS

    return rejected


# Compatibility aliases for common naming expectations.
throttle_requests = rejected_citizen_ids
find_rejected_requests = rejected_citizen_ids
