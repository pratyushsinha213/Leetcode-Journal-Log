class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        max_len = 0
        peaks = []

        for i in range(len(arr)-2):
            if arr[i] < arr[i+1] > arr[i+2]:
                peaks.append((i+1, arr[i+1]))

        for peak in peaks:
            p_idx = peak[0]
            left_count = right_count = 0
            for left in range(p_idx-1, 0, -1):
                if arr[left] > arr[left-1]:
                    left_count += 1
                else:
                    break
            left_count += 1
            for right in range(p_idx+1, len(arr)-1):
                if arr[right] > arr[right+1]:
                    right_count += 1
                else:
                    break
            right_count += 1
            max_len = max(max_len, 1+left_count+right_count)

        return max_len