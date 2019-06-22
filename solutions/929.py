"""
Solution for Algorithms #929: Unique Email Addresses

- N: Length of `emails`
- K: Number of unique emails
- L: Maximum length of an email
- Space Complexity: O(KL)
- Time Complexity: O(NL)

Runtime: 44 ms, faster than 91.43% of Python3 online submissions for Unique Email Addresses.
Memory Usage: 13.2 MB, less than 41.43% of Python3 online submissions for Unique Email Addresses.
"""
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = {}

        for email in emails:
            local, domain = email.split('@')
            parsed_email = local.split('+')[0].replace('.', '') + '@' + domain
            unique_emails[parsed_email] = True

        return len(unique_emails.keys())
