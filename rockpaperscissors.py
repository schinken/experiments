__author__ = 'schinken'

import random
import collections
import operator

SCISSOR  = 'scissor'
PAPER    = 'paper'
ROCK     = 'rock'
WELL     = 'well'
LIZARD   = 'lizard'
SPOCK    = 'spock'

rock_paper_scissor = {
    SCISSOR: ( PAPER ),
    PAPER  : ( ROCK ),
    ROCK   : ( SCISSOR ),
}

rock_paper_scissor_well = {
    SCISSOR: ( PAPER ),
    PAPER  : ( ROCK ),
    ROCK   : ( SCISSOR ),
    WELL   : ( SCISSOR, ROCK )
}

# BIG BANG THEORY - ROCK PAPER SCISSOR LIZARD SPOCK

rock_paper_scissor_lizard_spock = {
    SCISSOR: ( PAPER,   LIZARD  ), # Scissors cut paper,     Scissors decapitate lizard
    PAPER  : ( ROCK,    SPOCK   ), # Paper covers rock,      Paper disproves Spock
    ROCK   : ( LIZARD,  SCISSOR ), # Rock crushes lizard,    Rock crushes scissors
    LIZARD : ( SPOCK,   PAPER   ), # Lizard poisons Spock,   Lizard eats paper
    SPOCK  : ( SCISSOR, ROCK    ), # Spock smashes scissors, Spock vaporizes rock
}

class Fight:

    arsenal = None

    def __init__(self, arsenal):
        self.arsenal = arsenal

    def fight( self, weapon1, weapon2 ):
        if weapon2 in self.arsenal[ weapon1 ]:
            return True
        else:
            return False

    def pickRandomWeapon( self, filter=None ):

        choice = random.choice( self.arsenal.keys() )

        if filter:
            while filter is choice:
                choice = random.choice( self.arsenal.keys() )

        return choice


def main( runs=1000 ):

    statistics = collections.Counter()
    wins = 0

    fightGame = Fight( rock_paper_scissor_lizard_spock )

    for i in range( runs ):

        weapon1 = fightGame.pickRandomWeapon()
        weapon2 = fightGame.pickRandomWeapon( weapon1 )


        if fightGame.fight( weapon1, weapon2 ):
            print weapon1, "wins over", weapon2

            if weapon1 not in statistics:
                statistics[ weapon1 ] = collections.Counter()

            statistics[ weapon1 ][ weapon2 ] += 1
            wins += 1

        else:
            print weapon1, "fails over", weapon2


    print "="*30
    print "Ran",runs, "tests:"
    print "="*30

    for weapon1 in statistics:
        sum = reduce( operator.add, statistics[ weapon1 ].values() )
        print weapon1, "win probability is", ( float(sum)/float(wins) )*100


if __name__ == "__main__":
    main( 100000 )