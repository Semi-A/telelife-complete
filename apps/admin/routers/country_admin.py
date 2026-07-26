"""Authenticated country/admin API. Every mutation is audited."""
from __future__ import annotations
from uuid import uuid4
from fastapi import APIRouter,Depends,Form
from apps.admin.main import require_admin
from packages.core.repositories import admin_repo
from packages.core.services import admin
router=APIRouter(prefix='/api/admin',dependencies=[Depends(require_admin)])
@router.get('/stats')
async def stats():
 row=await admin_repo.stats();return dict(row) if row else {}
@router.get('/users')
async def users(limit:int=100):return [dict(x) for x in await admin_repo.users(min(limit,500))]
@router.get('/countries')
async def countries(limit:int=100):return [dict(x) for x in await admin_repo.countries(min(limit,500))]
@router.get('/audit')
async def audit(limit:int=100):return [dict(x) for x in await admin_repo.audits(min(limit,500))]
@router.post('/ban/{player_id}')
async def ban(player_id:int,enabled:bool=Form(...),reason:str|None=Form(None),actor:str=Depends(require_admin)):return {'applied':await admin.ban(actor,player_id,enabled,reason,str(uuid4()))}
@router.post('/grant-xp/{player_id}')
async def grant(player_id:int,amount:int=Form(...),actor:str=Depends(require_admin)):
 result=await admin.grant_xp(actor,player_id,amount,str(uuid4()));return {'granted':result.granted if result else 0}
@router.post('/feature/{key}')
async def feature(key:str,enabled:bool=Form(...),actor:str=Depends(require_admin)):return {'applied':await admin.feature(actor,key,enabled,str(uuid4()))}
