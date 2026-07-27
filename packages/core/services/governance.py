"""Executable constitutional rules for each government model."""
from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True,slots=True)
class Rules:
    leadership_selection:str
    public_elections:bool
    election_starter:str
    leader_may_override:bool=False
    candidate_screening:bool=False

RULES={
 "republic":Rules("popular","public"=="public","citizen"),
 "presidential":Rules("popular",True,"citizen"),
 "parliamentary":Rules("parliament",True,"citizen"),
 "semi_presidential":Rules("popular",True,"citizen"),
 "federal":Rules("popular",True,"citizen"),
 "direct_democracy":Rules("popular",True,"citizen"),
 "constitutional_monarchy":Rules("parliament",True,"citizen"),
 "council":Rules("council",True,"citizen"),
 "dictatorship":Rules("leader",True,"leader",leader_may_override=True),
 "theocracy":Rules("clerical",True,"leader",candidate_screening=True),
 "monarchy":Rules("hereditary",False,"none"),
 "military_junta":Rules("military_council",False,"none"),
 "oligarchy":Rules("elite_council",False,"none"),
}
def rules_for(code:str)->Rules:return RULES.get(code,RULES["republic"])