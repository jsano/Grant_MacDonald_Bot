import math
import random

# How many verses are in the total song
#verse = 3
# How many times each verse plays
#repeat = 2
# How many lines are in each verse
body = 10

# Pick a value from list ARGS at random
def rng(args):
    rng = math.floor(random.random() * len(args))
    return args[rng]

# Return/execute arg with a 50/50 chance, as well as if it did or not
def optional(arg):
    if random.random() < 0.5:
        if type(arg) is str:
            return arg, True
        else :
            return arg(), True
    else :
        return "", False

def military():
    opts = ["ARMY BOYS",
            "NAVY BOYS",
            "US MARINES",
            "US AIR SPACE FORCES"]
    return rng(opts) + ", "

def vehicle():
    opts = ["HELICOPTERS",
            "CHEVY ARMORED SILVERADOS",
            "RAM T-REX TRUCKS",
            "FORD RAPTOR TRUCKS"]
    return rng(opts)  + ", "

def location():
    opts = [rng(["PULLING UP TO THE ", "ON THE "]) + rng(["COCKSHIP", "CUMSHIP", "FUCKSHIP", "DRIVEWAY"]) + optional(".XXX")[0],
            "RIVEN ROCK, MONTECITO, CALIFORNIA",
            "ON THE ESCALADE RANCH",
            "AT RAM RANCH" + optional(", PRINCE EDWARD ISLAND, CAVENDISH")[0]]
    return rng(opts) + "?"

# A special trigger that's True when the subject is a butthole
BHflag = False

# Returns random subject or recipient based on input. This function returns with a space at the end
def subject_recipient(c):
    global BHflag
    ret = ""
    yes = False
    if c == "s" and random.random() < 0.5:
        ret, yes = optional(rng(["YEAH ", "YO "]))
    opts = ["PRINCE HARRY",
            "SHAWN MENDES",
            "JUSTIN BIEBER",
            "JONAS BROTHERS",
            "SHAWN DRISCOLL",
            "ANDALLA"]
    if c == "s":
        opts += [obj()]
        if not yes:
            opts += ["BLACK COCK GANG"]
    if c == "r":
        opts += ["THAT BOY",
                "YOU BOY",
                cock(),
                "YOUR " + obj()]
        if not yes:
            opts += ["THE BLACK COCK GANG"]
    ret += rng(opts)
    if "HOLE" in ret:
        BHflag = True
    if not yes and not BHflag and c == "s":
        ret += optional("'S " + rng([cock, obj])())[0]
    return ret + (" " if c == "s" else "")

# Returns random action to a subject. This function randomly picks and returns whether the recipient
# is a "c"ock, "p"erson, or "n"one. This function returns with a space at the end
def action():
    global BHflag 
    c = rng(["c", "p", "n"])
    ret = ""
    opts = []
    if BHflag:
        ret += "IN THE AIR "
        BHflag = False
    else:
        if random.random() < 0.5: 
            ret = optional("STRIP NAKED ")[0]
    opts += ["GETTING BUTTFUCKED" + optional(" AND BUTTFUCKED AND BUTTFUCKED")[0] + (" BY" if c == 'c' or c == 'p' else ""),
            "GETTING FUCKED" + optional(" AND FUCKED AND FUCKED")[0] + (" BY" if c == 'c' or c == 'p' else ""),
            "FUCKING" + optional(" AND FUCKING AND FUCKING")[0],
            rng(["SUCKING", "LICKING"]) + optional(" AND " + rng(["SUCKING", "LICKING"]) + " AND " + rng(["SUCKING", "LICKING"]))[0]]
    if c == "p":
        opts += ["DEEP UP"]
    if c == "n":
        opts += no_recipient_action() + [""]
    ret += rng(opts)
    return ret + (" " if not c == "n" else ""), c

def no_recipient_action():
    return ["ERUPTING WITH CUM" + optional(" ERUPTING WITH CUM, ERUPTING WITH CUM")[0],
            "JUST DONE FUCKED YOUR " + obj(),
            "ON THE FLOOR" + optional(" ON ALL FOURS ")[0],
            "SWALLOW ALL THAT CUM" + optional(" BOY")[0],
            "YOU LOVE SWALLOWING CUM" + optional(" BOY")[0],
            "YOU LOVE THAT " + cock() + " DEEP UP YOUR " + obj() + optional(" BOY")[0],
            "YOU LOVE BEING BUTTFUCKED" + optional(" BOY")[0],
            "SWALLOWING LOADS AND LOADS OF CUM, LOADS AND LOADS OF CUM",
            "BEGGING AND BEGGING FOR MORE, BEGGING AND BEGGING FOR MORE",
            "BEGGING AND BEGGING TO BE FUCKED, BEGGING AND BEGGING TO BE FUCKED",
            "OINKING AND OINKING AND OINKING, OINKING AND OINKING AND OINKING"]

def filler():
    opts = ["OH FUCK",
            rng([military, vehicle])() + "GONNA TRY TO RESCUE PRINCE HARRY" + optional(" FROM THE BLACK COCK GANG")[0],
            "CUM A FLOWING, CUM A FLOWING, CUM A FLOWING",
            "DEEP DEEP DEEP, DEEP DEEP DEEP",
            "IN IN IN, IN IN IN",
            "FUCKPIG WHORE, FUCKPIG WHORE, FUCKPIG WHORE",
            "UP AND DOWN, UP AND DOWN, UP AND DOWN",
            "DEEPER AND DEEPER AND DEEPER",
            "IN AND OUT, IN AND OUT, IN AND OUT"]
    return rng(opts)

def cock():
    ret = ""
    opts = [rng(["HUGE HARD ", "BIG ", "BIG HARD "]),
            race() + " ",
            "12 INCH ",
            "THROBBING ",
            "JOCKBOY ",
            "PLEDGEBOY ",
            "STUD ",
            ""]
    for i in range(3):
        cur = rng(opts)
        if not cur == "": 
            opts.remove(cur)
    for i in opts:
        ret += i
    ret += "COCK"
    ret += optional(" HARD AS ROCKS")[0]
    return ret

def race():
    opts = ["WHITE",
            "BLACK",
            "MEXICAN"]
    return rng(opts)

def obj():
    opts = [optional("BUTTER ")[0] + "BUTTHOLE",
            "BOYHOLE"]
    return rng(opts)

# START LYRICS
verse = ""
verse += "YO, WHAT DO " + rng(["WE", "I"]) + " SEE? " + optional(military)[0] + optional(vehicle)[0] + location() + "\n"
for i in range(body):
    verse += subject_recipient("s")
    a, b = action()
    verse += a
    if b == "c" or b == "p":
        verse += subject_recipient("r")
    verse += optional(", " + rng(no_recipient_action()) + " ")[0]
    verse += optional("\n" + filler())[0]
    verse += "\n"
#for i in range(repeat):
print(verse)