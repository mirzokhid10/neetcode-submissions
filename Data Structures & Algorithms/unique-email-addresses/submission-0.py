class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique=set()
        # local=""
        # domain=""
        for i in range(len(emails)):
            local=emails[i].split('@')[0]
            local=local.split('+')[0]
            local=local.replace('.', '')
            domain=emails[i].split('@')[-1]
            valid_email=local+"@"+domain
            unique.add(valid_email)
            
        return len(unique)