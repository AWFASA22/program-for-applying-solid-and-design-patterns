class Card:
    def __init__(self,cardnumber, expire_date,cvv):

        self._cardnumber = cardnumber
        self._expire_date = expire_date
        self._cvv = cvv

    
        # getter method 
    def get_cardnumber(self): 
        return self._cardnumber
    
    def get_expire_date(self): 
        return self._expire_date 
      
    def get_cvv(self): 
        return self._cvv
      
    # setter method 
    def set_cardnumber(self, x): 
        self._cardnumber = x 

    def set_cvv(self, x): 
        self._cvv = x 
    
    # setter method 
    def set_cvv(self, x): 
        self._expire_date = x 
    

    

