import role_counter
global rank_total
global qual_total
global merit_sum


def rank_diag(role_names, credit_emoji):

    global salary1
    salary1 = ""
    global salary2
    salary2 = ""
    global salary3
    salary3 = ""
    global salary4
    salary4 = ""
    global salary5
    salary5 = ""
    global salary6
    salary6 = ""
    global salary7
    salary7 = ""
    global salary8
    salary8 = ""
    global salary9
    salary9 = ""
    global salary10
    salary10 = ""
    global salary11
    salary11 = ""
    global salary12
    salary12 = ""
    global salary13
    salary13 = ""
    global salary14
    salary14 = ""
    global salary15
    salary15 = ""
    global salary16
    salary16 = ""
    global salary17
    salary17 = ""
    global salary18
    salary18 = ""
    global salary19
    salary19 = ""
    global salary20
    salary20 = ""
    global salary21
    salary21 = ""
    global salary22
    salary22 = ""
    global salary23
    salary23 = ""
    global salary24
    salary24 = ""
    global salary25
    salary25 = ""
    global salary26
    salary26 = ""
    global salary27
    salary27 = ""

    rank1 = 'Marshal Commander'
    rank2 = 'Commander'
    rank3 = 'Major'
    rank4 = 'RC Captain'
    rank5 = 'ARC Captain'
    rank6 = 'Commodore'
    rank7 = 'Captain'
    rank8 = 'RC Lieutenant'
    rank9 = 'ARC Lieutenant'
    rank10 = 'Lieutenant'
    rank11 = 'Colonel'
    rank12 = '2nd Lieutenant'
    rank13 = 'RC Sergeant'
    rank14 = 'ARC Sergeant'
    rank15 = 'Sergeant Major'
    rank16 = 'Flight Commander'
    rank17 = 'Republic Commando'
    rank18 = 'ARC Trooper'
    rank19 = 'Flight Captain'
    rank20 = 'Sergeant'
    rank21 = 'Corporal'
    rank22 = 'Flight Lieutenant'
    rank23 = 'Lance Corporal'
    rank24 = 'Flight Officer'
    rank25 = 'Clone Trooper'
    rank26 = 'Clone Pilot'
    rank27 = 'Technical Commander'

    if any(ext == rank1 for ext in role_names):
        salary1 = f"{rank1} - {credit_emoji} `50000`\n"
    if any(ext == rank2 for ext in role_names):
        salary2 = f"{rank2} - {credit_emoji} `30000`\n"
    if any(ext == rank3 for ext in role_names):
        salary3 = f"{rank3} - {credit_emoji} `15000`\n"
    if any(ext == rank4 for ext in role_names):
        salary4 = f"{rank4} - {credit_emoji} `15000`\n"
    if any(ext == rank5 for ext in role_names):
        salary5 = f"{rank5} - {credit_emoji} `15000`\n"
    if any(ext == rank6 for ext in role_names):
        salary6 = f"{rank6} - {credit_emoji} `15000`\n"
    if any(ext == rank7 for ext in role_names):
        salary7 = f"{rank7} - {credit_emoji} `10000`\n"
    if any(ext == rank8 for ext in role_names):
        salary6 = f"{rank8} - {credit_emoji} `10000`\n"
    if any(ext == rank9 for ext in role_names):
        salary9 = f"{rank9} - {credit_emoji} `10000`\n"
    if any(ext == rank10 for ext in role_names):
        salary10 = f"{rank10} - {credit_emoji} `8000`\n"
    if any(ext == rank11 for ext in role_names):
        salary11 = f"{rank11} - {credit_emoji} `10000`\n"
    if any(ext == rank12 for ext in role_names):
        salary12 = f"{rank12} - {credit_emoji} `7000`\n"
    if any(ext == rank13 for ext in role_names):
        salary13 = f"{rank13} - {credit_emoji} `5000`\n"
    if any(ext == rank14 for ext in role_names):
        salary14 = f"{rank14} - {credit_emoji} `5000`\n"
    if any(ext == rank15 for ext in role_names):
        salary15 = f"{rank15} - {credit_emoji} `5000`\n"
    if any(ext == rank16 for ext in role_names):
        salary16 = f"{rank16} - {credit_emoji} `7500`\n"
    if any(ext == rank17 for ext in role_names):
        salary17 = f"{rank17} - {credit_emoji} `23000`\n"
    if any(ext == rank18 for ext in role_names):
        salary18 = f"{rank18} - {credit_emoji} `23000`\n"
    if any(ext == rank19 for ext in role_names):
        salary19 = f"{rank19} - {credit_emoji} `5000`\n"
    if any(ext == rank20 for ext in role_names):
        salary20 = f"{rank20} - {credit_emoji} `2500`\n"
    if any(ext == rank21 for ext in role_names):
        salary21 = f"{rank21} - {credit_emoji} `2000`\n"
    if any(ext == rank22 for ext in role_names):
        salary22 = f"{rank22} - {credit_emoji} `2500`\n"
    if any(ext == rank23 for ext in role_names):
        salary23 = f"{rank23} - {credit_emoji} `1500`\n"
    if any(ext == rank24 for ext in role_names):
        salary24 = f"{rank24} - {credit_emoji} `1500`\n"
    if any(ext == rank25 for ext in role_names):
        salary25 = f"{rank25} - {credit_emoji} `1000`\n"
    if any(ext == rank26 for ext in role_names):
        salary26 = f"{rank26} - {credit_emoji} `1000`\n"
    if any(ext == rank27 for ext in role_names):
        salary27 = f"{rank27} - {credit_emoji} `20000`\n"

    rank_total = (salary1 + salary2 + salary27 + salary3 + salary4 + salary5 + salary6 + salary7 + salary8 +
                  salary9 + salary10 + salary11 + salary12 + salary13 + salary14 + salary15 + salary16 + salary17 +
                  salary18 + salary19 + salary20 + salary21 + salary22 + salary23 + salary24 + salary25 + salary26)

    return rank_total


def medal_diag(role_names, credit_emoji):
    global valor
    valor = ""
    global count1
    count1 = ""
    global count2
    count2 = ""
    global count3
    count3 = ""
    global count4
    count4 = ""
    global count5
    count5 = ""
    global count6
    count6 = ""
    global count7
    count7 = ""
    global count8
    count8 = ""
    global count9
    count9 = ""
    global count10
    count10 = ""
    global count11
    count11 = ""
    global count12
    count12 = ""
    global count13
    count13 = ""
    global count14
    count14 = ""
    global count15
    count15 = ""
    global count16
    count16 = ""
    global count17
    count17 = ""
    global count18
    count18 = ""
    global count19
    count19 = ""
    global count20
    count20 = ""
    global count21
    count21 = ""
    global count22
    count22 = ""
    global count23
    count23 = ""
    global count24
    count24 = ""
    global count25
    count25 = ""
    global count26
    count26 = ""
    global count27
    count27 = ""
    global count28
    count28 = ""
    global count29
    count29 = ""
    global count30
    count30 = ""
    global count31
    count31 = ""
    global count32
    count32 = ""
    global count33
    count33 = ""
    global count34
    count34 = ""
    global count35
    count35 = ""
    global count36
    count36 = ""
    global count37
    count37 = ""
    global count38
    count38 = ""
    global count39
    count39 = ""
    global count40
    count40 = ""
    global count41
    count41 = ""
    global count42
    count42 = ""
    global count43
    count43 = ""
    global count44
    count44 = ""
    global count45
    count45 = ""
    global count46
    count46 = ""
    global count47
    count47 = ""
    global count48
    count48 = ""
    global count49
    count49 = ""
    global count50
    count50 = ""
    global count51
    count51 = ""
    global count52
    count52 = ""
    global count53
    count53 = ""
    global count54
    count54 = ""
    global count55
    count55 = ""
    global count56
    count56 = ""
    global count57
    count57 = ""
    global count58
    count58 = ""
    global count59
    count59 = ""
    global count60
    count60 = ""
    global count61
    count61 = ""
    global count62
    count62 = ""
    global count63
    count63 = ""
    global count64
    count64 = ""
    global count65
    count65 = ""
    global count66
    count66 = ""
    global count67
    count67 = ""
    global count68
    count68 = ""
    global count69
    count69 = ""
    global count70
    count70 = ""

    medal_of_valor = 'Medal of Valor'
    medal1 = '41st Service Medal'
    medal2 = 'Cadet Master'
    medal3 = 'Mythical Instructor'
    medal4 = 'Legendary Instructor'
    medal5 = 'Hero of The 41st'
    medal6 = 'Absolutely Demolished'
    medal7 = 'Legendary Ranger'
    medal8 = 'Battle Hardened'
    medal9 = 'Bane of Clankers'
    medal10 = 'Order of Dedication'
    medal11 = 'Vaunted Veteran Medal'
    medal12 = 'Seppie Scourge'
    medal13 = 'Plot Armor'
    medal14 = 'Superior Genetics'
    medal15 = 'Flawless Leadership'
    medal16 = 'Supporting Act'
    medal17 = 'May the Score be with you'
    medal18 = 'Deadly and Discrete'
    medal19 = 'The Best of the Best'
    medal20 = 'Clanker Crusher'
    medal21 = 'Terror in the Sky'
    medal22 = 'True Trooper'
    medal23 = 'Siegebreaker'
    medal24 = 'Top Gun'
    medal25 = '41st Representation Medal'
    medal26 = 'Mythical ARF Medal'
    medal27 = 'Legendary ARF Medal'
    medal28 = 'Mythical Engineer Medal'
    medal29 = 'Elite ARF Medal'
    medal30 = 'Legendary Engineer Medal'
    medal31 = 'Veteran ARF Medal'
    medal32 = 'Elite Engineer Medal'
    medal33 = 'Mythical Commando Medal'
    medal34 = 'Mythical ARC Medal'
    medal35 = 'Mythical Aerial Medal'
    medal36 = 'Mythical Officer Medal'
    medal37 = 'Mythical Specialist Medal'
    medal38 = 'Mythical Heavy Medal'
    medal39 = 'Mythical Assault Medal'
    medal40 = 'Veteran Engineer Medal'
    medal41 = 'Legendary Commando Medal'
    medal42 = 'Legendary ARC Medal'
    medal43 = 'Legendary Aerial Medal'
    medal44 = 'Legendary Officer Medal'
    medal45 = 'Legendary Specialist Medal'
    medal46 = 'Legendary Heavy Medal'
    medal47 = 'Legendary Assault Medal'
    medal48 = 'Elite Commando Medal'
    medal49 = 'Elite ARC Medal'
    medal50 = 'Elite Aerial Medal'
    medal51 = 'Elite Officer Medal'
    medal52 = 'Elite Specialist Medal'
    medal53 = 'Elite Heavy Medal'
    medal54 = 'Elite Assault Medal'
    medal55 = 'Veteran Commando Medal'
    medal56 = 'Veteran ARC Medal'
    medal57 = 'Veteran Aerial Medal'
    medal58 = 'Veteran Officer Medal'
    medal59 = 'Veteran Specialist Medal'
    medal60 = 'Veteran Heavy Medal'
    medal61 = 'Veteran Assault Medal'
    medal62 = 'Lone Survivor'
    medal63 = 'Exemplar'
    medal64 = 'Professional Soldier'
    medal65 = 'One Man Army'
    medal66 = 'The Good Batch'
    medal67 = 'Bred for War'
    medal68 = 'Outstanding Dedication'
    medal69 = 'Fireteam on Fire'
    medal70 = 'First Try'

    if any(ext == medal_of_valor for ext in role_names):
        valor = f"{medal_of_valor} - {credit_emoji} `20000`"
    if any(ext == medal1 for ext in role_names):
        count1 = f"{medal1} - {credit_emoji} `3000`"
    if any(ext == medal2 for ext in role_names):
        count2 = f"{medal2} - {credit_emoji} `3000`"
    if any(ext == medal3 for ext in role_names):
        count3 = f"{medal3} - {credit_emoji} `3000`"
    if any(ext == medal4 for ext in role_names):
        count4 = f"{medal4} - {credit_emoji} `3000`"
    if any(ext == medal5 for ext in role_names):
        count5 = f"{medal5} - {credit_emoji} `2500`"
    if any(ext == medal6 for ext in role_names):
        count6 = f"{medal6} - {credit_emoji} `2000`"
    if any(ext == medal7 for ext in role_names):
        count7 = f"{medal7} - {credit_emoji} `2000`"
    if any(ext == medal8 for ext in role_names):
        count8 = f"{medal8} - {credit_emoji} `2000`"
    if any(ext == medal9 for ext in role_names):
        count9 = f"{medal9} - {credit_emoji} `2000`"
    if any(ext == medal10 for ext in role_names):
        count10 = f"{medal10} - {credit_emoji} `2000`"
    if any(ext == medal11 for ext in role_names):
        count11 = f"{medal11} - {credit_emoji} `2000`"
    if any(ext == medal12 for ext in role_names):
        count12 = f"{medal12} - {credit_emoji} `1500`"
    if any(ext == medal13 for ext in role_names):
        count13 = f"{medal13} - {credit_emoji} `1500`"
    if any(ext == medal14 for ext in role_names):
        count14 = f"{medal14} - {credit_emoji} `1500`"
    if any(ext == medal15 for ext in role_names):
        count15 = f"{medal15} - {credit_emoji} `1500`"
    if any(ext == medal16 for ext in role_names):
        count16 = f"{medal16} - {credit_emoji} `1000`"
    if any(ext == medal17 for ext in role_names):
        count17 = f"{medal17} - {credit_emoji} `1000`"
    if any(ext == medal18 for ext in role_names):
        count18 = f"{medal18} - {credit_emoji} `1000`"
    if any(ext == medal19 for ext in role_names):
        count19 = f"{medal19} - {credit_emoji} `1000`"
    if any(ext == medal20 for ext in role_names):
        count20 = f"{medal20} - {credit_emoji} `1000`"
    if any(ext == medal21 for ext in role_names):
        count21 = f"{medal21} - {credit_emoji} `1000`"
    if any(ext == medal22 for ext in role_names):
        count22 = f"{medal22} - {credit_emoji} `1000`"
    if any(ext == medal23 for ext in role_names):
        count23 = f"{medal23} - {credit_emoji} `1000`"
    if any(ext == medal24 for ext in role_names):
        count24 = f"{medal24} - {credit_emoji} `1000`"
    if any(ext == medal25 for ext in role_names):
        count25 = f"{medal25} - {credit_emoji} `1000`"
    if any(ext == medal26 for ext in role_names):
        count26 = f"{medal26} - {credit_emoji} `7500`"
    if any(ext == medal27 for ext in role_names):
        count27 = f"{medal27} - {credit_emoji} `6000`"
    if any(ext == medal28 for ext in role_names):
        count28 = f"{medal28} - {credit_emoji} `5000`"
    if any(ext == medal29 for ext in role_names):
        count29 = f"{medal29} - {credit_emoji} `4500`"
    if any(ext == medal30 for ext in role_names):
        count30 = f"{medal30} - {credit_emoji} `4000`"
    if any(ext == medal31 for ext in role_names):
        count31 = f"{medal31} - {credit_emoji} `3000`"
    if any(ext == medal32 for ext in role_names):
        count32 = f"{medal32} - {credit_emoji} `3000`"
    if any(ext == medal33 for ext in role_names):
        count33 = f"{medal33} - {credit_emoji} `2500`"
    if any(ext == medal34 for ext in role_names):
        count34 = f"{medal34} - {credit_emoji} `2500`"
    if any(ext == medal35 for ext in role_names):
        count35 = f"{medal35} - {credit_emoji} `2500`"
    if any(ext == medal36 for ext in role_names):
        count36 = f"{medal36} - {credit_emoji} `2500`"
    if any(ext == medal37 for ext in role_names):
        count37 = f"{medal37} - {credit_emoji} `2500`"
    if any(ext == medal38 for ext in role_names):
        count38 = f"{medal38} - {credit_emoji} `2500`"
    if any(ext == medal39 for ext in role_names):
        count39 = f"{medal39} - {credit_emoji} `2500`"
    if any(ext == medal40 for ext in role_names):
        count40 = f"{medal40} - {credit_emoji} `2000`"
    if any(ext == medal41 for ext in role_names):
        count41 = f"{medal41} - {credit_emoji} `2000`"
    if any(ext == medal42 for ext in role_names):
        count42 = f"{medal42} - {credit_emoji} `2000`"
    if any(ext == medal43 for ext in role_names):
        count43 = f"{medal43} - {credit_emoji} `2000`"
    if any(ext == medal44 for ext in role_names):
        count44 = f"{medal44} - {credit_emoji} `2000`"
    if any(ext == medal45 for ext in role_names):
        count45 = f"{medal45} - {credit_emoji} `2000`"
    if any(ext == medal46 for ext in role_names):
        count46 = f"{medal46} - {credit_emoji} `2000`"
    if any(ext == medal47 for ext in role_names):
        count47 = f"{medal47} - {credit_emoji} `2000`"
    if any(ext == medal48 for ext in role_names):
        count48 = f"{medal48} - {credit_emoji} `1500`"
    if any(ext == medal49 for ext in role_names):
        count49 = f"{medal49} - {credit_emoji} `1500`"
    if any(ext == medal50 for ext in role_names):
        count50 = f"{medal50} - {credit_emoji} `1500`"
    if any(ext == medal51 for ext in role_names):
        count51 = f"{medal51} - {credit_emoji} `1500`"
    if any(ext == medal52 for ext in role_names):
        count52 = f"{medal52} - {credit_emoji} `1500`"
    if any(ext == medal53 for ext in role_names):
        count53 = f"{medal53} - {credit_emoji} `1500`"
    if any(ext == medal54 for ext in role_names):
        count54 = f"{medal54} - {credit_emoji} `1500`"
    if any(ext == medal55 for ext in role_names):
        count55 = f"{medal55} - {credit_emoji} `1000`"
    if any(ext == medal56 for ext in role_names):
        count56 = f"{medal56} - {credit_emoji} `1000`"
    if any(ext == medal57 for ext in role_names):
        count57 = f"{medal57} - {credit_emoji} `1000`"
    if any(ext == medal58 for ext in role_names):
        count58 = f"{medal58} - {credit_emoji} `1000`"
    if any(ext == medal59 for ext in role_names):
        count59 = f"{medal59} - {credit_emoji} `1000`"
    if any(ext == medal60 for ext in role_names):
        count60 = f"{medal60} - {credit_emoji} `1000`"
    if any(ext == medal61 for ext in role_names):
        count61 = f"{medal61} - {credit_emoji} `1000`"
    if any(ext == medal62 for ext in role_names):
        count62 = f"{medal62} - {credit_emoji} `2000`"
    if any(ext == medal63 for ext in role_names):
        count63 = f"{medal63} - {credit_emoji} `1000`"
    if any(ext == medal64 for ext in role_names):
        count64 = f"{medal64} - {credit_emoji} `5000`"
    if any(ext == medal65 for ext in role_names):
        count65 = f"{medal65} - {credit_emoji} `1500`"
    if any(ext == medal66 for ext in role_names):
        count66 = f"{medal66} - {credit_emoji} `4000`"
    if any(ext == medal67 for ext in role_names):
        count67 = f"{medal67} - {credit_emoji} `1500`"
    if any(ext == medal68 for ext in role_names):
        count68 = f"{medal68} - {credit_emoji} `4000`"
    if any(ext == medal69 for ext in role_names):
        count69 = f"{medal69} - {credit_emoji} `3000`"
    if any(ext == medal70 for ext in role_names):
        count70 = f"{medal70} - {credit_emoji} `3000`"

    medal_total = (valor + count1 + count2 + count3 + count4 + count5 + count6 + count7 + count8 + count9 +
                   count10 + count11 + count12 + count13 + count14 + count15 + count16 + count17 + count18 +
                   count19 + count20 + count21 + count22 + count23 + count24 + count25 + count26 + count27 +
                   count28 + count29 + count30 + count31 + count32 + count33 + count34 + count35 + count36 +
                   count37 + count38 + count39 + count40 + count41 + count42 + count43 + count44 + count45 +
                   count46 + count47 + count48 + count49 + count50 + count51 + count52 + count53 + count54 +
                   count55 + count56 + count57 + count58 + count59 + count60 + count61 + count62 + count63 +
                   count64 + count65 + count66 + count67 + count68 + count69 + count70)

    return medal_total

def qual_diag(role_names, credit_emoji):

    global reward1
    reward1 = ""
    global reward2
    reward2 = ""
    global reward3
    reward3 = ""
    global reward4
    reward4 = ""
    global reward5
    reward5 = ""
    global reward6
    reward6 = ""
    global reward7
    reward7 = ""
    global reward8
    reward8 = ""
    global reward9
    reward9 = ""
    global reward10
    reward10 = ""
    global reward11
    reward11 = ""
    global reward12
    reward12 = ""
    global reward13
    reward13 = ""
    global reward14
    reward14 = ""
    global reward15
    reward15 = ""
    global reward16
    reward16 = ""
    global reward17
    reward17 = ""
    global reward18
    reward18 = ""
    global reward19
    reward19 = ""
    global reward20
    reward20 = ""
    global reward21
    reward21 = ""
    global reward22
    reward22 = ""
    global reward23
    reward23 = ""
    global reward24
    reward24 = ""
    global reward25
    reward25 = ""
    global reward26
    reward26 = ""
    global reward27
    reward27 = ""
    global reward28
    reward28 = ""
    global reward29
    reward29 = ""
    global reward30
    reward30 = ""

    qual1 = 'Scout Trooper'
    qual2 = 'Aerial Trooper'
    qual3 = 'Engineer'
    qual4 = 'Ace Pilot'
    qual5 = 'ARF Trooper'
    qual6 = 'Interceptor Pilot'
    qual7 = 'Bomber Pilot'
    qual8 = 'Veteran Trooper'
    qual9 = 'Strike Cadre'
    qual10 = 'Juggernaut Cadre'
    qual11 = 'Shadow Cadre'
    qual12 = 'ARC Qualification'
    qual13 = 'Frontliner'
    qual14 = 'Submachine Gunner'
    qual15 = 'Rifleman'
    qual16 = 'CQC Trooper'
    qual17 = 'Suppessor'
    qual18 = 'Grenadier'
    qual19 = 'Heavy Rifleman'
    qual20 = 'Hunter'
    qual21 = 'Aggressor'
    qual22 = 'Sniper'
    qual23 = 'Slug Shooter'
    qual24 = 'Sharpshooter'
    qual25 = 'Operative'
    qual26 = 'Urban Warrior'
    qual27 = 'Gunslinger'
    qual28 = 'HERO Pilot - First Class'
    qual29 = 'HERO Pilot - Second Class'
    qual30 = 'Galactic Marine'

    if any(ext == qual1 for ext in role_names):
        reward1 = f"{qual1} - {credit_emoji} `3000`"
    if any(ext == qual2 for ext in role_names):
        reward2 = f"{qual2} - {credit_emoji} `2500`"
    if any(ext == qual3 for ext in role_names):
        reward3 = f"{qual3} - {credit_emoji} `2500`"
    if any(ext == qual4 for ext in role_names):
        reward4 = f"{qual4} - {credit_emoji} `3000`"
    if any(ext == qual5 for ext in role_names):
        reward5 = f"{qual5} - {credit_emoji} `2000`"
    if any(ext == qual6 for ext in role_names):
        reward6 = f"{qual6} - {credit_emoji} `2000`"
    if any(ext == qual7 for ext in role_names):
        reward7 = f"{qual7} - {credit_emoji} `2000`"
    if any(ext == qual8 for ext in role_names):
        reward8 = f"{qual8} - {credit_emoji} `2000`"
    if any(ext == qual9 for ext in role_names):
        reward9 = f"{qual9} - {credit_emoji} `3000`"
    if any(ext == qual10 for ext in role_names):
        reward10 = f"{qual10} - {credit_emoji} `3000`"
    if any(ext == qual11 for ext in role_names):
        reward11 = f"{qual11} - {credit_emoji} `3000`"
    if any(ext == qual12 for ext in role_names):
        reward12 = f"{qual12} - {credit_emoji} `7500`"
    if any(ext == qual13 for ext in role_names):
        reward13 = f"{qual13} - {credit_emoji} `2000`"
    if any(ext == qual14 for ext in role_names):
        reward14 = f"{qual14} - {credit_emoji} `1500`"
    if any(ext == qual15 for ext in role_names):
        reward15 = f"{qual15} - {credit_emoji} `1500`"
    if any(ext == qual16 for ext in role_names):
        reward16 = f"{qual16} - {credit_emoji} `1500`"
    if any(ext == qual17 for ext in role_names):
        reward17 = f"{qual17} - {credit_emoji} `1000`"
    if any(ext == qual18 for ext in role_names):
        reward18 = f"{qual18} - {credit_emoji} `1500`"
    if any(ext == qual19 for ext in role_names):
        reward19 = f"{qual19} - {credit_emoji} `2000`"
    if any(ext == qual20 for ext in role_names):
        reward20 = f"{qual20} - {credit_emoji} `1000`"
    if any(ext == qual21 for ext in role_names):
        reward21 = f"{qual21} - {credit_emoji} `1500`"
    if any(ext == qual22 for ext in role_names):
        reward22 = f"{qual22} - {credit_emoji} `2000`"
    if any(ext == qual23 for ext in role_names):
        reward23 = f"{qual23} - {credit_emoji} `1000`"
    if any(ext == qual24 for ext in role_names):
        reward24 = f"{qual24} - {credit_emoji} `1500`"
    if any(ext == qual25 for ext in role_names):
        reward25 = f"{qual25} - {credit_emoji} `1000`"
    if any(ext == qual26 for ext in role_names):
        reward26 = f"{qual26} - {credit_emoji} `1500`"
    if any(ext == qual27 for ext in role_names):
        reward27 = f"{qual27} - {credit_emoji} `1000`"
    if any(ext == qual28 for ext in role_names):
        reward28 = f"{qual28} - {credit_emoji} `8000`"
    if any(ext == qual29 for ext in role_names):
        reward29 = f"{qual29} - {credit_emoji} `4000`"
    if any(ext == qual30 for ext in role_names):
        reward30 = f"{qual30} - {credit_emoji} `3000`"

    qual_total = (reward1 + reward2 + reward3 + reward4 + reward5 + reward6 + reward7 + reward8 + reward9 +
                  reward10 + reward11 + reward12 + reward13 + reward14 + reward15 + reward16 + reward17 +
                  reward18 + reward19 + reward20 + reward21 + reward22 + reward23 + reward24 + reward25 +
                  reward26 + reward27 + reward28 + reward29 + reward30)

    return qual_total

