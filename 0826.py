class Student() :
    def __init__(self, name = "", age = 0, semester = 0) :
        self.name = name
        self.age = age
        self.semester = semester
    def __str__(self) :
        text = f"이름 : {self.name}\n나이 : {self.age}\n학기 : {self.semester}"
        return(text)
    
class RPS() :
    import random
    
    def __init__(self, action_space = []) :
        self.action_space = action_space
        self.actions = []
    
    def act(self) :
        lenth = len(self.action_space)
        self.actions.append(self.action_space[random.randint(0, lenth-1)])
    
    def __repr__(self) :
        txt = f"낼 수 있는 패 : {self.action_space}\n기록 : {self.actions}"
        return txt