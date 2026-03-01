import abc
class ScoreGroup(abc.ABC):
    def __init__(self, desc="ScoreGrp"):
        self.desc = desc
    
    def get_desc(self):
        return self.desc
    
    @abc.abstractmethod
    def get_score(self):
        pass
    
    @abc.abstractmethod
    def get_full(self):
        pass
    
class LeafGroup(ScoreGroup):
    def __init__(self, desc="ScoreGrp"):
        super().__init__(desc)

class FixedLeafGroup(LeafGroup):
    def __init__(self, desc="LeafGrp", score=1, status=False):
        super().__init__(desc)
        self.score = score
        self.status = status
    def get_score(self):
        return self.score if self.status else 0
    
    def get_full(self):
        return self.score
    
    def get_status(self):
        return self.status

    def set_status(self, s:bool):
        self.status = s
        
class MercifulLeafGroup(LeafGroup):
    def __init__(self, desc="LeafGrp", status=False):
        super().__init__(desc)
        score = 0
        self.score = score
        self.status = status
    def get_score(self):
        return self.score if self.status else 0
    
    def get_full(self):
        return self.score
    
    def get_status(self):
        return self.status

    def set_status(self, s:bool):
        self.status = s
    
class MutableLeafGroup(LeafGroup):
    def __init__(self, desc="LeafGrp", score_max=1, score_min=0, initial = 0):
        super().__init__(desc)
        self.score_max = score_max
        self.score_min = score_min
        self.score=initial
        assert score_max >= score_min and score_min <= initial and score_max >= initial, "Range is wrong!"
        
    def get_score(self):
        return max(self.score_min, min(self.score_max,self.score))
    
    def set_score(self,score):
        self.score = max(self.score_min, min(self.score_max,score))
        
    def get_range(self):
        return self.score_min, self.score_max
    
    def get_full(self):
        return self.score_max
    

class SummaryGroup(ScoreGroup):
    def __init__(self, desc="ScoreGrp",  subgroups: list[ScoreGroup]=[],maximum=5, minimum=0):
        assert maximum >= minimum, "Maximum must be greater than minimum! ✍️✍️✍️✍️✍️"
        super().__init__(desc)
        self.subgroups = subgroups
        self.maximum = maximum
        self.minimum = minimum
    def get_maximum(self):
        return self.maximum
    def get_minimum(self):
        return self.minimum
    def get_full(self):
        return self.get_maximum()

class AverageGroup(SummaryGroup):
    def __init__(self, desc="ScoreGrp", subgroups: list[ScoreGroup]=[], maximum = 5, minimum=0,basic_score=0):
        super().__init__(desc,subgroups,maximum, minimum)
        self.basic_score = basic_score
    def get_score(self):
        all_sco = self.basic_score
        for g in self.subgroups:
            all_sco += g.get_score()
        return min(max(all_sco / len(self.subgroups), self.minimum), self.maximum)

class AddGroup(SummaryGroup):
    def __init__(self, desc="ScoreGrp", subgroups: list[ScoreGroup]=[], maximum = 5, minimum=0,basic_score=0):
        super().__init__(desc,subgroups,maximum, minimum)
        self.basic_score = basic_score
    def get_score(self):
        all_sco = self.basic_score
        for g in self.subgroups:
            all_sco += g.get_score()
        return min(max(all_sco, self.minimum), self.maximum)
    
def generate_report(tree: ScoreGroup, addon:str):
    res = ""
    def _inner_generate_report(t: ScoreGroup, level:int):
        nonlocal res
        score = t.get_score()
        if abs(score - 0) < 1e-10 and isinstance(t, LeafGroup) and (not isinstance(t, MercifulLeafGroup) or not t.get_status()): return
        reportstr = '\t'*level + "{} ({:.2f})".format(t.get_desc(), score) + '\n'
        res += reportstr
        if isinstance(t, SummaryGroup):
            for k in t.subgroups:
                _inner_generate_report(k, level+1)
    _inner_generate_report(tree, 0)
    res = res + "\n" + addon
    return res
        