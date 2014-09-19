import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

P2P_PREFIX = 'fbc0b6db'.decode('hex')
P2P_PORT = 11036
ADDRESS_VERSION = 38
RPC_PORT = 21036
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'greencoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: __import__('gre_subsidy').GetBlockBaseValue(height),
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 63 # s
SYMBOL = 'GRE'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'greencoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/greencoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.greencoin'), 'greencoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://fst.webboise.com/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://fst.webboise.com/address/'
TX_EXPLORER_URL_PREFIX = 'http://fst.webboise.com/tx/'
SANE_TARGET_RANGE = (2**256//100000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 1e8,
CHARITY_ADDRESS='AD3325CA903AC90A5D936358C1C34609A030DFEB'.decode('hex')
