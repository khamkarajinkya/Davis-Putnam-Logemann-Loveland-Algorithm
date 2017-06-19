import itertools

class Solver:
    def __init__(self, cnf):
        cnf_l = list(cnf)
        self.cnf=[]
        for item in cnf_l:
            if item not in self.cnf:
                self.cnf.append(list(item))
        self.literals = []
        for item in  self.cnf:
            for i in item:
                if i not in self.literals:
                    self.literals.append(i)

    def solve(self):
        return self.dpll(self.cnf,self.literals)
        
    def dpll(self,cnf,l):
        for item in cnf:
            if len(item)==1:
                cnf,l=self.unit_p(cnf,l)
        if [] in cnf:
            return False
        if not cnf:
            return True
        s=l
        t=self.most_common(cnf)
        cnf1=cnf
        if t in s:
            s.remove(t)
        r1=self.reduced(cnf,t)
        r2=self.reduced(cnf1,-t)
        return(self.dpll(r1,s) or self.dpll(r2,s))
    
    def unit_p(self,cnf,l):
        t1=0
        temp=[]
        t=cnf
        s=l
        for item in t:
            if len(item)==1:
                t1=item[0]
        for item in t:
            if t1 in item:
                temp.append(item)
        if len(temp)>0:
            t=[x for x in t if x not in temp]
        for item in cnf:
            if (t1*-1) in item:
                temp=[]
                t.remove(item)
                t.append([x for x in item if x != -t1])
        if t1 in s:
            s.remove(t1)
        if -t1 in s:
            s.remove(-t1)
        return t,s
        
    def reduced (self,cnf,v):
        temp=[]
        t=cnf
        for item in t:
            if v in item:
                temp.append(item)
        if len(temp)>0:
            t=[x for x in t if x not in temp]
        for item in cnf:
            if (v*-1) in item:
                temp=[]
                t.remove(item)
                t.append([x for x in item if x != -v])
        #print ("After Reduced",len(self.cnf_l),"\n",cnf)
        return t
        
    
    def most_common(self,lst):
        merged = list(itertools.chain(*lst))      #most frequent item
        if len(merged)>0:
            return max(set(merged), key=merged.count)
        else:
            self.ou=True     #length of senetence is 0
