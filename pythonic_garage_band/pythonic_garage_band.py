from abc import abstractmethod

class Band():

    bands = []
    def __init__(self,name,members):
        '''
        this method take a name.
        '''
        self.name=name
        self.members=members
        Band.bands.append(self)
        
    def __str__(self):
        '''
        this method control how the output would be.
        '''
        return f" this band call {self.name}"

    def __repr__(self):
        '''
        this method control how the instance would be represented.
        '''
        return f"{self.name}"

    def play_solos(self):
        result=''
        for i in self.members:
            result+=f"this is {i}, i am a {i.play_solo()}\n"
        return result
        

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
    def play_solo(cls):
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
        return f"{self.name}"

    def __repr__(self):
        '''
        this method control how to represent the instance.
        '''
        return f"{self.name}"

    def get_instrument():
        '''
        this method return a string of instrument name.
        '''
        return "my instrument is guitar"

    def play_solo(cls):
        '''
        this method return a string of playing solo ability.
        '''
        return "guitarist"

    

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
        return f"{self.name}"

    def __repr__(self):
        '''
        this method control how to represent the instance.
        '''
        return f"{self.name}"

    def get_instrument():
        '''
        this method return a string of instrument name.
        '''
        return "my instrument is bass"

    def play_solo(cls):
        '''
        this method return a string of playing solo ability.
        '''
        return "bassist"

    

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
        return f"{self.name}"

    def __repr__(self):
        '''
        this method control how to represent the instance.
        '''
        return f"{self.name}"

    def get_instrument(cli):
        '''
        this method return a string of instrument name.
        '''
        return "my instrument is drum"

    def play_solo(cli):
        '''
        this method return a string of playing solo ability.
        '''
        return "drummer"



if __name__ == "__main__":
    jhon=Drummer('jhon')
    salma=Guitarist('salma')
    leo=Bassist('leo')
    
    metal=Band('metal',[jhon,salma,leo])

    print(metal.play_solos())