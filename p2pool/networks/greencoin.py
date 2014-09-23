from p2pool.bitcoin import networks

PARENT = networks.nets['greencoin'] 
SHARE_PERIOD = 10 # seconds 
CHAIN_LENGTH = 24*60*60//10 # shares 
REAL_CHAIN_LENGTH = 24*60*60//10 # shares 
TARGET_LOOKBEHIND = 200 # shares 
SPREAD = 30 # blocks 
IDENTIFIER='a135b7d5b8c9923411'.decode('hex')
PREFIX='72108cea5fef629121'.decode('hex')
P2P_PORT = 23661 
MIN_TARGET = 0 
MAX_TARGET = 2**256//2**20 - 1 
PERSIST = False 
WORKER_PORT = 3333 
BOOTSTRAP_ADDRS = ''.split(' ') 
ANNOUNCE_CHANNEL = '#greencoin' 
VERSION_CHECK = lambda v: True 
VERSION_WARNING = lambda v: 'Upgrade greencoin to >= 0.8.5.1!' if v < 70002 else None
