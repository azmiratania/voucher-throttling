import unittest

from voucher_throttling import rejected_citizen_ids


class VoucherThrottlingTests(unittest.TestCase):
    def test_example_scenario(self):
        requests = [[1, 10], [2, 11], [1, 12], [1, 15], [2, 15]]
        self.assertEqual(rejected_citizen_ids(requests), [1, 2])

    def test_rejected_request_does_not_extend_cooldown(self):
        requests = [[42, 7], [42, 8], [42, 12]]
        self.assertEqual(rejected_citizen_ids(requests), [42])

    def test_boundary_at_five_seconds_is_allowed(self):
        requests = [[5, 100], [5, 104], [5, 105], [5, 106]]
        self.assertEqual(rejected_citizen_ids(requests), [5, 5])


if __name__ == "__main__":
    unittest.main()
