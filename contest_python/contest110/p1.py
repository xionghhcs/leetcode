class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        new_logs = [item.split()[1:] for item in logs]
        new_logs = [''.join(item) for item in new_logs]
        result0 = []
        result1 = []
        for idx, item in enumerate(new_logs):
            if item.isdigit() is False:
                result0.append(logs[idx])
            else:
                result1.append(logs[idx])
        result0.sort(reverse=False)
        return result0 + result1
