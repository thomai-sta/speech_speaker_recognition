
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\xe4Ed`\xa7\xf3\xac\x99\xa1*/\x03\xebsAB'
    
_lr_action_items = {'MACRO_V':([0,4,6,13,14,18,20,22,24,25,26,27,28,30,32,34,35,39,41,42,44,46,47,48,49,50,52,53,55,56,57,61,67,72,73,74,77,78,79,],[1,1,-37,-16,-4,-8,-6,-7,-38,-40,-36,-39,-41,-3,43,-5,-21,-35,-22,-37,-23,-27,-29,-25,-26,-34,-20,-24,-17,-28,-33,-32,-31,-9,43,-30,-37,-19,-18,]),'BEGINHMM':([16,],[29,]),'MACRO_T':([0,4,6,13,14,18,20,22,24,25,26,27,28,30,34,39,42,44,46,47,48,49,50,52,53,55,56,57,59,61,67,69,70,72,74,75,76,77,78,79,],[2,2,-37,-16,-4,-8,-6,-7,-38,-40,-36,-39,-41,-3,-5,-35,-37,-23,-27,-29,-25,-26,-34,-20,-24,-17,-28,-33,63,-32,-31,-12,-11,-9,-30,-13,-10,-37,-19,-18,]),'MACRO_U':([0,4,6,13,14,17,18,20,22,24,25,26,27,28,30,34,39,42,44,46,47,48,49,50,52,53,55,56,57,61,62,66,67,72,74,77,78,79,],[3,3,-37,-16,-4,31,-8,-6,-7,-38,-40,-36,-39,-41,-3,-5,-35,-37,-23,-27,-29,-25,-26,-34,-20,-24,-17,-28,-33,-32,31,31,-31,-9,-30,-37,-19,-18,]),'MACRO_S':([0,4,6,13,14,18,20,22,24,25,26,27,28,30,34,39,42,44,46,47,48,49,50,52,53,55,56,57,61,62,67,72,74,77,78,79,],[8,8,-37,-16,-4,-8,-6,-7,-38,-40,-36,-39,-41,-3,-5,-35,-37,-23,-27,-29,-25,-26,-34,-20,-24,-17,-28,-33,-32,68,-31,-9,-30,-37,-19,-18,]),'ENDHMM':([47,48,56,64,65,71,],[-29,-25,-28,-14,72,-15,]),'INT':([15,19,21,23,24,25,26,27,28,33,39,40,50,54,57,58,61,67,],[24,36,37,38,-38,-40,24,-39,-41,45,24,51,24,60,24,62,24,24,]),'FLOAT':([15,24,25,26,27,28,36,37,38,39,47,50,57,60,61,67,],[25,-38,-40,25,-39,-41,47,47,47,25,47,25,25,66,25,25,]),'TRANSP':([10,24,25,26,27,28,39,42,44,46,47,50,52,53,55,56,57,59,61,67,69,70,74,75,76,77,78,79,],[21,-38,-40,-36,-39,-41,-35,-37,-23,-27,-29,-34,-20,-24,-17,-28,-33,21,-32,-31,-12,-11,-30,-13,-10,-37,-19,-18,]),'STATE':([24,25,26,27,28,39,42,44,46,47,50,51,52,53,55,56,57,61,67,69,70,74,75,77,78,79,],[-38,-40,-36,-39,-41,-35,-37,-23,-27,-29,-34,58,-20,-24,-17,-28,-33,-32,-31,-12,58,-30,-13,-37,-19,-18,]),'NUMSTATES':([29,],[40,]),'NUMMIXES':([17,62,],[33,33,]),'MIXTURE':([24,25,26,27,28,39,44,45,46,47,50,53,56,57,61,67,74,77,78,],[-38,-40,-36,-39,-41,-35,-23,54,-27,-29,-34,-24,-28,-33,-32,-31,-30,-37,54,]),'MEAN':([11,17,62,66,],[23,23,23,23,]),'OTHER_TAG':([6,15,24,25,26,27,28,39,42,44,46,47,50,53,56,57,61,67,77,],[15,28,-38,-40,28,-39,-41,28,15,-23,-27,-29,28,-24,-28,28,28,28,15,]),'VARIANCE':([9,32,35,41,47,49,56,73,],[19,19,-21,-22,-29,-26,-28,19,]),'MACRO_O':([0,4,6,13,14,18,20,22,24,25,26,27,28,30,34,39,42,44,46,47,48,49,50,52,53,55,56,57,61,67,72,74,77,78,79,],[6,6,-37,-16,-4,-8,-6,-7,-38,-40,-36,-39,-41,-3,-5,-35,-37,-23,-27,-29,-25,-26,-34,-20,-24,-17,-28,-33,-32,-31,-9,-30,-37,-19,-18,]),'$end':([4,5,6,12,13,14,18,20,22,24,25,26,27,28,30,34,39,42,44,46,47,48,49,50,52,53,55,56,57,61,67,72,74,77,78,79,],[-2,0,-37,-1,-16,-4,-8,-6,-7,-38,-40,-36,-39,-41,-3,-5,-35,-37,-23,-27,-29,-25,-26,-34,-20,-24,-17,-28,-33,-32,-31,-9,-30,-37,-19,-18,]),'MACRO_H':([0,4,6,13,14,18,20,22,24,25,26,27,28,30,34,39,42,44,46,47,48,49,50,52,53,55,56,57,61,67,72,74,77,78,79,],[7,7,-37,-16,-4,-8,-6,-7,-38,-40,-36,-39,-41,-3,-5,-35,-37,-23,-27,-29,-25,-26,-34,-20,-24,-17,-28,-33,-32,-31,-9,-30,-37,-19,-18,]),'NAME':([1,2,3,7,8,15,24,25,26,27,28,31,39,43,50,57,61,63,67,68,],[9,10,11,16,17,27,-38,-40,27,-39,-41,41,27,53,27,27,27,71,27,75,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'state_var':([32,73,],[42,77,]),'hmmdef_state':([62,],[70,]),'tmat':([10,59,],[20,64,]),'filler':([6,42,77,],[13,52,78,]),'macro':([0,4,],[4,4,]),'state_mean':([17,62,66,],[32,32,73,]),'hmmdef_tmat':([59,],[65,]),'macros':([0,4,],[5,12,]),'state':([17,62,],[34,69,]),'vector':([36,37,38,47,],[46,48,49,56,]),'hmmdef_states':([51,70,],[59,76,]),'var':([9,32,73,],[18,44,44,]),'hmmdef':([16,],[30,]),'filler1':([15,26,39,50,57,61,67,],[26,39,50,57,61,67,74,]),'globaloptions':([6,],[14,]),'state_mixtures':([45,78,],[55,79,]),'mean':([11,17,62,66,],[22,35,35,35,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> macros","S'",1,None,None,None),
  ('macros -> macro macros','macros',2,'p_macros','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',29),
  ('macros -> macro','macros',1,'p_macros','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',30),
  ('macro -> MACRO_H NAME hmmdef','macro',3,'p_macro','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',45),
  ('macro -> MACRO_O globaloptions','macro',2,'p_macro','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',46),
  ('macro -> MACRO_S NAME state','macro',3,'p_macro','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',47),
  ('macro -> MACRO_T NAME tmat','macro',3,'p_macro','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',48),
  ('macro -> MACRO_U NAME mean','macro',3,'p_macro','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',49),
  ('macro -> MACRO_V NAME var','macro',3,'p_macro','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',50),
  ('hmmdef -> BEGINHMM NUMSTATES INT hmmdef_states hmmdef_tmat ENDHMM','hmmdef',6,'p_hmmdef','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',69),
  ('hmmdef_states -> STATE INT hmmdef_state hmmdef_states','hmmdef_states',4,'p_hmmdef_states','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',77),
  ('hmmdef_states -> STATE INT hmmdef_state','hmmdef_states',3,'p_hmmdef_states','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',78),
  ('hmmdef_state -> state','hmmdef_state',1,'p_hmmdef_state','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',87),
  ('hmmdef_state -> MACRO_S NAME','hmmdef_state',2,'p_hmmdef_state','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',88),
  ('hmmdef_tmat -> tmat','hmmdef_tmat',1,'p_hmmdef_tmat','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',100),
  ('hmmdef_tmat -> MACRO_T NAME','hmmdef_tmat',2,'p_hmmdef_tmat','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',101),
  ('globaloptions -> filler','globaloptions',1,'p_globaloptions','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',113),
  ('state -> NUMMIXES INT state_mixtures','state',3,'p_state_1','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',119),
  ('state_mixtures -> MIXTURE INT FLOAT state_mean state_var filler state_mixtures','state_mixtures',7,'p_state_mixtures','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',127),
  ('state_mixtures -> MIXTURE INT FLOAT state_mean state_var filler','state_mixtures',6,'p_state_mixtures','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',128),
  ('state -> state_mean state_var filler','state',3,'p_state_2','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',137),
  ('state_mean -> mean','state_mean',1,'p_state_mean','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',143),
  ('state_mean -> MACRO_U NAME','state_mean',2,'p_state_mean','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',144),
  ('state_var -> var','state_var',1,'p_state_var','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',156),
  ('state_var -> MACRO_V NAME','state_var',2,'p_state_var','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',157),
  ('tmat -> TRANSP INT vector','tmat',3,'p_tmat','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',169),
  ('mean -> MEAN INT vector','mean',3,'p_mean','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',177),
  ('var -> VARIANCE INT vector','var',3,'p_var','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',185),
  ('vector -> FLOAT vector','vector',2,'p_vector','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',193),
  ('vector -> FLOAT','vector',1,'p_vector','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',194),
  ('filler -> OTHER_TAG filler1 filler1 filler1 filler1 filler1 filler1 filler1','filler',8,'p_filler','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',203),
  ('filler -> OTHER_TAG filler1 filler1 filler1 filler1 filler1 filler1','filler',7,'p_filler','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',204),
  ('filler -> OTHER_TAG filler1 filler1 filler1 filler1 filler1','filler',6,'p_filler','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',205),
  ('filler -> OTHER_TAG filler1 filler1 filler1 filler1','filler',5,'p_filler','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',206),
  ('filler -> OTHER_TAG filler1 filler1 filler1','filler',4,'p_filler','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',207),
  ('filler -> OTHER_TAG filler1 filler1','filler',3,'p_filler','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',208),
  ('filler -> OTHER_TAG filler1','filler',2,'p_filler','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',209),
  ('filler -> <empty>','filler',0,'p_filler','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',210),
  ('filler1 -> INT','filler1',1,'p_filler1','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',216),
  ('filler1 -> NAME','filler1',1,'p_filler1','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',217),
  ('filler1 -> FLOAT','filler1',1,'p_filler1','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',218),
  ('filler1 -> OTHER_TAG','filler1',1,'p_filler1','/Users/joro/Documents/Phd/UPF/voxforge/myScripts/htk2s3/htk_parser.py',219),
]
