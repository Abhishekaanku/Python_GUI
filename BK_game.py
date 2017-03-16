import cards,games,random
class BK_card(cards.Card):
    ranks=["7","8","9","10","J","Q","K","A"]
    def value(self):
        v=BK_card.ranks.index(self.rank)
        return v
class BK_deck(cards.Deck):
    def populate(self):
        for i in BK_card.ranks:
            for j in BK_card.suit:
                self.add(BK_card(i,j))
    def shuffle(self):
        random.shuffle(self.cards)
class BK_hand(cards.Hand):
    def __init__(self,name,point=0):
        super(BK_hand,self).__init__()
        self.name=name
        self.point=point
    def __str__(self):
        rep=self.name+"\t"+super(BK_hand,self).__str__()+"\t("+str(self.point)+")"
        return rep
class BK_player(BK_hand):
    def is_hit(self):
        ans=games.response("Are you ready to throw first? ")
        return ans
    def throw(self):
        print("Enter the card you want to throw from yor deck")
        s=input("Enter card suit: ")
        r=input("Enter card rank: ")
        card=BK_card(r,s)
        for i in self.cards:
            if str(i)==str(card):
                return i
class BK_auto(BK_hand):
    def move(self,card,suit):
        move=None
        moves=[]
        suit_move=[]
        for i in self.cards:
            if i.suit==card.suit:
                moves.append(i)
            if i.suit==suit:
                suit_move.append(i)
        if moves:
            for j in moves:
                if j.value()>card.value():
                    move=j
                    return move
            if not move:
                move=moves[0]
                for i in moves:
                    if move.value()>i.value():
                        move=i
                return move
        if not len(suit_move)==0:
            move=suit_move[0]
            for i in suit_move:
                if move.value()>i.value():
                    move=i
            return move
        if not move:
            move=self.cards[0]
            for i in self.cards:
                if move.value()>i.value():
                    move=i
            return move  
    def throw(self):
        th=self.cards[0]
        for i in self.cards:
            if th.value()<i.value():
                th=i
        return th
    def preferred_suit(self):
        for i in BK_card.suit:
            m=0
            for j in self.cards:
                if j.suit==i:
                    m+=1
            if m>=2:
                return i
class BK_game(object):
    def __init__(self,name):
        self.human=BK_player(name)
        self.comp=BK_auto("Computer")
        self.deck=BK_deck()
        self.deck.populate()
        self.deck.shuffle()
        self.box=BK_hand("Box")
    def play(self):
        turn=1
        hit=self.human.is_hit()
        if hit=="y":
            turn=0
            a=int(input("Enter the number from where you eant to cut the deck: "))
            self.deck.cut(num=a)
            self.deck.deal([self.human,self.comp],5)
            print(self.human)
            suit=input("Enter the preferred suit: ")
            print()
        else:
            turn=1
            a=random.randint(1,52)
            self.deck.cut(num=a)
            self.deck.deal([self.human,self.comp],5)
            suit=self.comp.preferred_suit()
            print("Preferred suit is ",suit)
            print()
        self.deck.deal([self.human,self.comp],11)
        for j in self.comp.cards:
            j.flip()
        print(self.human)
        print(self.comp)
        while self.human.cards:
            if turn==0:
                i=self.human.throw()
                j=self.comp.move(i,suit)
                j.flip()
                print("Computer's move: ",end="")
                print(j)
                self.human.give(i,self.box)
                self.comp.give(j,self.box)
                if i.suit==j.suit:
                    if i.value()>j.value():
                        self.human.point+=1
                    else:
                        self.comp.point+=1
                        turn=1
                else:
                    if j.suit==suit:
                        self.comp.point+=1
                        turn=1
                    else:
                        self.human.point+=1
                print(self.human)
                print(self.comp)
                print()
            elif turn==1:
                i=self.comp.throw()
                print("Computer's throw: ",end="")
                i.flip()
                print(i)
                j=self.human.throw()
                self.human.give(j,self.box)
                self.comp.give(i,self.box)
                if i.suit==j.suit:
                    if i.value()>j.value():
                        self.comp.point+=1
                    else:
                        self.human.point+=1
                        turn=0
                else:
                    if j.suit==suit:
                        self.human.point+=1
                        turn=0
                    else:
                        self.comp.point+=1
                print(self.human)
                print(self.comp)
                print()
        if self.human.point>self.comp.point:
            print(self.human.name,"Won the game")
        elif self.human.point<self.comp.point:
            print("Computer won the game")
        elif self.human.point==self.comp.point:
            print("TIE")
        self.box.clear()
def main():
    print("\tWelcome to the KingKong Game")
    name=input("Enter your name: ")
    print()
    again=None
    while again!="n":
        game=BK_game(name)
        game.play()
        again=games.response("Do you want to play again? ")
main()
input("\nPress Enter to EXIT")
    
    
                    
                    
                
                
                
                
            
            
        
        










        
                
                
        
                
    
