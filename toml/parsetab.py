
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACH APOSTROFE APR ASPA ATC ATO BIN BOOLEAN CHAR COMMENT DATE DOT_SEP DOUBLEAPOSTROFE DOUBLEASPA ESCAPE ESC_BACKSPACE ESC_CRETURN ESC_FF ESC_HEX4 ESC_HEX8 ESC_NL ESC_QUOTE ESC_REVERSE ESC_TAB FCH FLOAT FPR HEX IGUAL INF INTEGER MINUS NAN NEWLINE OCT PLUS TIME TIME_DELIM TRIPLEAPOSTROFE TRIPLEASPA TWODOT_SEP UNDERSC0RE UNDERSCORE VIRGULA WHITESPACETOML : TITLES GROUPSTITLES : KVALUE EXPRESSION TITLESTITLES :GROUPS : SECCAO EXPRESSION GROUPSGROUPS : SECCAO : TABLE EXPRESSION ATRIBUICOESSECCAO :ATRIBUICOES : KVALUE EXPRESSION ATRIBUICOESATRIBUICOES :EXPRESSION : COMMENT EXPRESSIONEXPRESSION : NEWLINE EXPRESSIONEXPRESSION :KVALUE : KEY kvwhitespace IGUAL kvwhitespace VALUEkvwhitespace : WHITESPACEkvwhitespace :KEY : SIMPLEKEYKEY : DOTKEYSIMPLEKEY : QUOTEDKEYSIMPLEKEY : UNQUOTEDKEYUNQUOTEDKEY : OCCURRENCES UNQUOTEDKEYAUXUNQUOTEDKEYAUX : OCCURRENCES UNQUOTEDKEYAUXUNQUOTEDKEYAUX :OCCURRENCES : CHAROCCURRENCES : INTEGEROCCURRENCES : MINUSOCCURRENCES : UNDERSCOREQUOTEDKEY : BASICSTRINGQUOTEDKEY : LITERALSTRINGDOTKEY : SIMPLEKEY DOT_SEP SIMPLEKEY DOTSIMPKEYDOTSIMPKEY : DOT_SEP SIMPLEKEY DOTSIMPKEYDOTSIMPKEY : VALUE : STRINGVALUE : BOOLEANVALUE : INTEGERVALUE : ARRAYVALUE : INLINETABLEVALUE : DATETIMEDATETIME : LOCALDATETIMEDATETIME : LOCALDATEDATETIME : LOCALTIMELOCALDATETIME : LOCALDATE LOCALTIMELOCALDATE : DATELOCALTIME : TIMEVALUE : FLOATSTRING : MULTILINEBASICSTRINGSTRING : BASICSTRINGSTRING : MLLITERALSTRINGSTRING : LITERALSTRINGBASICSTRING : ASPA BC ASPABC : BASICCHAR BCBC :BASICCHAR : BASICUNESCAPEDBASICCHAR : ESCAPEDBASICUNESCAPED : WHITESPACEBASICUNESCAPED : CHARBASICUNESCAPED : INTEGERBASICUNESCAPED : FLOATBASICUNESCAPED : MINUSBASICUNESCAPED : APOSTROFEBASICUNESCAPED : ESCAPEDBASICUNESCAPED : DOT_SEPBASICUNESCAPED : TWODOT_SEPESCAPED : ESC_QUOTEESCAPED : ESC_REVERSEESCAPED : ESC_BACKSPACEESCAPED : ESC_FFESCAPED : ESC_NLESCAPED : ESC_CRETURNESCAPED : ESC_TABESCAPED : ESC_HEX4ESCAPED : ESC_HEX8MULTILINEBASICSTRING : TRIPLEASPA MLNL MLBASICBODY TRIPLEASPAMLNL : NEWLINEMLNL :MLBCSTRDELIM : ASPA ASPA ASPAMLBASICBODY : MLBCMLBC : CONTENTQUOTE MLBCCONTENTQUOTE : MLBCONTENTCONTENTQUOTE : MLBQUOTESMLBC :MLBCONTENT : MLBCHARMLBCONTENT : NEWLINEMLBCONTENT : MLBESCAPEDNLMLBCONTENT : TWODOT_SEPMLBCONTENT : DOT_SEPMLBCONTENT : VIRGULAMLBCHAR : MLBUNESCAPEDMLBCHAR : ESCAPEDMLBQUOTES : ASPAMLBQUOTES : DOUBLEASPAMLBQUOTES :MLBUNESCAPED : WHITESPACEMLBUNESCAPED : CHARMLBESCAPEDNL : ESCAPE NEWLINE WHNLWHNL : SPACENEWLINE WHNLWHNL :SPACENEWLINE : WHITESPACESPACENEWLINE : NEWLINELITERALSTRING : APOSTROFE LCH APOSTROFELCH : LITERALCHAR LCHLCH :LITERALCHAR : CHARLITERALCHAR : ESCAPEDLITERALCHAR : WHITESPACELITERALCHAR : TWODOT_SEPLITERALCHAR : ASPALITERALCHAR : ESCAPEMLLITERALSTRING : TRIPLEAPOSTROFE NLR MLLITERALBODY TRIPLEAPOSTROFENLR : NEWLINENLR :MLLITERALBODY : MLLCMLLC : MLLCONTENTQUOTES MLLCMLLCONTENTQUOTES : MLLCONTENTMLLCONTENTQUOTES : MLLQUOTESMLLC :MLLCONTENT : MLLCHARMLLCONTENT : NEWLINEMLLCHAR : CHARMLLCHAR : DOT_SEPMLLCHAR : WHITESPACEMLLCHAR : VIRGULAMLLQUOTES : DOUBLEAPOSTROFEMLLQUOTES : APOSTROFEMLLQUOTES :ARRAY : APR ARRAYVALUES WSCOMMENTNEWLINE FPRARRAYVALUES :ARRAYVALUES : WSCOMMENTNEWLINE VALUE ARRAYCONTEUDOARRAYCONTEUDO :ARRAYCONTEUDO : WSCOMMENTNEWLINE VIRGULA ARRAYVALUESWSCOMMENTNEWLINE :WSCOMMENTNEWLINE : INNERCOMMENT WSCOMMENTNEWLINEINNERCOMMENT : WHITESPACEINNERCOMMENT : COMMENTOUNAO NEWLINECOMMENTOUNAO : COMMENTCOMMENTOUNAO :TABLE : STDTABLETABLE : TABLEARRAYSTDTABLE : APR KEY FPRINLINETABLE : ACH FCHINLINETABLE : ACH INLINETABLEWS INLINEKVALUE INLINETABLEWS FCHINLINETABLEWS : INLINETABLEWS : WHITESPACEINLINEKVALUE : INLINEKVALUE INLINETABLEWS VIRGULA INLINETABLEWS KVALUEINLINEKVALUE : KVALUETABLEARRAY : ATO KEY ATC'
    
_lr_action_items = {'APR':([0,2,3,19,20,21,22,25,26,27,29,62,63,66,67,68,69,72,74,77,78,79,80,81,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,100,101,104,105,107,109,110,111,114,117,125,126,160,164,167,169,170,],[-3,23,-12,-12,-12,-136,-137,-3,-12,-12,-14,23,-9,-2,-10,-11,-15,-49,-99,-6,-12,-138,-145,97,-9,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,-130,-38,-39,-40,-42,-43,-8,97,-130,-132,-139,-41,-131,-133,-125,-72,-108,-130,-140,]),'ATO':([0,2,3,19,20,21,22,25,26,27,62,63,66,67,68,72,74,77,78,79,80,84,85,86,87,88,89,90,91,92,93,94,95,96,99,100,101,104,105,107,114,117,160,164,167,170,],[-3,24,-12,-12,-12,-136,-137,-3,-12,-12,24,-9,-2,-10,-11,-49,-99,-6,-12,-138,-145,-9,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,-38,-39,-40,-42,-43,-8,-139,-41,-125,-72,-108,-140,]),'COMMENT':([0,2,3,19,20,21,22,25,26,27,62,63,66,67,68,72,74,77,78,79,80,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,100,101,104,105,107,108,110,111,114,117,124,126,160,162,164,167,169,170,176,],[-3,-7,26,26,26,-136,-137,-3,26,26,-7,-9,-2,-10,-11,-49,-99,-6,26,-138,-145,-9,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,113,-38,-39,-40,-42,-43,-8,113,113,-132,-139,-41,113,-133,-125,-127,-72,-108,113,-140,-129,]),'NEWLINE':([0,2,3,19,20,21,22,25,26,27,45,46,47,48,49,50,51,52,53,62,63,66,67,68,72,74,77,78,79,80,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,100,101,102,103,104,105,107,108,110,111,112,113,114,117,118,119,120,121,124,126,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,149,150,151,152,153,154,155,156,157,158,159,160,162,164,166,167,169,170,172,173,174,175,176,178,],[-3,-7,27,27,27,-136,-137,-3,27,27,-63,-64,-65,-66,-67,-68,-69,-70,-71,-7,-9,-2,-10,-11,-49,-99,-6,27,-138,-145,-9,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,-126,-38,-39,-40,119,121,-42,-43,-8,-135,-135,-132,126,-134,-139,-41,135,-73,153,-109,-128,-133,135,-78,-79,-81,-82,-83,-84,-85,-86,-89,-90,-87,-88,166,-92,-93,153,-113,-114,-116,-117,-122,-123,-118,-119,-120,-121,-125,-127,-72,172,-108,-126,-140,-98,-94,172,-97,-129,-95,]),'$end':([0,1,2,3,18,19,20,21,22,25,26,27,62,63,66,67,68,72,74,76,77,78,79,80,84,85,86,87,88,89,90,91,92,93,94,95,96,99,100,101,104,105,107,114,117,160,164,167,170,],[-3,0,-5,-12,-1,-12,-12,-136,-137,-3,-12,-12,-5,-9,-2,-10,-11,-49,-99,-4,-6,-12,-138,-145,-9,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,-38,-39,-40,-42,-43,-8,-139,-41,-125,-72,-108,-140,]),'ASPA':([0,3,12,13,20,21,22,23,24,25,26,27,29,30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,63,67,68,69,72,73,74,78,79,80,81,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,105,109,110,111,114,115,116,117,118,119,125,126,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,160,164,166,167,169,170,171,172,173,174,175,177,178,],[12,-12,-51,60,-12,-136,-137,12,12,12,-12,-12,-14,12,72,-51,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,60,-102,-103,-104,-105,-106,-107,12,-10,-11,-15,-49,-50,-99,-12,-138,-145,12,12,12,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,-130,-141,-38,-39,-40,-74,-42,-43,12,-130,-132,-139,12,-142,-41,140,-73,-131,-133,140,-78,-79,-81,-82,-83,-84,-85,-86,-89,-90,-87,-88,-92,-93,-125,-72,-96,-108,-130,-140,-141,-98,-94,-96,-97,12,-95,]),'APOSTROFE':([0,3,12,13,20,21,22,23,24,25,26,27,29,30,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,67,68,69,72,74,75,78,79,80,81,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,103,104,105,109,110,111,114,115,116,117,120,121,125,126,149,150,151,152,153,154,155,156,157,158,159,160,164,167,169,170,171,177,],[13,-12,42,-101,-12,-136,-137,13,13,13,-12,-12,-14,13,42,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,74,-101,-102,-103,-104,-105,-106,-107,13,-10,-11,-15,-49,-99,-100,-12,-138,-145,13,13,13,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,-130,-141,-38,-39,-40,-110,-42,-43,13,-130,-132,-139,13,-142,-41,155,-109,-131,-133,155,-113,-114,-116,-117,-122,-123,-118,-119,-120,-121,-125,-72,-108,-130,-140,-141,13,]),'CHAR':([0,3,11,12,13,14,15,16,17,20,21,22,23,24,25,26,27,30,31,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,63,67,68,72,74,78,79,80,82,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,102,103,104,105,114,115,116,117,118,119,120,121,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,149,150,151,152,153,154,155,156,157,158,159,160,164,166,167,170,171,172,173,174,175,177,178,],[14,-12,14,38,56,-23,-24,-25,-26,-12,-136,-137,14,14,14,-12,-12,14,14,38,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,56,-102,-103,-104,-105,-106,-107,14,-10,-11,-49,-99,-12,-138,-145,14,14,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,-141,-38,-39,-40,-74,-110,-42,-43,-139,14,-142,-41,146,-73,156,-109,146,-78,-79,-81,-82,-83,-84,-85,-86,-89,-90,-87,-88,-92,-93,156,-113,-114,-116,-117,-122,-123,-118,-119,-120,-121,-125,-72,-96,-108,-140,-141,-98,-94,-96,-97,14,-95,]),'INTEGER':([0,3,11,12,14,15,16,17,20,21,22,23,24,25,26,27,29,30,31,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,63,67,68,69,72,74,78,79,80,81,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,109,110,111,114,115,116,117,125,126,160,164,167,169,170,171,177,],[15,-12,15,39,-23,-24,-25,-26,-12,-136,-137,15,15,15,-12,-12,-14,15,15,39,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,15,-10,-11,-15,-49,-99,-12,-138,-145,88,15,15,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,-130,-141,-38,-39,-40,-42,-43,88,-130,-132,-139,15,-142,-41,-131,-133,-125,-72,-108,-130,-140,-141,15,]),'MINUS':([0,3,11,12,14,15,16,17,20,21,22,23,24,25,26,27,30,31,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,63,67,68,72,74,78,79,80,82,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,104,105,114,115,116,117,160,164,167,170,171,177,],[16,-12,16,41,-23,-24,-25,-26,-12,-136,-137,16,16,16,-12,-12,16,16,41,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,16,-10,-11,-49,-99,-12,-138,-145,16,16,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,-141,-38,-39,-40,-42,-43,-139,16,-142,-41,-125,-72,-108,-140,-141,16,]),'UNDERSCORE':([0,3,11,14,15,16,17,20,21,22,23,24,25,26,27,30,31,63,67,68,72,74,78,79,80,82,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,104,105,114,115,116,117,160,164,167,170,171,177,],[17,-12,17,-23,-24,-25,-26,-12,-136,-137,17,17,17,-12,-12,17,17,17,-10,-11,-49,-99,-12,-138,-145,17,17,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,-141,-38,-39,-40,-42,-43,-139,17,-142,-41,-125,-72,-108,-140,-141,17,]),'WHITESPACE':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,31,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,69,70,71,72,74,83,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,110,111,114,117,118,119,120,121,122,124,126,127,128,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,149,150,151,152,153,154,155,156,157,158,159,160,162,164,166,167,169,170,171,172,173,174,175,176,178,179,],[29,-16,-17,-18,-19,-27,-28,-22,37,58,-23,-24,-25,-26,-22,-20,37,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,58,-102,-103,-104,-105,-106,-107,29,-31,-21,-49,-99,-29,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,111,116,-38,-39,-40,-74,-110,-42,-43,-31,111,111,-132,-139,-41,145,-73,158,-109,-30,111,-133,116,-144,145,-78,-79,-81,-82,-83,-84,-85,-86,-89,-90,-87,-88,-92,-93,158,-113,-114,-116,-117,-122,-123,-118,-119,-120,-121,-125,-127,-72,175,-108,111,-140,116,-98,-94,175,-97,-129,-95,-143,]),'IGUAL':([4,5,6,7,8,9,10,11,14,15,16,17,28,29,31,32,70,71,72,74,83,106,122,],[-15,-16,-17,-18,-19,-27,-28,-22,-23,-24,-25,-26,69,-14,-22,-20,-31,-21,-49,-99,-29,-31,-30,]),'FPR':([5,6,7,8,9,10,11,14,15,16,17,31,32,64,70,71,72,74,83,86,87,88,89,90,91,92,93,94,95,96,97,99,100,101,104,105,106,108,110,111,114,117,122,123,124,125,126,160,162,164,167,169,170,176,],[-16,-17,-18,-19,-27,-28,-22,-23,-24,-25,-26,-22,-20,79,-31,-21,-49,-99,-29,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,-126,-38,-39,-40,-42,-43,-31,-130,-130,-132,-139,-41,-30,160,-128,-131,-133,-125,-127,-72,-108,-126,-140,-129,]),'ATC':([5,6,7,8,9,10,11,14,15,16,17,31,32,65,70,71,72,74,83,106,122,],[-16,-17,-18,-19,-27,-28,-22,-23,-24,-25,-26,-22,-20,80,-31,-21,-49,-99,-29,-31,-30,]),'DOT_SEP':([5,7,8,9,10,11,12,14,15,16,17,31,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,70,71,72,74,102,103,106,118,119,120,121,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,149,150,151,152,153,154,155,156,157,158,159,166,172,173,174,175,178,],[30,-18,-19,-27,-28,-22,43,-23,-24,-25,-26,-22,-20,43,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,82,-21,-49,-99,-74,-110,82,138,-73,157,-109,138,-78,-79,-81,-82,-83,-84,-85,-86,-89,-90,-87,-88,-92,-93,157,-113,-114,-116,-117,-122,-123,-118,-119,-120,-121,-96,-98,-94,-96,-97,-95,]),'FLOAT':([12,29,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,69,81,97,109,110,111,125,126,169,],[40,-14,40,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-15,92,-130,92,-130,-132,-131,-133,-130,]),'TWODOT_SEP':([12,13,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,102,118,119,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,166,172,173,174,175,178,],[44,59,44,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,59,-102,-103,-104,-105,-106,-107,-74,137,-73,137,-78,-79,-81,-82,-83,-84,-85,-86,-89,-90,-87,-88,-92,-93,-96,-98,-94,-96,-97,-95,]),'ESC_QUOTE':([12,13,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,102,118,119,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,166,172,173,174,175,178,],[45,45,45,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,45,-102,-103,-104,-105,-106,-107,-74,45,-73,45,-78,-79,-81,-82,-83,-84,-85,-86,-89,-90,-87,-88,-92,-93,-96,-98,-94,-96,-97,-95,]),'ESC_REVERSE':([12,13,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,102,118,119,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,166,172,173,174,175,178,],[46,46,46,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,46,-102,-103,-104,-105,-106,-107,-74,46,-73,46,-78,-79,-81,-82,-83,-84,-85,-86,-89,-90,-87,-88,-92,-93,-96,-98,-94,-96,-97,-95,]),'ESC_BACKSPACE':([12,13,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,102,118,119,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,166,172,173,174,175,178,],[47,47,47,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,47,-102,-103,-104,-105,-106,-107,-74,47,-73,47,-78,-79,-81,-82,-83,-84,-85,-86,-89,-90,-87,-88,-92,-93,-96,-98,-94,-96,-97,-95,]),'ESC_FF':([12,13,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,102,118,119,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,166,172,173,174,175,178,],[48,48,48,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,48,-102,-103,-104,-105,-106,-107,-74,48,-73,48,-78,-79,-81,-82,-83,-84,-85,-86,-89,-90,-87,-88,-92,-93,-96,-98,-94,-96,-97,-95,]),'ESC_NL':([12,13,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,102,118,119,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,166,172,173,174,175,178,],[49,49,49,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,49,-102,-103,-104,-105,-106,-107,-74,49,-73,49,-78,-79,-81,-82,-83,-84,-85,-86,-89,-90,-87,-88,-92,-93,-96,-98,-94,-96,-97,-95,]),'ESC_CRETURN':([12,13,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,102,118,119,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,166,172,173,174,175,178,],[50,50,50,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,50,-102,-103,-104,-105,-106,-107,-74,50,-73,50,-78,-79,-81,-82,-83,-84,-85,-86,-89,-90,-87,-88,-92,-93,-96,-98,-94,-96,-97,-95,]),'ESC_TAB':([12,13,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,102,118,119,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,166,172,173,174,175,178,],[51,51,51,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,51,-102,-103,-104,-105,-106,-107,-74,51,-73,51,-78,-79,-81,-82,-83,-84,-85,-86,-89,-90,-87,-88,-92,-93,-96,-98,-94,-96,-97,-95,]),'ESC_HEX4':([12,13,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,102,118,119,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,166,172,173,174,175,178,],[52,52,52,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,52,-102,-103,-104,-105,-106,-107,-74,52,-73,52,-78,-79,-81,-82,-83,-84,-85,-86,-89,-90,-87,-88,-92,-93,-96,-98,-94,-96,-97,-95,]),'ESC_HEX8':([12,13,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,102,118,119,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,166,172,173,174,175,178,],[53,53,53,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,53,-102,-103,-104,-105,-106,-107,-74,53,-73,53,-78,-79,-81,-82,-83,-84,-85,-86,-89,-90,-87,-88,-92,-93,-96,-98,-94,-96,-97,-95,]),'ESCAPE':([13,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,102,118,119,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,166,172,173,174,175,178,],[61,-63,-64,-65,-66,-67,-68,-69,-70,-71,61,-102,-103,-104,-105,-106,-107,-74,144,-73,144,-78,-79,-81,-82,-83,-84,-85,-86,-89,-90,-87,-88,-92,-93,-96,-98,-94,-96,-97,-95,]),'BOOLEAN':([29,69,81,97,109,110,111,125,126,169,],[-14,-15,87,-130,87,-130,-132,-131,-133,-130,]),'ACH':([29,69,81,97,109,110,111,125,126,169,],[-14,-15,98,-130,98,-130,-132,-131,-133,-130,]),'TRIPLEASPA':([29,45,46,47,48,49,50,51,52,53,69,81,97,102,109,110,111,118,119,125,126,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,165,166,169,172,173,174,175,178,],[-14,-63,-64,-65,-66,-67,-68,-69,-70,-71,-15,102,-130,-74,102,-130,-132,-80,-73,-131,-133,164,-76,-80,-78,-79,-81,-82,-83,-84,-85,-86,-89,-90,-87,-88,-92,-93,-77,-96,-130,-98,-94,-96,-97,-95,]),'TRIPLEAPOSTROFE':([29,69,81,97,103,109,110,111,120,121,125,126,147,148,149,150,151,152,153,154,155,156,157,158,159,168,169,],[-14,-15,103,-130,-110,103,-130,-132,-115,-109,-131,-133,167,-111,-115,-113,-114,-116,-117,-122,-123,-118,-119,-120,-121,-112,-130,]),'DATE':([29,69,81,97,109,110,111,125,126,169,],[-14,-15,104,-130,104,-130,-132,-131,-133,-130,]),'TIME':([29,69,81,97,100,104,109,110,111,125,126,169,],[-14,-15,105,-130,105,-42,105,-130,-132,-131,-133,-130,]),'VIRGULA':([45,46,47,48,49,50,51,52,53,72,74,85,86,87,88,89,90,91,92,93,94,95,96,99,100,101,102,103,104,105,110,111,114,116,117,118,119,120,121,124,125,126,127,128,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,149,150,151,152,153,154,155,156,157,158,159,160,161,163,164,166,167,170,172,173,174,175,178,179,],[-63,-64,-65,-66,-67,-68,-69,-70,-71,-49,-99,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,-38,-39,-40,-74,-110,-42,-43,-130,-132,-139,-142,-41,139,-73,159,-109,-130,-131,-133,-141,-144,139,-78,-79,-81,-82,-83,-84,-85,-86,-89,-90,-87,-88,-92,-93,159,-113,-114,-116,-117,-122,-123,-118,-119,-120,-121,-125,169,171,-72,-96,-108,-140,-98,-94,-96,-97,-95,-143,]),'DOUBLEASPA':([45,46,47,48,49,50,51,52,53,102,118,119,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,166,172,173,174,175,178,],[-63,-64,-65,-66,-67,-68,-69,-70,-71,-74,141,-73,141,-78,-79,-81,-82,-83,-84,-85,-86,-89,-90,-87,-88,-92,-93,-96,-98,-94,-96,-97,-95,]),'FCH':([72,74,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,104,105,114,116,117,127,128,160,163,164,167,170,179,],[-49,-99,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,114,-38,-39,-40,-42,-43,-139,-142,-41,-141,-144,-125,170,-72,-108,-140,-143,]),'DOUBLEAPOSTROFE':([103,120,121,149,150,151,152,153,154,155,156,157,158,159,],[-110,154,-109,154,-113,-114,-116,-117,-122,-123,-118,-119,-120,-121,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'TOML':([0,],[1,]),'TITLES':([0,25,],[2,66,]),'KVALUE':([0,25,63,84,115,177,],[3,3,78,78,128,179,]),'KEY':([0,23,24,25,63,84,115,177,],[4,64,65,4,4,4,4,4,]),'SIMPLEKEY':([0,23,24,25,30,63,82,84,115,177,],[5,5,5,5,70,5,106,5,5,5,]),'DOTKEY':([0,23,24,25,63,84,115,177,],[6,6,6,6,6,6,6,6,]),'QUOTEDKEY':([0,23,24,25,30,63,82,84,115,177,],[7,7,7,7,7,7,7,7,7,7,]),'UNQUOTEDKEY':([0,23,24,25,30,63,82,84,115,177,],[8,8,8,8,8,8,8,8,8,8,]),'BASICSTRING':([0,23,24,25,30,63,81,82,84,109,115,177,],[9,9,9,9,9,9,94,9,9,94,9,9,]),'LITERALSTRING':([0,23,24,25,30,63,81,82,84,109,115,177,],[10,10,10,10,10,10,96,10,10,96,10,10,]),'OCCURRENCES':([0,11,23,24,25,30,31,63,82,84,115,177,],[11,31,11,11,11,11,31,11,11,11,11,11,]),'GROUPS':([2,62,],[18,76,]),'SECCAO':([2,62,],[19,19,]),'TABLE':([2,62,],[20,20,]),'STDTABLE':([2,62,],[21,21,]),'TABLEARRAY':([2,62,],[22,22,]),'EXPRESSION':([3,19,20,26,27,78,],[25,62,63,67,68,84,]),'kvwhitespace':([4,69,],[28,81,]),'UNQUOTEDKEYAUX':([11,31,],[32,71,]),'BC':([12,34,],[33,73,]),'BASICCHAR':([12,34,],[34,34,]),'BASICUNESCAPED':([12,34,],[35,35,]),'ESCAPED':([12,13,34,55,118,131,],[36,57,36,57,143,143,]),'LCH':([13,55,],[54,75,]),'LITERALCHAR':([13,55,],[55,55,]),'ATRIBUICOES':([63,84,],[77,107,]),'DOTSIMPKEY':([70,106,],[83,122,]),'VALUE':([81,109,],[85,124,]),'STRING':([81,109,],[86,86,]),'ARRAY':([81,109,],[89,89,]),'INLINETABLE':([81,109,],[90,90,]),'DATETIME':([81,109,],[91,91,]),'MULTILINEBASICSTRING':([81,109,],[93,93,]),'MLLITERALSTRING':([81,109,],[95,95,]),'LOCALDATETIME':([81,109,],[99,99,]),'LOCALDATE':([81,109,],[100,100,]),'LOCALTIME':([81,100,109,],[101,117,101,]),'ARRAYVALUES':([97,169,],[108,176,]),'WSCOMMENTNEWLINE':([97,108,110,124,169,],[109,123,125,161,109,]),'INNERCOMMENT':([97,108,110,124,169,],[110,110,110,110,110,]),'COMMENTOUNAO':([97,108,110,124,169,],[112,112,112,112,112,]),'INLINETABLEWS':([98,127,171,],[115,163,177,]),'MLNL':([102,],[118,]),'NLR':([103,],[120,]),'INLINEKVALUE':([115,],[127,]),'MLBASICBODY':([118,],[129,]),'MLBC':([118,131,],[130,165,]),'CONTENTQUOTE':([118,131,],[131,131,]),'MLBCONTENT':([118,131,],[132,132,]),'MLBQUOTES':([118,131,],[133,133,]),'MLBCHAR':([118,131,],[134,134,]),'MLBESCAPEDNL':([118,131,],[136,136,]),'MLBUNESCAPED':([118,131,],[142,142,]),'MLLITERALBODY':([120,],[147,]),'MLLC':([120,149,],[148,168,]),'MLLCONTENTQUOTES':([120,149,],[149,149,]),'MLLCONTENT':([120,149,],[150,150,]),'MLLQUOTES':([120,149,],[151,151,]),'MLLCHAR':([120,149,],[152,152,]),'ARRAYCONTEUDO':([124,],[162,]),'WHNL':([166,174,],[173,178,]),'SPACENEWLINE':([166,174,],[174,174,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> TOML","S'",1,None,None,None),
  ('TOML -> TITLES GROUPS','TOML',2,'p_TOML','tomlex.py',115),
  ('TITLES -> KVALUE EXPRESSION TITLES','TITLES',3,'p_TITLES1','tomlex.py',120),
  ('TITLES -> <empty>','TITLES',0,'p_TITLES2','tomlex.py',125),
  ('GROUPS -> SECCAO EXPRESSION GROUPS','GROUPS',3,'p_GROUPS1','tomlex.py',129),
  ('GROUPS -> <empty>','GROUPS',0,'p_GROUPS2','tomlex.py',135),
  ('SECCAO -> TABLE EXPRESSION ATRIBUICOES','SECCAO',3,'p_SECCAO1','tomlex.py',139),
  ('SECCAO -> <empty>','SECCAO',0,'p_SECCAO2','tomlex.py',146),
  ('ATRIBUICOES -> KVALUE EXPRESSION ATRIBUICOES','ATRIBUICOES',3,'p_ATRIBUICOES1','tomlex.py',150),
  ('ATRIBUICOES -> <empty>','ATRIBUICOES',0,'p_ATRIBUICOES2','tomlex.py',156),
  ('EXPRESSION -> COMMENT EXPRESSION','EXPRESSION',2,'p_EXPRESSION1','tomlex.py',160),
  ('EXPRESSION -> NEWLINE EXPRESSION','EXPRESSION',2,'p_EXPRESSION2','tomlex.py',164),
  ('EXPRESSION -> <empty>','EXPRESSION',0,'p_EXPRESSION3','tomlex.py',168),
  ('KVALUE -> KEY kvwhitespace IGUAL kvwhitespace VALUE','KVALUE',5,'p_KVALUE','tomlex.py',172),
  ('kvwhitespace -> WHITESPACE','kvwhitespace',1,'p_kvwhitespace1','tomlex.py',180),
  ('kvwhitespace -> <empty>','kvwhitespace',0,'p_kvwhitespace2','tomlex.py',184),
  ('KEY -> SIMPLEKEY','KEY',1,'p_KEY1','tomlex.py',188),
  ('KEY -> DOTKEY','KEY',1,'p_KEY2','tomlex.py',192),
  ('SIMPLEKEY -> QUOTEDKEY','SIMPLEKEY',1,'p_SIMPLEKEY1','tomlex.py',197),
  ('SIMPLEKEY -> UNQUOTEDKEY','SIMPLEKEY',1,'p_SIMPLEKEY2','tomlex.py',201),
  ('UNQUOTEDKEY -> OCCURRENCES UNQUOTEDKEYAUX','UNQUOTEDKEY',2,'p_UNQUOTEDKEY1','tomlex.py',206),
  ('UNQUOTEDKEYAUX -> OCCURRENCES UNQUOTEDKEYAUX','UNQUOTEDKEYAUX',2,'p_UNQUOTEDKEY2','tomlex.py',211),
  ('UNQUOTEDKEYAUX -> <empty>','UNQUOTEDKEYAUX',0,'p_UNQUOTEDKEY3','tomlex.py',216),
  ('OCCURRENCES -> CHAR','OCCURRENCES',1,'p_OCCURRENCES1','tomlex.py',220),
  ('OCCURRENCES -> INTEGER','OCCURRENCES',1,'p_OCCURRENCES2','tomlex.py',224),
  ('OCCURRENCES -> MINUS','OCCURRENCES',1,'p_OCCURRENCES3','tomlex.py',229),
  ('OCCURRENCES -> UNDERSCORE','OCCURRENCES',1,'p_OCCURRENCES4','tomlex.py',234),
  ('QUOTEDKEY -> BASICSTRING','QUOTEDKEY',1,'p_QUOTEDKEY1','tomlex.py',239),
  ('QUOTEDKEY -> LITERALSTRING','QUOTEDKEY',1,'p_QUOTEDKEY2','tomlex.py',244),
  ('DOTKEY -> SIMPLEKEY DOT_SEP SIMPLEKEY DOTSIMPKEY','DOTKEY',4,'p_DOTKEY','tomlex.py',248),
  ('DOTSIMPKEY -> DOT_SEP SIMPLEKEY DOTSIMPKEY','DOTSIMPKEY',3,'p_DOTSIMPKEY1','tomlex.py',252),
  ('DOTSIMPKEY -> <empty>','DOTSIMPKEY',0,'p_DOTSIMPKEY2','tomlex.py',257),
  ('VALUE -> STRING','VALUE',1,'p_VALUE1','tomlex.py',261),
  ('VALUE -> BOOLEAN','VALUE',1,'p_VALUE2','tomlex.py',266),
  ('VALUE -> INTEGER','VALUE',1,'p_VALUE3','tomlex.py',270),
  ('VALUE -> ARRAY','VALUE',1,'p_VALUE4','tomlex.py',274),
  ('VALUE -> INLINETABLE','VALUE',1,'p_VALUE5','tomlex.py',278),
  ('VALUE -> DATETIME','VALUE',1,'p_VALUE6','tomlex.py',283),
  ('DATETIME -> LOCALDATETIME','DATETIME',1,'p_DATETIME1','tomlex.py',287),
  ('DATETIME -> LOCALDATE','DATETIME',1,'p_DATETIME2','tomlex.py',291),
  ('DATETIME -> LOCALTIME','DATETIME',1,'p_DATETIME3','tomlex.py',295),
  ('LOCALDATETIME -> LOCALDATE LOCALTIME','LOCALDATETIME',2,'p_LOCALDATETIME','tomlex.py',299),
  ('LOCALDATE -> DATE','LOCALDATE',1,'p_LOCALDATE','tomlex.py',303),
  ('LOCALTIME -> TIME','LOCALTIME',1,'p_LOCALTIME','tomlex.py',307),
  ('VALUE -> FLOAT','VALUE',1,'p_VALUE7','tomlex.py',311),
  ('STRING -> MULTILINEBASICSTRING','STRING',1,'p_STRING1','tomlex.py',317),
  ('STRING -> BASICSTRING','STRING',1,'p_STRING2','tomlex.py',322),
  ('STRING -> MLLITERALSTRING','STRING',1,'p_STRING3','tomlex.py',327),
  ('STRING -> LITERALSTRING','STRING',1,'p_STRING4','tomlex.py',331),
  ('BASICSTRING -> ASPA BC ASPA','BASICSTRING',3,'p_BASICSTRING','tomlex.py',336),
  ('BC -> BASICCHAR BC','BC',2,'p_BC','tomlex.py',341),
  ('BC -> <empty>','BC',0,'p_BC2','tomlex.py',345),
  ('BASICCHAR -> BASICUNESCAPED','BASICCHAR',1,'p_BASICCHAR1','tomlex.py',349),
  ('BASICCHAR -> ESCAPED','BASICCHAR',1,'p_BASICCHAR2','tomlex.py',354),
  ('BASICUNESCAPED -> WHITESPACE','BASICUNESCAPED',1,'p_BASICUNESCAPED1','tomlex.py',358),
  ('BASICUNESCAPED -> CHAR','BASICUNESCAPED',1,'p_BASICUNESCAPED2','tomlex.py',362),
  ('BASICUNESCAPED -> INTEGER','BASICUNESCAPED',1,'p_BASICUNESCAPED3','tomlex.py',366),
  ('BASICUNESCAPED -> FLOAT','BASICUNESCAPED',1,'p_BASICUNESCAPED4','tomlex.py',370),
  ('BASICUNESCAPED -> MINUS','BASICUNESCAPED',1,'p_BASICUNESCAPED5','tomlex.py',374),
  ('BASICUNESCAPED -> APOSTROFE','BASICUNESCAPED',1,'p_BASICUNESCAPED6','tomlex.py',378),
  ('BASICUNESCAPED -> ESCAPED','BASICUNESCAPED',1,'p_BASICUNESCAPED7','tomlex.py',382),
  ('BASICUNESCAPED -> DOT_SEP','BASICUNESCAPED',1,'p_BASICUNESCAPED8','tomlex.py',386),
  ('BASICUNESCAPED -> TWODOT_SEP','BASICUNESCAPED',1,'p_BASICUNESCAPED9','tomlex.py',390),
  ('ESCAPED -> ESC_QUOTE','ESCAPED',1,'p_ESCAPED1','tomlex.py',396),
  ('ESCAPED -> ESC_REVERSE','ESCAPED',1,'p_ESCAPED2','tomlex.py',401),
  ('ESCAPED -> ESC_BACKSPACE','ESCAPED',1,'p_ESCAPED3','tomlex.py',406),
  ('ESCAPED -> ESC_FF','ESCAPED',1,'p_ESCAPED4','tomlex.py',411),
  ('ESCAPED -> ESC_NL','ESCAPED',1,'p_ESCAPED5','tomlex.py',416),
  ('ESCAPED -> ESC_CRETURN','ESCAPED',1,'p_ESCAPED6','tomlex.py',421),
  ('ESCAPED -> ESC_TAB','ESCAPED',1,'p_ESCAPED7','tomlex.py',426),
  ('ESCAPED -> ESC_HEX4','ESCAPED',1,'p_ESCAPED8','tomlex.py',431),
  ('ESCAPED -> ESC_HEX8','ESCAPED',1,'p_ESCAPED9','tomlex.py',437),
  ('MULTILINEBASICSTRING -> TRIPLEASPA MLNL MLBASICBODY TRIPLEASPA','MULTILINEBASICSTRING',4,'p_MULTILINEBASICSTRING','tomlex.py',443),
  ('MLNL -> NEWLINE','MLNL',1,'p_MLNL1','tomlex.py',447),
  ('MLNL -> <empty>','MLNL',0,'p_MLNL2','tomlex.py',451),
  ('MLBCSTRDELIM -> ASPA ASPA ASPA','MLBCSTRDELIM',3,'p_MLBCSTRDELIM','tomlex.py',455),
  ('MLBASICBODY -> MLBC','MLBASICBODY',1,'p_MLBASICBODY','tomlex.py',459),
  ('MLBC -> CONTENTQUOTE MLBC','MLBC',2,'p_MLBC1','tomlex.py',463),
  ('CONTENTQUOTE -> MLBCONTENT','CONTENTQUOTE',1,'p_CONTENTQUOTE1','tomlex.py',467),
  ('CONTENTQUOTE -> MLBQUOTES','CONTENTQUOTE',1,'p_CONTENTQUOTE2','tomlex.py',471),
  ('MLBC -> <empty>','MLBC',0,'p_MLBC2','tomlex.py',475),
  ('MLBCONTENT -> MLBCHAR','MLBCONTENT',1,'p_MLBCONTENT1','tomlex.py',479),
  ('MLBCONTENT -> NEWLINE','MLBCONTENT',1,'p_MLBCONTENT2','tomlex.py',483),
  ('MLBCONTENT -> MLBESCAPEDNL','MLBCONTENT',1,'p_MLBCONTENT3','tomlex.py',487),
  ('MLBCONTENT -> TWODOT_SEP','MLBCONTENT',1,'p_MLBCONTENT4','tomlex.py',491),
  ('MLBCONTENT -> DOT_SEP','MLBCONTENT',1,'p_MLBCONTENT5','tomlex.py',495),
  ('MLBCONTENT -> VIRGULA','MLBCONTENT',1,'p_MLBCONTENT6','tomlex.py',499),
  ('MLBCHAR -> MLBUNESCAPED','MLBCHAR',1,'p_MLBCHAR1','tomlex.py',503),
  ('MLBCHAR -> ESCAPED','MLBCHAR',1,'p_MLBCHAR2','tomlex.py',507),
  ('MLBQUOTES -> ASPA','MLBQUOTES',1,'p_MLBQUOTES1','tomlex.py',511),
  ('MLBQUOTES -> DOUBLEASPA','MLBQUOTES',1,'p_MLBQUOTES2','tomlex.py',515),
  ('MLBQUOTES -> <empty>','MLBQUOTES',0,'p_MLBQUOTES3','tomlex.py',519),
  ('MLBUNESCAPED -> WHITESPACE','MLBUNESCAPED',1,'p_MLBUNESCAPED1','tomlex.py',523),
  ('MLBUNESCAPED -> CHAR','MLBUNESCAPED',1,'p_MLBUNESCAPED2','tomlex.py',527),
  ('MLBESCAPEDNL -> ESCAPE NEWLINE WHNL','MLBESCAPEDNL',3,'p_MLBESCAPEDNL','tomlex.py',531),
  ('WHNL -> SPACENEWLINE WHNL','WHNL',2,'p_WHNL1','tomlex.py',536),
  ('WHNL -> <empty>','WHNL',0,'p_WHNL2','tomlex.py',540),
  ('SPACENEWLINE -> WHITESPACE','SPACENEWLINE',1,'p_SPACENEWLINE1','tomlex.py',544),
  ('SPACENEWLINE -> NEWLINE','SPACENEWLINE',1,'p_SPACENEWLINE2','tomlex.py',548),
  ('LITERALSTRING -> APOSTROFE LCH APOSTROFE','LITERALSTRING',3,'p_LITERALSTRING','tomlex.py',552),
  ('LCH -> LITERALCHAR LCH','LCH',2,'p_LCH1','tomlex.py',557),
  ('LCH -> <empty>','LCH',0,'p_LCH2','tomlex.py',561),
  ('LITERALCHAR -> CHAR','LITERALCHAR',1,'p_LITERALCHAR1','tomlex.py',565),
  ('LITERALCHAR -> ESCAPED','LITERALCHAR',1,'p_LITERALCHAR2','tomlex.py',569),
  ('LITERALCHAR -> WHITESPACE','LITERALCHAR',1,'p_LITERALCHAR3','tomlex.py',573),
  ('LITERALCHAR -> TWODOT_SEP','LITERALCHAR',1,'p_LITERALCHAR4','tomlex.py',577),
  ('LITERALCHAR -> ASPA','LITERALCHAR',1,'p_LITERALCHAR5','tomlex.py',581),
  ('LITERALCHAR -> ESCAPE','LITERALCHAR',1,'p_LITERALCHAR6','tomlex.py',585),
  ('MLLITERALSTRING -> TRIPLEAPOSTROFE NLR MLLITERALBODY TRIPLEAPOSTROFE','MLLITERALSTRING',4,'p_MLLITERALSTRING','tomlex.py',589),
  ('NLR -> NEWLINE','NLR',1,'p_NLR1','tomlex.py',593),
  ('NLR -> <empty>','NLR',0,'p_NLR2','tomlex.py',597),
  ('MLLITERALBODY -> MLLC','MLLITERALBODY',1,'p_MLLITERALBODY','tomlex.py',601),
  ('MLLC -> MLLCONTENTQUOTES MLLC','MLLC',2,'p_MLLC1','tomlex.py',605),
  ('MLLCONTENTQUOTES -> MLLCONTENT','MLLCONTENTQUOTES',1,'p_MLLCONTENTQUOTES1','tomlex.py',609),
  ('MLLCONTENTQUOTES -> MLLQUOTES','MLLCONTENTQUOTES',1,'p_MLLCONTENTQUOTES2','tomlex.py',613),
  ('MLLC -> <empty>','MLLC',0,'p_MLLC2','tomlex.py',617),
  ('MLLCONTENT -> MLLCHAR','MLLCONTENT',1,'p_MLLCONTENT1','tomlex.py',621),
  ('MLLCONTENT -> NEWLINE','MLLCONTENT',1,'p_MLLCONTENT2','tomlex.py',625),
  ('MLLCHAR -> CHAR','MLLCHAR',1,'p_MLLCHAR1','tomlex.py',629),
  ('MLLCHAR -> DOT_SEP','MLLCHAR',1,'p_MLLCHAR2','tomlex.py',633),
  ('MLLCHAR -> WHITESPACE','MLLCHAR',1,'p_MLLCHAR3','tomlex.py',637),
  ('MLLCHAR -> VIRGULA','MLLCHAR',1,'p_MLLCHAR4','tomlex.py',641),
  ('MLLQUOTES -> DOUBLEAPOSTROFE','MLLQUOTES',1,'p_MLLQUOTES1','tomlex.py',645),
  ('MLLQUOTES -> APOSTROFE','MLLQUOTES',1,'p_MLLQUOTES2','tomlex.py',649),
  ('MLLQUOTES -> <empty>','MLLQUOTES',0,'p_MLLQUOTES3','tomlex.py',657),
  ('ARRAY -> APR ARRAYVALUES WSCOMMENTNEWLINE FPR','ARRAY',4,'p_ARRAY','tomlex.py',661),
  ('ARRAYVALUES -> <empty>','ARRAYVALUES',0,'p_ARRAYVALUES1','tomlex.py',665),
  ('ARRAYVALUES -> WSCOMMENTNEWLINE VALUE ARRAYCONTEUDO','ARRAYVALUES',3,'p_ARRAYVALUES2','tomlex.py',669),
  ('ARRAYCONTEUDO -> <empty>','ARRAYCONTEUDO',0,'p_ARRAYVALUES3','tomlex.py',675),
  ('ARRAYCONTEUDO -> WSCOMMENTNEWLINE VIRGULA ARRAYVALUES','ARRAYCONTEUDO',3,'p_ARRAYVALUES4','tomlex.py',680),
  ('WSCOMMENTNEWLINE -> <empty>','WSCOMMENTNEWLINE',0,'p_WSCOMMENTNEWLINE1','tomlex.py',696),
  ('WSCOMMENTNEWLINE -> INNERCOMMENT WSCOMMENTNEWLINE','WSCOMMENTNEWLINE',2,'p_WSCOMMENTNEWLINE2','tomlex.py',701),
  ('INNERCOMMENT -> WHITESPACE','INNERCOMMENT',1,'p_INNERCOMMENT1','tomlex.py',705),
  ('INNERCOMMENT -> COMMENTOUNAO NEWLINE','INNERCOMMENT',2,'p_INNERCOMMENT2','tomlex.py',709),
  ('COMMENTOUNAO -> COMMENT','COMMENTOUNAO',1,'p_COMMENTOUNAO1','tomlex.py',713),
  ('COMMENTOUNAO -> <empty>','COMMENTOUNAO',0,'p_COMMENTOUNAO2','tomlex.py',717),
  ('TABLE -> STDTABLE','TABLE',1,'p_TABLE1','tomlex.py',720),
  ('TABLE -> TABLEARRAY','TABLE',1,'p_TABLE2','tomlex.py',724),
  ('STDTABLE -> APR KEY FPR','STDTABLE',3,'p_STDTABLE','tomlex.py',728),
  ('INLINETABLE -> ACH FCH','INLINETABLE',2,'p_INLINETABLE','tomlex.py',736),
  ('INLINETABLE -> ACH INLINETABLEWS INLINEKVALUE INLINETABLEWS FCH','INLINETABLE',5,'p_INLINETABLE2','tomlex.py',740),
  ('INLINETABLEWS -> <empty>','INLINETABLEWS',0,'p_INLINETABLEWS1','tomlex.py',744),
  ('INLINETABLEWS -> WHITESPACE','INLINETABLEWS',1,'p_INLINETABLEWS2','tomlex.py',747),
  ('INLINEKVALUE -> INLINEKVALUE INLINETABLEWS VIRGULA INLINETABLEWS KVALUE','INLINEKVALUE',5,'p_INLINEKVALUE','tomlex.py',750),
  ('INLINEKVALUE -> KVALUE','INLINEKVALUE',1,'p_INLINEKVALUE2','tomlex.py',756),
  ('TABLEARRAY -> ATO KEY ATC','TABLEARRAY',3,'p_TABLEARRAY1','tomlex.py',760),
]
