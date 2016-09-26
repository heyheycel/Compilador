
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'B12C95A8F24356BCA2B53D773970166F'
    
_lr_action_items = {'PARENDER':([6,10,15,17,18,39,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,64,],[-33,-34,-10,-35,-11,62,65,-27,-17,-19,-21,-14,-18,-16,-15,-20,-26,-13,-12,-23,-25,-22,-24,66,67,68,]),'MAYORIGUALQUE':([6,9,10,12,17,18,45,54,58,60,],[-33,-35,-34,26,-35,26,-27,-26,-25,-24,]),'IGUAL':([6,9,10,12,17,18,45,54,58,60,],[-33,None,-34,36,-35,36,-27,-26,-25,-24,]),'DIFERENTE':([6,9,10,12,17,18,45,54,58,60,],[-33,-35,-34,30,-35,30,-27,-26,-25,-24,]),'MENORQUE':([6,9,10,12,17,18,45,54,58,60,],[-33,-35,-34,32,-35,32,-27,-26,-25,-24,]),'PRINT':([0,],[4,]),'RESTA':([6,9,10,12,17,18,42,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[-33,-35,-34,35,-35,35,35,-27,35,35,35,35,35,35,35,35,-26,35,35,35,-25,35,-24,]),'SUMA':([6,9,10,12,17,18,42,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[-33,-35,-34,37,-35,37,37,-27,37,37,37,37,37,37,37,37,-26,37,37,37,-25,37,-24,]),'NOTIN':([6,9,10,12,17,18,45,54,58,60,],[-33,-35,-34,23,-35,23,-27,-26,-25,-24,]),'PUNTOS':([20,65,],[43,-28,]),'ISNOT':([6,9,10,12,17,18,45,54,58,60,],[-33,-35,-34,24,-35,24,-27,-26,-25,-24,]),'MAYORQUE':([6,9,10,12,17,18,45,54,58,60,],[-33,-35,-34,33,-35,33,-27,-26,-25,-24,]),'IS':([6,9,10,12,17,18,45,54,58,60,],[-33,-35,-34,27,-35,27,-27,-26,-25,-24,]),'PARENIZQ':([0,4,11,13,],[8,14,21,38,]),'$end':([1,2,3,5,6,7,9,10,12,17,42,43,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,66,67,68,],[-5,-4,-6,0,-33,-3,-35,-34,-2,-35,-1,-29,-27,-17,-19,-21,-14,-18,-16,-15,-20,-26,-13,-12,-23,-25,-22,-24,-32,-9,-8,-7,]),'DIVISION':([6,9,10,12,17,18,42,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[-33,-35,-34,22,-35,22,22,-27,22,22,22,22,22,22,22,22,-26,22,22,22,22,22,22,]),'STRING':([14,],[39,]),'DISTINTO':([6,9,10,12,17,18,45,54,58,60,],[-33,-35,-34,25,-35,25,-27,-26,-25,-24,]),'IDENTIFICADOR':([0,8,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,41,],[9,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'NUMERO':([0,8,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,41,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'MULTIPLICACION':([6,9,10,12,17,18,42,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[-33,-35,-34,31,-35,31,31,-27,31,31,31,31,31,31,31,31,-26,31,31,31,31,31,31,]),'IN':([6,9,10,12,17,18,45,54,58,60,],[-33,-35,-34,28,-35,28,-27,-26,-25,-24,]),'IGUALA':([6,9,10,12,17,18,45,54,58,60,],[-33,-35,-34,34,-35,34,-27,-26,-25,-24,]),'IF':([0,],[11,]),'AND':([6,10,15,16,17,18,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[-33,-34,-10,40,-35,-11,-27,-17,-19,-21,-14,-18,-16,-15,-20,-26,-13,-12,-23,-25,-22,-24,]),'MENORIGUALQUE':([6,9,10,12,17,18,45,54,58,60,],[-33,-35,-34,29,-35,29,-27,-26,-25,-24,]),'NOT':([0,],[13,]),'OR':([6,10,15,16,17,18,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[-33,-34,-10,41,-35,-11,-27,-17,-19,-21,-14,-18,-16,-15,-20,-26,-13,-12,-23,-25,-22,-24,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expresion':([0,8,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,41,],[12,18,42,18,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,18,18,18,]),'sentencia':([0,],[5,]),'expresiones':([8,21,38,40,41,],[16,44,61,63,64,]),'expresionLogica':([0,],[1,]),'expresionRelacional':([0,8,21,38,40,41,],[2,15,15,15,15,15,]),'terminal':([0,8,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,41,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'print_stc':([0,],[3,]),'test':([11,],[20,]),'if_stc':([0,],[7,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sentencia","S'",1,None,None,None),
  ('sentencia -> IDENTIFICADOR IGUAL expresion','sentencia',3,'p_asignacion','parser.py',15),
  ('sentencia -> expresion','sentencia',1,'p_sentencia_expr','parser.py',21),
  ('sentencia -> if_stc','sentencia',1,'p_sentencia_expr','parser.py',22),
  ('sentencia -> expresionRelacional','sentencia',1,'p_sentencia_expr','parser.py',23),
  ('sentencia -> expresionLogica','sentencia',1,'p_sentencia_expr','parser.py',24),
  ('sentencia -> print_stc','sentencia',1,'p_sentencia_expr','parser.py',25),
  ('expresionLogica -> PARENIZQ expresiones OR expresiones PARENDER','expresionLogica',5,'p_expresion_logica','parser.py',30),
  ('expresionLogica -> PARENIZQ expresiones AND expresiones PARENDER','expresionLogica',5,'p_expresion_logica','parser.py',31),
  ('expresionLogica -> NOT PARENIZQ expresiones PARENDER','expresionLogica',4,'p_expresion_logica','parser.py',32),
  ('expresiones -> expresionRelacional','expresiones',1,'p_expresiones','parser.py',36),
  ('expresiones -> expresion','expresiones',1,'p_expresiones','parser.py',37),
  ('expresionRelacional -> expresion MAYORQUE expresion','expresionRelacional',3,'p_expresion_relacional','parser.py',40),
  ('expresionRelacional -> expresion MENORQUE expresion','expresionRelacional',3,'p_expresion_relacional','parser.py',41),
  ('expresionRelacional -> expresion MAYORIGUALQUE expresion','expresionRelacional',3,'p_expresion_relacional','parser.py',42),
  ('expresionRelacional -> expresion MENORIGUALQUE expresion','expresionRelacional',3,'p_expresion_relacional','parser.py',43),
  ('expresionRelacional -> expresion IN expresion','expresionRelacional',3,'p_expresion_relacional','parser.py',44),
  ('expresionRelacional -> expresion NOTIN expresion','expresionRelacional',3,'p_expresion_relacional','parser.py',45),
  ('expresionRelacional -> expresion IS expresion','expresionRelacional',3,'p_expresion_relacional','parser.py',46),
  ('expresionRelacional -> expresion ISNOT expresion','expresionRelacional',3,'p_expresion_relacional','parser.py',47),
  ('expresionRelacional -> expresion DIFERENTE expresion','expresionRelacional',3,'p_expresion_relacional','parser.py',48),
  ('expresionRelacional -> expresion DISTINTO expresion','expresionRelacional',3,'p_expresion_relacional','parser.py',49),
  ('expresionRelacional -> expresion IGUAL expresion','expresionRelacional',3,'p_expresion_relacional','parser.py',50),
  ('expresionRelacional -> expresion IGUALA expresion','expresionRelacional',3,'p_expresion_relacional','parser.py',51),
  ('expresion -> expresion SUMA expresion','expresion',3,'p_expresion_aritmetica','parser.py',55),
  ('expresion -> expresion RESTA expresion','expresion',3,'p_expresion_aritmetica','parser.py',56),
  ('expresion -> expresion MULTIPLICACION expresion','expresion',3,'p_expresion_aritmetica','parser.py',57),
  ('expresion -> expresion DIVISION expresion','expresion',3,'p_expresion_aritmetica','parser.py',58),
  ('test -> PARENIZQ expresiones PARENDER','test',3,'p_test','parser.py',69),
  ('if_stc -> IF test PUNTOS','if_stc',3,'p_if_stc','parser.py',72),
  ('else -> ELSE PUNTOS','else',2,'p_else_stc','parser.py',76),
  ('elif -> ELIF test PUNTOS','elif',3,'p_elif_stc','parser.py',80),
  ('print_stc -> PRINT PARENIZQ STRING PARENDER','print_stc',4,'p_print_stc','parser.py',84),
  ('expresion -> terminal','expresion',1,'p_expresion_terminal','parser.py',88),
  ('terminal -> NUMERO','terminal',1,'p_terminal_numero','parser.py',92),
  ('terminal -> IDENTIFICADOR','terminal',1,'p_terminal_variable','parser.py',96),
]
