import hashlib
class Block(): 
    def __init__(self, data, previous_hash):
        self.hash = hashlib.sha256()
        self.nounce = 0
        self.data = data
        self.previous_hash = previous_hash
    def mine(self, difficulty):
        #SEARCHED FOR THE NOUNCE THAT MATCHS THE HASH WHICH CORRESPONDS TO THE DATA
        self.hash.update(str(self).encode('utf-8'))
        while int(self.hash.hexdigest(), 16) > 2**(256 - difficulty):
            self.nounce += 1
            self.hash.update(str(self).encode('utf-8'))


    def __str__(self):
        return "{}{}{}".format(self.previous_hash.hexdigest(),self.data, self.nounce,)    
   