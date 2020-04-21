
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CHAR COLON COMA COMMENT_TEXT CST_CHAR CST_FLOAT CST_INT CST_STRING DIVIDE DO ELSE EQUAL FLOAT FOR FUNCTION GT ID IF INT LEFTBRACE LEFTBRACK LEFTPAR LT MAIN MINUS MULTIPLY NOTEQUAL OR PERCENT PLUS PRINT PROGRAM READ RETURN RIGHTBRACE RIGHTBRACK RIGHTPAR SEMICOLON THEN TO VAR VOID WHILEprogram : PROGRAM ID SEMICOLON programVars programFunc mainprogramVars : vars\n                   | programFunc : function programFunc\n                   | main : MAIN LEFTPAR RIGHTPAR LEFTBRACE statement RIGHTBRACEassignment : ID EQUAL exp SEMICOLONdeclaration : VAR declarationPrimdeclarationPrim : primitive vars SEMICOLON declarationPrim\n                       | primitive : INT\n                 | FLOAT\n                 | CHAR return : RETURN LEFTPAR exp RIGHTPARif : IF LEFTPAR exp RIGHTPAR THEN LEFTBRACE statement RIGHTBRACE ifElseifElse : ELSE LEFTBRACE statement RIGHTBRACE\n              | comment : COMMENT_TEXTwhile : WHILE LEFTPAR exp RIGHTPAR DO statementfor : FOR declaration TO exp DO statementvars : ID varsArray SEMICOLONvarsComa : COMA vars\n                | varsArray : LEFTBRACK CST_INT RIGHTBRACK varsMatrix\n                 | varsComa varsMatrix : LEFTBRACK CST_INT RIGHTBRACK\n                  | varsComa function : functionType LEFTPAR param RIGHTPAR SEMICOLON LEFTBRACE statement RIGHTBRACE\n                | functionType LEFTPAR RIGHTPAR SEMICOLON LEFTBRACE statement RIGHTBRACEfunctionType : FUNCTION primitive\n                    | FUNCTION VOIDparam : primitive ID functionParamfunctionParam : COMA param\n                    | cst_prim : CST_INT\n                | CST_FLOAT\n                | CST_CHAR factor : LEFTPAR exp RIGHTPAR\n            | cst_prim\n            | module\n            | IDterm : factor termFunction\n            | factor termFunction : MULTIPLY term\n                    | DIVIDE term\n                    | exp : term expFunction\n            | term expFunction : PLUS exp\n                    | MINUS exp\n                    | read : READ LEFTPAR id_list RIGHTPARid_list : ID id_listFunctionid_listFunction : COMA id_list\n                        | print : PRINT LEFTPAR printFunction RIGHTPARprintFunction : print_param COMA printFunction2\n                    | print_param printFunction2 : printFunctionprint_param : exp\n                    | CST_STRING\n                    | ID statement : return\n                | if statementFunction\n                | comment statementFunction\n                | read statementFunction\n                | print statementFunction\n                | assignment statementFunction\n                | declaration statementFunction\n                | module statementFunctionstatementFunction : statementmodule : ID LEFTPAR moduleFunctionmoduleFunction : ID COMA moduleFunction\n                        | ID RIGHTPAR\n                        | exp COMA moduleFunction\n                        | exp RIGHTPAR'
    
_lr_action_items = {'CST_CHAR':([68,71,80,81,82,88,109,111,114,115,121,124,126,],[85,85,85,85,85,85,85,85,85,85,85,85,85,]),'LEFTBRACK':([6,28,],[8,33,]),'RETURN':([41,45,47,50,52,53,55,57,58,59,60,64,79,106,117,120,122,123,125,127,137,138,139,141,143,144,146,148,],[48,48,48,48,48,-18,48,48,48,48,-10,48,-8,-72,-52,-56,-10,-7,-76,-74,-9,-75,-73,48,-17,-15,48,-16,]),'THEN':([128,],[140,]),'READ':([41,45,47,50,52,53,55,57,58,59,60,64,79,106,117,120,122,123,125,127,137,138,139,141,143,144,146,148,],[49,49,49,49,49,-18,49,49,49,49,-10,49,-8,-72,-52,-56,-10,-7,-76,-74,-9,-75,-73,49,-17,-15,49,-16,]),'VOID':([13,],[22,]),'EQUAL':([61,],[80,]),'CHAR':([13,27,42,60,122,],[24,24,24,24,24,]),'COMA':([6,28,37,85,86,87,89,90,92,93,94,96,98,99,100,101,104,105,106,110,116,125,127,129,130,131,132,133,138,139,],[11,11,42,-37,-48,-39,-36,-40,-43,-35,-41,118,-61,121,-60,-41,124,126,-72,-47,-42,-76,-74,-49,-50,-38,-44,-45,-75,-73,]),'PROGRAM':([0,],[2,]),'PRINT':([41,45,47,50,52,53,55,57,58,59,60,64,79,106,117,120,122,123,125,127,137,138,139,141,143,144,146,148,],[51,51,51,51,51,-18,51,51,51,51,-10,51,-8,-72,-52,-56,-10,-7,-76,-74,-9,-75,-73,51,-17,-15,51,-16,]),'MINUS':([85,86,87,89,90,92,93,94,101,105,106,116,125,127,131,132,133,138,139,],[-37,111,-39,-36,-40,-43,-35,-41,-41,-41,-72,-42,-76,-74,-38,-44,-45,-75,-73,]),'COMMENT_TEXT':([41,45,47,50,52,53,55,57,58,59,60,64,79,106,117,120,122,123,125,127,137,138,139,141,143,144,146,148,],[53,53,53,53,53,-18,53,53,53,53,-10,53,-8,-72,-52,-56,-10,-7,-76,-74,-9,-75,-73,53,-17,-15,53,-16,]),'SEMICOLON':([3,6,9,10,17,18,28,32,34,35,38,46,85,86,87,89,90,92,93,94,102,103,106,110,116,125,127,129,130,131,132,133,138,139,],[4,-23,17,-25,-21,-22,-23,39,-27,-24,44,-26,-37,-48,-39,-36,-40,-43,-35,-41,122,123,-72,-47,-42,-76,-74,-49,-50,-38,-44,-45,-75,-73,]),'RIGHTPAR':([27,29,31,37,43,63,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,106,107,110,112,116,119,125,127,129,130,131,132,133,134,135,136,138,139,],[32,36,38,-34,-32,-33,-37,-48,-39,-36,-40,113,-43,-35,-41,117,-55,120,-61,-58,-60,-41,125,127,-72,128,-47,131,-42,-53,-76,-74,-49,-50,-38,-44,-45,-54,-59,-57,-75,-73,]),'CST_INT':([8,33,68,71,80,81,82,88,109,111,114,115,121,124,126,],[16,40,93,93,93,93,93,93,93,93,93,93,93,93,93,]),'PLUS':([85,86,87,89,90,92,93,94,101,105,106,116,125,127,131,132,133,138,139,],[-37,109,-39,-36,-40,-43,-35,-41,-41,-41,-72,-42,-76,-74,-38,-44,-45,-75,-73,]),'$end':([1,26,73,],[0,-1,-6,]),'FUNCTION':([4,5,7,12,17,84,108,],[-3,-2,13,13,-21,-29,-28,]),'RIGHTBRACK':([16,40,],[28,46,]),'DIVIDE':([85,87,89,90,92,93,94,101,105,106,125,127,131,138,139,],[-37,-39,-36,-40,115,-35,-41,-41,-41,-72,-76,-74,-38,-75,-73,]),'RIGHTBRACE':([54,56,65,66,67,70,72,74,75,76,77,83,113,142,147,],[73,-63,84,-65,-71,-70,-64,-67,-66,-68,-69,108,-14,143,148,]),'ELSE':([143,],[145,]),'VAR':([41,45,47,50,52,53,55,57,58,59,60,64,79,106,117,120,122,123,125,127,137,138,139,141,143,144,146,148,],[60,60,60,60,60,-18,60,60,60,60,-10,60,-8,-72,-52,-56,-10,-7,-76,-74,-9,-75,-73,60,-17,-15,60,-16,]),'ID':([2,4,11,21,23,24,30,41,45,47,50,52,53,55,57,58,59,60,64,68,69,71,78,79,80,81,82,88,106,109,111,114,115,117,118,120,121,122,123,124,125,126,127,137,138,139,141,143,144,146,148,],[3,6,6,-11,-12,-13,37,61,61,61,61,61,-18,61,61,61,61,-10,61,94,96,101,6,-8,94,105,94,94,-72,94,94,94,94,-52,96,-56,101,-10,-7,105,-76,105,-74,-9,-75,-73,61,-17,-15,61,-16,]),'IF':([41,45,47,50,52,53,55,57,58,59,60,64,79,106,117,120,122,123,125,127,137,138,139,141,143,144,146,148,],[62,62,62,62,62,-18,62,62,62,62,-10,62,-8,-72,-52,-56,-10,-7,-76,-74,-9,-75,-73,62,-17,-15,62,-16,]),'LEFTBRACE':([36,39,44,140,145,],[41,45,64,141,146,]),'MULTIPLY':([85,87,89,90,92,93,94,101,105,106,125,127,131,138,139,],[-37,-39,-36,-40,114,-35,-41,-41,-41,-72,-76,-74,-38,-75,-73,]),'INT':([13,27,42,60,122,],[21,21,21,21,21,]),'FLOAT':([13,27,42,60,122,],[23,23,23,23,23,]),'LEFTPAR':([15,20,21,22,23,24,25,48,49,51,61,62,68,71,80,81,82,88,94,101,105,109,111,114,115,121,124,126,],[27,-30,-11,-31,-12,-13,29,68,69,71,81,82,88,88,88,88,88,88,81,81,81,88,88,88,88,88,88,88,]),'CST_FLOAT':([68,71,80,81,82,88,109,111,114,115,121,124,126,],[89,89,89,89,89,89,89,89,89,89,89,89,89,]),'CST_STRING':([71,121,],[98,98,]),'MAIN':([4,5,7,12,14,17,19,84,108,],[-3,-2,-5,-5,25,-21,-4,-29,-28,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'comment':([41,45,47,50,52,55,57,58,59,64,141,146,],[47,47,47,47,47,47,47,47,47,47,47,47,]),'printFunction':([71,121,],[97,135,]),'primitive':([13,27,42,60,122,],[20,30,30,78,78,]),'vars':([4,11,78,],[5,18,102,]),'statementFunction':([47,50,52,55,57,58,59,],[66,70,72,74,75,76,77,]),'cst_prim':([68,71,80,81,82,88,109,111,114,115,121,124,126,],[87,87,87,87,87,87,87,87,87,87,87,87,87,]),'module':([41,45,47,50,52,55,57,58,59,64,68,71,80,81,82,88,109,111,114,115,121,124,126,141,146,],[50,50,50,50,50,50,50,50,50,50,90,90,90,90,90,90,90,90,90,90,90,90,90,50,50,]),'id_list':([69,118,],[95,134,]),'expFunction':([86,],[110,]),'ifElse':([143,],[144,]),'programVars':([4,],[7,]),'print_param':([71,121,],[99,99,]),'printFunction2':([121,],[136,]),'functionParam':([37,],[43,]),'if':([41,45,47,50,52,55,57,58,59,64,141,146,],[52,52,52,52,52,52,52,52,52,52,52,52,]),'declarationPrim':([60,122,],[79,137,]),'id_listFunction':([96,],[119,]),'param':([27,42,],[31,63,]),'program':([0,],[1,]),'programFunc':([7,12,],[14,19,]),'statement':([41,45,47,50,52,55,57,58,59,64,141,146,],[54,65,67,67,67,67,67,67,67,83,142,147,]),'factor':([68,71,80,81,82,88,109,111,114,115,121,124,126,],[92,92,92,92,92,92,92,92,92,92,92,92,92,]),'print':([41,45,47,50,52,55,57,58,59,64,141,146,],[55,55,55,55,55,55,55,55,55,55,55,55,]),'main':([14,],[26,]),'termFunction':([92,],[116,]),'moduleFunction':([81,124,126,],[106,138,139,]),'function':([7,12,],[12,12,]),'return':([41,45,47,50,52,55,57,58,59,64,141,146,],[56,56,56,56,56,56,56,56,56,56,56,56,]),'read':([41,45,47,50,52,55,57,58,59,64,141,146,],[57,57,57,57,57,57,57,57,57,57,57,57,]),'assignment':([41,45,47,50,52,55,57,58,59,64,141,146,],[58,58,58,58,58,58,58,58,58,58,58,58,]),'varsComa':([6,28,],[10,34,]),'declaration':([41,45,47,50,52,55,57,58,59,64,141,146,],[59,59,59,59,59,59,59,59,59,59,59,59,]),'varsMatrix':([28,],[35,]),'functionType':([7,12,],[15,15,]),'term':([68,71,80,81,82,88,109,111,114,115,121,124,126,],[86,86,86,86,86,86,86,86,132,133,86,86,86,]),'varsArray':([6,],[9,]),'exp':([68,71,80,81,82,88,109,111,121,124,126,],[91,100,103,104,107,112,129,130,100,104,104,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMICOLON programVars programFunc main','program',6,'p_program','lexerparser.py',123),
  ('programVars -> vars','programVars',1,'p_programVars','lexerparser.py',127),
  ('programVars -> <empty>','programVars',0,'p_programVars','lexerparser.py',128),
  ('programFunc -> function programFunc','programFunc',2,'p_programFunc','lexerparser.py',131),
  ('programFunc -> <empty>','programFunc',0,'p_programFunc','lexerparser.py',132),
  ('main -> MAIN LEFTPAR RIGHTPAR LEFTBRACE statement RIGHTBRACE','main',6,'p_main','lexerparser.py',135),
  ('assignment -> ID EQUAL exp SEMICOLON','assignment',4,'p_assignment','lexerparser.py',138),
  ('declaration -> VAR declarationPrim','declaration',2,'p_declaration','lexerparser.py',141),
  ('declarationPrim -> primitive vars SEMICOLON declarationPrim','declarationPrim',4,'p_declarationPrim','lexerparser.py',144),
  ('declarationPrim -> <empty>','declarationPrim',0,'p_declarationPrim','lexerparser.py',145),
  ('primitive -> INT','primitive',1,'p_primitive','lexerparser.py',148),
  ('primitive -> FLOAT','primitive',1,'p_primitive','lexerparser.py',149),
  ('primitive -> CHAR','primitive',1,'p_primitive','lexerparser.py',150),
  ('return -> RETURN LEFTPAR exp RIGHTPAR','return',4,'p_return','lexerparser.py',153),
  ('if -> IF LEFTPAR exp RIGHTPAR THEN LEFTBRACE statement RIGHTBRACE ifElse','if',9,'p_if','lexerparser.py',156),
  ('ifElse -> ELSE LEFTBRACE statement RIGHTBRACE','ifElse',4,'p_ifElse','lexerparser.py',159),
  ('ifElse -> <empty>','ifElse',0,'p_ifElse','lexerparser.py',160),
  ('comment -> COMMENT_TEXT','comment',1,'p_comment','lexerparser.py',163),
  ('while -> WHILE LEFTPAR exp RIGHTPAR DO statement','while',6,'p_while','lexerparser.py',166),
  ('for -> FOR declaration TO exp DO statement','for',6,'p_for','lexerparser.py',169),
  ('vars -> ID varsArray SEMICOLON','vars',3,'p_vars','lexerparser.py',172),
  ('varsComa -> COMA vars','varsComa',2,'p_varsComa','lexerparser.py',175),
  ('varsComa -> <empty>','varsComa',0,'p_varsComa','lexerparser.py',176),
  ('varsArray -> LEFTBRACK CST_INT RIGHTBRACK varsMatrix','varsArray',4,'p_varsArray','lexerparser.py',179),
  ('varsArray -> varsComa','varsArray',1,'p_varsArray','lexerparser.py',180),
  ('varsMatrix -> LEFTBRACK CST_INT RIGHTBRACK','varsMatrix',3,'p_varsMatrix','lexerparser.py',183),
  ('varsMatrix -> varsComa','varsMatrix',1,'p_varsMatrix','lexerparser.py',184),
  ('function -> functionType LEFTPAR param RIGHTPAR SEMICOLON LEFTBRACE statement RIGHTBRACE','function',8,'p_function','lexerparser.py',187),
  ('function -> functionType LEFTPAR RIGHTPAR SEMICOLON LEFTBRACE statement RIGHTBRACE','function',7,'p_function','lexerparser.py',188),
  ('functionType -> FUNCTION primitive','functionType',2,'p_functionType','lexerparser.py',191),
  ('functionType -> FUNCTION VOID','functionType',2,'p_functionType','lexerparser.py',192),
  ('param -> primitive ID functionParam','param',3,'p_param','lexerparser.py',195),
  ('functionParam -> COMA param','functionParam',2,'p_functionParam','lexerparser.py',198),
  ('functionParam -> <empty>','functionParam',0,'p_functionParam','lexerparser.py',199),
  ('cst_prim -> CST_INT','cst_prim',1,'p_cst_prim','lexerparser.py',202),
  ('cst_prim -> CST_FLOAT','cst_prim',1,'p_cst_prim','lexerparser.py',203),
  ('cst_prim -> CST_CHAR','cst_prim',1,'p_cst_prim','lexerparser.py',204),
  ('factor -> LEFTPAR exp RIGHTPAR','factor',3,'p_factor','lexerparser.py',207),
  ('factor -> cst_prim','factor',1,'p_factor','lexerparser.py',208),
  ('factor -> module','factor',1,'p_factor','lexerparser.py',209),
  ('factor -> ID','factor',1,'p_factor','lexerparser.py',210),
  ('term -> factor termFunction','term',2,'p_term','lexerparser.py',213),
  ('term -> factor','term',1,'p_term','lexerparser.py',214),
  ('termFunction -> MULTIPLY term','termFunction',2,'p_termFunction','lexerparser.py',217),
  ('termFunction -> DIVIDE term','termFunction',2,'p_termFunction','lexerparser.py',218),
  ('termFunction -> <empty>','termFunction',0,'p_termFunction','lexerparser.py',219),
  ('exp -> term expFunction','exp',2,'p_exp','lexerparser.py',222),
  ('exp -> term','exp',1,'p_exp','lexerparser.py',223),
  ('expFunction -> PLUS exp','expFunction',2,'p_expFunction','lexerparser.py',226),
  ('expFunction -> MINUS exp','expFunction',2,'p_expFunction','lexerparser.py',227),
  ('expFunction -> <empty>','expFunction',0,'p_expFunction','lexerparser.py',228),
  ('read -> READ LEFTPAR id_list RIGHTPAR','read',4,'p_read','lexerparser.py',231),
  ('id_list -> ID id_listFunction','id_list',2,'p_id_list','lexerparser.py',234),
  ('id_listFunction -> COMA id_list','id_listFunction',2,'p_id_listFunction','lexerparser.py',237),
  ('id_listFunction -> <empty>','id_listFunction',0,'p_id_listFunction','lexerparser.py',238),
  ('print -> PRINT LEFTPAR printFunction RIGHTPAR','print',4,'p_print','lexerparser.py',241),
  ('printFunction -> print_param COMA printFunction2','printFunction',3,'p_printFunction','lexerparser.py',244),
  ('printFunction -> print_param','printFunction',1,'p_printFunction','lexerparser.py',245),
  ('printFunction2 -> printFunction','printFunction2',1,'p_printFunction2','lexerparser.py',247),
  ('print_param -> exp','print_param',1,'p_print_param','lexerparser.py',250),
  ('print_param -> CST_STRING','print_param',1,'p_print_param','lexerparser.py',251),
  ('print_param -> ID','print_param',1,'p_print_param','lexerparser.py',252),
  ('statement -> return','statement',1,'p_statement','lexerparser.py',255),
  ('statement -> if statementFunction','statement',2,'p_statement','lexerparser.py',256),
  ('statement -> comment statementFunction','statement',2,'p_statement','lexerparser.py',257),
  ('statement -> read statementFunction','statement',2,'p_statement','lexerparser.py',258),
  ('statement -> print statementFunction','statement',2,'p_statement','lexerparser.py',259),
  ('statement -> assignment statementFunction','statement',2,'p_statement','lexerparser.py',260),
  ('statement -> declaration statementFunction','statement',2,'p_statement','lexerparser.py',261),
  ('statement -> module statementFunction','statement',2,'p_statement','lexerparser.py',262),
  ('statementFunction -> statement','statementFunction',1,'p_statementFunction','lexerparser.py',265),
  ('module -> ID LEFTPAR moduleFunction','module',3,'p_module','lexerparser.py',268),
  ('moduleFunction -> ID COMA moduleFunction','moduleFunction',3,'p_moduleFunction','lexerparser.py',271),
  ('moduleFunction -> ID RIGHTPAR','moduleFunction',2,'p_moduleFunction','lexerparser.py',272),
  ('moduleFunction -> exp COMA moduleFunction','moduleFunction',3,'p_moduleFunction','lexerparser.py',273),
  ('moduleFunction -> exp RIGHTPAR','moduleFunction',2,'p_moduleFunction','lexerparser.py',274),
]
