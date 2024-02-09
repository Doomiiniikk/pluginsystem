## template module class
# from Doms import Doms


class Dom():

    def install(self):
        """tell the handler about myself, what I can do and how it should be done"""
        raise NotImplementedError

    def uninstall(self):
        """tell the handler about myself and that I am not working for it anymore"""
        raise NotImplementedError
    
    def teller(self):
        """talk to the handler, what it wants done and what I want in return"""
        raise NotImplementedError
    