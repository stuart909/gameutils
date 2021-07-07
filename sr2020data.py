#Written by Stuart Anderson
#GNU 3.0 License
#SR2020 game file editor utility for usage in Python IDLE

import re, sqlite3

class Data_Tools:
    def search(self, val, skey, gkey):
        return [i[gkey] for i in self.data if val in i[skey]]

    def get(self, val, key):
        return [i for i in self.data if val == i[key]]

    def pull(self, vals, key):
        return [i for i in self.data if i[key] in vals]

    def save(self):
        with open(self.path, 'w', encoding='latin-1') as file:
            out = []
            for i in self.junk[:4]:
                out.append(i)
            for i in self.data:
                s=""
                d = [j for j in i.values()]
                for j in d:
                    s=s+j+', '
                out.append(s)
            for i in self.junk[4:]:
                out.append(i)
            for i in out:
                file.write("%s\n" % i)

            file.close()
    def set_max_id(self, ID):
        self.max_id = max([int(i[ID]) for i in self.data])

class Units(Data_Tools):
    def __init__(self):
        self.path = 'G:\Program Files (x86)\Steam\steamapps\common\Supreme Ruler Ultimate\Maps\DATA\DEFAULT.UNIT'
        self.keys = ['SR5ID', 'ModelCode+EquipName', 'ClassNum', 'PicNum', '(YearAvail - 1900)', '(OutOfProd - 1900)', '`market availability`', 'TargetType', 'MoveType', 'Initiative', 'StealthStr', 'CarrierCapacity', 'Regions', 'NumSquadInBatt', 'Crew', 'UGTo', 'ReplaceBy', 'RefitTo', 'AbandonTo', 'Speed', 'MisislePtsCapacity', 'SpotType1', 'SpotType2', 'TechReq1', 'TechReq2', 'DaysToBuild', 'Cost', 'IGCost', 'URCost', 'Weight', 'SupplyLevel', 'TransportCap', 'MoveRange', 'TurretArc', 'FuelCap', 'CombatTime', 'SupplyCap', 'SoftAttack', 'HardAttack', 'FortAttack', 'LowAirAttack', 'MidAirAttack', 'HighAirAttack', 'NavalSurfaceAttack', 'NavalSubAttack', 'CloseCombatAttack', 'GroundDefense', 'TacAirDefense', 'IndirectDefense', 'CloseDefense', 'GroundAttRange', 'AirAttRange', 'SurfaceAttRange', 'SubAttRange', 'UPGRADEUnit', 'MISSILEUnit', 'IndirectFlag', 'BalisticArt', 'NBCProt', 'TurretRot', 'LimitedFiringArc', 'TurretImmed', 'LongDeckCarrier', 'DirectDef', 'ECMEquipped', 'NoEffLossMove', 'RiverXing', 'Airdrop', 'AirTanker', 'AirRefuel', 'ShortDeckTakeOff', 'LongDeckTakeOff', 'Amphibious', '0-1', '0-2', 'BridgeBuild', 'UGDemol', 'EngineeringUnit', 'DockToUnload', 'StandOffUnit', 'MoveFirePenalty', 'NoLandCap', 'HasProduction', 'SupplyMoveOnly', 'LowVisibility', 'NavalPort', 'uBase', 'uIndustry', 'uUrban', 'uTransport', 'uBridging', 'uRubble', 'uSynth', '0-3', 'uContainer', 'OnePerHex', 'Chem', 'StratNuke', 'TacNuke', 'MisLaunchAuth', 'GuidedMis', 'NoBuild', 'DefRes', 'NoResearch', 'UsesLargerPicSize', 'HasShadow', 'LaunchType', 'MisislePtsValue', 'NuclearYield', 'uContainX', 'uSpecialty', 'uEntrench', 'Pollution', 'uProdTech', 'uBuildCap', 'uStoreType', 'uStoreCap', 'GndMoveCost', 'NavalMoveCost', 'uRawSourceX', 'HexReq1', 'HexReq2', 'uBuildClassMask', 'FireSNDA', 'FireSNDB', 'FireSNDC', '`Death sound`', '`Move sound`', '0-4', '`pic 1`', '`pic 2`', '`pic 3`', '`pic 4`', 'uSpecialType']
        self.id = 'SR5ID'
        self.name = 'ModelCode+EquipName'
        self.cat = 'ClassNum'
        self.junk = []
        self.data = self.load()
        self.set_max_id('SR5ID')

    def load(self):
        result = []
        with open(self.path, encoding='latin-1') as units:
            def fix(x):
                [i.replace(',','') for i in re.findall(r'".*,.*"',x)]
                
            u = units.read().splitlines()
            [fix(i) for i in u]
            for i in u[:4]:
                self.junk.append(i)
            for i in u[4:]:
                tmp = i.split(', ')
                d = {}
                if len(tmp)-1 == len(self.keys):
                    for j in range(len(self.keys)):
                        d.update({self.keys[j]:tmp[j]})
                    result.append(d)
                else:
                    self.junk.append(i)
            units.close()
        return result
        

class Research(Data_Tools):
    def __init__(self):
        self.path = 'G:\Program Files (x86)\Steam\steamapps\common\Supreme Ruler Ultimate\Maps\DATA\DEFAULT.TTRX'
        self.keys = ['ID', 'Category', 'SR6 Tech Level', 'Pic', 'Prereq 1', 'Prereq 2', 'Effect 1', 'Effect 2', 'Effect Value 1', 'Effect Value 2', 'Time to Res', 'Cost', 'Pop Support', 'World Support', 'AI Interest', 'Tradeable?', 'Set by Default', 'Unit Requirement', 'Tech Requirement', 'Facility Requirement', 'EraTech', 'Cabinet AI Interest', 'WM Offer Interest', 'Short Title']
        self.junk = []
        self.id = 'ID'
        self.cat = 'Category'
        self.name = 'Short Title'
        self.data = self.load()
        self.set_max_id('ID')
        
    def load(self):
        result = []
        with open(self.path, encoding='latin-1', errors='backslashreplace') as research:
            def fix(x):
                [i.replace(',','') for i in re.findall(r'".*,.*"',x)]
                
            u = research.read().splitlines()
            [fix(i) for i in u]
            for i in u[:4]:
                self.junk.append(i)
            for i in u[4:]:
                tmp = i.split(', ')
                d = {}
                if len(tmp)-1 == len(self.keys):
                    for j in range(len(self.keys)):
                        d.update({self.keys[j]:tmp[j]})
                    result.append(d)
                else:
                    self.junk.append(i)
            research.close()
        return result

class Database:
    def __init__(self):
        self.u = Units()
        self.r = Research()
        self.conn = sqlite3.connect(':memory:')
        self.c = self.conn.cursor()
        self.loaded = False
        self.name = "None"
    
    def start(self):
        self.loaded = True
        self.name = "Memory Default"
        self.c.execute('''CREATE TABLE units ('SR5ID', 'ModelCode+EquipName', 'ClassNum', 'PicNum', '(YearAvail - 1900)', '(OutOfProd - 1900)', '`market availability`', 'TargetType', 'MoveType', 'Initiative', 'StealthStr', 'CarrierCapacity', 'Regions', 'NumSquadInBatt', 'Crew', 'UGTo', 'ReplaceBy', 'RefitTo', 'AbandonTo', 'Speed', 'MisislePtsCapacity', 'SpotType1', 'SpotType2', 'TechReq1', 'TechReq2', 'DaysToBuild', 'Cost', 'IGCost', 'URCost', 'Weight', 'SupplyLevel', 'TransportCap', 'MoveRange', 'TurretArc', 'FuelCap', 'CombatTime', 'SupplyCap', 'SoftAttack', 'HardAttack', 'FortAttack', 'LowAirAttack', 'MidAirAttack', 'HighAirAttack', 'NavalSurfaceAttack', 'NavalSubAttack', 'CloseCombatAttack', 'GroundDefense', 'TacAirDefense', 'IndirectDefense', 'CloseDefense', 'GroundAttRange', 'AirAttRange', 'SurfaceAttRange', 'SubAttRange', 'UPGRADEUnit', 'MISSILEUnit', 'IndirectFlag', 'BalisticArt', 'NBCProt', 'TurretRot', 'LimitedFiringArc', 'TurretImmed', 'LongDeckCarrier', 'DirectDef', 'ECMEquipped', 'NoEffLossMove', 'RiverXing', 'Airdrop', 'AirTanker', 'AirRefuel', 'ShortDeckTakeOff', 'LongDeckTakeOff', 'Amphibious', '0-1', '0-2', 'BridgeBuild', 'UGDemol', 'EngineeringUnit', 'DockToUnload', 'StandOffUnit', 'MoveFirePenalty', 'NoLandCap', 'HasProduction', 'SupplyMoveOnly', 'LowVisibility', 'NavalPort', 'uBase', 'uIndustry', 'uUrban', 'uTransport', 'uBridging', 'uRubble', 'uSynth', '0-3', 'uContainer', 'OnePerHex', 'Chem', 'StratNuke', 'TacNuke', 'MisLaunchAuth', 'GuidedMis', 'NoBuild', 'DefRes', 'NoResearch', 'UsesLargerPicSize', 'HasShadow', 'LaunchType', 'MisislePtsValue', 'NuclearYield', 'uContainX', 'uSpecialty', 'uEntrench', 'Pollution', 'uProdTech', 'uBuildCap', 'uStoreType', 'uStoreCap', 'GndMoveCost', 'NavalMoveCost', 'uRawSourceX', 'HexReq1', 'HexReq2', 'uBuildClassMask', 'FireSNDA', 'FireSNDB', 'FireSNDC', '`Death sound`', '`Move sound`', '0-4', '`pic 1`', '`pic 2`', '`pic 3`', '`pic 4`', 'uSpecialType')''')
        self.c.execute('''CREATE TABLE research ('ID', 'Category', 'SR6 Tech Level', 'Pic', 'Prereq 1', 'Prereq 2', 'Effect 1', 'Effect 2', 'Effect Value 1', 'Effect Value 2', 'Time to Res', 'Cost', 'Pop Support', 'World Support', 'AI Interest', 'Tradeable?', 'Set by Default', 'Unit Requirement', 'Tech Requirement', 'Facility Requirement', 'EraTech', 'Cabinet AI Interest', 'WM Offer Interest', 'Short Title')''')
        self.commit()
        [self.c.execute("INSERT INTO units VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", [i['SR5ID'],i['ModelCode+EquipName'],i['ClassNum'],i['PicNum'],i['(YearAvail - 1900)'],i['(OutOfProd - 1900)'],i['`market availability`'],i['TargetType'],i['MoveType'],i['Initiative'],i['StealthStr'],i['CarrierCapacity'],i['Regions'],i['NumSquadInBatt'],i['Crew'],i['UGTo'],i['ReplaceBy'],i['RefitTo'],i['AbandonTo'],i['Speed'],i['MisislePtsCapacity'],i['SpotType1'],i['SpotType2'],i['TechReq1'],i['TechReq2'],i['DaysToBuild'],i['Cost'],i['IGCost'],i['URCost'],i['Weight'],i['SupplyLevel'],i['TransportCap'],i['MoveRange'],i['TurretArc'],i['FuelCap'],i['CombatTime'],i['SupplyCap'],i['SoftAttack'],i['HardAttack'],i['FortAttack'],i['LowAirAttack'],i['MidAirAttack'],i['HighAirAttack'],i['NavalSurfaceAttack'],i['NavalSubAttack'],i['CloseCombatAttack'],i['GroundDefense'],i['TacAirDefense'],i['IndirectDefense'],i['CloseDefense'],i['GroundAttRange'],i['AirAttRange'],i['SurfaceAttRange'],i['SubAttRange'],i['UPGRADEUnit'],i['MISSILEUnit'],i['IndirectFlag'],i['BalisticArt'],i['NBCProt'],i['TurretRot'],i['LimitedFiringArc'],i['TurretImmed'],i['LongDeckCarrier'],i['DirectDef'],i['ECMEquipped'],i['NoEffLossMove'],i['RiverXing'],i['Airdrop'],i['AirTanker'],i['AirRefuel'],i['ShortDeckTakeOff'],i['LongDeckTakeOff'],i['Amphibious'],i['0-1'],i['0-2'],i['BridgeBuild'],i['UGDemol'],i['EngineeringUnit'],i['DockToUnload'],i['StandOffUnit'],i['MoveFirePenalty'],i['NoLandCap'],i['HasProduction'],i['SupplyMoveOnly'],i['LowVisibility'],i['NavalPort'],i['uBase'],i['uIndustry'],i['uUrban'],i['uTransport'],i['uBridging'],i['uRubble'],i['uSynth'],i['0-3'],i['uContainer'],i['OnePerHex'],i['Chem'],i['StratNuke'],i['TacNuke'],i['MisLaunchAuth'],i['GuidedMis'],i['NoBuild'],i['DefRes'],i['NoResearch'],i['UsesLargerPicSize'],i['HasShadow'],i['LaunchType'],i['MisislePtsValue'],i['NuclearYield'],i['uContainX'],i['uSpecialty'],i['uEntrench'],i['Pollution'],i['uProdTech'],i['uBuildCap'],i['uStoreType'],i['uStoreCap'],i['GndMoveCost'],i['NavalMoveCost'],i['uRawSourceX'],i['HexReq1'],i['HexReq2'],i['uBuildClassMask'],i['FireSNDA'],i['FireSNDB'],i['FireSNDC'],i['`Death sound`'],i['`Move sound`'],i['0-4'],i['`pic 1`'],i['`pic 2`'],i['`pic 3`'],i['`pic 4`'],i['uSpecialType']]) for i in self.u.data]
        [self.c.execute("INSERT INTO research VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", [i['ID'], i['Category'], i['SR6 Tech Level'], i['Pic'], i['Prereq 1'], i['Prereq 2'], i['Effect 1'], i['Effect 2'], i['Effect Value 1'], i['Effect Value 2'], i['Time to Res'], i['Cost'], i['Pop Support'], i['World Support'], i['AI Interest'], i['Tradeable?'], i['Set by Default'], i['Unit Requirement'], i['Tech Requirement'], i['Facility Requirement'], i['EraTech'], i['Cabinet AI Interest'], i['WM Offer Interest'], i['Short Title']]) for i in self.r.data]
        self.commit()

    def commit(self):
        self.conn.commit()

    def load(self, path):
        self.loaded = True
        self.name = path
        self.conn = sqlite3.connect(path)
        self.c = self.conn.cursor()

    def dump_units(self):
        if self.loaded:
            data = self.c.execute("select * from units")
            result = []
            for i in data:
                d = {}
                for j, k in enumerate(self.u.keys):
                    d.update({k:i[j]})
                result.append(d)
            self.u.data = result
        else:
            print("No DB loaded")

    def dump_research(self):
        if self.loaded:
            data = self.c.execute("select * from research")
            result = []
            for i in data:
                d = {}
                for j, k in enumerate(self.r.keys):
                    d.update({k:i[j]})
                result.append(d)
            self.r.data = result
        else:
            print("No DB loaded")


db = Database()
db.load("C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python38-32\\tmp.db")
#u = Units()
#r = Research()
