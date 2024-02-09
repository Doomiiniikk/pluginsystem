

class Domlogger():

    def __init__(self) -> None:
        
        
        ### Unsure how to define this
        self.esc : str = 0x1b
        self.red : str = 0x1f
        self.green : str = 0x20
        self.yellow : str = 0x21
        self.blue : str = 0x22
        self.white : str = 0x0 
        self.reset : str = 0x0
        
        pass

    def out(self, msg : str, logType : str = "Info") -> None:
        
        
        self.Info(msg=f"Did you know you can run a function named DomLogger.{logType}() to print instead of DomLogger.out()")
        match logType:
            case "Info":
                self.Info(msg=msg)
            case "Warn":
                self.Warn(msg=msg)
            case "Error":
                self.Error(msg=msg)
                
        

        pass
    def __format(self): # break up an incoming string to apply formatting
        
        pass

    def LogInfo(self, msg) -> None:
        infoMessage = f"\033[{self.blue}m[I]\033[{self.reset}m > {msg}"
        print(infoMessage)
    
    def LogWarn(self, msg) -> None:
        warnMessage = f"\033[{self.yellow}m[W]\033[{self.reset}m > {msg}"
        print(warnMessage)
    
    def LogError(self, msg) -> None:
        errorMessage = f"\033[{self.red}m[E]\033[{self.reset}m > {msg}"
        print(errorMessage)

if __name__ == "__main__":
    dL = Domlogger()

    dL.out("TEST", "Warn")