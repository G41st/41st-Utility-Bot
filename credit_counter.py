global merit_total
global demerit_total
global rank_total
global qual_total
global merit_sum


def credit_counter(role_names, discord_id):
    d_id = str(discord_id)

    global salary1
    salary1 = 0
    global salary2
    salary2 = 0
    global salary3
    salary3 = 0
    global salary4
    salary4 = 0
    global salary5
    salary5 = 0
    global salary6
    salary6 = 0
    global salary7
    salary7 = 0
    global salary8
    salary8 = 0
    global salary9
    salary9 = 0
    global salary10
    salary10 = 0
    global salary11
    salary11 = 0
    global salary12
    salary12 = 0
    global salary13
    salary13 = 0
    global salary14
    salary14 = 0
    global salary15
    salary15 = 0
    global salary16
    salary16 = 0
    global salary17
    salary17 = 0
    global salary18
    salary18 = 0
    global salary19
    salary19= 0
    global salary20
    salary20 = 0
    global salary21
    salary21 = 0
    global salary22
    salary22 = 0
    global salary23
    salary23 = 0
    global salary24
    salary24 = 0
    global salary25
    salary25 = 0
    global salary26
    salary26 = 0

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

    global valor
    valor = 0
    global count1
    count1 = 0
    global count2
    count2 = 0
    global count3
    count3 = 0
    global count4
    count4 = 0
    global count5
    count5 = 0
    global count6
    count6 = 0
    global count7
    count7 = 0
    global count8
    count8 = 0
    global count9
    count9 = 0
    global count10
    count10 = 0
    global count11
    count11 = 0
    global count12
    count12 = 0
    global count13
    count13 = 0
    global count14
    count14 = 0
    global count15
    count15 = 0
    global count16
    count16 = 0
    global count17
    count17 = 0
    global count18
    count18 = 0
    global count19
    count19 = 0
    global count20
    count20 = 0
    global count21
    count21 = 0
    global count22
    count22 = 0
    global count23
    count23 = 0
    global count24
    count24 = 0
    global count25
    count25 = 0
    global count26
    count26 = 0
    global count27
    count27 = 0
    global count28
    count28 = 0
    global count29
    count29 = 0
    global count30
    count30 = 0
    global count31
    count31 = 0
    global count32
    count32 = 0
    global count33
    count33 = 0
    global count34
    count34 = 0
    global count35
    count35 = 0
    global count36
    count36 = 0
    global count37
    count37 = 0
    global count38
    count38 = 0
    global count39
    count39 = 0
    global count40
    count40 = 0
    global count41
    count41 = 0
    global count42
    count42 = 0
    global count43
    count43 = 0
    global count44
    count44 = 0
    global count45
    count45 = 0
    global count46
    count46 = 0
    global count47
    count47 = 0
    global count48
    count48 = 0
    global count49
    count49 = 0
    global count50
    count50 = 0
    global count51
    count51 = 0
    global count52
    count52 = 0
    global count53
    count53 = 0
    global count54
    count54 = 0
    global count55
    count55 = 0
    global count56
    count56 = 0
    global count57
    count57 = 0
    global count58
    count58 = 0
    global count59
    count59 = 0
    global count60
    count60 = 0
    global count61
    count61 = 0

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
    medal25 = '41st Representaion Medal'
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

    global reward1
    reward1 = 0
    global reward2
    reward2 = 0
    global reward3
    reward3 = 0
    global reward4
    reward4 = 0
    global reward5
    reward5 = 0
    global reward6
    reward6 = 0
    global reward7
    reward7 = 0
    global reward8
    reward8 = 0
    global reward9
    reward9 = 0
    global reward10
    reward10 = 0
    global reward11
    reward11 = 0
    global reward12
    reward12 = 0
    global reward13
    reward13 = 0
    global reward14
    reward14 = 0
    global reward15
    reward15 = 0
    global reward16
    reward16 = 0
    global reward17
    reward17 = 0
    global reward18
    reward18 = 0
    global reward19
    reward19 = 0
    global reward20
    reward20 = 0
    global reward21
    reward21 = 0
    global reward22
    reward22 = 0
    global reward23
    reward23 = 0
    global reward24
    reward24 = 0
    global reward25
    reward25 = 0
    global reward26
    reward26 = 0
    global reward27
    reward27 = 0

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

    try:
        if any(ext in rank1 for ext in role_names):
            salary1 = 50000
        if any(ext in rank2 for ext in role_names):
            salary2 = 30000
        if any(ext in rank3 for ext in role_names):
            salary3 = 15000
        if any(ext in rank4 for ext in role_names):
            salary4 = 15000
        if any(ext in rank5 for ext in role_names):
            salary5 = 15000
        if any(ext in rank6 for ext in role_names):
            salary6 = 15000
        if any(ext in rank7 for ext in role_names):
            salary7 = 10000
        if any(ext in rank8 for ext in role_names):
            salary6 = 10000
        if any(ext in rank9 for ext in role_names):
            salary9 = 10000
        if any(ext in rank10 for ext in role_names):
            salary10 = 8000
        if any(ext in rank11 for ext in role_names):
            salary11 = 10000
        if any(ext in rank12 for ext in role_names):
            salary12 = 7000
        if any(ext in rank13 for ext in role_names):
            salary13 = 5000
        if any(ext in rank14 for ext in role_names):
            salary14 = 5000
        if any(ext in rank15 for ext in role_names):
            salary15 = 5000
        if any(ext in rank16 for ext in role_names):
            salary16 = 7500
        if any(ext in rank17 for ext in role_names):
            salary17 = 1000
        if any(ext in rank18 for ext in role_names):
            salary18 = 7500
        if any(ext in rank19 for ext in role_names):
            salary19 = 5000
        if any(ext in rank20 for ext in role_names):
            salary20 = 2500
        if any(ext in rank21 for ext in role_names):
            salary21 = 2000
        if any(ext in rank22 for ext in role_names):
            salary22 = 2000
        if any(ext in rank23 for ext in role_names):
            salary23 = 1500
        if any(ext in rank24 for ext in role_names):
            salary24 = 1500
        if any(ext in rank25 for ext in role_names):
            salary25 = 1000
        if any(ext in rank26 for ext in role_names):
            salary26 = 1000

        rank_total = (salary1 + salary2 + salary3 + salary4 + salary5 + salary6 + salary7 + salary8 + salary9 +
                      salary10 + salary11 + salary12 + salary13 + salary14 + salary15 + salary16 + salary17 + salary18
                      + salary19 + salary20 + salary21 + salary22 + salary23 + salary24 + salary25 + salary26)

        if any(ext in medal_of_valor for ext in role_names):
            valor = 20000
        if any(ext in medal1 for ext in role_names):
            count1 = 3000
        if any(ext in medal2 for ext in role_names):
            count2 = 3000
        if any(ext in medal3 for ext in role_names):
            count3 = 3000
        if any(ext in medal4 for ext in role_names):
            count4 = 3000
        if any(ext in medal5 for ext in role_names):
            count5 = 2500
        if any(ext in medal6 for ext in role_names):
            count6 = 2000
        if any(ext in medal7 for ext in role_names):
            count7 = 2000
        if any(ext in medal8 for ext in role_names):
            count8 = 2000
        if any(ext in medal9 for ext in role_names):
            count9 = 2000
        if any(ext in medal10 for ext in role_names):
            count10 = 2000
        if any(ext in medal11 for ext in role_names):
            count11 = 2000
        if any(ext in medal12 for ext in role_names):
            count12 = 1500
        if any(ext in medal13 for ext in role_names):
            count13 = 1500
        if any(ext in medal14 for ext in role_names):
            count14 = 1500
        if any(ext in medal15 for ext in role_names):
            count15 = 1500
        if any(ext in medal16 for ext in role_names):
            count16 = 1000
        if any(ext in medal17 for ext in role_names):
            count17 = 1000
        if any(ext in medal18 for ext in role_names):
            count18 = 1000
        if any(ext in medal19 for ext in role_names):
            count19 = 1000
        if any(ext in medal20 for ext in role_names):
            count20 = 1000
        if any(ext in medal21 for ext in role_names):
            count21 = 1000
        if any(ext in medal22 for ext in role_names):
            count22 = 1000
        if any(ext in medal23 for ext in role_names):
            count23 = 1000
        if any(ext in medal24 for ext in role_names):
            count24 = 1000
        if any(ext in medal25 for ext in role_names):
            count25 = 1000
        if any(ext in medal26 for ext in role_names):
            count26 = 7500
        if any(ext in medal27 for ext in role_names):
            count27 = 6000
        if any(ext in medal28 for ext in role_names):
            count28 = 5000
        if any(ext in medal29 for ext in role_names):
            count29 = 4500
        if any(ext in medal30 for ext in role_names):
            count30 = 4000
        if any(ext in medal31 for ext in role_names):
            count31 = 3000
        if any(ext in medal32 for ext in role_names):
            count32 = 3000
        if any(ext in medal33 for ext in role_names):
            count33 = 2500
        if any(ext in medal34 for ext in role_names):
            count34 = 2500
        if any(ext in medal35 for ext in role_names):
            count35 = 2500
        if any(ext in medal36 for ext in role_names):
            count36 = 2500
        if any(ext in medal37 for ext in role_names):
            count37 = 2500
        if any(ext in medal38 for ext in role_names):
            count38 = 2500
        if any(ext in medal39 for ext in role_names):
            count39 = 2500
        if any(ext in medal40 for ext in role_names):
            count40 = 2000
        if any(ext in medal41 for ext in role_names):
            count41 = 2000
        if any(ext in medal42 for ext in role_names):
            count42 = 2000
        if any(ext in medal43 for ext in role_names):
            count43 = 2000
        if any(ext in medal44 for ext in role_names):
            count44 = 2000
        if any(ext in medal45 for ext in role_names):
            count45 = 2000
        if any(ext in medal46 for ext in role_names):
            count46 = 2000
        if any(ext in medal47 for ext in role_names):
            count47 = 2000
        if any(ext in medal48 for ext in role_names):
            count48 = 1500
        if any(ext in medal49 for ext in role_names):
            count49 = 1500
        if any(ext in medal50 for ext in role_names):
            count50 = 1500
        if any(ext in medal51 for ext in role_names):
            count51 = 1500
        if any(ext in medal52 for ext in role_names):
            count52 = 1500
        if any(ext in medal53 for ext in role_names):
            count53 = 1500
        if any(ext in medal54 for ext in role_names):
            count54 = 1500
        if any(ext in medal55 for ext in role_names):
            count55 = 1000
        if any(ext in medal56 for ext in role_names):
            count56 = 1000
        if any(ext in medal57 for ext in role_names):
            count57 = 1000
        if any(ext in medal58 for ext in role_names):
            count58 = 1000
        if any(ext in medal59 for ext in role_names):
            count59 = 1000
        if any(ext in medal60 for ext in role_names):
            count60 = 1000
        if any(ext in medal61 for ext in role_names):
            count61 = 1000

        medal_total = (valor + count1 + count2 + count3 + count4 + count5 + count6 + count7 + count8 + count9 +
                       count10 + count11 + count12 + count13 + count14 + count15 + count16 + count17 + count18 +
                       count19 + count20 + count21 + count22 + count23 + count24 + count25 + count26 + count27 +
                       count28 + count29 + count30 + count31 + count32 + count33 + count34 + count35 + count36 +
                       count37 + count38 + count39 + count40 + count41 + count42 + count43 + count44 + count45 +
                       count46 + count47 + count48 + count49 + count50 + count51 + count52 + count53 + count54 +
                       count55 + count56 + count57 + count58 + count59 + count60 + count61)

        if any(ext in qual1 for ext in role_names):
            reward1 = 3000
        if any(ext in qual2 for ext in role_names):
            reward2 = 2000
        if any(ext in qual3 for ext in role_names):
            reward3 = 2500
        if any(ext in qual4 for ext in role_names):
            reward4 = 5000
        if any(ext in qual5 for ext in role_names):
            reward5 = 2000
        if any(ext in qual6 for ext in role_names):
            reward6 = 2000
        if any(ext in qual7 for ext in role_names):
            reward7 = 2000
        if any(ext in qual8 for ext in role_names):
            reward8 = 2000
        if any(ext in qual9 for ext in role_names):
            reward9 = 3000
        if any(ext in qual10 for ext in role_names):
            reward10 = 3000
        if any(ext in qual11 for ext in role_names):
            reward11 = 3000
        if any(ext in qual12 for ext in role_names):
            reward12 = 7500
        if any(ext in qual13 for ext in role_names):
            reward13 = 2000
        if any(ext in qual14 for ext in role_names):
            reward14 = 1500
        if any(ext in qual15 for ext in role_names):
            reward15 = 1000
        if any(ext in qual16 for ext in role_names):
            reward16 = 1500
        if any(ext in qual17 for ext in role_names):
            reward17 = 1000
        if any(ext in qual18 for ext in role_names):
            reward18 = 1500
        if any(ext in qual19 for ext in role_names):
            reward19 = 2000
        if any(ext in qual20 for ext in role_names):
            reward20 = 1000
        if any(ext in qual21 for ext in role_names):
            reward21 = 1500
        if any(ext in qual22 for ext in role_names):
            reward22 = 2000
        if any(ext in qual23 for ext in role_names):
            reward23 = 1000
        if any(ext in qual24 for ext in role_names):
            reward24 = 1500
        if any(ext in qual25 for ext in role_names):
            reward25 = 1000
        if any(ext in qual26 for ext in role_names):
            reward26 = 1500
        if any(ext in qual27 for ext in role_names):
            reward27 = 1000

        qual_total = (reward1 + reward2 + reward3 + reward4 + reward5 + reward6 + reward7 + reward8 + reward9 +
                      reward10 + reward11 + reward12 + reward13 + reward14 + reward15 + reward16 + reward17 +
                      reward18 + reward19 + reward20 + reward21 + reward22 + reward23 + reward24 + reward25 +
                      reward26 + reward27)

        with open("merit.txt", 'r') as f:

            for number, line in enumerate(f):
                if d_id not in line:
                    merit_total = 0
                if d_id in line:
                    line_number = number

                    with open("merit.txt", 'r') as f:
                        file_read = f.readlines()
                        file_int1_read = int(line_number)
                        file_int2_read = (file_int1_read + 1)
                        file_to_read = file_read[file_int2_read]
                        file_to_read_stripped = file_to_read.strip()
                        merit_total = int(file_to_read_stripped)

                        with open("demerit.txt", 'r') as f:
                            for number, line in enumerate(f):
                                if d_id not in line:
                                    demerit_total = 0
                                if d_id in line:
                                    line_number = number

                                    with open("demerit.txt", 'r') as f:
                                        file_read = f.readlines()
                                        file_int1_read = int(line_number)
                                        file_int2_read = (file_int1_read + 1)
                                        file_to_read = file_read[file_int2_read]
                                        file_to_read_stripped = file_to_read.strip()
                                        demerit_total = int(file_to_read_stripped)

                                        trooper_sum = rank_total + qual_total
                                        medal_sum = trooper_sum + medal_total
                                        merit_sum = medal_sum + merit_total
                                        total = merit_sum - demerit_total

        return total
    except UnboundLocalError:
        return False
