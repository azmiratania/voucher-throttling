# voucher-throttling

A Python rate limiter that enforces cooldown periods for voucher distribution requests. Ensures fair access by allowing only one successful request per citizen within a specified cooldown window.

## Overview

This project implements a rate-limiting system for voucher distribution. A citizen can successfully redeem a voucher only once every `cooldown` seconds. Any requests that fall within the cooldown window are rejected, while rejected requests do not reset or extend the cooldown period.

**Key Assumption:** Input requests are assumed to be sorted by timestamp.

## Features

- ✅ Simple and efficient rate limiting algorithm
- ✅ Prevents voucher abuse through cooldown enforcement
- ✅ Rejected requests don't reset cooldowns
- ✅ Comprehensive test suite
- ✅ Minimal dependencies

## How It Works

### Algorithm

The rate limiter tracks the last approved request timestamp for each citizen. When a new request arrives:

1. If no previous approved request exists, the request is **approved**
2. If the request arrives within the cooldown window `[T, T + cooldown - 1]` (where T is the last approval time), it is **rejected**
3. If the request arrives after the cooldown window, it is **approved** and becomes the new reference point

### Example

```python
from rate_limiter import rejected_requests

requests = [[1, 10], [2, 11], [1, 12], [1, 15], [2, 15]]
result = rejected_requests(requests, cooldown=5)
print(result)  # Output: [1, 2]

# Timeline (cooldown=5):
# Citizen 1 @ t=10 ✓ approved
# Citizen 2 @ t=11 ✓ approved
# Citizen 1 @ t=12 ✗ rejected (within cooldown: 10 + 5 = 15)
# Citizen 1 @ t=15 ✓ approved (exactly at boundary)
# Citizen 2 @ t=15 ✗ rejected (within cooldown: 11 + 5 = 16)
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/azmiratania/voucher-throttling.git
cd voucher-throttling
```

2. Ensure you have Python 3.9+ installed:
```bash
python --version
```

## Usage

### Basic Usage

```python
from rate_limiter import rejected_requests

# Define requests as [citizen_id, timestamp]
requests = [
    [1, 10],
    [2, 11],
    [1, 12],
    [1, 15],
    [2, 15]
]

# Get list of rejected citizen IDs (default cooldown = 5)
rejected = rejected_requests(requests)
print(rejected)  # [1, 2]
```

### Custom Cooldown

```python
# Use a custom cooldown period (in seconds)
rejected = rejected_requests(requests, cooldown=10)
```

### Running the Example

```bash
python rate_limiter.py
```

## Testing

Run the test suite to verify the rate limiter:

```bash
python -m unittest test_rate_limiter.py
```

Or run directly:

```bash
python test_rate_limiter.py
```

### Test Coverage

The test suite includes:
- Basic functionality with the problem example
- Empty request list
- Multiple citizens requesting at the same time
- Boundary testing (exactly at cooldown boundary)
- Cooldown persistence (rejected requests don't reset)
- Same-timestamp requests
- Burst requests from a single citizen

## Time Complexity

- **Time:** O(n) where n is the number of requests
- **Space:** O(m) where m is the number of unique citizens

## Requirements

- Python 3.9 or higher
- No external dependencies

## Project Structure

```
voucher-throttling/
├── README.md                 # This file
├── rate_limiter.py          # Main rate limiter implementation
└── test_rate_limiter.py     # Unit tests
```

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests to improve this project.

## License

This project is open source and available under the MIT License.

## Contact

For questions or feedback, please open an issue on the [GitHub repository](https://github.com/azmiratania/voucher-throttling).
