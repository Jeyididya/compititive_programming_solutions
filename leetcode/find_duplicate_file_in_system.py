class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        di={}
        fl=False
        for i in paths:
            dir_ = i.split()
            for j in dir_[1:]:
                fl = j.split("(")
                content = fl[1][:-1]
                fil = fl[0][:-1]
                if content in  di:
                    ss=dir_[0]+"/"+fil
                    di[content].append(ss+"t")
                    fl=True
                else:
                    di[content]=[dir_[0]+"/"+fil+"t"]
                    
        an =[di[i] for i in di if len(di[i]) >1]
        if not fl:
            return []
        return an
        