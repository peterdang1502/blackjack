from deck import Deck
from player import Player
from dealer import Dealer

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def deal_cards(self):
        for i in range(2):
            self.player.receive_card(self.deck.draw_card())
            self.dealer.receive_card(self.deck.draw_card())

if __name__ == '__main__':
    game = Game()
    game.deal_cards()
    game.player.print_cards()
    game.dealer.print_cards()