from abc import abstractmethod

class Band():

    bands = []
    def __init__(self,name):
        '''
        this method take a name.
        '''
        self.name=name
        Band.bands.append(self)
        
    def __str__(self):
        '''
        this method control how the output would be.
        '''
        return f"this is {self.name}"

    def __repr__(self):
        '''
        this method control how the instance would be represented.
        '''
       return f"{self.name}"

    @classmethod
    def to_list(cls):
        return cls.bands

class Musician():

    def __init__(self,name):
        pass

    @abstractmethod
    def get_instrument():
        '''
        this get_instrument method let every sub class have get_instrument method.
        '''
        pass

    @abstractmethod
    def play_solo():
        '''
        this play_solo method let every sub class have play_solo method.
        '''
        pass

class Guitarist(Musician):

    def __init__(self,name):
        '''
        this method take a name.
        '''
        self.name=name

    def __str__(self):
        '''
        this method control how the output will looklike.
        '''
        return f"this is {self.name}"

    def __repr__(self):
        '''
        this method control how to represent the instance.
        '''
       return f"(this is {self.name})"

    def get_instrument():
        '''
        this method return a string of instrument name.
        '''
        return "my instrument is guitar"

    def play_solo():
        '''
        this method return a string of playing solo ability.
        '''
        return "i could play solo"

    

class Bassist(Musician):

    def __init__(self,name):
        '''
        this method take a name.
        '''
        self.name=name

    def __str__(self):
        '''
        this method control how the output will looklike.
        '''
        return f"this is {self.name}"

    def __repr__(self):
        '''
        this method control how to represent the instance.
        '''
       return f"(this is {self.name})"

    def get_instrument():
        '''
        this method return a string of instrument name.
        '''
        return "my instrument is bass"

    def play_solo():
        '''
        this method return a string of playing solo ability.
        '''
        return "i couldn't play solo"

    

class Drummer(Musician):

    def __init__(self,name):
        '''
        this method take a name.
        '''
        self.name=name

    def __str__(self):
        '''
        this method control how the output will looklike.
        '''
        return f"this is {self.name}"

    def __repr__(self):
        '''
        this method control how to represent the instance.
        '''
       return f"(this is {self.name})"

    def get_instrument(cli):
        '''
        this method return a string of instrument name.
        '''
        return "my instrument is drum"

    def play_solo(cli):
        '''
        this method return a string of playing solo ability.
        '''
        return "i could play solo"



if __name__ == "__main__":
    jhon=Drummer('jhon')
    print(jhon.play_solo())
    metal=Band('metal')
    rab=Band('rab')
    rock=Band('rock')
    print(rab.to_list())