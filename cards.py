import random
class Card(object):
    ranks=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    suit=["C","D","S","H"]
    def __init__(self,rank,suit,is_card_up=True):
        self.rank=rank
        self.suit=suit
        self.card_face=is_card_up
    def __str__(self):
        if self.card_face:
            rep=self.rank+self.suit
            return rep
        else:
            return "XX"
    def flip(self):
        self.card_face=not self.card_face
class Hand(object):
    def __init__(self):
        self.cards=[]
    def __str__(self):
        if self.cards:
            rep=""
            for i in self.cards:
                rep+=str(i)+" "
            return rep
        else:
            return "EMPTY"
    def clear(self):
        self.cards=[]
    def add(self,card):
        self.cards.append(card)
    def shuffle(self):
        random.shuffle(self.cards)
    def __delete(self,card):
        if card in self.cards:
            self.cards.remove(card)
        else:
            print("This card is not present in the hand")
    def give(self,card,friend):
        friend.add(card)
        self.__delete(card)
class Deck(Hand):
    def populate(self):
        for i in Card.rank:
            for j in Card.suit:
                self.add(Card(i,j))
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self,hands,per_hand=1):
        for i in range(per_hand):
            for j in hands:
                if self.cards:
                    self.give(self.cards[0],j)
                else:
                    print("Out of card")
    def cut(self,num):
        self.cards=self.cards[num:]+self.cards[:num]
if __name__=="__main__":
    print("You are running this program directly.This program is supposed to act as module for supporting other programs.")
input("Press enter to continue")


