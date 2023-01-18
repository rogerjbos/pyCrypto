import numpy as np
import pandas as pd
import time
import calendar
import datetime
import requests
import json
import os

POLKAHOLIC_API_KEY = os.getenv('POLKAHOLIC_API_KEY')

#' Get events from the Polkadot blockchain from the Polkaholic api
#' https://docs.polkaholic.io
#'
#' @name get_polkaholic_events
#' @title get_polkaholic_events
#' @encoding UTF-8
#' @concept Get events from the Polkadot blockchain from the Polkaholic api
#' @param chain string or integer specifying the target parachain
#' @param module string indicating which Polkadot module to use; leave blank for all.
#' @param call string indicating the module call (i.e. "Swap"); leave blank for all.
#' @param startDate string indicating the end date; leave blank for all.
#' @param endDate string indicating the start date; leave blank for all.
#'
#' @return data.table
#'
#' @examples
#' tmp = getPolkaholicEvents("karura", nobs = 100, module = "staking", call = '', startDate='2022-07-01', endDate='2022-07-20')
#'
#' @author Roger J. Bos, \email{roger.bos@@gmail.com}
def getPolkaholicEvents(chain, nobs = 100, module = "", call = "", startDate = "", endDate = ""):
  API_ENDPOINT = f"https://api.polkaholic.io/search/events?limit={nobs}&decorate=true&extra=usd,address,related,params,data"
  header = {"Authorization": os.getenv('POLKAHOLIC_API_KEY')}
  data = {"chainIdentifier": chain, "section": module, "method": call, "dateStart": startDate, "dateEnd": endDate}
  # Remove blank elements
  [data.pop(entry) for entry in data.copy() if data[entry] == '']

  r = requests.post(url = API_ENDPOINT, headers = header, data = data)
  if r.status_code != 200:
    raise Exception("Invalid request")
  out = pd.DataFrame(r.json())
  if 'blockTS' in out.columns:
    out['Date'] = pd.to_datetime(out['blockTS'],unit='s')
  return out

# Not working !!!  
def getPolkaholicEvents_test(chain, nobs = 100, module = "", call = "", startDate = "", endDate = ""):
  API_ENDPOINT = f"https://api.polkaholic.io/search/events?limit={nobs}&decorate=true&extra=usd,address,related,params,data"
  API_ENDPOINT = f"https://api.polkaholic.io/search/events?limit=1&decorate=true&extra=usd,address,related,data"
  API_ENDPOINT = "https://api.polkaholic.io/search/events?limit=1&decorate=true&extra=data"
  API_ENDPOINT = "https://api.polkaholic.io/search/events?limit=1"
  header = {"Authorization": os.getenv('POLKAHOLIC_API_KEY')}
  # if module != "" and call != "":
    # data = {"chainIdentifier": chain, "section": module, "method": call, "dateStart": startDate, "dateEnd": endDate}
  # elif module != "" and call == "":
  data = {"chainIdentifier": chain, "section": module, "dateStart": startDate, "dateEnd": endDate}
  # else: 
  #   data = {"chainIdentifier": chain, "dateStart": startDate, "dateEnd": endDate}
  r = requests.post(url = API_ENDPOINT, headers = header, data = data)
  # if r.status_code != 200:
  #   raise Exception("Invalid request")
  out = pd.DataFrame(r.json())
  # if 'blockTS' in out.columns:
  #   out['Date'] = pd.to_datetime(out['blockTS'],unit='s')
  out
  out['extrinsicHash']
  
  
  
  return out

#' Get supported chains from the Polkaholic api
#' https://docs.polkaholic.io
#'
#' @name get_polkaholic_chains
#' @title get_polkaholic_chains
#' @encoding UTF-8
#' @concept Get events from the Polkadot blockchain from the Polkaholic api
#' @param None
#'
#' @return data.table
#'
#' @examples
#' tmp = getPolkaholicChains()
#'
#' @author Roger J. Bos, \email{roger.bos@@gmail.com}
def getPolkaholicChains():
  API_ENDPOINT = f"https://api.polkaholic.io/chains"
  header = {"Authorization": os.getenv('POLKAHOLIC_API_KEY')}
  r = requests.get(url = API_ENDPOINT, headers = header)
  if r.status_code != 200:
    raise Exception("Invalid request")
  out = pd.DataFrame(r.json())
  if 'lastFinalizedTS' in out.columns:
    out['Date'] = pd.to_datetime(out['lastFinalizedTS'],unit='s')
  return out

#' Get events from the Polkadot blockchain from the Polkaholic api
#' https://docs.polkaholic.io
#'
#' @name get_polkaholic_chainlog
#' @title get_polkaholic_chainlog
#' @encoding UTF-8
#' @concept Get events from the Polkadot blockchain from the Polkaholic api
#' @param chain string or integer specifying the target parachain
#'
#' @return data.table
#'
#' @examples
#' tmp = getPolkaholicChainlog("astar")
#'
#' @author Roger J. Bos, \email{roger.bos@@gmail.com}
def getPolkaholicChainlog(chain):
  API_ENDPOINT = f"https://api.polkaholic.io/chainlog/{chain}"
  header = {"Authorization": os.getenv('POLKAHOLIC_API_KEY')}
  r = requests.get(url = API_ENDPOINT, headers = header)
  if r.status_code != 200:
      time.sleep(2)
      r = requests.get(url = API_ENDPOINT, headers = header)
      if r.status_code != 200:
        raise Exception("Invalid request")
      
  out = pd.DataFrame(r.json())
  out['id'] = chain
  return out

#' Get supported chains from the Polkaholic api
#' https://docs.polkaholic.io
#'
#' @name get_polkaholic_hash
#' @title get_polkaholic_hash
#' @encoding UTF-8
#' @concept Get hash lookup from the Polkadot blockchain from the Polkaholic api
#' @param TxHash string hash to lookup
#'
#' @return data.table
#'
#' @examples
#' tmp = getPolkaholicHash(txhash = '0x044e63a8548c51bac4f3cdf71cc3bc31e63b460f7652030604aee4361f1b1878')
#'
#' @author Roger J. Bos, \email{roger.bos@@gmail.com}
#' @export
def getPolkaholicHash(txhash):
  txhash = txhash.unique()
  data = []
  header = {'Authorization': os.getenv('POLKAHOLIC_API_KEY')}
  for h in range(len(txhash)):
    if h % 5 == 0:
      print("sleep")
      time.sleep(1)
    print(txhash[h])
    API_ENDPOINT = f"https://api.polkaholic.io/hash/{txhash[h]}"
    r = requests.get(url = API_ENDPOINT, headers = header)
    if r.status_code != 200:
      raise Exception("Invalid request")
    else:
      outi = r.json()
      data.append(outi)
  df = pd.DataFrame(data)
  return df

#' Get supported chains from the Polkaholic api
#' https://docs.polkaholic.io
#'
#' @name get_polkaholic_transaction
#' @title get_polkaholic_transaction
#' @encoding UTF-8
#' @concept Get events from the Polkadot blockchain from the Polkaholic api
#' @param TxHash string transaction hash
#'
#' @return data.table
#'
#' @examples
#' tmp = getPolkaholicTransaction(txhash = '0x8b91d038421d5aba4b3a651d70923fb0d41423b914d6dad910637aa2c9a2ad70')
#'
#' @author Roger J. Bos, \email{roger.bos@@gmail.com}
def getPolkaholicTransaction(txhash):

  txhash = txhash.unique()
  data = []
  header = {'Authorization': os.getenv('POLKAHOLIC_API_KEY')}
  for h in range(len(txhash)):
    if h % 5 == 0:
      # print("sleep")
      time.sleep(1)
    # print(txhash[h])
    API_ENDPOINT = f"https://api.polkaholic.io/tx/{txhash[h]}"
    r = requests.get(url = API_ENDPOINT, headers = header)
    if r.status_code != 200:
      raise Exception("Invalid request")
    else:
      outi = r.json()
      data.append(outi)
  df = pd.DataFrame(data)
  return df


def getPolkaholicExtrinsics(chain, nobs = 1, module = "staking", call = "", startDate = "", endDate = "", fromAddress = ""):
  API_ENDPOINT = f"https://api.polkaholic.io/search/extrinsics?limit={nobs}&decorate=true&extra=usd,address,related,data"
  API_ENDPOINT = f"https://api.polkaholic.io/search/extrinsics?decorate=true&extra=usd,address,related,data"
  header = {"Authorization": os.getenv('POLKAHOLIC_API_KEY')}
  data = {"chainIdentifier": chain, "section": module, "dateStart": startDate, "dateEnd": endDate, "fromAddress": fromAddress}
  # Remove blank elements
  [data.pop(entry) for entry in data.copy() if data[entry] == '']

  r = requests.post(url = API_ENDPOINT, headers = header, data = data)
  if r.status_code != 200:
    raise Exception("Invalid request")
  outi = r.json()
  outi
  
  out = pd.DataFrame(outi)
  out.tail(2)
  
  if 'blockTS' in out.columns:
    out['Date'] = pd.to_datetime(out['blockTS'],unit='s')
  return out

def getPolkaholicXcm(chain = "moonbeam", nobs = 9999, symbol = "kbtc", startDate = "2020-12-10", endDate = "2020-12-14"):

  # Convert dates into unixtime
  if isinstance(startDate, datetime.date) == False:
    startDate = datetime.datetime.strptime(startDate, '%Y-%m-%d')
  if isinstance(endDate, datetime.date) == False:
    endDate = datetime.datetime.strptime(endDate, '%Y-%m-%d')
  startTS = calendar.timegm(startDate.utctimetuple())
  endTS = calendar.timegm(endDate.utctimetuple())
  
  API_ENDPOINT = f"https://api.polkaholic.io/xcmtransfers?xcmType=xcmtransfer&chainIdentifier={chain}&symbol={symbol}&startTS={startTS}&endTS={endTS}&limit={nobs}"
  header = {"Authorization": os.getenv('POLKAHOLIC_API_KEY')}
  r = requests.get(url = API_ENDPOINT, headers = header)
  if r.status_code != 200:
    raise Exception("Invalid request")
  out = r.json()
  if len(out) > 0:
    out = pd.json_normalize(out)
    if 'xcmInfo.origination.ts' in out.columns:
      out['date'] = pd.to_datetime(out['xcmInfo.origination.ts'], unit='s')
    return out

