from ppci import wasm

def getLanguage(ba):
  m = wasm.Module(ba)
  sections = m.get_definitions_per_section()
  imports = sections['import']
  start = sections['start']
  customs = sections['custom']
  mem = next(filter(lambda x : x.kind == 'memory', imports))
  
  def hasName(name):
      lambda x : x.name == name
  
  # Tentative heuristics
  # (!) NOT tested with a reasonable sample set of binaries
  
  # Solang
  # * emits memory as the first import
  # * has custom sections named 'name' and 'producers'
  isSolang = bool(
      imports[0].kind == 'memory'
      and not start
      and customs
      and any(filter(hasName('name'), customs))
  )
  
  # Ask!
  # * has a start section
  # * has custom section named 'sourceMappingURL'
  # * imports declare memory after functions
  isAsk = bool(
      imports[0].kind != 'memory'
      and start
      and customs
      and any(filter(hasName('sourceMappingURL'), customs))
  )
  
  # Ink!
  # * no custom sections
  # * no start section
  # * imports declare memory after functions
  isInk = bool(
      imports[0].kind != 'memory'
      and not start
      and not customs
  )
  
  if isInk:
    return("Ink!")
  if isAsk:
    return("Ask!")
  if isSolang:
    return("Solidity")
  return("Unknown")
  
