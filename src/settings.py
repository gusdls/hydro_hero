TILE_SIZE = 32

SCREEN_WIDTH = 1240
SCREEN_HEIGHT = TILE_SIZE * 25

FPS = 60

BLACK = '#000000'
WHITE = '#ffffff'
GRAY = '#d3d3d3'
WATER_COLOR = '#0096ff'

BG_COLOR = '#808080'
BORDER_COLOR = '#111111'
WATER_STATUS_COLOR = '#0000ff'

enemies_data = {
    '1': {
        'name': 'bear',
        'size': (150, 150),
        'speed': 3,
        'notice_radius': 300
    },
    '2': {
        'name': 'beetle',
        'size': (100, 100),
        'speed': 3,
        'notice_radius': 300
    },
    '3': {
        'name': 'dog',
        'size': (100, 100),
        'speed': 5,
        'notice_radius': 300
    },
    '4': {
        'name': 'eagle',
        'size': (110, 110),
        'speed': 5,
        'notice_radius': 300
    },
    '5': {
        'name': 'vulture',
        'size': (100, 100),
        'speed': 4,
        'notice_radius': 300
    }
}