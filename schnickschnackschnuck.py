__author__ = 'schinken'

import random
import collections
import operator

SCISSOR  = 'scissor'
PAPER    = 'paper'
ROCK     = 'rock'
WELL     = 'well'

beats = {
    SCISSOR: ( PAPER ),
    PAPER  : ( ROCK ),
    ROCK   : ( SCISSOR ),
    WELL   : ( SCISSOR, ROCK )
}


def fight( weapon1, weapon2 ):
    if weapon2 in beats[ weapon1 ]:
        return True
    else:
        return False

def pickRandomWeapon( filter=None ):

    choice = random.choice( beats.keys() )

    if filter:
        while filter is choice:
            choice = random.choice( beats.keys() )

    return choice


def main( runs=1000 ):

    statistics = collections.Counter()
    wins = 0

    for i in range( runs ):

        weapon1 = pickRandomWeapon()
        weapon2 = pickRandomWeapon( weapon1 )


        if fight( weapon1, weapon2 ):
            print weapon1, "wins over", weapon2

            if weapon1 not in statistics:
                statistics[ weapon1 ] = collections.Counter()

            statistics[ weapon1 ][ weapon2 ] += 1
            wins += 1

        else:
            print weapon1, "fails over", weapon2


    for weapon1 in statistics:
        sum = reduce( operator.add, statistics[ weapon1 ].values() )
        print weapon1, "win probability is", ( float(sum)/float(wins) )*100

    print statistics

if __name__ == "__main__":
    main( 10000 )