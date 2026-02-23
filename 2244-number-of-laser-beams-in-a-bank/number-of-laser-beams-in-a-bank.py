class Solution:
    def numberOfBeams(self, bank):
        prev_devices = 0
        total_beams = 0

        for row in bank:
            # Count number of security devices in current row
            curr_devices = row.count('1')

            # If current row has devices
            if curr_devices > 0:
                # Multiply with previous non-zero row
                total_beams += prev_devices * curr_devices
                # Update previous device count
                prev_devices = curr_devices

        return total_beams


# Example usage:
bank1 = ["011001","000000","010100","001000"]
bank2 = ["000","111","000"]

sol = Solution()
print(sol.numberOfBeams(bank1))  # Output: 8
print(sol.numberOfBeams(bank2))  # Output: 0