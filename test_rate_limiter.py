import unittest

from rate_limiter import rejected_requests


class RejectedRequestsTest(unittest.TestCase):
    def test_problem_example(self):
        requests = [[1, 10], [2, 11], [1, 12], [1, 15], [2, 15]]
        self.assertEqual(rejected_requests(requests), [1, 2])

    def test_empty(self):
        self.assertEqual(rejected_requests([]), [])

    def test_all_first_requests_approved(self):
        self.assertEqual(rejected_requests([[1, 1], [2, 1], [3, 1]]), [])

    def test_reject_at_t_plus_4_allow_at_t_plus_5(self):
        self.assertEqual(rejected_requests([[1, 10], [1, 14]]), [1])
        self.assertEqual(rejected_requests([[1, 10], [1, 15]]), [])

    def test_rejected_request_does_not_reset_cooldown(self):
        requests = [[1, 10], [1, 12], [1, 14], [1, 15]]
        self.assertEqual(rejected_requests(requests), [1, 1])

    def test_same_timestamp_second_request_rejected(self):
        self.assertEqual(rejected_requests([[1, 10], [1, 10]]), [1])

    def test_burst_from_one_citizen(self):
        requests = [[7, 0], [7, 1], [7, 2], [7, 5], [7, 9]]
        self.assertEqual(rejected_requests(requests), [7, 7, 7])


if __name__ == "__main__":
    unittest.main()
