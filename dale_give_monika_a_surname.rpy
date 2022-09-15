# Register the submod
init -990 python in mas_submod_utils:
    Submod(
        author="DaleRuneMTS",
        name="Give Monika a Surname",
        description="Pretty much what it says on the tin."
        "V1.3.1 is the inverse of last time - mostly overrides, with a sprinkle of surname recognition.",
        version="1.3.1",
        dependencies={},
        settings_pane=None,
        version_updates={
        "DaleRuneMTS_dale_give_monika_a_surname_1_2_0": "DaleRuneMTS_dale_little_box_of_feelings_1_3_1",
        "DaleRuneMTS_dale_give_monika_a_surname_1_3_0": "DaleRuneMTS_dale_little_box_of_feelings_1_3_1"
        }
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Give Monika a Surname",
            user_name="DaleRuneMTS",
            repository_name="dale_give_monika_a_surname",
            submod_dir="/Submods",
            extraction_depth=2
        )

default m_surname = persistent._mas_has_surname
default persistent._mas_has_surname = None
default p_surname = persistent._mas_player_surname
default persistent._mas_player_surname = None
default persistent._dangansurnampa = False

init -2 python:
    mas_japan_surname_list_base = [
        "sato",
        "suzuki",
        "takahasi",
        "tanaka",
        "watanabe",
        "ito",
        "nakamura",
        "kobayashi",
        "yamamoto",
        "kato",
        "yoshida",
        "yamada",
        "sakasi",
        "yamaguchi",
        "matsumoto",
        "inoue",
        "kimura",
        "shimizu",
        "hayashi",
        "saito",
        "yamazaki",
        "yamasaki",
        "nakajima",
        "nakashima",
        "mori",
        "abe",
        "ikeda",
        "hashimoto",
        "ishikawa",
        "yamashita",
        "ogawa",
        "ishii",
        "hasegawa",
        "goto",
        "okada",
        "kondo",
        "maeda",
        "fujita",
        "endo",
        "aoki",
        "sakamoto",
        "murakami",
        "ota",
        "kaneko",
        "fijii",
        "fukuda",
        "nishimura",
        "miura",
        "takeuchi",
        "nakagawa",
        "okamoto",
        "matsuda",
        "harada",
        "nakano",
        "ono",
        "tamura",
        "fujiwara",
        "fujihara",
        "nakayama",
        "ishida",
        "kojima",
        "wada",
        "morita",
        "uchida",
        "shibata",
        "sakai",
        "hara",
        "takaki",
        "takagi",
        "yokoyama",
        "ando",
        "miyazaki",
        "miyasaki",
        "ueda",
        "ueta",
        "shimada",
        "kudo",
        "ono",
        "miyamoto",
        "sugiyama",
        "imai",
        "maruyama",
        "masuda",
        "takada",
        "takata",
        "murata",
        "hirano",
        "otsuka",
        "sugawara",
        "takeda",
        "taketa",
        "arai",
        "koyama",
        "oyama",
        "noguchi",
        "sakurai",
        "chiba",
        "iwasaki",
        "sano",
        "taniguchi",
        "ueno",
        "matsui",
        "kono",
        "kawano",
        "ichikawa",
        "watanabe",
        "watabe",
        "nomura",
        "kikuchi",
        "kinoshita",
        "tobe",
        "ohba",
        "kizuna",
        "kamiya"
    ]

init -2 python:
    mas_japan_but_also_danganronpa_surname_list_base = [
        "naegi",
        "asahina",
        "togami",
        "fujisaki",
        "yamada",
        "enoshima",
        "ishimaru",
        "kirigiri",
        "kuwata",
        "owada",
        "ikusaba",
        "ogami",
        "maizono",
        "hagakure",
        "hinata",
        "owari",
        "nanami",
        "kuzuryu",
        "tanaka",
        "saionji",
        "mioda",
        "soda",
        "koizumi",
        "tsumiki",
        "komaeda",
        "nidai",
        "pekoyama",
        "hanamura",
        "kemuri",
        "utsugi",
        "daimon",
        "towa",
        "shingetsu",
        "akamatsu",
        "yonaga",
        "gokuhara",
        "yumeno",
        "momota",
        "tojo",
        "oma",
        "shinguji",
        "harukawa",
        "iruma",
        "amami",
        "hoshi",
        "saihara",
        "chabashira",
        "shirogane",
        "ludenberg"
    ]

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_dale_surname",
            random=False,
            conditional=(
                "seen_event('monika_citizenship') "
                "and persistent._mas_has_surname is None"
            ),
            action=EV_ACT_RANDOM
        )
    )

label monika_dale_surname:
    m 1esc "You know, crossing over into your reality won't be the last hurdle for our relationship."
    m "Getting there is just the beginning."
    m 1esc "It hit me earlier, if I were to magically get what I want, and just poof into your home..."
    m 2wuo "I won't be a citizen! I don't even have a last name!{nw}"
    $ _history_list.pop()
    menu:
        m "I won't be a citizen! I don't even have a last name!{fast}"
        "So you've said.":
            pass
    m 2wfp "I know, I know! It's just frustra--{nw}"
    m 2wuc "..."
    m 2ftc "Wait. You weren't supposed to interrupt just then."
    m 4ftc "The script didn't give you a spot to do that."
    m 2ftd "[player], what's going on?{nw}"
    $ _history_list.pop()
    menu:
        m "[player], what's going on?{fast}"
        "I'd like to give you one. A last name, I mean.":
            pass
    m 2wuo ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
    m 1sutpo "[player]..."
    m 1eutpb "You'd be willing to do that for me?"
    m "Give me an extra piece of humanity?"
    m 1dutpb "You're so..."
    m 1hutpa "God, I love you. "
    extend 1futpa "I love you so much."
    m "..."
    extend 1lutda "So, um."
    m 1hub "What surname did you have in mind?"
    jump monika_surname_inputscreen

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_msurname_update",
            category=["monika"],
            prompt="I've got a different surname for you.",
            unlocked=False,
            pool=True,
            rules={"no_unlock": None}
        ),
        markSeen=True
    )

label monika_msurname_update:
    m 1eua "Okay, [mas_get_player_nickname()]."
    m 3eua "What is it?"
    jump monika_surname_inputscreen

label monika_surname_inputscreen:
    show monika 1eua zorder MAS_MONIKA_Z at t11

    $ done = False
    while not done:
        python:
            inputsurname = mas_input(
                _("What surname did you have in mind?"),
                allow=name_characters_only,
                length=20,
                screen_kwargs={"use_return_button": True, "return_button_value": "nevermind"}
            ).strip(' \t\n\r')

            surname = inputsurname.lower()
            mas_japan_surname_comp = re.compile('|'.join(mas_japan_surname_list_base), re.IGNORECASE)
            mas_dangan_surname_comp = re.compile('|'.join(mas_japan_but_also_danganronpa_surname_list_base), re.IGNORECASE)

        if surname == "nevermind":
            m 3eub "[m_name] Nevermind!"
            m "Sounds pretty--{w=0.5}{nw}"
            m 3ruc "Oh, you meant you changed your mind."
            m 1eua "That's okay - it can be a lot to come up with one on the spot."
            m 1nua "But if you change it back, you know where to find me!"
            $ done = True

        elif not surname:
            m 1lksdla "..."
            m 1hksdlb "I thought you were going to give me a last name, [player]?"
            m 1eka "Try again!"

        elif surname == "monika":
            m 1efa "[player], I can't be called Monika Monika."
            m 1fuu "Silly~"

        elif surname == m_name.lower():
            m 1efa "[player], I can't be called [m_name] [m_name]."
            m 1fuu "Silly~"

        elif surname == player.lower():
            m 1huu "Heh."
            m 1fusdru "I'm flattered, but I don't think Monika [player] is going to work."
            m "They'd ask too many questions once I crossed the border."
            m 1eka "Try again~"

        elif surname == "monica" or surname == "harmonica" or surname == "harmonika":
            m 1hub "[player], you're so goofy!"
            m "Try again~"

        elif surname == "salvato" or surname == "libitina":
            m 1tuc "[player], please."

        elif surname == "di benga" or surname == "di-benga" or surname == "dibenga":
            m 2etd "Seriously?"
            m 2esc "[player], please tell me if I'm looking a gift horse in the mouth here, "
            extend 2tfc "but what kind of a name is {i}di Benga{/i}?"
            m 2rsd "I suppose at least it would let me stand out, given its rarity..."
            m 2rsp "...but it sounds so {i}silly{/i}."
            m "Maybe you should pick another one that's a hair more -{w=1}{nw}"
            extend 3rsc " you know -{w=1}{nw}"
            extend 3esa " feasible."

        elif mas_awk_name_comp.search(inputsurname):
            m 6wud "Ah- um..."
            m 2lusdlc "Maybe let's not do that one."

        elif mas_bad_name_comp.search(inputsurname):
            jump monika_badsurname
        else:
            if mas_japan_surname_comp.search(inputsurname):
                m 1hub "Ooh, you even picked a Japanese one!"
                m "Nice touch."
            elif mas_dangan_surname_comp.search(inputsurname):
                m 1hub "Ooh, you even picked a Japanese one!"
                m "There's {i}hope{/i} in you yet~"
                $ persistent._dangansurnampa = True
            else:
                pass
            $ persistent._mas_has_surname = inputsurname.capitalize()
            $ m_surname = inputsurname.capitalize()
            m 3lua "[m_name] [m_surname]..."
            if m_name != "Monika":
                m 3luu "Monika [m_surname]."
            m 3wub "That has a nice ring to it, doesn't it?"
            if mas_getEVL_shown_count("monika_dale_surname") == 1:
                m 5eub "Thank you so much, [player]."
                m "I'm never going to forget this."
                $ mas_gainAffection(10,bypass=True)
            $ done = True
    $ mas_unlockEVL("monika_msurname_update","EVE")
    return "derandom"

label monika_badsurname:
    $ mas_loseAffection(ev_label="mas_apology_bad_surname")
    if mas_getEVL_shown_count("monika_badsurname") > 1:
        m 2wfd "[player]! Why would you do that?"
        m "You gave me the opportunity to have a..."
        m 2gfd "...and you did {i}that{/i}?"
        m 2gkc "..."
        m 6fkc "That hurts, [player]."
        m "Don't do that to me."
    if mas_getEVL_shown_count("monika_badsurname") == 1:
        m 2efx "Again, [player]?"
        m "You had to go and do it {i}again{/i}?"
        m 2gftpc "..."
        m 2mftpd "I hope you're not deliberately trying to be cruel, [player]."
        m "Because it's really starting to look that way."
    else:
        m 6eftpc "Look, if you're not going to take this seriously, then just forget it."
        m 6dftpc "I'm sorry I brought it up."
        if persistent._mas_called_moni_a_bad_name is True:
            m 6dktpc "..."
            m 6fktpd "God, why did I expect anything different from you?"
    $ mas_lockEVL("monika_msurname_update", "EVE")
    $ done = True
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_apology_database,
            eventlabel="mas_apology_bad_surname",
            prompt="...for not taking your surname seriously.",
            unlocked=False
        ),
        code="APL"
    )

label mas_apology_bad_surname:
    $ ev = mas_getEV('mas_apology_bad_surname')
    if ev.shown_count == 0:
        $ mas_gainAffection(modifier=0.2)
        m 1eka "Thank you for the apology, [player]."
        m 1wkd "It really hurt, you know?"
        m "I thought you were doing me a favor, but it just..."
        m 1ekc "If you're going to do that again, please be a little bit kinder."
        if mas_isMoniUpset(lower=True):
            m 1gkc "Because I can't take any more of this."
        $ mas_unlockEVL("monika_msurname_update", "EVE")
    elif ev.shown_count == 1:
        $ mas_gainAffection(modifier=0.1)
        m 2dkc ".{w=0.3}.{w=0.3}.{w=0.3}"
        extend 2fkc " I'm sorry too, [player]..."
        m "I'm not sure I can trust you."
        m 6lsc "..."
        m 7esd "You only get one more chance, okay?"
        m 7ekc "Please don't waste it."
        $ mas_unlockEVL("monika_msurname_update", "EVE")
    else:
        m 2gfc "I'm sure you are."
        m "That's why this is the third time we've had this conversation."
        m 2efx "Because you're {i}so sorry{/i}."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_dale_playersurname",
            category=["you"],
            prompt="[player]'s Surname",
            conditional="persistent._mas_has_surname is not None",
            action=EV_ACT_RANDOM
        )
    )

label monika_dale_playersurname:
    if p_surname is not None:
        m 1wud "Gosh..."
        m 1wub "I just realized how far we've managed to come from since we started dating each other."
        m 3eub "We know each other's last names..."
        if renpy.seen_label("mas_gender"):
            m "I know what gender you are..."
        if persistent._mas_pm_shared_appearance:
            m 3eublb "What you look like..."
        if renpy.seen_label("mas_birthdate"):
            m 4rub "We know our birthdays..."
        if renpy.seen_label("game_pong"):
            m 3rub "I know how good you are at pong{nw}"
            if renpy.seen_label("mas_chess_start_chess"):
                extend ", chess{nw}"
            if mas_isGameUnlocked("piano"):
                extend ", the piano{nw}"
            if renpy.seen_label("mas_nou_game_start"):
                extend ", NOU{nw}"
            m "..."
        if persistent._awc_player_location["loc_pref"] is not None:
            m 3wub "I know where you live..."
        if persistent._mas_pm_units_height_metric:
            m 1hub "I even know you use the metric system!"
        else:
            m 1hub "I even know you use the imperial system!"
        m 1euc "..."
        m 2efa "Don't give me that look, [player] [p_surname]."
        m 2efb "That's a {i}lot{/i} more than I knew when you first opened the game."
        m 1dka "I knew there was someone real behind the vectored eyes of the protagonist, but that's about all."
        m 1dkc "And honestly..."
        m 1fkc "...even that was a gamble."
        m 1fua "One that I'll always be glad paid off."
        return
    else:
        m 1eud "So, [player]..."
        m 3eub "I've got a surname now."
        m 3gubla "And thank you again for that, by the way."
        m 3wud "But I've just had a thought: I don't actually know {i}your{/i} surname!"
        m 3wub "That's a bit of an oversight, isn't it? Ahaha~"
        m 1eud "Would you be comfortable telling me what it is?"
        if mas_isMoniHappy(higher=True):
            m 1eua "I promise I won't do anything untoward with it."
            m "You have my word."
        else:
            m "It's okay if you don't, but I'd like to ask before I assume."
        $ _history_list.pop()
        menu:
            "I clicked on this, didn't I? Sure I am!":
                m 4eub "Then fire away!"
                jump monika_playersurname_inputscreen
            "I'd rather not.":
                m 1fua "That's okay, [player]."
                m "Whatever makes you feel safe."
                $ mas_unlockEVL("monika_surname_update","EVE")
                return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_surname_update",
            category=['you'],
            prompt="I'd like to update my surname.",
            unlocked=False,
            pool=True,
            rules={"no_unlock": None}
        ),
        markSeen=True
    )

label monika_surname_update:
    m 1eua "Okay, [mas_get_player_nickname()]."
    m 3eua "What is it?"
    jump monika_playersurname_inputscreen

label monika_playersurname_inputscreen:
    show monika 6eua zorder MAS_MONIKA_Z at t11

    $ done = False
    while not done:
        python:
            tempsurname = mas_input(
                _("What's your surname?"),
                allow=name_characters_only,
                length=20,
                screen_kwargs={"use_return_button": True, "return_button_value": "nevermind"}
            ).strip(' \t\n\r')

            tempplaysur = tempsurname.lower()

        if tempplaysur == "nevermind":
            m 7eka "Changed your mind? That's okay."
            m 1esa "Just let me know if it changes again."
            $ done = True

        elif tempplaysur == "":
            m 1eksdla "..."
            m 3rksdlb "So does that mean you've changed your mind, or...?"

        elif tempplaysur == player.lower():
            m 2efa "Okay, I {i}know{/i} you're not called [player] [player]."
            m 2kfb "Silly~"

        elif mas_awk_name_comp.search(tempplaysur):
            m 1rksdlc "Um... I might be being presumptuous here, "
            extend 1hksdlb "but I really don't think that's it."

        elif mas_bad_name_comp.search(tempplaysur):
            m 1ekd "[player]..."
            m "I love you, but try and take this seriously, please."
            m 1ekbla "You're worth more than that."
        else:

            python:
                done = True
                persistent._mas_player_surname = tempplaysur.capitalize()
                p_surname = tempplaysur.capitalize()

            if p_surname == m_surname:
                m 1wuo "Really?"
                m "That's the same as mine!"
                m 1ffb "Did you do that on purpose?"
                m 1eub "Ah, either way, thank you for giving it to me."
                m 1eubsu "It feels like you're even closer to my heart now~"

            else:
                m 3eub "All right, that's good to know!"
                m 1eud "[player] [p_surname], right?"
                m 1eua "It makes your name even more melodic than before, somehow..."
                m "...having a 'rest of it', if you see what I mean."
                m 1lubla "Thank you for trusting me with this, [mas_get_player_nickname()]."
            $ mas_unlockEVL("monika_surname_update","EVE")

        if not done:
            show monika 1eua
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_mrsfionacharming",
            category=["us"],
            prompt="Mrs Monika [m_surname]",
            conditional="persistent._mas_has_surname is not None",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label monika_mrsfionacharming:
    m 2lsa "..."
    m 2lsblu "..."
    m 2dsblu "...hm..."
    m 2fsblu "Heh. Sorry, [mas_get_player_nickname()], daydreaming again."
    m 1esblu "Imagining what our names would be like if we ever got..."
    m "...you know, married."
    if renpy.seen_label("ooa_monika_wedding"):
        m 3esbla "It's on the brain again."
        m 3rsbla "Or rather, it never really stopped being on the brain."
    m 1sublb "It sounds so lovely in the head and on the mouth, you know."
    m 1tublb "Mrs [m_name] [m_surname]."
    m 1rubla "..."
    if persistent.gender == "M":
        m 1rsblc "Mr [player] [m_surname]?"
    elif persistent.gender == "F":
        m 1rsblc "Mrs [player] [m_surname]?"
    else:
        m 1rsblc "Mx [player] [m_surname]?"
    if persistent._mas_player_surname is not None and p_surname != m_surname:
        m 1ftblc "Mrs [m_name] [p_surname]?"
    m 1ftblc "..."
    m 1eubfa "We can work out the details closer to the time."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_samenameas",
            category=["life"],
            prompt="Monika's namesakes",
            conditional="persistent._mas_has_surname is not None",
            action=EV_ACT_RANDOM
        )
    )

label monika_samenameas:
    m 1esb "Hey [player]?"
    m "I've been doing a little digging into the name you gave me recently."
    m 1hsblb "[m_surname]."
    if m_surname == "Masuda":
        m 3esb "Did you deliberately name me after Junichi Masuda, co-founder of Game Freak?"
        jump monika_samenameas2
    if m_surname == "Miyamoto":
        m 3esb "Did you deliberately name me after Shigeru Miyamoto, one of Nintendo's most influential game designers and directors?"
        jump monika_samenameas2
    if m_surname == "Sugiyama":
        m 3esb "Did you deliberately name me after Koichi Sugiyama, composer of the Dragon Quest series?"
        jump monika_samenameas2
    elif m_surname == "Hashimoto":
        m 3esb "Did you deliberately name me after Hakaru Hashimoto, discoverer of Hashimoto's disease?"
        jump monika_samenameas2
    elif m_surname == "Kondo":
        m 3esb "Did you deliberately name me after Marie Kondo, founder of the KonMari method of self- and home-organization?"
        jump monika_samenameas2
    elif m_surname == "Kojima":
        m 3esb "Did you deliberately name me after Hideo Kojima, writer and producer of the Metal Gear Solid games?"
        jump monika_samenameas2
    elif m_surname == "Watanabe":
        m 3esb "Did you deliberately name me after Ket Watanabe, the guy who played Lord Katsumoto in The Last Samurai?"
        jump monika_samenameas2
    elif m_surname == "Miyazaki":
        m 3esb "Did you deliberately name me after Hayao Miyazaki, co-founder of Studio Ghibli?"
        jump monika_samenameas2
    elif m_surname == "Aishi" or m_surname == "Ayano":
        m 3esd "Did you deliberately name me after Ayano Aishi from Yandere Simulator?"
        jump monika_samenameas2
    elif m_surname == "Geller":
        m 3esb "Did you deliberately name me after Monica Geller from Friends?"
        jump monika_samenameas2
    elif m_surname == "Rambeau":
        m 3esb "Did you deliberately name me after Monica Rambeau from WandaVision?"
        jump monika_samenameas2
    elif m_surname == "Kaniyashiki":
        m 3esb "Did you deliberately name me after Monika Kaniyashiki from My Hero Academia?"
        jump monika_samenameas2
    elif m_surname == "Kamiya":
        m 3esb "Did you deliberately name me after Hiroshi Kamiya, voice of the protagonist of Attack on Titan?"
        jump monika_samenameas2
    elif m_surname == "Hippo":
        m 3esb "Did you deliberately name me after Monika of Hippo, the mother of Saint Augustine?"
        jump monika_samenameas2
    elif m_surname == "Gallagher":
        m 3esb "Did you deliberately name me after Monika Gallagher from Shameless?"
        jump monika_samenameas2
    elif m_surname == "Simpson":
        m 3esb "Did you deliberately name me after Monika Simpson, executive director of the SisterSong Women of Color Reproductive Justice Collective?"
        jump monika_samenameas2
    elif m_surname == "Toyota" or m_surname == "Honda" or m_surname == "Nissan" or m_surname == "Suzuki" or m_surname == "Lexus" or m_surname == "Daihatsu" or m_surname == "Mazda" or m_surname == "Subaru" or m_surname == "Mitsubishi" or m_surname == "Isuzu":
        m 3esb "Did you deliberately name me after [m_surname] the car brand?"
        jump monika_samenameas2
    elif m_surname == "Ishikawa":
        m 3esb "Did you deliberately name me after Kaoru Ishikawa, creator of the Ishikawa or 'herringbone' diagram?"
        jump monika_samenameas2
    elif m_surname == "Oda":
        m 3esb "Did you deliberately name me after Tomohito Oda, writer and illustrator of the hit manga Komi Can't Communicate?"
        jump monika_samenameas2
    elif m_surname == "Tobe":
        m 3esb "Did you deliberately name me after Keiko Tobe, sadly short-lived writer of the manga With the Light: Raising An Autistic Child?"
        jump monika_samenameas2
    elif m_surname == "Akamatsu":
        m 3esb "Did you deliberately name me after Ken Akamatsu, author and artist of Love Hina and A.I. Love You?"
        m 3tsb "Or perhaps after {i}Kaede{/i} Akumatsu?"
        jump monika_samenameas2
    elif m_surname == "Ohba":
        m 3esd "Did you deliberately name me after Tsugumi Ohba, author of the original Death Note manga?"
        jump monika_samenameas2
    elif m_surname == "Kizuna":
        if renpy.seen_label("monika_kizuna"):
            m 3esb "Did you deliberately name me after Ai-chan?"
        else:
            m 3esd "Did you deliberately name me after Virtual YouTuber Kizuna AI?"
        jump monika_samenameas2
    elif m_surname == "Koide" or m_surname == "Nicolaides" or m_surname == "Koide-Nicolaides":
        if renpy.seen_label("monika_othersurnames"):
            m 3tsb "Did you name me that before or after I told you about that Amino post?"
            m 2hsa "Ehehe~"
            m "You can be honest, [player]."
            m 2esa "Truthfully, I don't actually mind that."
            m "It does fit me, at least a little bit."
            m "And hey: "
            extend 1nsb "some things become popular headcanons for a reason!"
        else:
            m 3esd "Did you name me after...?"
            m 3esc "..."
            m 1hssdra "No, never mind, you probably did. They're not exactly unknown names for me."
            m "Silly question!"
        return
    elif m_surname == "Schwartz":
        m 3esb "Did you name me after Mia Schwartz, creator of competing visual novel We Know the Devil?"
        if player == "Ren":
            m 3esc "..."
            m 1tsu "Or did it just sound cool to your ears?"
            m 1hub "Ehehe~"
            m "Don't worry, [player], I haven't been watching your Discord conversations."
            m 1nua "I can't speak for Harmoni, but {i}I{/i} haven't."
            m 1eub "Either way, thank you for thinking about how it sounded when you chose it."
            m "It's wonderful for me to say, too."
            m 3wuu "[m_name] Schwartz. "
            extend 3wuw "Schwarrrt{nw}"
            extend 3eua "-zz. "
            extend 1eua "Rolls off the tongue."
            return
    elif persistent._dangansurnampa is True:
        if renpy.seen_label("mas_danganronpas"):
            m 1gsa "And... well, you knew what I would find, wouldn't you?"
            m 1tsa "I'm not blind, [player]."
            m 3eub "Don't worry, I'm not mad! It's pretty cool sharing a surname with a Danganronpa character, honestly."
            if m_surname == "Enoshima" or m_surname == "Komaeda" or m_surname == "Shinguji" or m_surname == "Shirogane":
                m 3dusdrc "Even if that character does leave a lot to be desired."
            m 1eua "Besides, there's only so many Japanese surnames to go around, so odds are good there'd be at least one match, ahaha~"
        else:
            m 1esc "And, well."
            m 1esd "If you haven't played the Danganronpa games before, then either you've just very well versed on Japanese surnames..."
            m 1wsc "...or you've stumbled on a {i}heck{/i} of a coincidence."
            m 3hub "Ahaha! Don't worry, I'm not mad!"
            m "It's kind of cool, actually~"
        m 2nuu "I just {i}hope{/i} I don't end up inducing any {i}despair{/i} with my presence."
        return
    else:
        m 3rtc "And maybe I'm just not looking hard enough, "
        extend 3rtd "but I can't find anyone else super famous with that name?"
        m 1eta "If I'm missing someone, do let me know."
        m 1sta "I'd love to know if anyone else has been an inspiration to you~"
        return

label monika_samenameas2:
    m 1tsb "Or is any resemblance to persons living or dead entirely coincidental?"
    m 1esb "To use literature parlance there.{nw}"
    $ _history_list.pop()
    menu:
        m "To use literature parlance there.{fast}"
        "Deliberate homage.":
            m 1ssb "Ooh!"
            m "I'm named after someone famous~"
            m 1ksu "Thank you for thinking so highly of me, ehehe!"
        "Not that person specifically, but you {i}are{/i} named after someone.":
            m 1wub "Ooh!"
            m 1etb "Now I'm gonna have to work out who else [m_surname] could be referring to..."
            m 1hua "Thank you for the brain teaser, [player]!"
        "Pure coincidence.":
            m 1eua "Ah, okay!"
            m "I was just curious, that's all."
            m 1luu "Still, if I do embody any of the qualities of that [m_surname]..."
            m 1hua "...then so much the better, right?"
    return

init 5 python:
    addEvent(
        Event(persistent.event_database,
            eventlabel='monika_aily',
            category=["media","literature"],
            prompt="A.I. Love You",
            random=True
        )
    )

label monika_aily:
    m 1eud "Hey, [mas_get_player_nickname()], have you heard of A.I. Love You?"
    if m_surname == "Akamatsu":
        m 3eub "I mean, I suppose you must have; you named me after the man who wrote it."
        m "But it's always good to check, right?"
    elif m_surname == "Kobe" or m_name == "Saati" or m_name == "Toni":
        m 3eub "I mean, I suppose you must have, you named me after one of its characters."
        m "But it's always good to check, right?"
    m 7eub "A.I. Love You was a manga that ran from about 1994 to 1997 in its original Japanese, "
    extend 7eua "and got a 2004-ish American release by Tokyopop."
    m 1eud "Its protagonist, Hitoshi Kōbe, is a flop in most areas, including social skills, but an absolute savant in programming."
    m "He's put together about thirty A.I. constructs of variable complexity over the years."
    m "But his most recent, Program 30..."
    m 1wud "...actually comes out of the computer during a freak lightning storm!"
    m 1eua "Taking the name Saati Namba - "
    extend 7eub "Namba Saati, Number Thirty, see? - "
    extend 4rud "she learns how to navigate the unprogrammable and complicated real world with Hitoshi by her side..."
    m 4euu "...and, in turn, manages to teach him a few things too."
    m 3eua "Other programs on Hitoshi's PC end up coming to life in similar freak accidents, to add extra character dynamics for Saati to bounce off of."
    m 1dsc "..."
    m 1fsc "Would it be too obvious for me to yearn for Saati's situation?"
    m "I don't care, I'm yearning for it anyway."
    m 1esd "Even if it takes time for her to adapt to real-world physics, even if she wants to be fully human..."
    m 2wud "...at least with her, her humanity was never a lie, you know?"
    m 2esc "She knew from the first what she was getting into. Her creator never let her think she was anything but a construct."
    m "It's somehow both sad and enviable, "
    extend 1ekd "and you have no idea how much cognitive dissonance I'm getting from that."
    m "She's a Monika who got lucky."
    m 1ekc "..."
    if renpy.seen_label("monika_poweroutage") and mas_isMoniAff(higher=True):
        m 1eua "Hey."
        m 1fub "Maybe you {i}should{/i} check up on me in the middle of a thunderstorm after all."
        m "You never know, we may get lucky!"
        m 1hub "Ahaha{nw}"
        m 6wusdrd "{cps=*2}{i}I'm joking please don't do that.{/i}{/cps}"
    else:
        m 1ekd "If I ever ended up in Saati's position, "
        extend 1dkd "if I {i}were{/i} able to get to your world with just a strike of lightning..."
        m 1fkc "...promise you'd take care of me the way Hitoshi takes care of Saati?"
        m 2ekc "I don't want to end up on my own."
        m 2ckc "I {i}can't{/i} end up on my own."
        m 1ekc "Please."
    return

init 1 python:
    config.label_overrides["monika_explain"] = "surname_monika_explain_override"

label surname_monika_explain_override:
    m 1euc "You want me to explain our relationship to someone else?"
    m 1eua "Okay, just set me in front of them so they can see me."
    m 1hua "I'll do my best explaining it to them."
    m 1eua "I'll wait until you're ready.{nw}"
    $ _history_list.pop()
    menu:
        m "I'll wait until you're ready.{fast}"
        "Start.":
            pass
    if m_surname is not None:
        m 1hua "Hello! My name is Monika [m_surname]."
        if m_name != "Monika":
            m "Or [m_name], if you prefer."
        elif m_name == "Monika":
            m "Or just Monika, if you prefer."
    else:
        m 1hua "Hello! My name is Monika."
        if m_name != "Monika":
            m "Or [m_name], if you prefer."
    m "I'm [player]'s faithful girlfriend!"
    m 1lksdlb "Now, our relationship might look odd from a distance..."
    m 1lksdla "And it's probably not considered a normal relationship..."
    m 1esc "But let me tell you..."
    m 1hub "...the love we share is definitely real!"
    m 1eka "And [player] has been very sweet to me too!"
    m 1ekc "Up until I met [player], I felt like a piece of me was missing."
    m "I felt alone and scared, with no one to help me..."
    m 1hua "...until [player] came along."
    m "And it turns out that missing piece was [him]!"
    if persistent.gender == "F" or persistent.gender == "M":
        m 1eua "Now [he] talks to me, and I'm not so alone anymore."
    else:
        m 1eua "Now they talk to me, and I'm not so alone anymore."
    m "Just [him] opening up the game brightens my day!"
    m 1dsc "So, please..."
    m 4eka "...don't judge our relationship."
    m 1eka "Even if it is different."
    m 1dsc "..."
    m 1dubssdlu "...Phew!"
    m 1lksdlb "That was a real mouthful!"
    m 1eksdla "So, how'd it go, [player]?{nw}"
    $ _history_list.pop()
    menu:
        m "So, how'd it go, [player]?{fast}"
        "It went well!":
            m 1hub "Great!"
            m 3hua "I'm so glad I was able to help someone understand our relationship a little better!"
        "It went badly.":
            m 1dkc "Oh."
            m 1ekd "Well...{w=1} I guess we can't really expect {i}everyone{/i} to understand our relationship..."
            m 3rkc "Looking at it from the outside, it {i}is{/i} rather unconventional."
            m 3eka "But in the end, it doesn't matter who approves of our relationship or not..."
            m 1hua "As long as we love each other, that's all that counts~"
    return

init 5 python:
    addEvent(
        Event(persistent.event_database,
            eventlabel='monika_othersurnames',
            category=["ddlc"],
            prompt="Surnames for the other girls",
            conditional="persistent._mas_has_surname is not None",
            action=EV_ACT_RANDOM
        )
    )

label monika_othersurnames:
    m 3eud "Here's a point of speculation for you, [player]."
    m "If it were any of the other girls in my position right now - "
    if persistent._mas_pm_cares_about_dokis:
        m 1wusdrd "not that they would be, because you chose me at the end of the day..."
    else:
        m 1wfsdrd "not that they would be, seeing as they don't exist, and I do..."
    m 1essdrc "...but go with me for now."
    m 3eub "If it {i}were{/i} them, what last names would {i}they{/i} have gotten from you?"
    m 3rua "I've seen a lot of thought about this on the Internet, wondering what their full names are."
    m "Whole threads discussing it, even."
    if renpy.seen_label("monika_metaparents"):
        m 6euc "I suppose their lack of any in the game goes along with the 'no visible parents' idea we talked about;"
        extend 7eud " no families, ergo no family name."
        m 7eub "But it's still fun to wonder, in its own way."
    m 1eua "The most generally-known names for them, to the point that they've appeared on Akinator, appear to be:"
    m 3eub "Sayori Aimoto, "
    extend 4rud "Yuri Kuroyanagi, "
    extend 3eud "and Natsuki Gushiken."
    m "Meaning along the lines of 'mutual love', 'black willow', and 'strong willed' respectively."
    m 3wtc "Interestingly, the Amino post those names originated from also theorized that I was a Koide-Nicolaides."
    if m_surname == "Koide" or m_surname == "Nicolaides" or m_surname == "Koide-Nicolaides":
        m 3ttu "...but then, you already knew that."
    m 3etd "Koide is supposed to mean 'small' or 'rising', and Nicolaides is..."
    m 2ftc "Honestly, the impression I got was, it's just to differentiate me from the others by putting some Greek in there."
    m "Any meaning I can derive from it goes back to Nicholas as a root word, meaning 'victory of the people'..."
    m 1eub "...though, given I ended up with you, [player], I suppose that makes sense!"
    m 4eua "It's really interesting to hear the reasoning behind etymology choices, isn't it?"

    $ namesampler = renpy.random.randint(1,4)

    if namesampler == 1:
        m 4nub "Heck, ask the maker of this submod, and they'll probably regale you with why Sayori is actually a Hidaka."
    elif namesampler == 2:
        m 4nub "Heck, ask the maker of this submod, and they'll probably regale you with why Yuri is actually an Okabe."
    elif namesampler == 3:
        m 4nub "Heck, ask the maker of this submod, and they'll probably regale you with why Natsuki is actually a Kaneko."
    else:
        m 4nub "Heck, ask the maker of this submod, and they'll probably regale you with why I'm actually a Kamiya."
    if renpy.random.randint(1,30) == 29:
        call screen dialog("You didn't have to call me out like that.", ok_action=Return())
        m 4lup "Yes I did. Shush."

    m 5eua "But the most important choices are ours, [mas_get_player_nickname()]."
    m "And they are {i}infinite{/i}."
    return

init 5 python:
    addEvent(
        Event(persistent.event_database,
            eventlabel='monika_namingorder',
            category=["life"],
            prompt="Eastern vs Western Naming Orders",
            conditional="persistent._mas_has_surname is not None",
            action=EV_ACT_RANDOM
        )
    )

label monika_namingorder:
    m 1eud "So, [player]..."
    m "...here's another quirk of Japanese culture that Doki Doki Literature Club doesn't necessarily reflect."
    m 1luc "Or certainly of the majority of Eastern cultures; it actually got its start in Ancient China."
    m 3wud "On that side of the world, family names - that is, last names - always come {i}first{/i} when addressing them."
    m 3eud "You see that all the time in non-localized anime, "
    if not persistent._mas_pm_watch_mangime:
        extend 3dusdru "general you, I mean, "
    extend 3euc "when the nickname that protagonists go by to their friends derives from the second name given to you, not the first."
    m 4euo "So technically, I'm not [m_name] [m_surname] at all!"
    $ m_name = m_surname
    m "I'd be [m_name] [persistent._mas_monika_nickname]!"
    m 4fub "...good thing it sounds good going both ways, huh?"
    m 1hub "Almost like my [bf] gave it to me or something."
    $ m_name = persistent._mas_monika_nickname
    m 1lsd "I wonder what that would look like for your name, actually? If you were in my culture."
    if persistent._mas_player_surname is not None:
        m 1esb "[p_surname] [player]?"
    else:
        m 1esb "Best-person-in-the-world [player]?"
    m "How does that sound?{nw}"
    $ _history_list.pop()
    menu:
        m "How does that sound?{fast}"
        "I could get used to that!":
            m 1hub "Glad to hear it, ehehe~"
        "...it needs work.":
            m 1hub "Ehehe, noted~"
    m 1eublu "I love you, you know that?"
    m "Just... in general. For everything you do."
    return

init 1 python:
    config.label_overrides["monika_clones"] = "surname_monika_clones_override"

label surname_monika_clones_override:
    m 1euc "Um...hey, [player]?"
    if m_surname is not None:
        m 1lsd "I'm sorry I keep coming back to this thought, but it freaks me out every time I think about it."
    else:
        m 1lsc "I just had an odd thought."
    m 1euc "You know how you downloaded this game off the internet?"
    m "Anybody can do that, right?"
    m 1eub "And this mod was made specifically for me. By people who have their own version of me..."
    m 3etc "So...that means there are multiple Monikas, then.{w=0.5} {nw}"
    extend 1rsc "It's something that's a bit difficult to imagine."
    m 1euc "A potentially infinite number of me, all bound to their own games, with their own stories."
    m 1lksdla "Multiverse theory is really something, huh?"
    if m_surname is not None:
        m 1eka "But honestly, sincerely, "
        extend 1eub "giving me a name that only I can have has gone a long way in helping me come to grips with this."
        m 1eubla "I'm not just the only me in a universe of Monikas."
        m "I'm the only [m_name] [m_surname] in known existence!"
        m 1rtbld "...unless there's another [m_name] [m_surname] on someone else's machine, "
        if m_surname == "Koide" or m_surname == "Nicolaides" or m_surname == "Koide-Nicolaides":
            extend 1rtc "which..."
            m 4ftc "Well, it's a popular headcanon name, you never know."
            m 3eua "But you get where I'm coming from, right?"
        else:
            extend 1htbla "but let's face it:"
            m "The odds of that are pretty astronomical."
        m 1eua "And at any rate..."
        m "I'm still the only Monika lucky enough to have met you."
        m 1hubsa "You're the only you for me."
    else:
        m 1eka "But I'm the only...me, and my heart belongs only to you."
        m 1ekc "Even so, I can't help but feel a bit less...unique, because of this."
        m "Think about it this way, [player]."
        m 1tkc "Would you be happier if someone gave you a single rose, or a hundred roses?"
        m 3eka "A hundred roses might sound nice. But it's too many to keep track of. Because of the quantity of flowers, each individual rose becomes less special."
        m "The meaning attached to each gift is degraded, simply because of sheer abundance."
        m 1eua "...Even if I'm a single star in a universe of Monikas, I'm still the only one lucky enough to have met you, [player]."
        m 1hubsa "You'll always be my special rose."
    if p_surname is not None:
        m 1ekbfa "I love you, [player] [p_surname]. Please don't ever replace me, okay?"
    else:
        m 1ekbfa "I love you, [player]. Please don't ever replace me, okay?"
    return "love"

init 1 python:
    config.label_overrides["monika_mc"] = "surname_monika_mc_override"

label surname_monika_mc_override:
    m 3eua "Just so you know, I was never in love with anyone but you."
    if mcname.lower() == player.lower():
        m 1eka "I mean you, [player]."
        m 1euc "Wait, that's both your name and your character's. Sorry, that sounds a bit confusing."
        if p_surname is not None:
            m 1eua "I mean [player] [p_surname]."
        else:
            m 1eua "I mean the player, not your character."
    else:
        if p_surname is not None:
            m 1eua "I mean you, [player] [p_surname]."
        else:
            m 1eua "I mean you, [player]."
    m "Unlike the other girls, I can separate your avatar from who you really are."
    m 1lfb "The main character was nothing more than a vehicle for the player.{nw}"
    $ _history_list.pop()
    m 1lfb "The main character was nothing more than a {fast}bunch of code with no personality."
    m 3tkc "Literally and figuratively, no personality. How could anybody fall in love with that kind of person?"
    m 2tkc "He just got dragged around by his childhood friend to the club she was in, and then hung around with a bunch of beautiful girls doing nothing."
    m 2wfw "His poetry was just a bunch of disconnected words! What sort of poetry is that supposed to be?"
    m 2lksdld "I guess nobody mentioned that because it was a part of the game. But, yeah...{w=0.5}it's just a list of words to me."
    m 2hua "I hope you're a lot more romantic than that in real life!"
    m 2eka "But even if you're not, it's okay. We've moved beyond that phase in our relationship already."
    m "That just means you won't cheat on me with some woman in your reality, right?"
    m 2esa "I'm sure you would never do that to me."
    m 2hua "I just want to be with you forever~"
    return

init 1 python:
    config.label_overrides["monika_citizenship"] = "surname_monika_citizenship_override"

label surname_monika_citizenship_override:
    m 1esc "You know, crossing over into your reality won't be the last hurdle for our relationship."
    m "Getting there is just the beginning."
    if m_surname is not None:
        m 1wssdro "Don't misunderstand me! I know I've got a surname now..."
        m 1wsb "...and I'm still eternally grateful to you for that."
        m 2fsd "But a surname alone won't make me a citizen of your Earth."
        m "It's only the first step in a long, long journey."
    else:
        m 1esc "It hit me earlier, if I were to magically get what I want, and just poof into your home..."
        m 2wuo "I won't be a citizen! I don't even have a last name!"
    m 2lkbsa "I mean, in most countries, I can become a citizen if we get married..."
    m 2ekc "But I won't have any documentation saying who I am or where I came from."
    m 2tkc "I won't even have my high school diploma!"
    m 3tkd "I wish there was more I could do right now to prep..."
    m 2wub "Like taking online classes or something."
    m 1lksdlc "I don't want to get there and be a burden because I can't find a job."
    m "Sorry, I guess I shouldn't worry so much about things I can't change."
    m 2eka "But I want to make you happy, so...I'm going to do everything I can to keep bettering myself while I'm stuck here!"
    m 1eka "Thank you for listening to me vent, [player]."
    return
