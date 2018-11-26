class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        new_emails  = list()
        for e in emails:
            e_list = e.split('@')
            e_0 = e_list[0].replae('.', '')
            pos = e_0.find('+')
            if pos != -1:
                e_0 = e_0[:pos]
            new_emails.append(e_0 + e_list[-1])
        return len(set(new_emails))