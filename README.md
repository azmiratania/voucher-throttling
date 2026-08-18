# voucher-throttling

This repository contains a minimal implementation of voucher request throttling.

## Behavior

- Each citizen can have one approved request every 5 seconds.
- If a citizen is approved at time `T`, requests from that citizen at `T` through `T+4` are rejected.
- Rejected requests do **not** extend cooldown.

## Implementation

`voucher_throttling.rejected_citizen_ids(requests)` returns rejected citizen IDs in request order.
