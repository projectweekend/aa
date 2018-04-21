
NAME = 'name'
ATTACK = 'attack'
DEFENSE = 'defense'
COST = 'cost'
MOVEMENT = 'movement'
BONUS = 'bonus'
TYPE = 'type'

LAND = 'land'
AIR = 'air'
SEA = 'sea'

INFANTRY = 'Infantry'
ARTILLERY = 'Artillery'
MECHANIZED_INFANTRY = 'Mechanized Infantry'
TANK = 'Tank'
FIGHTER = 'Fighter'
TACTICAL_BOMBER = 'Tactical Bomber'
STRATEGIC_BOMBER = 'Strategic Bomber'
AIRCRAFT_CARRIER = 'Aircraft Carrier'
BATTLESHIP = 'Battleship'
DESTROYER = 'Destroyer'
CRUISER = 'Cruiser'
SUBMARINE = 'Submarine'
TRANSPORT = 'Transport'

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

LAND_UNITS = (
    INFANTRY,
    ARTILLERY,
    MECHANIZED_INFANTRY,
    TANK
)
AIR_UNITS = (
    FIGHTER,
    TACTICAL_BOMBER,
    STRATEGIC_BOMBER
)
SEA_UNITS = (
    TRANSPORT,
    SUBMARINE,
    DESTROYER,
    CRUISER,
    AIRCRAFT_CARRIER,
    BATTLESHIP
)

UNIT_INFO = {
    INFANTRY: {
        NAME: INFANTRY,
        ATTACK: 1,
        DEFENSE: 2,
        COST: 3,
        MOVEMENT: 1,
        TYPE: LAND,
        BONUS: {}
    },
    ARTILLERY: {
        NAME: ARTILLERY,
        ATTACK: 2,
        DEFENSE: 2,
        COST: 4,
        MOVEMENT: 2,
        TYPE: LAND,
        BONUS: {
            INFANTRY: {
                ATTACK: 2
            },
            MECHANIZED_INFANTRY: {
                ATTACK: 2
            }
        }
    },
    MECHANIZED_INFANTRY: {
        NAME: MECHANIZED_INFANTRY,
        ATTACK: 1,
        DEFENSE: 2,
        COST: 4,
        MOVEMENT: 2,
        TYPE: LAND,
        BONUS: {}
    },
    TANK: {
        NAME: TANK,
        ATTACK: 3,
        DEFENSE: 3,
        COST: 6,
        MOVEMENT: 2,
        TYPE: LAND,
        BONUS: {
            TACTICAL_BOMBER: {
                ATTACK: 4
            }
        }
    },
    FIGHTER: {
        NAME: FIGHTER,
        ATTACK: 3,
        DEFENSE: 4,
        COST: 10,
        MOVEMENT: 4,
        TYPE: AIR,
        BONUS: {
            TACTICAL_BOMBER: {
                ATTACK: 4
            }
        }
    },
    TACTICAL_BOMBER: {
        NAME: TACTICAL_BOMBER,
        ATTACK: 3,
        DEFENSE: 3,
        COST: 11,
        MOVEMENT: 4,
        TYPE: AIR,
        BONUS: {}
    },
    STRATEGIC_BOMBER: {
        NAME: STRATEGIC_BOMBER,
        ATTACK: 4,
        DEFENSE: 1,
        COST: 12,
        MOVEMENT: 6,
        TYPE: AIR,
        BONUS: {}
    },
    AIRCRAFT_CARRIER: {
        NAME: AIRCRAFT_CARRIER,
        ATTACK: 0,
        DEFENSE: 2,
        COST: 16,
        MOVEMENT: 2,
        TYPE: SEA,
        BONUS: {}
    },
    BATTLESHIP: {
        NAME: BATTLESHIP,
        ATTACK: 4,
        DEFENSE: 4,
        COST: 20,
        MOVEMENT: 2,
        TYPE: SEA,
        BONUS: {}
    },
    DESTROYER: {
        NAME: DESTROYER,
        ATTACK: 2,
        DEFENSE: 2,
        COST: 8,
        MOVEMENT: 2,
        TYPE: SEA,
        BONUS: {}
    },
    CRUISER: {
        NAME: CRUISER,
        ATTACK: 3,
        DEFENSE: 3,
        COST: 12,
        MOVEMENT: 2,
        TYPE: SEA,
        BONUS: {}
    },
    SUBMARINE: {
        NAME: SUBMARINE,
        ATTACK: 2,
        DEFENSE: 1,
        COST: 6,
        MOVEMENT: 2,
        TYPE: SEA,
        BONUS: {}
    },
    TRANSPORT: {
        NAME: TRANSPORT,
        ATTACK: 0,
        DEFENSE: 0,
        COST: 7,
        MOVEMENT: 2,
        TYPE: SEA,
        BONUS: {}
    }
}
