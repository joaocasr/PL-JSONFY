
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACH APOSTROFE APR ASPA ATC ATO BIN BOOLEAN CHAR COMMENT DATE DOT_SEP ESCAPE ESC_BACKSPACE ESC_CRETURN ESC_FF ESC_HEX4 ESC_HEX8 ESC_NL ESC_QUOTE ESC_REVERSE ESC_TAB FCH FLOAT FPR HEX IGUAL INF INTEGER MINUS NAN NEWLINE OCT PLUS TIME TIME_DELIM TWODOT_SEP UNDERSC0RE UNDERSCORE VIRGULA WHITESPACETOML : TITLES GROUPSTITLES : KVALUE EXPRESSION TITLESTITLES :GROUPS : SECCAO EXPRESSION GROUPSGROUPS : SECCAO : TABLE EXPRESSION ATRIBUICOESSECCAO :ATRIBUICOES : KVALUE EXPRESSION ATRIBUICOESATRIBUICOES :EXPRESSION : COMMENT EXPRESSIONEXPRESSION : NEWLINE EXPRESSIONEXPRESSION :KVALUE : KEY kvwhitespace IGUAL kvwhitespace VALUEkvwhitespace : WHITESPACEkvwhitespace :KEY : SIMPLEKEYKEY : DOTKEYSIMPLEKEY : QUOTEDKEYSIMPLEKEY : UNQUOTEDKEYUNQUOTEDKEY : OCCURRENCES UNQUOTEDKEYAUXUNQUOTEDKEYAUX : OCCURRENCES UNQUOTEDKEYAUXUNQUOTEDKEYAUX :OCCURRENCES : CHAROCCURRENCES : INTEGEROCCURRENCES : MINUSOCCURRENCES : UNDERSCOREQUOTEDKEY : BASICSTRINGQUOTEDKEY : LITERALSTRINGDOTKEY : SIMPLEKEY DOT_SEP SIMPLEKEY DOTSIMPKEYDOTSIMPKEY : DOT_SEP SIMPLEKEY DOTSIMPKEYDOTSIMPKEY : VALUE : STRINGVALUE : BOOLEANVALUE : INTEGERVALUE : ARRAYVALUE : DATETIMEDATETIME : OFFSETDATETIMEDATETIME : LOCALDATETIMEDATETIME : LOCALDATEDATETIME : LOCALTIMEOFFSETDATETIME : DATE TIMELOCALDATETIME : DATE TIMELOCALDATE : DATELOCALTIME : TIMEVALUE : FLOATSTRING : MULTILINEBASICSTRINGSTRING : BASICSTRINGSTRING : MLLITERALSTRINGSTRING : LITERALSTRINGBASICSTRING : ASPA BC ASPABC : BASICCHAR BCBC :BASICCHAR : BASICUNESCAPEDBASICCHAR : ESCAPEDBASICUNESCAPED : WHITESPACEBASICUNESCAPED : CHARBASICUNESCAPED : INTEGERBASICUNESCAPED : MINUSBASICUNESCAPED : APOSTROFEBASICUNESCAPED : ESCAPEDBASICUNESCAPED : DOT_SEPESCAPED : ESC_QUOTEESCAPED : ESC_REVERSEESCAPED : ESC_BACKSPACEESCAPED : ESC_FFESCAPED : ESC_NLESCAPED : ESC_CRETURNESCAPED : ESC_TABESCAPED : ESC_HEX4ESCAPED : ESC_HEX8MULTILINEBASICSTRING : MLBCSTRDELIM MLNL MLBASICBODY MLBCSTRDELIMMLNL : NEWLINEMLNL :MLBCSTRDELIM : ASPA ASPA ASPAMLBASICBODY : MLBCMLBC : MLBCONTENT MLBCMLBC :MLBQC : MLBQUOTES MLBCONTENT MLBC2 MLBQCMLBQC :MLBC2 : MLBCONTENT MLBC2MLBC2 :MLQ : MLBQUOTESMLQ :MLBCONTENT : MLBCHARMLBCONTENT : NEWLINEMLBCONTENT : MLBESCAPEDNLMLBCHAR : MLBUNESCAPEDMLBCHAR : ESCAPEDMLBQUOTES : ASPAMLBQUOTES : ASPA ASPAMLBUNESCAPED : WHITESPACEMLBUNESCAPED : CHARMLBESCAPEDNL : ESCAPE NEWLINE WHNLWHNL : SPACENEWLINE WHNLWHNL :SPACENEWLINE : WHITESPACESPACENEWLINE : NEWLINELITERALSTRING : APOSTROFE LCH APOSTROFELCH : LITERALCHAR LCHLCH :LITERALCHAR : CHARLITERALCHAR : ESCAPEDLITERALCHAR : WHITESPACEMLLITERALSTRING : MLLITERALSTRINGDELIM NLR MLLITERALBODY MLLITERALSTRINGDELIMNLR : NEWLINENLR :MLLITERALSTRINGDELIM : APOSTROFE APOSTROFE APOSTROFEMLLITERALBODY : MLLCMLLC : MLLCONTENT MLLCMLLC :MLLCONTENT : MLLCHARMLLCONTENT : NEWLINEMLLCHAR : CHARMLLCHAR : DOT_SEPMLLCHAR : WHITESPACEARRAY : APR ARRAYVALUES WSCOMMENTNEWLINE FPRARRAYVALUES :ARRAYVALUES : WSCOMMENTNEWLINE VALUE ARRAYCONTEUDOARRAYCONTEUDO :ARRAYCONTEUDO : WSCOMMENTNEWLINE VIRGULA ARRAYVALUESWSCOMMENTNEWLINE :WSCOMMENTNEWLINE : INNERCOMMENT WSCOMMENTNEWLINEINNERCOMMENT : WHITESPACEINNERCOMMENT : COMMENTOUNAO NEWLINECOMMENTOUNAO : COMMENTCOMMENTOUNAO :TABLE : APR KEY FPR'
    
_lr_action_items = {'APR':([0,2,3,19,20,22,23,24,26,54,55,57,58,59,60,63,65,68,69,70,71,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,95,96,98,100,101,102,111,115,116,128,137,138,141,145,148,],[-3,21,-12,-12,-12,-3,-12,-12,-14,21,-9,-2,-10,-11,-15,-50,-98,-6,-12,-127,86,-9,-13,-32,-33,-34,-35,-36,-45,-46,-47,-48,-49,-121,-37,-38,-39,-40,-43,-44,-8,86,-121,-123,-41,-122,-124,-74,-107,-116,-71,-104,-121,]),'COMMENT':([0,2,3,19,20,22,23,24,54,55,57,58,59,63,65,68,69,70,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,95,96,98,99,101,102,111,114,116,128,137,138,140,141,145,148,153,],[-3,-7,23,23,23,-3,23,23,-7,-9,-2,-10,-11,-50,-98,-6,23,-127,-9,-13,-32,-33,-34,-35,-36,-45,-46,-47,-48,-49,104,-37,-38,-39,-40,-43,-44,-8,104,104,-123,-41,104,-124,-74,-107,-116,-118,-71,-104,104,-120,]),'NEWLINE':([0,2,3,19,20,22,23,24,40,41,42,43,44,45,46,47,48,54,55,57,58,59,63,65,68,69,70,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,95,96,98,99,101,102,103,104,105,106,108,109,111,114,116,119,120,121,122,123,124,125,126,127,128,131,132,133,134,135,136,137,138,140,141,144,145,148,149,150,151,152,153,154,],[-3,-7,24,24,24,-3,24,24,-62,-63,-64,-65,-66,-67,-68,-69,-70,-7,-9,-2,-10,-11,-50,-98,-6,24,-127,-9,-13,-32,-33,-34,-35,-36,-45,-46,-47,-48,-49,-117,-37,-38,-39,-40,106,109,-43,-44,-8,-126,-126,-123,116,-125,121,-72,133,-105,-41,-119,-124,121,-84,-85,-86,-87,-88,144,-91,-92,-74,133,-111,-112,-113,-114,-115,-107,-116,-118,-71,149,-104,-117,-97,-93,149,-96,-120,-94,]),'$end':([0,1,2,3,18,19,20,22,23,24,54,55,57,58,59,63,65,67,68,69,70,74,75,76,77,78,79,80,81,82,83,84,85,87,88,89,90,95,96,98,111,128,137,138,141,145,],[-3,0,-5,-12,-1,-12,-12,-3,-12,-12,-5,-9,-2,-10,-11,-50,-98,-4,-6,-12,-127,-9,-13,-32,-33,-34,-35,-36,-45,-46,-47,-48,-49,-37,-38,-39,-40,-43,-44,-8,-41,-74,-107,-116,-71,-104,]),'ASPA':([0,3,12,20,21,22,23,24,26,27,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,55,58,59,60,63,64,65,69,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,95,96,100,101,102,105,106,107,111,115,116,117,118,119,120,121,122,123,124,126,127,128,137,138,141,142,143,144,145,148,149,150,151,152,154,],[12,-12,-52,-12,12,12,-12,-12,-14,12,63,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,12,-10,-11,-15,-50,-51,-98,-12,-127,92,12,12,-13,-32,-33,-34,-35,-36,-45,-46,-47,-48,-49,-121,-37,-38,-39,-40,-73,107,-43,-44,92,-121,-123,-77,-72,128,-41,-122,-124,142,-75,-77,-84,-85,-86,-87,-88,-91,-92,-74,-107,-116,-71,107,-76,-95,-104,-121,-97,-93,-95,-96,-94,]),'APOSTROFE':([0,3,12,13,20,21,22,23,24,26,27,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,58,59,60,63,65,66,69,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,94,95,96,100,101,102,108,109,110,111,115,116,128,129,130,131,132,133,134,135,136,137,138,141,145,146,147,148,],[13,-12,38,-100,-12,13,13,-12,-12,-14,13,38,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,65,-100,-101,-102,-103,13,-10,-11,-15,-50,-98,-99,-12,-127,94,13,13,-13,-32,-33,-34,-35,-36,-45,-46,-47,-48,-49,-121,-37,-38,-39,-40,38,-106,110,-43,-44,94,-121,-123,-110,-105,137,-41,-122,-124,-74,146,-108,-110,-111,-112,-113,-114,-115,-107,-116,-71,-104,110,-109,-121,]),'CHAR':([0,3,11,12,13,14,15,16,17,20,21,22,23,24,27,28,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,55,58,59,63,65,69,70,72,74,75,76,77,78,79,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,105,106,108,109,111,119,120,121,122,123,124,126,127,128,131,132,133,134,135,136,137,138,141,144,145,149,150,151,152,154,],[14,-12,14,35,51,-23,-24,-25,-26,-12,14,14,-12,-12,14,14,35,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,51,-101,-102,-103,14,-10,-11,-50,-98,-12,-127,14,14,-13,-32,-33,-34,-35,-36,-45,-46,-47,-48,-49,-37,-38,-39,-40,-73,35,-106,51,-43,-44,127,-72,134,-105,-41,127,-84,-85,-86,-87,-88,-91,-92,-74,134,-111,-112,-113,-114,-115,-107,-116,-71,-95,-104,-97,-93,-95,-96,-94,]),'INTEGER':([0,3,11,12,14,15,16,17,20,21,22,23,24,26,27,28,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,55,58,59,60,63,65,69,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,95,96,100,101,102,111,115,116,128,137,138,141,145,148,],[15,-12,15,36,-23,-24,-25,-26,-12,15,15,-12,-12,-14,15,15,36,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,15,-10,-11,-15,-50,-98,-12,-127,78,15,15,-13,-32,-33,-34,-35,-36,-45,-46,-47,-48,-49,-121,-37,-38,-39,-40,36,-43,-44,78,-121,-123,-41,-122,-124,-74,-107,-116,-71,-104,-121,]),'MINUS':([0,3,11,12,14,15,16,17,20,21,22,23,24,27,28,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,55,58,59,63,65,69,70,72,74,75,76,77,78,79,80,81,82,83,84,85,87,88,89,90,92,95,96,111,128,137,138,141,145,],[16,-12,16,37,-23,-24,-25,-26,-12,16,16,-12,-12,16,16,37,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,16,-10,-11,-50,-98,-12,-127,16,16,-13,-32,-33,-34,-35,-36,-45,-46,-47,-48,-49,-37,-38,-39,-40,37,-43,-44,-41,-74,-107,-116,-71,-104,]),'UNDERSCORE':([0,3,11,14,15,16,17,20,21,22,23,24,27,28,55,58,59,63,65,69,70,72,74,75,76,77,78,79,80,81,82,83,84,85,87,88,89,90,95,96,111,128,137,138,141,145,],[17,-12,17,-23,-24,-25,-26,-12,17,17,-12,-12,17,17,17,-10,-11,-50,-98,-12,-127,17,17,-13,-32,-33,-34,-35,-36,-45,-46,-47,-48,-49,-37,-38,-39,-40,-43,-44,-41,-74,-107,-116,-71,-104,]),'WHITESPACE':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,28,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,60,61,62,63,65,73,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,101,102,105,106,108,109,111,112,114,116,119,120,121,122,123,124,126,127,128,131,132,133,134,135,136,137,138,140,141,144,145,148,149,150,151,152,153,154,],[26,-16,-17,-18,-19,-27,-28,-22,34,53,-23,-24,-25,-26,-22,-20,34,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,53,-101,-102,-103,26,-31,-21,-50,-98,-29,-32,-33,-34,-35,-36,-45,-46,-47,-48,-49,102,-37,-38,-39,-40,-73,34,-106,53,-43,-44,-31,102,102,-123,126,-72,136,-105,-41,-30,102,-124,126,-84,-85,-86,-87,-88,-91,-92,-74,136,-111,-112,-113,-114,-115,-107,-116,-118,-71,152,-104,102,-97,-93,152,-96,-120,-94,]),'IGUAL':([4,5,6,7,8,9,10,11,14,15,16,17,25,26,28,29,61,62,63,65,73,97,112,],[-15,-16,-17,-18,-19,-27,-28,-22,-23,-24,-25,-26,60,-14,-22,-20,-31,-21,-50,-98,-29,-31,-30,]),'FPR':([5,6,7,8,9,10,11,14,15,16,17,28,29,56,61,62,63,65,73,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,95,96,97,99,101,102,111,112,113,114,115,116,128,137,138,140,141,145,148,153,],[-16,-17,-18,-19,-27,-28,-22,-23,-24,-25,-26,-22,-20,70,-31,-21,-50,-98,-29,-32,-33,-34,-35,-36,-45,-46,-47,-48,-49,-117,-37,-38,-39,-40,-43,-44,-31,-121,-121,-123,-41,-30,138,-119,-122,-124,-74,-107,-116,-118,-71,-104,-117,-120,]),'DOT_SEP':([5,7,8,9,10,11,12,14,15,16,17,28,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,61,62,63,65,92,93,97,108,109,131,132,133,134,135,136,137,],[27,-18,-19,-27,-28,-22,39,-23,-24,-25,-26,-22,-20,39,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,72,-21,-50,-98,39,-106,72,135,-105,135,-111,-112,-113,-114,-115,-107,]),'ESC_QUOTE':([12,13,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,91,92,94,105,106,119,120,121,122,123,124,126,127,128,144,149,150,151,152,154,],[40,40,40,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,40,-101,-102,-103,-73,40,40,40,-72,40,-84,-85,-86,-87,-88,-91,-92,-74,-95,-97,-93,-95,-96,-94,]),'ESC_REVERSE':([12,13,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,91,92,94,105,106,119,120,121,122,123,124,126,127,128,144,149,150,151,152,154,],[41,41,41,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,41,-101,-102,-103,-73,41,41,41,-72,41,-84,-85,-86,-87,-88,-91,-92,-74,-95,-97,-93,-95,-96,-94,]),'ESC_BACKSPACE':([12,13,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,91,92,94,105,106,119,120,121,122,123,124,126,127,128,144,149,150,151,152,154,],[42,42,42,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,42,-101,-102,-103,-73,42,42,42,-72,42,-84,-85,-86,-87,-88,-91,-92,-74,-95,-97,-93,-95,-96,-94,]),'ESC_FF':([12,13,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,91,92,94,105,106,119,120,121,122,123,124,126,127,128,144,149,150,151,152,154,],[43,43,43,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,43,-101,-102,-103,-73,43,43,43,-72,43,-84,-85,-86,-87,-88,-91,-92,-74,-95,-97,-93,-95,-96,-94,]),'ESC_NL':([12,13,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,91,92,94,105,106,119,120,121,122,123,124,126,127,128,144,149,150,151,152,154,],[44,44,44,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,44,-101,-102,-103,-73,44,44,44,-72,44,-84,-85,-86,-87,-88,-91,-92,-74,-95,-97,-93,-95,-96,-94,]),'ESC_CRETURN':([12,13,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,91,92,94,105,106,119,120,121,122,123,124,126,127,128,144,149,150,151,152,154,],[45,45,45,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,45,-101,-102,-103,-73,45,45,45,-72,45,-84,-85,-86,-87,-88,-91,-92,-74,-95,-97,-93,-95,-96,-94,]),'ESC_TAB':([12,13,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,91,92,94,105,106,119,120,121,122,123,124,126,127,128,144,149,150,151,152,154,],[46,46,46,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,46,-101,-102,-103,-73,46,46,46,-72,46,-84,-85,-86,-87,-88,-91,-92,-74,-95,-97,-93,-95,-96,-94,]),'ESC_HEX4':([12,13,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,91,92,94,105,106,119,120,121,122,123,124,126,127,128,144,149,150,151,152,154,],[47,47,47,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,47,-101,-102,-103,-73,47,47,47,-72,47,-84,-85,-86,-87,-88,-91,-92,-74,-95,-97,-93,-95,-96,-94,]),'ESC_HEX8':([12,13,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,91,92,94,105,106,119,120,121,122,123,124,126,127,128,144,149,150,151,152,154,],[48,48,48,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,48,-101,-102,-103,-73,48,48,48,-72,48,-84,-85,-86,-87,-88,-91,-92,-74,-95,-97,-93,-95,-96,-94,]),'BOOLEAN':([26,60,71,86,100,101,102,115,116,148,],[-14,-15,77,-121,77,-121,-123,-122,-124,-121,]),'FLOAT':([26,60,71,86,100,101,102,115,116,148,],[-14,-15,81,-121,81,-121,-123,-122,-124,-121,]),'DATE':([26,60,71,86,100,101,102,115,116,148,],[-14,-15,95,-121,95,-121,-123,-122,-124,-121,]),'TIME':([26,60,71,86,95,100,101,102,115,116,148,],[-14,-15,96,-121,111,96,-121,-123,-122,-124,-121,]),'ESCAPE':([40,41,42,43,44,45,46,47,48,91,105,106,119,120,121,122,123,124,126,127,128,144,149,150,151,152,154,],[-62,-63,-64,-65,-66,-67,-68,-69,-70,-73,125,-72,125,-84,-85,-86,-87,-88,-91,-92,-74,-95,-97,-93,-95,-96,-94,]),'VIRGULA':([63,65,76,77,78,79,80,81,82,83,84,85,87,88,89,90,95,96,101,102,111,114,115,116,128,137,138,139,141,145,],[-50,-98,-32,-33,-34,-35,-36,-45,-46,-47,-48,-49,-37,-38,-39,-40,-43,-44,-121,-123,-41,-121,-122,-124,-74,-107,-116,148,-71,-104,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'TOML':([0,],[1,]),'TITLES':([0,22,],[2,57,]),'KVALUE':([0,22,55,74,],[3,3,69,69,]),'KEY':([0,21,22,55,74,],[4,56,4,4,4,]),'SIMPLEKEY':([0,21,22,27,55,72,74,],[5,5,5,61,5,97,5,]),'DOTKEY':([0,21,22,55,74,],[6,6,6,6,6,]),'QUOTEDKEY':([0,21,22,27,55,72,74,],[7,7,7,7,7,7,7,]),'UNQUOTEDKEY':([0,21,22,27,55,72,74,],[8,8,8,8,8,8,8,]),'BASICSTRING':([0,21,22,27,55,71,72,74,100,],[9,9,9,9,9,83,9,9,83,]),'LITERALSTRING':([0,21,22,27,55,71,72,74,100,],[10,10,10,10,10,85,10,10,85,]),'OCCURRENCES':([0,11,21,22,27,28,55,72,74,],[11,28,11,11,11,28,11,11,11,]),'GROUPS':([2,54,],[18,67,]),'SECCAO':([2,54,],[19,19,]),'TABLE':([2,54,],[20,20,]),'EXPRESSION':([3,19,20,23,24,69,],[22,54,55,58,59,74,]),'kvwhitespace':([4,60,],[25,71,]),'UNQUOTEDKEYAUX':([11,28,],[29,62,]),'BC':([12,31,92,],[30,64,30,]),'BASICCHAR':([12,31,92,],[31,31,31,]),'BASICUNESCAPED':([12,31,92,],[32,32,32,]),'ESCAPED':([12,13,31,50,92,94,105,119,],[33,52,33,52,33,52,124,124,]),'LCH':([13,50,94,],[49,66,49,]),'LITERALCHAR':([13,50,94,],[50,50,50,]),'ATRIBUICOES':([55,74,],[68,98,]),'DOTSIMPKEY':([61,97,],[73,112,]),'VALUE':([71,100,],[75,114,]),'STRING':([71,100,],[76,76,]),'ARRAY':([71,100,],[79,79,]),'DATETIME':([71,100,],[80,80,]),'MULTILINEBASICSTRING':([71,100,],[82,82,]),'MLLITERALSTRING':([71,100,],[84,84,]),'OFFSETDATETIME':([71,100,],[87,87,]),'LOCALDATETIME':([71,100,],[88,88,]),'LOCALDATE':([71,100,],[89,89,]),'LOCALTIME':([71,100,],[90,90,]),'MLBCSTRDELIM':([71,100,117,],[91,91,141,]),'MLLITERALSTRINGDELIM':([71,100,129,],[93,93,145,]),'ARRAYVALUES':([86,148,],[99,153,]),'WSCOMMENTNEWLINE':([86,99,101,114,148,],[100,113,115,139,100,]),'INNERCOMMENT':([86,99,101,114,148,],[101,101,101,101,101,]),'COMMENTOUNAO':([86,99,101,114,148,],[103,103,103,103,103,]),'MLNL':([91,],[105,]),'NLR':([93,],[108,]),'MLBASICBODY':([105,],[117,]),'MLBC':([105,119,],[118,143,]),'MLBCONTENT':([105,119,],[119,119,]),'MLBCHAR':([105,119,],[120,120,]),'MLBESCAPEDNL':([105,119,],[122,122,]),'MLBUNESCAPED':([105,119,],[123,123,]),'MLLITERALBODY':([108,],[129,]),'MLLC':([108,131,],[130,147,]),'MLLCONTENT':([108,131,],[131,131,]),'MLLCHAR':([108,131,],[132,132,]),'ARRAYCONTEUDO':([114,],[140,]),'WHNL':([144,151,],[150,154,]),'SPACENEWLINE':([144,151,],[151,151,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> TOML","S'",1,None,None,None),
  ('TOML -> TITLES GROUPS','TOML',2,'p_TOML','tomlex.py',105),
  ('TITLES -> KVALUE EXPRESSION TITLES','TITLES',3,'p_TITLES1','tomlex.py',110),
  ('TITLES -> <empty>','TITLES',0,'p_TITLES2','tomlex.py',115),
  ('GROUPS -> SECCAO EXPRESSION GROUPS','GROUPS',3,'p_GROUPS1','tomlex.py',119),
  ('GROUPS -> <empty>','GROUPS',0,'p_GROUPS2','tomlex.py',124),
  ('SECCAO -> TABLE EXPRESSION ATRIBUICOES','SECCAO',3,'p_SECCAO1','tomlex.py',128),
  ('SECCAO -> <empty>','SECCAO',0,'p_SECCAO2','tomlex.py',134),
  ('ATRIBUICOES -> KVALUE EXPRESSION ATRIBUICOES','ATRIBUICOES',3,'p_ATRIBUICOES1','tomlex.py',138),
  ('ATRIBUICOES -> <empty>','ATRIBUICOES',0,'p_ATRIBUICOES2','tomlex.py',144),
  ('EXPRESSION -> COMMENT EXPRESSION','EXPRESSION',2,'p_EXPRESSION1','tomlex.py',148),
  ('EXPRESSION -> NEWLINE EXPRESSION','EXPRESSION',2,'p_EXPRESSION2','tomlex.py',152),
  ('EXPRESSION -> <empty>','EXPRESSION',0,'p_EXPRESSION3','tomlex.py',156),
  ('KVALUE -> KEY kvwhitespace IGUAL kvwhitespace VALUE','KVALUE',5,'p_KVALUE','tomlex.py',160),
  ('kvwhitespace -> WHITESPACE','kvwhitespace',1,'p_kvwhitespace1','tomlex.py',164),
  ('kvwhitespace -> <empty>','kvwhitespace',0,'p_kvwhitespace2','tomlex.py',168),
  ('KEY -> SIMPLEKEY','KEY',1,'p_KEY1','tomlex.py',172),
  ('KEY -> DOTKEY','KEY',1,'p_KEY2','tomlex.py',176),
  ('SIMPLEKEY -> QUOTEDKEY','SIMPLEKEY',1,'p_SIMPLEKEY1','tomlex.py',181),
  ('SIMPLEKEY -> UNQUOTEDKEY','SIMPLEKEY',1,'p_SIMPLEKEY2','tomlex.py',185),
  ('UNQUOTEDKEY -> OCCURRENCES UNQUOTEDKEYAUX','UNQUOTEDKEY',2,'p_UNQUOTEDKEY1','tomlex.py',190),
  ('UNQUOTEDKEYAUX -> OCCURRENCES UNQUOTEDKEYAUX','UNQUOTEDKEYAUX',2,'p_UNQUOTEDKEY2','tomlex.py',195),
  ('UNQUOTEDKEYAUX -> <empty>','UNQUOTEDKEYAUX',0,'p_UNQUOTEDKEY3','tomlex.py',200),
  ('OCCURRENCES -> CHAR','OCCURRENCES',1,'p_OCCURRENCES1','tomlex.py',204),
  ('OCCURRENCES -> INTEGER','OCCURRENCES',1,'p_OCCURRENCES2','tomlex.py',208),
  ('OCCURRENCES -> MINUS','OCCURRENCES',1,'p_OCCURRENCES3','tomlex.py',213),
  ('OCCURRENCES -> UNDERSCORE','OCCURRENCES',1,'p_OCCURRENCES4','tomlex.py',218),
  ('QUOTEDKEY -> BASICSTRING','QUOTEDKEY',1,'p_QUOTEDKEY1','tomlex.py',223),
  ('QUOTEDKEY -> LITERALSTRING','QUOTEDKEY',1,'p_QUOTEDKEY2','tomlex.py',228),
  ('DOTKEY -> SIMPLEKEY DOT_SEP SIMPLEKEY DOTSIMPKEY','DOTKEY',4,'p_DOTKEY','tomlex.py',232),
  ('DOTSIMPKEY -> DOT_SEP SIMPLEKEY DOTSIMPKEY','DOTSIMPKEY',3,'p_DOTSIMPKEY1','tomlex.py',236),
  ('DOTSIMPKEY -> <empty>','DOTSIMPKEY',0,'p_DOTSIMPKEY2','tomlex.py',241),
  ('VALUE -> STRING','VALUE',1,'p_VALUE1','tomlex.py',245),
  ('VALUE -> BOOLEAN','VALUE',1,'p_VALUE2','tomlex.py',250),
  ('VALUE -> INTEGER','VALUE',1,'p_VALUE3','tomlex.py',254),
  ('VALUE -> ARRAY','VALUE',1,'p_VALUE4','tomlex.py',258),
  ('VALUE -> DATETIME','VALUE',1,'p_VALUE6','tomlex.py',266),
  ('DATETIME -> OFFSETDATETIME','DATETIME',1,'p_DATETIME1','tomlex.py',270),
  ('DATETIME -> LOCALDATETIME','DATETIME',1,'p_DATETIME2','tomlex.py',274),
  ('DATETIME -> LOCALDATE','DATETIME',1,'p_DATETIME3','tomlex.py',278),
  ('DATETIME -> LOCALTIME','DATETIME',1,'p_DATETIME4','tomlex.py',282),
  ('OFFSETDATETIME -> DATE TIME','OFFSETDATETIME',2,'p_OFFSETDATETIME','tomlex.py',286),
  ('LOCALDATETIME -> DATE TIME','LOCALDATETIME',2,'p_LOCALDATETIME','tomlex.py',290),
  ('LOCALDATE -> DATE','LOCALDATE',1,'p_LOCALDATE','tomlex.py',295),
  ('LOCALTIME -> TIME','LOCALTIME',1,'p_LOCALTIME','tomlex.py',299),
  ('VALUE -> FLOAT','VALUE',1,'p_VALUE7','tomlex.py',303),
  ('STRING -> MULTILINEBASICSTRING','STRING',1,'p_STRING1','tomlex.py',309),
  ('STRING -> BASICSTRING','STRING',1,'p_STRING2','tomlex.py',314),
  ('STRING -> MLLITERALSTRING','STRING',1,'p_STRING3','tomlex.py',319),
  ('STRING -> LITERALSTRING','STRING',1,'p_STRING4','tomlex.py',323),
  ('BASICSTRING -> ASPA BC ASPA','BASICSTRING',3,'p_BASICSTRING1','tomlex.py',328),
  ('BC -> BASICCHAR BC','BC',2,'p_BASICSTRING2','tomlex.py',333),
  ('BC -> <empty>','BC',0,'p_BASICSTRING3','tomlex.py',337),
  ('BASICCHAR -> BASICUNESCAPED','BASICCHAR',1,'p_BASICCHAR1','tomlex.py',341),
  ('BASICCHAR -> ESCAPED','BASICCHAR',1,'p_BASICCHAR2','tomlex.py',346),
  ('BASICUNESCAPED -> WHITESPACE','BASICUNESCAPED',1,'p_BASICUNESCAPED1','tomlex.py',350),
  ('BASICUNESCAPED -> CHAR','BASICUNESCAPED',1,'p_BASICUNESCAPED2','tomlex.py',355),
  ('BASICUNESCAPED -> INTEGER','BASICUNESCAPED',1,'p_BASICUNESCAPED3','tomlex.py',360),
  ('BASICUNESCAPED -> MINUS','BASICUNESCAPED',1,'p_BASICUNESCAPED4','tomlex.py',364),
  ('BASICUNESCAPED -> APOSTROFE','BASICUNESCAPED',1,'p_BASICUNESCAPED5','tomlex.py',369),
  ('BASICUNESCAPED -> ESCAPED','BASICUNESCAPED',1,'p_BASICUNESCAPED6','tomlex.py',373),
  ('BASICUNESCAPED -> DOT_SEP','BASICUNESCAPED',1,'p_BASICUNESCAPED7','tomlex.py',377),
  ('ESCAPED -> ESC_QUOTE','ESCAPED',1,'p_ESCAPED1','tomlex.py',383),
  ('ESCAPED -> ESC_REVERSE','ESCAPED',1,'p_ESCAPED2','tomlex.py',388),
  ('ESCAPED -> ESC_BACKSPACE','ESCAPED',1,'p_ESCAPED3','tomlex.py',393),
  ('ESCAPED -> ESC_FF','ESCAPED',1,'p_ESCAPED4','tomlex.py',398),
  ('ESCAPED -> ESC_NL','ESCAPED',1,'p_ESCAPED5','tomlex.py',403),
  ('ESCAPED -> ESC_CRETURN','ESCAPED',1,'p_ESCAPED6','tomlex.py',408),
  ('ESCAPED -> ESC_TAB','ESCAPED',1,'p_ESCAPED7','tomlex.py',413),
  ('ESCAPED -> ESC_HEX4','ESCAPED',1,'p_ESCAPED8','tomlex.py',418),
  ('ESCAPED -> ESC_HEX8','ESCAPED',1,'p_ESCAPED9','tomlex.py',424),
  ('MULTILINEBASICSTRING -> MLBCSTRDELIM MLNL MLBASICBODY MLBCSTRDELIM','MULTILINEBASICSTRING',4,'p_MULTILINEBASICSTRING','tomlex.py',430),
  ('MLNL -> NEWLINE','MLNL',1,'p_MLNL1','tomlex.py',434),
  ('MLNL -> <empty>','MLNL',0,'p_MLNL2','tomlex.py',438),
  ('MLBCSTRDELIM -> ASPA ASPA ASPA','MLBCSTRDELIM',3,'p_MLBCSTRDELIM','tomlex.py',442),
  ('MLBASICBODY -> MLBC','MLBASICBODY',1,'p_MLBASICBODY','tomlex.py',446),
  ('MLBC -> MLBCONTENT MLBC','MLBC',2,'p_MLBC1','tomlex.py',452),
  ('MLBC -> <empty>','MLBC',0,'p_MLBC2','tomlex.py',456),
  ('MLBQC -> MLBQUOTES MLBCONTENT MLBC2 MLBQC','MLBQC',4,'p_MLBQC1','tomlex.py',460),
  ('MLBQC -> <empty>','MLBQC',0,'p_MLBQC2','tomlex.py',464),
  ('MLBC2 -> MLBCONTENT MLBC2','MLBC2',2,'p_MLBC2_1','tomlex.py',468),
  ('MLBC2 -> <empty>','MLBC2',0,'p_MLBC2_2','tomlex.py',473),
  ('MLQ -> MLBQUOTES','MLQ',1,'p_MLQ1','tomlex.py',478),
  ('MLQ -> <empty>','MLQ',0,'p_MLQ2','tomlex.py',482),
  ('MLBCONTENT -> MLBCHAR','MLBCONTENT',1,'p_MLBCONTENT1','tomlex.py',486),
  ('MLBCONTENT -> NEWLINE','MLBCONTENT',1,'p_MLBCONTENT2','tomlex.py',490),
  ('MLBCONTENT -> MLBESCAPEDNL','MLBCONTENT',1,'p_MLBCONTENT3','tomlex.py',494),
  ('MLBCHAR -> MLBUNESCAPED','MLBCHAR',1,'p_MLBCHAR1','tomlex.py',498),
  ('MLBCHAR -> ESCAPED','MLBCHAR',1,'p_MLBCHAR2','tomlex.py',502),
  ('MLBQUOTES -> ASPA','MLBQUOTES',1,'p_MLBQUOTES1','tomlex.py',506),
  ('MLBQUOTES -> ASPA ASPA','MLBQUOTES',2,'p_MLBQUOTES2','tomlex.py',510),
  ('MLBUNESCAPED -> WHITESPACE','MLBUNESCAPED',1,'p_MLBUNESCAPED1','tomlex.py',514),
  ('MLBUNESCAPED -> CHAR','MLBUNESCAPED',1,'p_MLBUNESCAPED2','tomlex.py',518),
  ('MLBESCAPEDNL -> ESCAPE NEWLINE WHNL','MLBESCAPEDNL',3,'p_MLBESCAPEDNL','tomlex.py',522),
  ('WHNL -> SPACENEWLINE WHNL','WHNL',2,'p_WHNL1','tomlex.py',527),
  ('WHNL -> <empty>','WHNL',0,'p_WHNL2','tomlex.py',531),
  ('SPACENEWLINE -> WHITESPACE','SPACENEWLINE',1,'p_SPACENEWLINE1','tomlex.py',535),
  ('SPACENEWLINE -> NEWLINE','SPACENEWLINE',1,'p_SPACENEWLINE2','tomlex.py',539),
  ('LITERALSTRING -> APOSTROFE LCH APOSTROFE','LITERALSTRING',3,'p_LITERALSTRING','tomlex.py',543),
  ('LCH -> LITERALCHAR LCH','LCH',2,'p_LCH1','tomlex.py',549),
  ('LCH -> <empty>','LCH',0,'p_LCH2','tomlex.py',553),
  ('LITERALCHAR -> CHAR','LITERALCHAR',1,'p_LITERALCHAR1','tomlex.py',557),
  ('LITERALCHAR -> ESCAPED','LITERALCHAR',1,'p_LITERALCHAR2','tomlex.py',561),
  ('LITERALCHAR -> WHITESPACE','LITERALCHAR',1,'p_LITERALCHAR3','tomlex.py',565),
  ('MLLITERALSTRING -> MLLITERALSTRINGDELIM NLR MLLITERALBODY MLLITERALSTRINGDELIM','MLLITERALSTRING',4,'p_MLLITERALSTRING','tomlex.py',569),
  ('NLR -> NEWLINE','NLR',1,'p_NLR1','tomlex.py',573),
  ('NLR -> <empty>','NLR',0,'p_NLR2','tomlex.py',577),
  ('MLLITERALSTRINGDELIM -> APOSTROFE APOSTROFE APOSTROFE','MLLITERALSTRINGDELIM',3,'p_MLLITERALSTRINGDELIM','tomlex.py',581),
  ('MLLITERALBODY -> MLLC','MLLITERALBODY',1,'p_MLLITERALBODY','tomlex.py',589),
  ('MLLC -> MLLCONTENT MLLC','MLLC',2,'p_MLLC1','tomlex.py',594),
  ('MLLC -> <empty>','MLLC',0,'p_MLLC2','tomlex.py',599),
  ('MLLCONTENT -> MLLCHAR','MLLCONTENT',1,'p_MLLCONTENT1','tomlex.py',627),
  ('MLLCONTENT -> NEWLINE','MLLCONTENT',1,'p_MLLCONTENT2','tomlex.py',631),
  ('MLLCHAR -> CHAR','MLLCHAR',1,'p_MLLCHAR1','tomlex.py',635),
  ('MLLCHAR -> DOT_SEP','MLLCHAR',1,'p_MLLCHAR2','tomlex.py',639),
  ('MLLCHAR -> WHITESPACE','MLLCHAR',1,'p_MLLCHAR3','tomlex.py',643),
  ('ARRAY -> APR ARRAYVALUES WSCOMMENTNEWLINE FPR','ARRAY',4,'p_ARRAY','tomlex.py',655),
  ('ARRAYVALUES -> <empty>','ARRAYVALUES',0,'p_ARRAYVALUES1','tomlex.py',659),
  ('ARRAYVALUES -> WSCOMMENTNEWLINE VALUE ARRAYCONTEUDO','ARRAYVALUES',3,'p_ARRAYVALUES2','tomlex.py',663),
  ('ARRAYCONTEUDO -> <empty>','ARRAYCONTEUDO',0,'p_ARRAYVALUES3','tomlex.py',669),
  ('ARRAYCONTEUDO -> WSCOMMENTNEWLINE VIRGULA ARRAYVALUES','ARRAYCONTEUDO',3,'p_ARRAYVALUES4','tomlex.py',674),
  ('WSCOMMENTNEWLINE -> <empty>','WSCOMMENTNEWLINE',0,'p_WSCOMMENTNEWLINE1','tomlex.py',690),
  ('WSCOMMENTNEWLINE -> INNERCOMMENT WSCOMMENTNEWLINE','WSCOMMENTNEWLINE',2,'p_WSCOMMENTNEWLINE2','tomlex.py',694),
  ('INNERCOMMENT -> WHITESPACE','INNERCOMMENT',1,'p_INNERCOMMENT1','tomlex.py',698),
  ('INNERCOMMENT -> COMMENTOUNAO NEWLINE','INNERCOMMENT',2,'p_INNERCOMMENT2','tomlex.py',702),
  ('COMMENTOUNAO -> COMMENT','COMMENTOUNAO',1,'p_COMMENTOUNAO1','tomlex.py',706),
  ('COMMENTOUNAO -> <empty>','COMMENTOUNAO',0,'p_COMMENTOUNAO2','tomlex.py',710),
  ('TABLE -> APR KEY FPR','TABLE',3,'p_TABLE','tomlex.py',737),
]
