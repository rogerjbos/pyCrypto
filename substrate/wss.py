import pandas as pd
import json
import random

def get_wss(chain):
  try:
    df = pd.DataFrame(WSS_ENDPOINTS[chain.lower()])
    return [df[random.choice(list(df))][0], df.size]
  except:
    return None

# https://paritytech.github.io/polkadot_network_directory/registry.json
# import json
# import urllib.request  # the lib that handles the url stuff
# data = urllib.request.urlopen('https://paritytech.github.io/polkadot_network_directory/registry.json') # it's a file like object and works just like a file
# w = json.load(data)
# data.close()
# for k in w['rpc_endpoints'].keys():
#   print(f"{k} has endpoints: {w['rpc_endpoints'][k]}")

# Define wss endpoints in JSON
wss_json = """{
   "acala": [
    {
      "Acala Foundation 0": "wss://acala-rpc-0.aca-api.network",
      "Acala Foundation 1": "wss://acala-rpc-1.aca-api.network",
      "Acala Foundation 3": "wss://acala-rpc-3.aca-api.network/ws",
      "Polkawallet 0": "wss://acala.polkawallet.io",
      "OnFinality": "wss://acala-polkadot.api.onfinality.io/public-ws",
      "Dwellir": "wss://acala-rpc.dwellir.com",
      "Automata 1RPC": "wss://1rpc.io/aca"
    }
  ],
   "ajuna": [
    {
      "AjunaNetwork": "wss://rpc-parachain.ajuna.network"
    }
  ],
   "odyssey": [
    {
      "AresProtocol": "wss://wss.odyssey.aresprotocol.io"
    }
  ],
   "astar": [
    {
      "Astar": "wss://rpc.astar.network",
      "Blast": "wss://astar.public.blastapi.io",
      "Dwellir": "wss://astar-rpc.dwellir.com",
      "OnFinality": "wss://astar.api.onfinality.io/public-ws",
      "RadiumBlock": "wss://astar.public.curie.radiumblock.co/ws",
      "Pinknode": "wss://public-rpc.pinknode.io/astar",
      "Automata 1RPC": "wss://1rpc.io/astr"
    }
  ],
   "bifrost-ksm": [
    {
      "Liebi": "wss://hk.p.bifrost-rpc.liebi.com/ws",
      "OnFinality": "wss://bifrost-polkadot.api.onfinality.io/public-ws"
    }
  ],
   "bitgreen": [
    {
      "Bitgreen": "wss://mainnet.bitgreen.org"
    }
  ],
   "centrifuge": [
    {
      "Centrifuge": "wss://fullnode.parachain.centrifuge.io",
      "OnFinality": "wss://centrifuge-parachain.api.onfinality.io/public-ws"
    }
  ],
   "clover": [
    {
      "Clover": "wss://rpc-para.clover.finance"
    }
  ],
   "coinversation": [
    {
      "Coinversation": "wss://rpc.coinversation.io/"
    }
  ],
   "composable": [
    {
      "Composable": "wss://rpc.composable.finance"
    }
  ],
   "crustParachain": [
    {
      "Crust": "wss://rpc.crust.network"
    }
  ],
   "darwinia": [
    {
      "Darwinia Network": "wss://parachain-rpc.darwinia.network"
    }
  ],
   "efinity": [
    {
      "Efinity": "wss://rpc.efinity.io",
      "Dwellir": "wss://efinity-rpc.dwellir.com",
      "OnFinality": "wss://efinity.api.onfinality.io/public-ws"
    }
  ],
   "equilibrium": [
    {
      "Equilibrium": "wss://node.pol.equilibrium.io/",
      "Dwellir": "wss://equilibrium-rpc.dwellir.com"
    }
  ],
   "frequency": [
    {
      "Frequency 0": "wss://0.rpc.frequency.xyz",
      "Frequency 1": "wss://1.rpc.frequency.xyz"
    }
  ],
   "geminis": [
    {
      "Geminis": "wss://rpc.geminis.network"
    }
  ],
   "hashed": [
    {
      "Hashed Systems": "wss://c1.hashed.network"
    }
  ],
   "hydradx": [
    {
      "Galactic Council": "wss://rpc.hydradx.cloud",
      "Dwellir": "wss://hydradx-rpc.dwellir.com"
    }
  ],
   "integritee-shell": [
    {
      "Integritee": "wss://polkadot.api.integritee.network"
    }
  ],
   "interlay": [
    {
      "Kintsugi Labs": "wss://api.interlay.io/parachain",
      "OnFinality": "wss://interlay.api.onfinality.io/public-ws"
    }
  ],
   "kapex": [
    {
      "Totem": "wss://k-ui.kapex.network"
    }
  ],
   "kilt": [
    {
      "KILT Protocol": "wss://spiritnet.kilt.io/",
      "OnFinality": "wss://spiritnet.api.onfinality.io/public-ws",
      "Dwellir": "wss://kilt-rpc.dwellir.com"
    }
  ],
   "kylin": [
    {
      "Kylin Network": "wss://polkadot.kylin-node.co.uk"
    }
  ],
   "litentry": [
    {
      "Litentry": "wss://rpc.litentry-parachain.litentry.io",
      "Dwellir": "wss://litentry-rpc.dwellir.com"
    }
  ],
   "manta": [
    {
      "Manta Kuhlii": "wss://kuhlii.manta.systems",
      "Manta Munkiana": "wss://munkiana.manta.systems",
      "Manta Pectinata": "wss://pectinata.manta.systems"
    }
  ],
   "moonbeam": [
    {
      "Moonbeam Foundation": "wss://wss.api.moonbeam.network",
      "Blast": "wss://moonbeam.public.blastapi.io",
      "OnFinality": "wss://moonbeam.api.onfinality.io/public-ws",
      "Pinknode": "wss://public-rpc.pinknode.io/moonbeam",
      "Automata 1RPC": "wss://1rpc.io/glmr",
      "Dwellir": "wss://moonbeam-rpc.dwellir.com"
    }
  ],
   "nodle": [
    {
      "OnFinality": "wss://nodle-parachain.api.onfinality.io/public-ws",
      "Dwellir": "wss://eden-rpc.dwellir.com",
      "Pinknode": "wss://public-rpc.pinknode.io/nodle"
    }
  ],
   "oak": [
    {
      "OAK": "wss://rpc.oak.tech"
    }
  ],
   "omnibtc": [
    {
      "OmniBTC": "wss://omnibtc.io/ws"
    }
  ],
   "origintrail": [
    {
      "TraceLabs": "wss://parachain-rpc.origin-trail.network"
    }
  ],
   "parallel": [
    {
      "OnFinality": "wss://parallel.api.onfinality.io/public-ws",
      "Parallel": "wss://rpc.parallel.fi"
    }
  ],
   "pendulum": [
    {
      "PendulumChain": "wss://rpc.pendulumchain.tech"
    }
  ],
   "phala": [
    {
      "Phala": "wss://api.phala.network/ws",
      "OnFinality": "wss://phala.api.onfinality.io/public-ws"
    }
  ],
   "polkadex": [
    {
      "Polkadex Team": "wss://mainnet.polkadex.trade/",
      "OnFinality": "wss://polkadex.api.onfinality.io/public-ws"
    }
  ],
   "subdao": [
    {
      "SubDAO": "wss://parachain-rpc.subdao.org"
    }
  ],
   "subgame": [
    {
      "SubGame": "wss://gamma.subgame.org/" 
    }
  ],
   "unique": [
    {
      "Unique America": "wss://us-ws.unique.network/",
      "Unique Asia": "wss://asia-ws.unique.network/",
      "Unique Europe": "wss://eu-ws.unique.network/"
    }
  ],
   "statemint": [
    {
      "Parity": "wss://statemint-rpc.polkadot.io",
      "OnFinality": "wss://statemint.api.onfinality.io/public-ws",
      "Dwellir": "wss://statemint-rpc.dwellir.com",
      "Pinknode": "wss://public-rpc.pinknode.io/statemint",
      "RadiumBlock": "wss://statemint.public.curie.radiumblock.xyz/ws"
    }
  ],
   "polkadotcollectives": [
    {
      "Parity": "wss://polkadot-collectives-rpc.polkadot.io"
    }
  ],
   "polkadot": [
    {
      "Parity": "wss://rpc.polkadot.io",
      "OnFinality": "wss://polkadot.api.onfinality.io/public-ws",
      "Dwellir": "wss://polkadot-rpc.dwellir.com",
      "Pinknode": "wss://public-rpc.pinknode.io/polkadot",
      "RadiumBlock": "wss://polkadot.public.curie.radiumblock.co/ws",
      "Automata 1RPC": "wss://1rpc.io/dot",
      "Dotters Net": "wss://rpc.dotters.network/polkadot"
    }
  ],
  
  
   "altair": [
    {
      "Centrifuge": "wss://fullnode.altair.centrifuge.io",
      "OnFinality": "wss://altair.api.onfinality.io/public-ws"
    }
  ],
   "amplitude": [
    {
      "PendulumChain": "wss://rpc-amplitude.pendulumchain.tech"
    }
  ],
   "bajun": [
    {
      "AjunaNetwork": "wss://rpc-parachain.bajun.network",
      "Dwellir": "wss://bajun-rpc.dwellir.com",
      "OnFinality": "wss://bajun.api.onfinality.io/public-ws"
    }
  ],
   "basilisk": [
    {
      "Basilisk": "wss://rpc.basilisk.cloud",
      "Dwellir": "wss://basilisk-rpc.dwellir.com"
    }
  ],
   "bifrost-dot": [
    {
      "Liebi": "wss://bifrost-rpc.liebi.com/ws",
      "OnFinality": "wss://bifrost-parachain.api.onfinality.io/public-ws",
      "Dwellir": "wss://bifrost-rpc.dwellir.com"
    }
  ],
   "bitcountrypioneer": [
    {
      "OnFinality": "wss://pioneer.api.onfinality.io/public-ws"
    }
  ],
   "calamari": [
    {
      "Manta Network": "wss://ws.calamari.systems/"
    }
  ],
   "ajuna": [
    {
      "Crust": "wss://rpc-shadow.crust.network/"
    }
  ],
   "ipci": [
    {
      "Airalab": "wss://kusama.rpc.ipci.io"
    }
  ],
   "crab": [
    {
      "Darwinia Network": "wss://crab-parachain-rpc.darwinia.network/"
    }
  ],
   "dorafactory": [
    {
      "DORA": "wss://kusama.dorafactory.org"
    }
  ],
   "genshiro": [
    {
      "Equilibrium": "wss://node.genshiro.io"
    }
  ],
   "gm": [
    {
      "bLd Nodes": "wss://ws.gm.bldnodes.org",
      "TerraBioDAO": "wss://ws-node-gm.terrabiodao.org",
      "Leemo": "wss://leemo.gmordie.com",
      "GM Intern": "wss://intern.gmordie.com"
    }
  ],
   "imbue": [
    {
      "Imbue Network": "wss://imbue-kusama.imbue.network"
    }
  ],
   "integritee": [
    {
      "Integritee": "wss://kusama.api.integritee.network",
      "OnFinality": "wss://integritee-kusama.api.onfinality.io/public-ws"
    }
  ],
   "tinkernet": [
    {
      "InvArch Team": "wss://tinker.invarch.network",
      "OnFinality": "wss://invarch-tinkernet.api.onfinality.io/public-ws"
    }
  ],
   "kabocha": [
    {
      "JelliedOwl": "wss://kabocha.jelliedowl.net"
    }
  ],
   "karura": [
    {
      "Acala Foundation 0": "wss://karura-rpc-0.aca-api.network",
      "Acala Foundation 1": "wss://karura-rpc-1.aca-api.network",
      "Acala Foundation 2": "wss://karura-rpc-2.aca-api.network/ws",
      "Acala Foundation 3": "wss://karura-rpc-3.aca-api.network/ws",
      "Polkawallet 0": "wss://karura.polkawallet.io",
      "OnFinality": "wss://karura.api.onfinality.io/public-ws",
      "Dwellir": "wss://karura-rpc.dwellir.com"
    }
  ],
   "khala": [
    {
      "Phala": "wss://khala-api.phala.network/ws",
      "OnFinality": "wss://khala.api.onfinality.io/public-ws",
      "Dwellir": "wss://khala-rpc.dwellir.com",
      "Pinknode": "wss://public-rpc.pinknode.io/khala"
    }
  ],
   "kico": [
    {
      "DICO Foundation": "wss://rpc.kico.dico.io"
    }
  ],
   "kintsugi": [
    {
      "Kintsugi Labs": "wss://api-kusama.interlay.io/parachain",
      "OnFinality": "wss://kintsugi.api.onfinality.io/public-ws"
    }
  ],
   "kpron": [
    {
      "Kpron": "wss://kusama-kpron-rpc.apron.network/"
    }
  ],
   "listen": [
    {
      "Listen Foundation 1": "wss://rpc.mainnet.listen.io",
      "Listen Foundation 2": "wss://wss.mainnet.listen.io"
    }
  ],
   "litmus": [
    {
      "Litentry": "wss://rpc.litmus-parachain.litentry.io"
    }
  ],
   "loomnetwork": [
    {
      "LoomNetwork": "wss://kusama.dappchains.com"
    }
  ],
   "luhn": [
    {
      "Hashed Systems": "wss://c1.luhn.network"
    }
  ],
   "mangatax": [
    {
      "Mangata": "wss://prod-kusama-collator-01.mangatafinance.cloud",
      "OnFinality": "wss://mangata-x.api.onfinality.io/public-ws"
    }
  ],
   "mars": [
    {
      "AresProtocol": "wss://wss.mars.aresprotocol.io"
    }
  ],
   "moonriver": [
    {
      "Moonbeam Foundation": "wss://wss.api.moonriver.moonbeam.network",
      "Blast": "wss://moonriver.public.blastapi.io",
      "OnFinality": "wss://moonriver.api.onfinality.io/public-ws",
      "Pinknode": "wss://public-rpc.pinknode.io/moonriver",
      "Dwellir": "wss://moonriver-rpc.dwellir.com"
    }
  ],
   "parallel-heiko": [
    {
      "Parallel": "wss://heiko-rpc.parallel.fi"
    }
  ],
   "picasso": [
    {
      "Composable": "wss://rpc.composablenodes.tech"
    }
  ],
   "pichiu": [
    {
      "Kylin Network": "wss://kusama.kylin-node.co.uk",
      "OnFinality": "wss://pichiu.api.onfinality.io/public-ws"
    }
  ],
   "polkasmith": [
    {
      "PolkaSmith": "wss://wss-polkasmith.polkafoundry.com"
    }
  ],
   "quartz": [
    {
      "Unique America": "wss://us-ws-quartz.unique.network",
      "Unique Asia": "wss://asia-ws-quartz.unique.network",
      "Unique Europe": "wss://eu-ws-quartz.unique.network"
    }
  ],
   "riodefi": [
    {
      "RioProtocol": "wss://rio-kusama.riocorenetwork.com"
    }
  ],
   "robonomics": [
    {
      "Airalab": "wss://kusama.rpc.robonomics.network/",
      "OnFinality": "wss://robonomics.api.onfinality.io/public-ws",
      "Samsara": "wss://robonomics.0xsamsara.com",
      "Leemo": "wss://robonomics.leemo.me"
    }
  ],
   "sakura": [
    {
      "Clover": "wss://api-sakura.clover.finance"
    }
  ],
   "shadow": [
    {
      "Crust": "wss://rpc-shadow.crust.network/"
    }
  ],
   "shiden": [
    {
      "StakeTechnologies": "wss://rpc.shiden.astar.network",
      "Blast": "wss://shiden.public.blastapi.io",
      "Dwellir": "wss://shiden-rpc.dwellir.com",
      "OnFinality": "wss://shiden.api.onfinality.io/public-ws",
      "Pinknode": "wss://public-rpc.pinknode.io/shiden"
    }
  ],
   "shiden": [
    {
      "StakeTechnologies": "wss://rpc.shiden.astar.network"
    }
  ],
   "snow": [
    {
      "IceNetwork": "wss://snow-rpc.icenetwork.io"
    }
  ],
   "sora": [
    {
      "Soramitsu": "wss://ws.parachain-collator-1.c1.sora2.soramitsu.co.jp"
    }
  ],
   "subgame": [
    {
      "SubGame": "wss://gamma.subgame.org/"
    }
  ],
   "subsocialx": [
    {
      "Dappforce 1": "wss://para.f3joule.space",
      "Dappforce 2": "wss://para.subsocial.network"
    }
  ],
   "tanganika": [
    {
      "DataHighway": "wss://tanganika.datahighway.com"
    }
  ],
   "turing": [
    {
      "OAK": "wss://rpc.turing.oak.tech",
      "Dwellir": "wss://turing-rpc.dwellir.com"
    }
  ],
   "unorthodox": [
    {
      "Standard Protocol": "wss://rpc.kusama.standard.tech"
    }
  ],
   "zeitgeist": [
    {
      "Dwellir": "wss://zeitgeist-rpc.dwellir.com",
      "OnFinality": "wss://zeitgeist.api.onfinality.io/public-ws"
    }
  ],
   "statemine": [
    {
      "Parity": "wss://statemine-rpc.polkadot.io",
      "OnFinality": "wss://statemine.api.onfinality.io/public-ws",
      "Dwellir": "wss://statemine-rpc.dwellir.com",
      "Pinknode": "wss://public-rpc.pinknode.io/statemine",
      "RadiumBlock": "wss://statemine.public.curie.radiumblock.co/ws"
    }
  ],
   "encointer": [
    {
      "Encointer Association": "wss://kusama.api.encointer.org",
      "OnFinality": "wss://encointer.api.onfinality.io/public-ws"
    }
  ],
   "kusama": [
    {
      "Parity": "wss://kusama-rpc.polkadot.io",
      "OnFinality": "wss://kusama.api.onfinality.io/public-ws",
      "Dwellir": "wss://kusama-rpc.dwellir.com",
      "RadiumBlock": "wss://kusama.public.curie.radiumblock.xyz/ws",
      "Pinknode": "wss://public-rpc.pinknode.io/kusama",
      "Automata 1RPC": "wss://1rpc.io/ksm",
      "Dotters Net": "wss://rpc.dotters.network/kusama"
    }
  ]
}
"""
WSS_ENDPOINTS = json.loads(wss_json)



