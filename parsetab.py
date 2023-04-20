
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACH APOSTROFE APR ASPA ATC ATO BIN BOOLEAN CHAR COMMENT DATE_FULLYEAR DATE_MDAY DATE_MONTH DOT_SEP ESCAPE ESC_BACKSPACE ESC_CRETURN ESC_FF ESC_HEX4 ESC_HEX8 ESC_NL ESC_QUOTE ESC_REVERSE ESC_TAB FCH FLOAT FPR HEX IGUAL INF INTEGER MINUS NAN NEWLINE OCT PLUS TIME_DELIM TIME_HOUR TIME_MIN TIME_SEC TIME_SECFRAC UNDERSC0RE UNDERSCORE VIRGULA WHITESPACETOML : EXPRESSION TOML2TOML2 : NEWLINE EXPRESSION TOML2TOML2 :EXPRESSION : KVALUE EXPRESSION2EXPRESSION : EXPRESSION2EXPRESSION : TABLE EXPRESSION2EXPRESSION2 :EXPRESSION2 : COMMENTKVALUE : KEY kvwhitespace IGUAL kvwhitespace VALUEkvwhitespace : WHITESPACEkvwhitespace :KEY : SIMPLEKEYKEY : DOTKEYSIMPLEKEY : QUOTEDKEYSIMPLEKEY : UNQUOTEDKEYUNQUOTEDKEY : OCCURRENCES UNQUOTEDKEYAUXUNQUOTEDKEYAUX : OCCURRENCES UNQUOTEDKEYAUXUNQUOTEDKEYAUX :OCCURRENCES : CHAROCCURRENCES : INTEGEROCCURRENCES : MINUSOCCURRENCES : UNDERSCOREQUOTEDKEY : BASICSTRINGQUOTEDKEY : LITERALSTRINGDOTKEY : SIMPLEKEY DOT_SEP SIMPLEKEY DOTSIMPKEYDOTSIMPKEY : DOT_SEP SIMPLEKEY DOTSIMPKEYDOTSIMPKEY : VALUE : STRINGVALUE : BOOLEANVALUE : INTEGERVALUE : ARRAYVALUE : FLOATSTRING : MULTILINEBASICSTRINGSTRING : BASICSTRINGSTRING : MLLITERALSTRINGSTRING : LITERALSTRINGBASICSTRING : ASPA BC ASPABC : BASICCHAR BCBC : BASICCHAR : BASICUNESCAPEDBASICCHAR : ESCAPEDBASICUNESCAPED : WHITESPACEBASICUNESCAPED : CHARBASICUNESCAPED : INTEGERBASICUNESCAPED : MINUSBASICUNESCAPED : APOSTROFEBASICUNESCAPED : ESCAPEDBASICUNESCAPED : DOT_SEPESCAPED : ESC_QUOTEESCAPED : ESC_REVERSEESCAPED : ESC_BACKSPACEESCAPED : ESC_FFESCAPED : ESC_NLESCAPED : ESC_CRETURNESCAPED : ESC_TABESCAPED : ESC_HEX4ESCAPED : ESC_HEX8MULTILINEBASICSTRING : MLBCSTRDELIM MLNL MLBASICBODY MLBCSTRDELIMMLNL : NEWLINEMLBCSTRDELIM : ASPA ASPA ASPAMLBASICBODY : MLBC MLBQC MLQMLBC : MLBCONTENT MLBCMLBC : MLBQC : MLBQUOTES MLBCONTENT MLBC2 MLBQCMLBQC : MLBC2 : MLBCONTENT MLBC2MLBC2 : MLQ : MLBQUOTESMLQ : MLBCONTENT : MLBCHARMLBCONTENT : NEWLINEMLBCONTENT : MLBESCAPEDNLMLBCHAR : MLBUNESCAPEDMLBCHAR : ESCAPEDMLBQUOTES : ASPAMLBQUOTES : ASPA ASPAMLBUNESCAPED : WHITESPACEMLBUNESCAPED : CHARMLBESCAPEDNL : ESCAPE WHITESPACE NEWLINE WHNLWHNL : SPACENEWLINE WHNLWHNL : SPACENEWLINE : WHITESPACESPACENEWLINE : NEWLINELITERALSTRING : APOSTROFE LCH APOSTROFELCH : LITERALCHAR LCHLCH : LITERALCHAR : CHARLITERALCHAR : ESCAPEDMLLITERALSTRING : MLLITERALSTRINGDELIM NLR MLLITERALBODY NLR MLLITERALSTRINGDELIMNLR : NEWLINENLR :MLLITERALSTRINGDELIM : APOSTROFE APOSTROFE APOSTROFEMLLITERALBODY : MLLC MLLQC MLLQMLLC : MLLCONTENT MLLCMLLC :MLLQC :MLLQC : MLLQUOTES MLLCONTENT MLLC2 MLLQCMLLC2 : MLLCONTENT MLLC2MLLC2 : MLLQ :MLLQ : MLLQUOTESMLLCONTENT : MLLCHARMLLCONTENT : NEWLINEMLLCHAR : CHARMLLQUOTES : APOSTROFE APOSTROFEMLLQUOTES : APOSTROFEARRAY : APR ARRAYVALUES WSCOMMENTNEWLINE FPRARRAYVALUES :ARRAYVALUES : WSCOMMENTNEWLINE VALUE ARRAYCONTEUDOARRAYCONTEUDO :ARRAYCONTEUDO : WSCOMMENTNEWLINE VIRGULA ARRAYVALUESWSCOMMENTNEWLINE :WSCOMMENTNEWLINE : INNERCOMMENT WSCOMMENTNEWLINEINNERCOMMENT : WHITESPACEINNERCOMMENT : COMMENTOUNAO NEWLINECOMMENTOUNAO : COMMENTCOMMENTOUNAO :TABLE : APR KEY FPR'
    
_lr_action_items = {'NEWLINE':([0,2,3,4,5,7,23,24,25,42,43,44,45,46,47,48,49,50,55,57,60,62,68,69,70,71,72,73,74,75,76,77,78,79,81,84,86,87,88,89,90,91,93,94,98,100,103,104,105,106,107,108,110,111,112,113,114,115,116,117,118,119,120,122,123,126,127,129,131,132,133,134,135,138,139,140,141,143,144,145,146,147,148,150,151,152,153,154,155,158,159,160,],[-7,23,-7,-5,-7,-8,-7,-4,-6,-49,-50,-51,-52,-53,-54,-55,-56,-57,23,-118,-37,-84,-9,-28,-29,-30,-31,-32,-33,-34,-35,-36,-108,91,94,-117,-117,-114,100,-116,105,-59,117,-90,-110,-115,105,-70,-71,-72,-73,-74,-77,-78,-60,94,-96,117,-102,-103,-104,-92,-107,-109,-58,105,-75,140,-100,117,-106,-94,-108,105,-76,151,-89,-93,-101,117,-105,-111,105,-82,-83,-79,151,117,-96,-80,-98,-97,]),'$end':([0,1,2,3,4,5,7,22,23,24,25,55,57,60,62,64,68,69,70,71,72,73,74,75,76,77,112,119,120,123,141,],[-7,0,-3,-7,-5,-7,-8,-1,-7,-4,-6,-3,-118,-37,-84,-2,-9,-28,-29,-30,-31,-32,-33,-34,-35,-36,-60,-92,-107,-58,-89,]),'COMMENT':([0,3,5,23,57,60,62,68,69,70,71,72,73,74,75,76,77,78,84,86,87,98,100,112,119,120,122,123,135,141,147,],[7,7,7,7,-118,-37,-84,-9,-28,-29,-30,-31,-32,-33,-34,-35,-36,89,89,89,-114,89,-115,-60,-92,-107,-109,-58,89,-89,-111,]),'APR':([0,23,27,56,65,78,85,86,87,99,100,135,],[8,8,-10,-11,78,-112,78,-112,-114,-113,-115,-112,]),'ASPA':([0,8,16,23,27,29,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,56,61,65,66,78,80,85,86,87,90,91,92,99,100,101,102,103,104,105,106,107,108,110,111,124,125,127,128,135,136,137,138,139,140,148,149,150,151,152,153,156,157,158,],[16,16,-39,16,-10,16,60,-39,-40,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-11,-38,80,16,-112,92,80,-112,-114,-63,-59,112,-113,-115,124,127,-63,-70,-71,-72,-73,-74,-77,-78,92,127,139,-62,-112,-61,-68,-67,-76,-81,-67,127,-82,-83,-79,-81,-66,-64,-80,]),'APOSTROFE':([0,8,16,17,23,27,29,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,56,63,65,66,78,80,81,82,85,86,87,93,94,95,99,100,113,114,115,116,117,118,119,130,131,133,134,135,142,143,144,145,146,154,155,159,160,],[17,17,40,-86,17,-10,17,40,-40,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,62,-86,-87,-88,-11,-85,82,17,-112,40,-91,95,82,-112,-114,-95,-90,119,-113,-115,-91,133,-95,-102,-103,-104,-92,142,133,146,-94,-112,95,-93,-101,-99,-105,-99,133,-98,-97,]),'CHAR':([0,8,15,16,17,18,19,20,21,23,29,30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,66,80,81,82,90,91,93,94,103,104,105,106,107,108,110,111,115,116,117,118,119,126,127,132,133,138,139,140,145,146,148,150,151,152,153,154,158,],[18,18,18,37,53,-19,-20,-21,-22,18,18,18,37,-40,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,53,-87,-88,18,37,-91,53,111,-59,118,-90,111,-70,-71,-72,-73,-74,-77,-78,118,-102,-103,-104,-92,111,-75,118,-106,111,-76,-81,118,-105,111,-82,-83,-79,-81,118,-80,]),'INTEGER':([0,8,15,16,18,19,20,21,23,27,29,30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,56,65,66,78,80,85,86,87,99,100,135,],[19,19,19,38,-19,-20,-21,-22,19,-10,19,19,38,-40,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-11,71,19,-112,38,71,-112,-114,-113,-115,-112,]),'MINUS':([0,8,15,16,18,19,20,21,23,29,30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,66,80,],[20,20,20,39,-19,-20,-21,-22,20,20,20,39,-40,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,20,39,]),'UNDERSCORE':([0,8,15,18,19,20,21,23,29,30,66,],[21,21,21,-19,-20,-21,-22,21,21,21,21,]),'WHITESPACE':([6,9,10,11,12,13,14,15,16,18,19,20,21,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,56,58,59,60,62,67,69,70,71,72,73,74,75,76,77,78,80,83,84,86,87,90,91,96,98,100,103,104,105,106,107,108,109,110,111,112,119,120,122,123,126,127,135,138,139,140,141,147,148,150,151,152,153,158,],[27,-12,-13,-14,-15,-23,-24,-18,36,-19,-20,-21,-22,-18,-16,36,-40,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,27,-27,-17,-37,-84,-25,-28,-29,-30,-31,-32,-33,-34,-35,-36,87,36,-27,87,87,-114,110,-59,-26,87,-115,110,-70,-71,-72,-73,-74,129,-77,-78,-60,-92,-107,-109,-58,110,-75,87,110,-76,150,-89,-111,110,-82,-83,-79,150,-80,]),'IGUAL':([6,9,10,11,12,13,14,15,18,19,20,21,26,27,30,31,58,59,60,62,67,83,96,],[-11,-12,-13,-14,-15,-23,-24,-18,-19,-20,-21,-22,56,-10,-18,-16,-27,-17,-37,-84,-25,-27,-26,]),'FPR':([9,10,11,12,13,14,15,18,19,20,21,28,30,31,58,59,60,62,67,69,70,71,72,73,74,75,76,77,78,83,84,86,87,96,97,98,99,100,112,119,120,122,123,135,141,147,],[-12,-13,-14,-15,-23,-24,-18,-19,-20,-21,-22,57,-18,-16,-27,-17,-37,-84,-25,-28,-29,-30,-31,-32,-33,-34,-35,-36,-108,-27,-112,-112,-114,-26,120,-110,-113,-115,-60,-92,-107,-109,-58,-108,-89,-111,]),'DOT_SEP':([9,11,12,13,14,15,16,18,19,20,21,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,58,59,60,62,80,83,],[29,-14,-15,-23,-24,-18,41,-19,-20,-21,-22,-18,-16,41,-40,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,66,-17,-37,-84,41,66,]),'ESC_QUOTE':([16,17,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,80,82,90,91,103,104,105,106,107,108,110,111,126,127,138,139,140,148,150,151,152,153,158,],[42,42,42,-40,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,42,-87,-88,42,42,42,-59,42,-70,-71,-72,-73,-74,-77,-78,42,-75,42,-76,-81,42,-82,-83,-79,-81,-80,]),'ESC_REVERSE':([16,17,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,80,82,90,91,103,104,105,106,107,108,110,111,126,127,138,139,140,148,150,151,152,153,158,],[43,43,43,-40,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,43,-87,-88,43,43,43,-59,43,-70,-71,-72,-73,-74,-77,-78,43,-75,43,-76,-81,43,-82,-83,-79,-81,-80,]),'ESC_BACKSPACE':([16,17,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,80,82,90,91,103,104,105,106,107,108,110,111,126,127,138,139,140,148,150,151,152,153,158,],[44,44,44,-40,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,44,-87,-88,44,44,44,-59,44,-70,-71,-72,-73,-74,-77,-78,44,-75,44,-76,-81,44,-82,-83,-79,-81,-80,]),'ESC_FF':([16,17,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,80,82,90,91,103,104,105,106,107,108,110,111,126,127,138,139,140,148,150,151,152,153,158,],[45,45,45,-40,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,45,-87,-88,45,45,45,-59,45,-70,-71,-72,-73,-74,-77,-78,45,-75,45,-76,-81,45,-82,-83,-79,-81,-80,]),'ESC_NL':([16,17,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,80,82,90,91,103,104,105,106,107,108,110,111,126,127,138,139,140,148,150,151,152,153,158,],[46,46,46,-40,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,46,-87,-88,46,46,46,-59,46,-70,-71,-72,-73,-74,-77,-78,46,-75,46,-76,-81,46,-82,-83,-79,-81,-80,]),'ESC_CRETURN':([16,17,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,80,82,90,91,103,104,105,106,107,108,110,111,126,127,138,139,140,148,150,151,152,153,158,],[47,47,47,-40,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,47,-87,-88,47,47,47,-59,47,-70,-71,-72,-73,-74,-77,-78,47,-75,47,-76,-81,47,-82,-83,-79,-81,-80,]),'ESC_TAB':([16,17,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,80,82,90,91,103,104,105,106,107,108,110,111,126,127,138,139,140,148,150,151,152,153,158,],[48,48,48,-40,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,48,-87,-88,48,48,48,-59,48,-70,-71,-72,-73,-74,-77,-78,48,-75,48,-76,-81,48,-82,-83,-79,-81,-80,]),'ESC_HEX4':([16,17,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,80,82,90,91,103,104,105,106,107,108,110,111,126,127,138,139,140,148,150,151,152,153,158,],[49,49,49,-40,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,49,-87,-88,49,49,49,-59,49,-70,-71,-72,-73,-74,-77,-78,49,-75,49,-76,-81,49,-82,-83,-79,-81,-80,]),'ESC_HEX8':([16,17,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,80,82,90,91,103,104,105,106,107,108,110,111,126,127,138,139,140,148,150,151,152,153,158,],[50,50,50,-40,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,50,-87,-88,50,50,50,-59,50,-70,-71,-72,-73,-74,-77,-78,50,-75,50,-76,-81,50,-82,-83,-79,-81,-80,]),'BOOLEAN':([27,56,65,78,85,86,87,99,100,135,],[-10,-11,70,-112,70,-112,-114,-113,-115,-112,]),'FLOAT':([27,56,65,78,85,86,87,99,100,135,],[-10,-11,73,-112,73,-112,-114,-113,-115,-112,]),'ESCAPE':([42,43,44,45,46,47,48,49,50,90,91,103,104,105,106,107,108,110,111,126,127,138,139,140,148,150,151,152,153,158,],[-49,-50,-51,-52,-53,-54,-55,-56,-57,109,-59,109,-70,-71,-72,-73,-74,-77,-78,109,-75,109,-76,-81,109,-82,-83,-79,-81,-80,]),'VIRGULA':([60,62,69,70,71,72,73,74,75,76,77,86,87,98,99,100,112,119,120,121,123,141,],[-37,-84,-28,-29,-30,-31,-32,-33,-34,-35,-36,-112,-114,-112,-113,-115,-60,-92,-107,135,-58,-89,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'TOML':([0,],[1,]),'EXPRESSION':([0,23,],[2,55,]),'KVALUE':([0,23,],[3,3,]),'EXPRESSION2':([0,3,5,23,],[4,24,25,4,]),'TABLE':([0,23,],[5,5,]),'KEY':([0,8,23,],[6,28,6,]),'SIMPLEKEY':([0,8,23,29,66,],[9,9,9,58,83,]),'DOTKEY':([0,8,23,],[10,10,10,]),'QUOTEDKEY':([0,8,23,29,66,],[11,11,11,11,11,]),'UNQUOTEDKEY':([0,8,23,29,66,],[12,12,12,12,12,]),'BASICSTRING':([0,8,23,29,65,66,85,],[13,13,13,13,75,13,75,]),'LITERALSTRING':([0,8,23,29,65,66,85,],[14,14,14,14,77,14,77,]),'OCCURRENCES':([0,8,15,23,29,30,66,],[15,15,30,15,15,30,15,]),'TOML2':([2,55,],[22,64,]),'kvwhitespace':([6,56,],[26,65,]),'UNQUOTEDKEYAUX':([15,30,],[31,59,]),'BC':([16,33,80,],[32,61,32,]),'BASICCHAR':([16,33,80,],[33,33,33,]),'BASICUNESCAPED':([16,33,80,],[34,34,34,]),'ESCAPED':([16,17,33,52,80,82,90,103,126,138,148,],[35,54,35,54,35,54,108,108,108,108,108,]),'LCH':([17,52,82,],[51,63,51,]),'LITERALCHAR':([17,52,82,],[52,52,52,]),'DOTSIMPKEY':([58,83,],[67,96,]),'VALUE':([65,85,],[68,98,]),'STRING':([65,85,],[69,69,]),'ARRAY':([65,85,],[72,72,]),'MULTILINEBASICSTRING':([65,85,],[74,74,]),'MLLITERALSTRING':([65,85,],[76,76,]),'MLBCSTRDELIM':([65,85,101,],[79,79,123,]),'MLLITERALSTRINGDELIM':([65,85,130,],[81,81,141,]),'ARRAYVALUES':([78,135,],[84,147,]),'WSCOMMENTNEWLINE':([78,84,86,98,135,],[85,97,99,121,85,]),'INNERCOMMENT':([78,84,86,98,135,],[86,86,86,86,86,]),'COMMENTOUNAO':([78,84,86,98,135,],[88,88,88,88,88,]),'MLNL':([79,],[90,]),'NLR':([81,113,],[93,130,]),'MLBASICBODY':([90,],[101,]),'MLBC':([90,103,],[102,128,]),'MLBCONTENT':([90,103,126,138,148,],[103,103,138,148,148,]),'MLBCHAR':([90,103,126,138,148,],[104,104,104,104,104,]),'MLBESCAPEDNL':([90,103,126,138,148,],[106,106,106,106,106,]),'MLBUNESCAPED':([90,103,126,138,148,],[107,107,107,107,107,]),'MLLITERALBODY':([93,],[113,]),'MLLC':([93,115,],[114,134,]),'MLLCONTENT':([93,115,132,145,154,],[115,115,145,154,154,]),'MLLCHAR':([93,115,132,145,154,],[116,116,116,116,116,]),'ARRAYCONTEUDO':([98,],[122,]),'MLBQC':([102,149,],[125,157,]),'MLBQUOTES':([102,125,149,],[126,137,126,]),'MLLQC':([114,155,],[131,160,]),'MLLQUOTES':([114,131,155,],[132,144,132,]),'MLQ':([125,],[136,]),'MLLQ':([131,],[143,]),'MLBC2':([138,148,],[149,156,]),'WHNL':([140,153,],[152,158,]),'SPACENEWLINE':([140,153,],[153,153,]),'MLLC2':([145,154,],[155,159,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> TOML","S'",1,None,None,None),
  ('TOML -> EXPRESSION TOML2','TOML',2,'p_TOML','tomlex.py',112),
  ('TOML2 -> NEWLINE EXPRESSION TOML2','TOML2',3,'p_TOML2','tomlex.py',116),
  ('TOML2 -> <empty>','TOML2',0,'p_TOML3','tomlex.py',120),
  ('EXPRESSION -> KVALUE EXPRESSION2','EXPRESSION',2,'p_EXPRESSION2','tomlex.py',124),
  ('EXPRESSION -> EXPRESSION2','EXPRESSION',1,'p_EXPRESSION1','tomlex.py',128),
  ('EXPRESSION -> TABLE EXPRESSION2','EXPRESSION',2,'p_EXPRESSION3','tomlex.py',132),
  ('EXPRESSION2 -> <empty>','EXPRESSION2',0,'p_EXPRESSION2_2','tomlex.py',136),
  ('EXPRESSION2 -> COMMENT','EXPRESSION2',1,'p_EXPRESSION2_1','tomlex.py',140),
  ('KVALUE -> KEY kvwhitespace IGUAL kvwhitespace VALUE','KVALUE',5,'p_KVALUE','tomlex.py',144),
  ('kvwhitespace -> WHITESPACE','kvwhitespace',1,'p_kvwhitespace1','tomlex.py',148),
  ('kvwhitespace -> <empty>','kvwhitespace',0,'p_kvwhitespace2','tomlex.py',152),
  ('KEY -> SIMPLEKEY','KEY',1,'p_KEY1','tomlex.py',156),
  ('KEY -> DOTKEY','KEY',1,'p_KEY2','tomlex.py',160),
  ('SIMPLEKEY -> QUOTEDKEY','SIMPLEKEY',1,'p_SIMPLEKEY1','tomlex.py',164),
  ('SIMPLEKEY -> UNQUOTEDKEY','SIMPLEKEY',1,'p_SIMPLEKEY2','tomlex.py',168),
  ('UNQUOTEDKEY -> OCCURRENCES UNQUOTEDKEYAUX','UNQUOTEDKEY',2,'p_UNQUOTEDKEY1','tomlex.py',172),
  ('UNQUOTEDKEYAUX -> OCCURRENCES UNQUOTEDKEYAUX','UNQUOTEDKEYAUX',2,'p_UNQUOTEDKEY2','tomlex.py',176),
  ('UNQUOTEDKEYAUX -> <empty>','UNQUOTEDKEYAUX',0,'p_UNQUOTEDKEY3','tomlex.py',180),
  ('OCCURRENCES -> CHAR','OCCURRENCES',1,'p_OCCURRENCES1','tomlex.py',184),
  ('OCCURRENCES -> INTEGER','OCCURRENCES',1,'p_OCCURRENCES2','tomlex.py',188),
  ('OCCURRENCES -> MINUS','OCCURRENCES',1,'p_OCCURRENCES3','tomlex.py',192),
  ('OCCURRENCES -> UNDERSCORE','OCCURRENCES',1,'p_OCCURRENCES4','tomlex.py',196),
  ('QUOTEDKEY -> BASICSTRING','QUOTEDKEY',1,'p_QUOTEDKEY1','tomlex.py',200),
  ('QUOTEDKEY -> LITERALSTRING','QUOTEDKEY',1,'p_QUOTEDKEY2','tomlex.py',204),
  ('DOTKEY -> SIMPLEKEY DOT_SEP SIMPLEKEY DOTSIMPKEY','DOTKEY',4,'p_DOTKEY','tomlex.py',208),
  ('DOTSIMPKEY -> DOT_SEP SIMPLEKEY DOTSIMPKEY','DOTSIMPKEY',3,'p_DOTSIMPKEY1','tomlex.py',212),
  ('DOTSIMPKEY -> <empty>','DOTSIMPKEY',0,'p_DOTSIMPKEY2','tomlex.py',216),
  ('VALUE -> STRING','VALUE',1,'p_VALUE1','tomlex.py',220),
  ('VALUE -> BOOLEAN','VALUE',1,'p_VALUE2','tomlex.py',224),
  ('VALUE -> INTEGER','VALUE',1,'p_VALUE3','tomlex.py',228),
  ('VALUE -> ARRAY','VALUE',1,'p_VALUE4','tomlex.py',232),
  ('VALUE -> FLOAT','VALUE',1,'p_VALUE7','tomlex.py',244),
  ('STRING -> MULTILINEBASICSTRING','STRING',1,'p_STRING1','tomlex.py',248),
  ('STRING -> BASICSTRING','STRING',1,'p_STRING2','tomlex.py',252),
  ('STRING -> MLLITERALSTRING','STRING',1,'p_STRING3','tomlex.py',256),
  ('STRING -> LITERALSTRING','STRING',1,'p_STRING4','tomlex.py',260),
  ('BASICSTRING -> ASPA BC ASPA','BASICSTRING',3,'p_BASICSTRING1','tomlex.py',264),
  ('BC -> BASICCHAR BC','BC',2,'p_BASICSTRING2','tomlex.py',268),
  ('BC -> <empty>','BC',0,'p_BASICSTRING3','tomlex.py',272),
  ('BASICCHAR -> BASICUNESCAPED','BASICCHAR',1,'p_BASICCHAR1','tomlex.py',276),
  ('BASICCHAR -> ESCAPED','BASICCHAR',1,'p_BASICCHAR2','tomlex.py',280),
  ('BASICUNESCAPED -> WHITESPACE','BASICUNESCAPED',1,'p_BASICUNESCAPED1','tomlex.py',284),
  ('BASICUNESCAPED -> CHAR','BASICUNESCAPED',1,'p_BASICUNESCAPED2','tomlex.py',288),
  ('BASICUNESCAPED -> INTEGER','BASICUNESCAPED',1,'p_BASICUNESCAPED3','tomlex.py',292),
  ('BASICUNESCAPED -> MINUS','BASICUNESCAPED',1,'p_BASICUNESCAPED4','tomlex.py',296),
  ('BASICUNESCAPED -> APOSTROFE','BASICUNESCAPED',1,'p_BASICUNESCAPED5','tomlex.py',300),
  ('BASICUNESCAPED -> ESCAPED','BASICUNESCAPED',1,'p_BASICUNESCAPED6','tomlex.py',304),
  ('BASICUNESCAPED -> DOT_SEP','BASICUNESCAPED',1,'p_BASICUNESCAPED7','tomlex.py',308),
  ('ESCAPED -> ESC_QUOTE','ESCAPED',1,'p_ESCAPED1','tomlex.py',313),
  ('ESCAPED -> ESC_REVERSE','ESCAPED',1,'p_ESCAPED2','tomlex.py',317),
  ('ESCAPED -> ESC_BACKSPACE','ESCAPED',1,'p_ESCAPED3','tomlex.py',321),
  ('ESCAPED -> ESC_FF','ESCAPED',1,'p_ESCAPED4','tomlex.py',325),
  ('ESCAPED -> ESC_NL','ESCAPED',1,'p_ESCAPED5','tomlex.py',329),
  ('ESCAPED -> ESC_CRETURN','ESCAPED',1,'p_ESCAPED6','tomlex.py',333),
  ('ESCAPED -> ESC_TAB','ESCAPED',1,'p_ESCAPED7','tomlex.py',337),
  ('ESCAPED -> ESC_HEX4','ESCAPED',1,'p_ESCAPED8','tomlex.py',341),
  ('ESCAPED -> ESC_HEX8','ESCAPED',1,'p_ESCAPED9','tomlex.py',347),
  ('MULTILINEBASICSTRING -> MLBCSTRDELIM MLNL MLBASICBODY MLBCSTRDELIM','MULTILINEBASICSTRING',4,'p_MULTILINEBASICSTRING','tomlex.py',353),
  ('MLNL -> NEWLINE','MLNL',1,'p_MLNL','tomlex.py',357),
  ('MLBCSTRDELIM -> ASPA ASPA ASPA','MLBCSTRDELIM',3,'p_MLBCSTRDELIM','tomlex.py',361),
  ('MLBASICBODY -> MLBC MLBQC MLQ','MLBASICBODY',3,'p_MLBASICBODY','tomlex.py',365),
  ('MLBC -> MLBCONTENT MLBC','MLBC',2,'p_MLBC1','tomlex.py',369),
  ('MLBC -> <empty>','MLBC',0,'p_MLBC2','tomlex.py',373),
  ('MLBQC -> MLBQUOTES MLBCONTENT MLBC2 MLBQC','MLBQC',4,'p_MLBQC1','tomlex.py',377),
  ('MLBQC -> <empty>','MLBQC',0,'p_MLBQC2','tomlex.py',381),
  ('MLBC2 -> MLBCONTENT MLBC2','MLBC2',2,'p_MLBC2_1','tomlex.py',385),
  ('MLBC2 -> <empty>','MLBC2',0,'p_MLBC2_2','tomlex.py',389),
  ('MLQ -> MLBQUOTES','MLQ',1,'p_MLQ1','tomlex.py',393),
  ('MLQ -> <empty>','MLQ',0,'p_MLQ2','tomlex.py',397),
  ('MLBCONTENT -> MLBCHAR','MLBCONTENT',1,'p_MLBCONTENT1','tomlex.py',401),
  ('MLBCONTENT -> NEWLINE','MLBCONTENT',1,'p_MLBCONTENT2','tomlex.py',405),
  ('MLBCONTENT -> MLBESCAPEDNL','MLBCONTENT',1,'p_MLBCONTENT3','tomlex.py',409),
  ('MLBCHAR -> MLBUNESCAPED','MLBCHAR',1,'p_MLBCHAR1','tomlex.py',413),
  ('MLBCHAR -> ESCAPED','MLBCHAR',1,'p_MLBCHAR2','tomlex.py',417),
  ('MLBQUOTES -> ASPA','MLBQUOTES',1,'p_MLBQUOTES1','tomlex.py',421),
  ('MLBQUOTES -> ASPA ASPA','MLBQUOTES',2,'p_MLBQUOTES2','tomlex.py',425),
  ('MLBUNESCAPED -> WHITESPACE','MLBUNESCAPED',1,'p_MLBUNESCAPED1','tomlex.py',429),
  ('MLBUNESCAPED -> CHAR','MLBUNESCAPED',1,'p_MLBUNESCAPED2','tomlex.py',433),
  ('MLBESCAPEDNL -> ESCAPE WHITESPACE NEWLINE WHNL','MLBESCAPEDNL',4,'p_MLBESCAPEDNL','tomlex.py',437),
  ('WHNL -> SPACENEWLINE WHNL','WHNL',2,'p_WHNL1','tomlex.py',441),
  ('WHNL -> <empty>','WHNL',0,'p_WHNL2','tomlex.py',445),
  ('SPACENEWLINE -> WHITESPACE','SPACENEWLINE',1,'p_SPACENEWLINE1','tomlex.py',449),
  ('SPACENEWLINE -> NEWLINE','SPACENEWLINE',1,'p_SPACENEWLINE2','tomlex.py',453),
  ('LITERALSTRING -> APOSTROFE LCH APOSTROFE','LITERALSTRING',3,'p_LITERALSTRING','tomlex.py',457),
  ('LCH -> LITERALCHAR LCH','LCH',2,'p_LCH1','tomlex.py',461),
  ('LCH -> <empty>','LCH',0,'p_LCH2','tomlex.py',465),
  ('LITERALCHAR -> CHAR','LITERALCHAR',1,'p_LITERALCHAR1','tomlex.py',469),
  ('LITERALCHAR -> ESCAPED','LITERALCHAR',1,'p_LITERALCHAR2','tomlex.py',473),
  ('MLLITERALSTRING -> MLLITERALSTRINGDELIM NLR MLLITERALBODY NLR MLLITERALSTRINGDELIM','MLLITERALSTRING',5,'p_MLLITERALSTRING','tomlex.py',477),
  ('NLR -> NEWLINE','NLR',1,'p_NLR1','tomlex.py',481),
  ('NLR -> <empty>','NLR',0,'p_NLR2','tomlex.py',485),
  ('MLLITERALSTRINGDELIM -> APOSTROFE APOSTROFE APOSTROFE','MLLITERALSTRINGDELIM',3,'p_MLLITERALSTRINGDELIM','tomlex.py',489),
  ('MLLITERALBODY -> MLLC MLLQC MLLQ','MLLITERALBODY',3,'p_MLLITERALBODY','tomlex.py',497),
  ('MLLC -> MLLCONTENT MLLC','MLLC',2,'p_MLLC1','tomlex.py',501),
  ('MLLC -> <empty>','MLLC',0,'p_MLLC2','tomlex.py',506),
  ('MLLQC -> <empty>','MLLQC',0,'p_MLLQC1','tomlex.py',510),
  ('MLLQC -> MLLQUOTES MLLCONTENT MLLC2 MLLQC','MLLQC',4,'p_MLLQC2','tomlex.py',514),
  ('MLLC2 -> MLLCONTENT MLLC2','MLLC2',2,'p_MLLC2_1','tomlex.py',518),
  ('MLLC2 -> <empty>','MLLC2',0,'p_MLLC2_2','tomlex.py',522),
  ('MLLQ -> <empty>','MLLQ',0,'p_MLLQ1','tomlex.py',526),
  ('MLLQ -> MLLQUOTES','MLLQ',1,'p_MLLQ2','tomlex.py',530),
  ('MLLCONTENT -> MLLCHAR','MLLCONTENT',1,'p_MLLCONTENT1','tomlex.py',534),
  ('MLLCONTENT -> NEWLINE','MLLCONTENT',1,'p_MLLCONTENT2','tomlex.py',538),
  ('MLLCHAR -> CHAR','MLLCHAR',1,'p_MLLCHAR','tomlex.py',542),
  ('MLLQUOTES -> APOSTROFE APOSTROFE','MLLQUOTES',2,'p_MLLQUOTES1','tomlex.py',546),
  ('MLLQUOTES -> APOSTROFE','MLLQUOTES',1,'p_MLLQUOTES2','tomlex.py',550),
  ('ARRAY -> APR ARRAYVALUES WSCOMMENTNEWLINE FPR','ARRAY',4,'p_ARRAY','tomlex.py',554),
  ('ARRAYVALUES -> <empty>','ARRAYVALUES',0,'p_ARRAYVALUES1','tomlex.py',558),
  ('ARRAYVALUES -> WSCOMMENTNEWLINE VALUE ARRAYCONTEUDO','ARRAYVALUES',3,'p_ARRAYVALUES2','tomlex.py',562),
  ('ARRAYCONTEUDO -> <empty>','ARRAYCONTEUDO',0,'p_ARRAYVALUES3','tomlex.py',566),
  ('ARRAYCONTEUDO -> WSCOMMENTNEWLINE VIRGULA ARRAYVALUES','ARRAYCONTEUDO',3,'p_ARRAYVALUES4','tomlex.py',570),
  ('WSCOMMENTNEWLINE -> <empty>','WSCOMMENTNEWLINE',0,'p_WSCOMMENTNEWLINE1','tomlex.py',586),
  ('WSCOMMENTNEWLINE -> INNERCOMMENT WSCOMMENTNEWLINE','WSCOMMENTNEWLINE',2,'p_WSCOMMENTNEWLINE2','tomlex.py',590),
  ('INNERCOMMENT -> WHITESPACE','INNERCOMMENT',1,'p_INNERCOMMENT1','tomlex.py',594),
  ('INNERCOMMENT -> COMMENTOUNAO NEWLINE','INNERCOMMENT',2,'p_INNERCOMMENT2','tomlex.py',598),
  ('COMMENTOUNAO -> COMMENT','COMMENTOUNAO',1,'p_COMMENTOUNAO1','tomlex.py',602),
  ('COMMENTOUNAO -> <empty>','COMMENTOUNAO',0,'p_COMMENTOUNAO2','tomlex.py',606),
  ('TABLE -> APR KEY FPR','TABLE',3,'p_TABLE','tomlex.py',610),
]
