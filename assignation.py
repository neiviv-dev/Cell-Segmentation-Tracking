from Classes import Cell
import numpy as np

L0=[
Cell(1,57.78827361563518, 39.42410423452769,	1535),
Cell(2,138.75902004454343, 67.55723830734966,	2245),
Cell(3,228.31483496554225, 159.4570184983678,	2757),
Cell(4,17.8107202680067, 158.47403685092127,	1194),
Cell(5,87.54123711340206, 153.24278350515465,	1940),
Cell(6,178.4858223062382, 324.55671077504724,	1058),
Cell(7,227.07535121328226, 362.1392081736909,	783),
Cell(8,131.08048289738431, 401.1579476861167,	994),
Cell(9,712.4738067520373, 412.12747380675205,	1718),
Cell(10,191.55281090289608, 430.3833049403748,	1174),
Cell(11,385.3885542168675, 442.7808734939759,	1328),
Cell(12,464.2167606768735, 451.9959709911362,	1241),
Cell(13,564.7456843403206, 489.38995067817507,	3244),
Cell(14,60.096802074330164, 475.96888504753673,	1157),
Cell(15,445.0593569661995, 512.8549051937346,	1213),
Cell(16,498.1435239206534, 586.5787631271878,	857),
Cell(17,741.5690607734807, 611.3580110497237,	905),
Cell(18,593.0115350488021, 620.3531499556344,	1127),
Cell(19,798.4149443561208, 612.2209856915739,	629),
Cell(20,434.0, 602.0,	25),
Cell(21,474.14065934065934, 622.6307692307693,	910),
Cell(22,73.19730510105872, 642.5274302213667,	1039),
Cell(23,680.9897959183673, 706.2755102040817,	196),
Cell(24,768.0714285714286, 730.8282172373082,	1694),
Cell(25,102.67056323060574, 740.1880977683315,	941),
Cell(26,851.0885264997088, 769.5521258008154,	1717),
Cell(27,194.17492984097288, 778.1403180542563,	1069),
Cell(28,699.4165232358004, 803.8525530694205,	1743),
Cell(29,104.0023282887078, 838.0500582072177,	859),
Cell(30,773.0350492880614, 884.828039430449,	913),
Cell(31,465.0241789967521, 906.854565138939,	2771),
Cell(32,95.18, 893.8688888888889,	900),
Cell(33,844.1568088033013, 913.6726272352132,	727),
Cell(34,645.7266055045872, 932.6733944954128,	1090),
Cell(35,127.0, 934.0555555555555,	162),
Cell(36,725.4254498714653, 973.4807197943445,	778),
Cell(37,19.938091769847052, 980.8237436270939,	1373),
Cell(38,868.6400651465798, 984.4918566775244,	614)
]

L1=[
Cell(1,56.4470509383378, 37.75201072386059,	1492),
Cell(2,138.30181979582778, 66.41455836662229,	2253),
Cell(3,224.42950581395348, 156.39425872093022,	2752),
Cell(4,16.09090909090909, 156.67909090909092,	1100),
Cell(5,87.3403720462544, 150.5761689291101,	1989),
Cell(6,178.1054104477612, 321.64179104477614,	1072),
Cell(7,226.64194373401534, 360.3081841432225,	782),
Cell(8,713.2456140350877, 409.2360446570973,	1881),
Cell(9,129.08639523336643, 401.50347567030786,	1007),
Cell(10,190.675, 430.2133928571429,	1120),
Cell(11,384.0744601638124, 441.8354430379747,	1343),
Cell(12,464.60893854748605, 450.0399042298484,	1253),
Cell(13,565.1670724284845, 486.8761412051126,	3286),
Cell(14,59.09918032786885, 471.4139344262295,	1220),
Cell(15,449.10499139414804, 510.5671256454389,	1162),
Cell(16,498.52797202797206, 584.7902097902098,	858),
Cell(17,740.8076923076923, 609.3031674208145,	884),
Cell(18,793.7107843137255, 605.9362745098039,	612),
Cell(19,592.0296684118674, 619.1221640488657,	1146),
Cell(20,432.1475409836066, 601.0491803278688,	61),
Cell(21,479.9138613861386, 620.3079207920792,	1010),
Cell(22,67.325, 637.323,	1000),
Cell(23,678.7399103139013, 706.0807174887892,	223),
Cell(24,766.8721986674742, 728.7589339794064,	1651),
Cell(25,103.8936170212766, 738.1808510638298,	940),
Cell(26,852.2076344707924, 770.9705031810295,	1729),
Cell(27,192.5468895078923, 775.0779944289693,	1077),
Cell(28,699.8790810157195, 801.0229746070133,	1654),
Cell(29,104.35491329479768, 836.5421965317919,	865),
Cell(30,772.2883977900552, 883.0685082872928,	905),
Cell(31,462.09117221418234, 903.9157018813314,	2764),
Cell(32,95.39400665926748, 890.8712541620422,	901),
Cell(33,843.4886515353805, 911.0894526034713,	749),
Cell(34,644.7747502270663, 930.4050862851952,	1101),
Cell(35,129.1219512195122, 930.1414634146341,	205),
Cell(36,725.457627118644, 973.910411622276,	826),
Cell(37,19.78359908883827, 980.3295368261199,	1317),
Cell(38,867.6938110749186, 983.1026058631921,	614),
Cell(39,742.0, 1022.0,	27)
]
def cost(dist:float,surf:float,ver=0):
    match ver:
        case 0:
            return 1.5/dist+1/surf
        case 1:
            if surf<10:
                return 2/dist
            else:
                return 1/dist
        case _ :
            return 0

def Segment(ListeT0: list[Cell], ListeT1: list[Cell],marginD=float('inf')):
    """
    Renvoie une liste de paire de taille len(ListeT0), 
    celle ci est l'assignation linéaire des point de ListeT0 avec ceux de Liste T1, 
    les couples étant les indices de chaque cellule dans leur liste respective.
    marginD peut être spécifié pour avoir une ROI autour de la cellule étudié, 
    évitant l'évaluation de cellule trop eloignée, elle est par défaut à +inf mais peut être 
    choisi si besoin (préférables)
    """
    out=[]
    for i in range(0,len(ListeT0)):
        ix,iy=ListeT0[i].centroid
        isurf=ListeT0[i].surface
        max=(-1,0)#couple initalisé aux valeurs de base
        for j in range(0,len(ListeT1)):
            jx,jy=ListeT1[j].centroid
            jsurf=ListeT1[j].surface
            #paramêtres de la note
            dist=np.sqrt(pow(ix-jx,2)+pow(iy-jy,2))
            if (dist<marginD):
            #calcul de la note, peut être modulé
                surf=abs(isurf-jsurf)
                if (surf==0):
                    surf=0.000000000000000000000000001
                if (dist==0):
                    dist=0.000000000000000000000000001
                grade =cost(dist,surf)
                #comparaison avec la note la plus haute
                if (max[1]<grade and ListeT1[j].ID!=-1):
                    max=(j,grade)
        if max[1]>0:#cas où la note obtenue a été modifiée
            ListeT1[max[0]].ID=-1 #on retire la cellule des cellules assignables
            #ajoute l'assignation à la liste
            print((i,max[0]))
            out.append((i,max[0]))
    for i in range(0,len(ListeT1)):
        ListeT1[i].ID=0
    for i in out:
        ListeT1[i[1]].ID=ListeT0[i[0]].ID
        ListeT1[i[1]].time=ListeT0[i[0]].time
    return out

def getHighestID(ListeTi:list[Cell]):
    #/!\ Il faut quand même comparer la sortie avec celle du temps précédent 
    out=0
    for i in ListeTi:
        if i.ID>out:
            out=i.ID
    return out

def updateIDs(ListeT1:list[Cell],maxIDs,time):
    it=1
    for i in ListeT1:
        if i.ID==0:
            #on crée un nouveau ID pour les cellules qui n'en ont pas afin de créer un nouveau tracé
            i.ID=maxIDs+it
            it+=1
            i.time=time
        print(i.ID)

def initT0(ListeT0:list[Cell]):
    for i in ListeT0:
        i.time=0


Segment(L0,L1,1)
maxIDs=getHighestID(L0)
updateIDs(L1,maxIDs,1000)
print("Id le plus haut :",getHighestID(L1))
#Segment(L0,L1,100)
#Segment(L0,L1)