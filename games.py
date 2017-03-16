class Game:
    def _init_(self,name,score):
        self.name=name
        self.score=score
    def _str_(self):
        rep=self.name+"\t:\t"+str(self.score)
        return rep
def response(question):
        response=None
        while response not in ("y","n"):
            response=input(question).lower()
        return response
def respond(question,low,high):
        response=None
        while response not in range(low,high):
            response=int(input(question))
        return response
if __name__=="__main__":
    print("You are running this program directly.This program is supposed to act as module for supporting other programs.")
input("Press enter to continue")
            
