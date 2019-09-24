from flask import Flask,render_template,request
from pymongo import MongoClient
client = MongoClient()
db = client.CIVIL
collection = db.electives
one=[
{"subject":"English","code":"15HE1101","elective":"0","lab":"0"},
{"subject":"Mathematics-I","code":"15BM1101","elective":"0","lab":"0"},
{"subject":"Principles of Chemical Engineering ","code":"15CH1101","elective":"0","lab":"0"},
{"subject":"Physical Chemistry ","code":" 15BC1105 ","elective":"0","lab":"0"},
{"subject":"Basic Electrical Engineering","code":"15EE1153","elective":"1","lab":"0"},
{"subject":"Elements Of EE & ME","code":" 15EM1101 ","elective":"1","lab":"0"},
{"subject":"Electronics Engineering","code":" 15EC1145","elective":"1","lab":"0"},
{"subject":"Engineering Workshop","code":" 15MT1101 ","elective":"0","lab":"1"},
{"subject":"English Language Lab","code":" 15HE1102 ","elective":"0","lab":"1"},
{"subject":"Physical Chemistry Lab ","code":"15BC1106","elective":"0","lab":"1"},
]
two=[
{"subject":"Mathematics-II","code":" 15BM1102","elective":"0","lab":"0"},
{"subject":"Physics","code":"15BP1101","elective":"0","lab":"0"},
{"subject":"Engineering Mechanics","code":" 15ME1101 ","elective":"0","lab":"0"},
{"subject":"Organic Chemistry","code":"15BC1107","elective":"0","lab":"0"},
{"subject":"Computer programming through-C","code":"15CT1102","elective":"0","lab":"0"},
{"subject":"Engineering Drawing","code":" 15ME1102 ","elective":"0","lab":"1"},
{"subject":"Physics Lab","code":"15BP1102","elective":"0","lab":"1"},
{"subject":"Computer Programming Lab ","code":"15CT1103","elective":"0","lab":"1"},
{"subject":"Organic Chemistry Lab","code":" 15BC1108 ","elective":"0","lab":"1"},
]
three=[
{"subject":"Environmental Chemistry","code":" 15BC1103","elective":"2","lab":"0"},
{"subject":"Probability, Statistics & Numerical Methods ","code":"15BM1103","elective":"2","lab":"0"},
{"subject":"Random Variables & Numerical Methods ","code":"15BM1107","elective":"2","lab":"0"},
{"subject":"Probability and Statistics","code":" 15BM1105  ","elective":"2","lab":"0"},
{"subject":"Chemical Engineering Thermodynamics - I","code":" 15CH1102","elective":"0","lab":"0"},
{"subject":"Momentum Transfer","code":" 15CH1103","elective":"0","lab":"0"},
{"subject":"Chemical Process Calculations","code":" 15CH1104","elective":"0","lab":"0"},
{"subject":"Mechanical  Operations","code":" 15CH1105","elective":"0","lab":"0"},
{"subject":"Environmental Studies ","code":"15BC1104","elective":"0","lab":"0"},
{"subject":"Mechanical Operations Lab ","code":" 15CH1106 ","elective":"0","lab":"1"},
{"subject":"Momentum Transfer Lab","code":" 15CH1107 ","elective":"0","lab":"1"},
]
four=[
{"subject":"Chemical Technology ","code":"15CH1108","elective":"0","lab":"0"},
{"subject":"Process Heat transfer","code":" 15CH1109 ","elective":"0","lab":"0"},
{"subject":"Chemical Engineering Thermodynamics -II","code":"15CH1110","elective":"0","lab":"0"},
{"subject":"Mass Transfer Operation-I","code":"15CH1111","elective":"0","lab":"0"},
{"subject":"Materail Science For Chemical Engineers","code":"15CH1113","elective":"3","lab":"0"},
{"subject":"Nano Technology","code":" Nano Technology","elective":"3","lab":"0"},
{"subject":"Polymer Engineering ","code":" 15CH1115 ","elective":"3","lab":"0"},
{"subject":"Process Instrumentation ","code":"15CH1112 ","elective":"0","lab":"0"},
{"subject":"Process Heat transfer Lab ","code":" 15CH1116 ","elective":"0","lab":"1"},
{"subject":"Basic Computations Lab ","code":"15CH1117","elective":"0","lab":"1"},
]

five=[
{"subject":"Numerical Methods in Chemical Engineering ","code":"15CH1118","elective":"0","lab":"0"},
{"subject":"Chemical Reaction Engineering-I","code":" 15CH1119","elective":"0","lab":"0"},
{"subject":"Mass Transfer Operation-II","code":"15CH1120","elective":"0","lab":"0"},
{"subject":"Industrial Pollution and Control","code":" 15CH1121","elective":"0","lab":"0"},
{"subject":"Process Dynamics and Control","code":" 15CH1122","elective":"0","lab":"0"},
{"subject":"Green Chemical Engineering ","code":"15CH1123","elective":"4","lab":"0"},
{"subject":"Petroleum Refining and Petrochemicals ","code":" 15CH1124 ","elective":"4","lab":"0"},
{"subject":"Instrumentation Methods for  Chemical Analysis","code":" 15CH1125 ","elective":"4","lab":"0"},
{"subject":"Mass Transfer Operations Lab","code":" 15CH1126","elective":"0","lab":"0"},
{"subject":"English ","code":"15HE1101","elective":"5","lab":"0"},
{"subject":"  English Language Lab ","code":" 15HE1103 ","elective":"5","lab":"1"},
{"subject":"  Management Science ","code":" 15HM1102 ","elective":"5","lab":"0"},
{"subject":"  Professional Ethics (16 hrs)","code":" 15HM11PE ","elective":"5","lab":"0"},
]
six=[{"subject":" Management Science ","code":"15HM1102","elective":"0","lab":"0"},
{"subject":" Chemical Reaction Engineering-II","code":"15CH1127","elective":"0","lab":"0"},
{"subject":" Chemical Plant Design and Economics ","code":" 15CH1128 ","elective":"0","lab":"0"},
{"subject":"  Energy Engineering  ","code":"15CH1129","elective":"6","lab":"0"},
{"subject":"  Corrosion Engineering ","code":"15CH1130","elective":"6","lab":"0"},
{"subject":"  Safety & Hazard Analysis ","code":"15CH1131","elective":"6","lab":"0"},
{"subject":" Air pollution ","code":"15CH1132","elective":"7","lab":"0"},
{"subject":" Novel Separation Processes ","code":" 15CH1133 ","elective":"7","lab":"0"},
{"subject":" Environmental Biotechnology ","code":" 15CH1134 ","elective":"7","lab":"0"},
{"subject":" Industry Lectures (16 hrs) ","code":" 15CH11IL ","elective":"0","lab":"0"},
{"subject":" Process Dynamics and Control Lab ","code":"15CH1135","elective":"0","lab":"1"},
{"subject":" Chemical Reaction Engineering Lab ","code":" 15CH1136 ","elective":"0","lab":"1"},
]
seven=[
{"subject":" Chemical  Process  Equipment   Design","code":"15CH1137 ","elective":"0","lab":"0"},
{"subject":" Transport Phenomena","code":"15CH1138","elective":"0","lab":"0"},
{"subject":"  Process Modeling and Simulation ","code":"15CH1139","elective":"8","lab":"0"},
{"subject":"  Chemical Engineering Mathematics ","code":" 15CH1140 ","elective":"8","lab":"0"},
{"subject":"  Waste Water Treatment ","code":"15CH1141","elective":"8","lab":"0"},
{"subject":"  Biochemical Engineering ","code":"15CH1142","elective":"8","lab":"0"},
{"subject":"  Optimization of Chemical Processes ","code":"15CH1143","elective":"9","lab":"0"},
{"subject":"  Solid Waste Management ","code":"15CH1144","elective":"9","lab":"0"},
{"subject":"  Computational Fluid Dynamics ","code":"15CH1145","elective":"9","lab":"0"},
{"subject":"  Downstream processing in Bio processing","code":"15CH1146","elective":"9","lab":"0"},
{"subject":"    COMSOL (24 hrs)","code":" 15CH11S1 ","elective":"10","lab":"0"},
{"subject":"    HEN (24 hrs)","code":"15CH11S4","elective":"10","lab":"0"},
{"subject":" Computer Aided Design of Chemical Equipment Lab","code":" 15CH1147 ","elective":"0","lab":"1"},
{"subject":" Control System Design, Simulation and Optimization lab ","code":" 15CH1148 ","elective":"0","lab":"1"},
{"subject":" Industry Oriented Mini Project ","code":" 15CH11MP ","elective":"0","lab":"0"},
]

electives=[{"elective_no":"1","elective_name":"ENGINEERING SCIENCE ELECTIVE"},
{"elective_no":"2","elective_name":"ENGINEERING SCIENCE ELECTIVE LAB"},
{"elective_no":"3","elective_name":"BASIC SCIENCE ELECTIVE"},
{"elective_no":"4","elective_name":"PROFESSIONAL ELECTIVE-I"},
{"elective_no":"5","elective_name":"PROFESSIONAL ELECTIVE-II"},
{"elective_no":"6","elective_name":"PROFESSIONAL ELECTIVE-III"},
{"elective_no":"7","elective_name":"PROFESSIONAL ELECTIVE-IV"},
{"elective_no":"8","elective_name":"PROFESSIONAL ELECTIVE-V"},
{"elective_no":"9","elective_name":"PROFESSIONAL ELECTIVE-VI"},
{"elective_no":"10","elective_name":"SKILL BASED LAB ELECTIVE-I"},
]

collection.insert_many(electives)
