class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        ages = 0

        for i in details:
            if int(i[11:13]) > 60:
                ages +=1
        return ages