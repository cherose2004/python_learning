# -*- coding: utf-8 -*-
# __author__ = "maple"
"""
zzh
    hhz
        xxx
zcg

"""
reply_list = [
    {'id':1,'name':"zzh",'parent_id':None},
    {'id':2,'name':"zzh",'parent_id':1},
    {'id':3,'name':"zcg",'parent_id':None},
    {'id':4,'name':"xxx",'parent_id':2},
    # ...
]

"""

reply_dict = {
    1:{'id':1,'name':"zzh",'parent_id':None,'children':[{'id':2,'name':"zzh",'parent_id':1,'children':[{'id':4,'name':"xxx",'parent_id':2},]},,]},
    4:{'id':4,'name':"xxx",'parent_id':2},
}
"""


data_dict = [
    {'id':1,'name':"zzh",'parent_id':None,'children':[{'id':2,'name':"zzh",'parent_id':1,'children':[{'id':4,'name':"xxx",'parent_id':2},]},]},
    {'id':3,'name':"zcg",'parent_id':None},
]