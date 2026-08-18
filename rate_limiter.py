"""Voucher distribution request rate-limiter.

A citizen may have only one successful request every `cooldown` seconds.
If a request is approved at time T, later requests from the same citizen
in the inclusive window [T, T + cooldown - 1] are rejected.

Rejected requests do not reset or extend the cooldown.
The input is assumed to be sorted by timestamp.
"""

from __future__ import annotations


def rejected_requests(requests: list[list[int]], cooldown: int = 5) -> list[int]:
    """Return citizen IDs whose voucher requests are rejected, in arrival order."""
    last_approved: dict[int, int] = {}
    rejected: list[int] = []

    for citizen_id, timestamp in requests:
        previous = last_approved.get(citizen_id)
        if previous is not None and timestamp < previous + cooldown:
            rejected.append(citizen_id)
            continue
        last_approved[citizen_id] = timestamp

    return rejected


if __name__ == "__main__":
    example = [[1, 10], [2, 11], [1, 12], [1, 15], [2, 15]]
    print(rejected_requests(example))
