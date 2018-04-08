
ATTACK = 'attack'
DEFENSE = 'defense'
COST = 'cost'
MOVEMENT = 'movement'
BONUS = 'bonus'

INFANTRY = 'infantry'
ARTILLERY = 'artillery'
MECHANIZED_INFANTRY = 'mechanized_infantry'
TANK = 'tank'
FIGHTER = 'fighter'
TACTICAL_BOMBER = 'tactical_bomber'
STRATEGIC_BOMBER = 'strategic_bomber'
AIRCRAFT_CARRIER = 'aircraft_carrier'
BATTLESHIP = 'battleship'
DESTROYER = 'destroyer'
CRUISER = 'cruiser'
SUBMARINE = 'submarine'
TRANSPORT = 'transport'

UNIT_NAMES = (
    INFANTRY,
    ARTILLERY,
    MECHANIZED_INFANTRY,
    TANK,
    FIGHTER,
    TACTICAL_BOMBER,
    STRATEGIC_BOMBER,
    AIRCRAFT_CARRIER,
    BATTLESHIP,
    DESTROYER,
    CRUISER,
    SUBMARINE,
    TRANSPORT
)

UNIT_INFO = {
    INFANTRY: {
        ATTACK: 1,
        DEFENSE: 2,
        COST: 3,
        MOVEMENT: 1,
        BONUS: 'Attacks at 2 when supported by Artillery'
    },
    ARTILLERY: {
        ATTACK: 2,
        DEFENSE: 2,
        COST: 4,
        MOVEMENT: 2,
        BONUS: 'Supports Infantry and Mechanized Infantry'
    },
    MECHANIZED_INFANTRY: {
        ATTACK: 1,
        DEFENSE: 2,
        COST: 4,
        MOVEMENT: 2,
        BONUS: 'Attacks at 2 when supported by Artillery'
    },
    TANK: {
        ATTACK: 3,
        DEFENSE: 3,
        COST: 6,
        MOVEMENT: 2,
        BONUS: 'Supports Tactical Bomber'
    },
    FIGHTER: {
        ATTACK: 3,
        DEFENSE: 4,
        COST: 10,
        MOVEMENT: 4,
        BONUS: 'Supports Tactical Bomber'
    },
    TACTICAL_BOMBER: {
        ATTACK: 3,
        DEFENSE: 3,
        COST: 11,
        MOVEMENT: 4,
        BONUS: 'Attacks at 4 when supported by Fighter or Tank'
    },
    STRATEGIC_BOMBER: {
        ATTACK: 4,
        DEFENSE: 1,
        COST: 12,
        MOVEMENT: 6,
        BONUS: ''
    },
    AIRCRAFT_CARRIER: {
        ATTACK: 0,
        DEFENSE: 2,
        COST: 16,
        MOVEMENT: 2,
        BONUS: ''
    },
    BATTLESHIP: {
        ATTACK: 4,
        DEFENSE: 4,
        COST: 20,
        MOVEMENT: 2,
        BONUS: ''
    },
    DESTROYER: {
        ATTACK: 2,
        DEFENSE: 2,
        COST: 8,
        MOVEMENT: 2,
        BONUS: ''
    },
    CRUISER: {
        ATTACK: 3,
        DEFENSE: 3,
        COST: 12,
        MOVEMENT: 2,
        BONUS: ''
    },
    SUBMARINE: {
        ATTACK: 2,
        DEFENSE: 1,
        COST: 6,
        MOVEMENT: 2,
        BONUS: ''
    }
}
