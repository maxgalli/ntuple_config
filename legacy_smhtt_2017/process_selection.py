from ntuple_processor.utils import Selection



"""Base processes

List of base processes, mostly containing only weights:
    - triggerweight
    - singlelepton_triggerweight
    - tau_by_iso_id_weight
    - ele_hlt_Z_vtx_weight
    - lumi_weight
    - DY_base_process_selection
    - TT_process_selection
    - VV_process_selection
    - W_process_selection
    - HTT_base_process_selection
    - HTT_process_selection
    - HWW_process_selection
"""


def triggerweight(channel):
    weight = ("1.0", "triggerweight")

    singleMC = "singleTriggerMCEfficiencyWeightKIT_1"
    crossMCL = "crossTriggerMCEfficiencyWeight_1"
    MCTau_1 = "((byTightDeepTau2017v2p1VSjet_1<0.5 && byVLooseDeepTau2017v2p1VSjet_1>0.5)*crossTriggerMCEfficiencyWeight_vloose_DeepTau_1 + (byTightDeepTau2017v2p1VSjet_1>0.5)*crossTriggerMCEfficiencyWeight_tight_DeepTau_1)"
    MCTau_2 = MCTau_1.replace("_1","_2")

    if "mt" in channel:
        trig_sL = "(trg_singlemuon_27 || trg_singlemuon_24)"
        trig_X = "(pt_1 > 21 && pt_1 < 25 && trg_crossmuon_mu20tau27)"

        MuTauMC = "*".join([trig_sL, singleMC]) + "+" + "*".join([trig_X, crossMCL, MCTau_2])
        MuTauData = MuTauMC.replace("MC","Data")
        MuTau = "("+MuTauData+")/("+MuTauMC+")"
        weight = (MuTau,"triggerweight")

    elif "et" in channel:
        trig_sL = "(trg_singleelectron_35 || trg_singleelectron_32 || trg_singleelectron_27)"
        trig_X = "(pt_1>25 && pt_1<28 && trg_crossele_ele24tau30)"

        ElTauMC = "*".join([trig_sL, singleMC]) + "+" + "*".join([trig_X, crossMCL, MCTau_2])
        ElTauData = ElTauMC.replace("MC","Data")
        ElTau = "("+ElTauData+")/("+ElTauMC+")"
        weight = (ElTau,"triggerweight")

    elif "tt" in channel:
        DiTauMC = "*".join([MCTau_1,MCTau_2])
        DiTauData = DiTauMC.replace("MC","Data")
        DiTau = "("+DiTauData+")/("+DiTauMC+")"
        weight = (DiTau,"triggerweight")

    elif "em" in channel:
        weight = (
            "(trigger_23_data_Weight_2*trigger_12_data_Weight_1*(trg_muonelectron_mu23ele12==1)+trigger_23_data_Weight_1*trigger_8_data_Weight_2*(trg_muonelectron_mu8ele23==1) - trigger_23_data_Weight_2*trigger_23_data_Weight_1*(trg_muonelectron_mu8ele23==1 && trg_muonelectron_mu23ele12==1))/(trigger_23_mc_Weight_2*trigger_12_mc_Weight_1*(trg_muonelectron_mu23ele12==1)+trigger_23_mc_Weight_1*trigger_8_mc_Weight_2*(trg_muonelectron_mu8ele23==1) - trigger_23_mc_Weight_2*trigger_23_mc_Weight_1*(trg_muonelectron_mu8ele23==1 && trg_muonelectron_mu23ele12==1))",
            "trigger_lepton_sf")

    elif "mm" in channel:
        weight = (
            "singleTriggerDataEfficiencyWeightKIT_1/singleTriggerMCEfficiencyWeightKIT_1",
            "trigger_lepton_sf")

    return weight


def singlelepton_triggerweight(channel):
    weight = ("1.0","triggerweight")

    MCTau_1 = "((byTightDeepTau2017v2p1VSjet_1<0.5 && byMediumDeepTau2017v2p1VSjet_1>0.5)*crossTriggerMCEfficiencyWeight_medium_DeepTau_1 + (byTightDeepTau2017v2p1VSjet_1>0.5)*crossTriggerMCEfficiencyWeight_tight_DeepTau_1)"
    MCTau_2 = MCTau_1.replace("_1","_2")

    if "mt" in channel or "et" in channel:
        weight = ("singleTriggerDataEfficiencyWeightKIT_1/singleTriggerMCEfficiencyWeightKIT_1","triggerweight")
    elif "tt" in channel:
        DiTauMC = "*".join([MCTau_1,MCTau_2])
        DiTauData = DiTauMC.replace("MC","Data")
        DiTau = "("+DiTauData+")/("+DiTauMC+")"
        weight = (DiTau,"triggerweight")

    return weight


def tau_by_iso_id_weight(channel):
    weight = ("1.0","taubyIsoIdWeight")
    if "mt" in channel or "et" in channel:
        weight = ("((gen_match_2 == 5)*tauIDScaleFactorWeight_tight_DeepTau2017v2p1VSjet_2 + (gen_match_2 != 5))", "taubyIsoIdWeight")
    elif "tt" in channel:
        dm11_nom = 0.64049393
        weight = ("(((gen_match_1 == 5)*(((decayMode_1!=11)*tauIDScaleFactorWeight_tight_DeepTau2017v2p1VSjet_1)+((decayMode_1==11)*{dm11_nom})) + (gen_match_1 != 5))*((gen_match_2 == 5)*(((decayMode_2!=11)*tauIDScaleFactorWeight_tight_DeepTau2017v2p1VSjet_2)+((decayMode_2==11)*{dm11_nom})) + (gen_match_2 != 5)))".format(dm11_nom=dm11_nom), "taubyIsoIdWeight")
    return weight


def ele_hlt_Z_vtx_weight(channel):
    weight = ("1.0","eleHLTZvtxWeight")
    if "et" in channel:
        weight = ("(trg_singleelectron_35 || trg_singleelectron_32 || trg_singleelectron_27 || trg_crossele_ele24tau30)*0.991 + (!(trg_singleelectron_35 || trg_singleelectron_32 || trg_singleelectron_27 || trg_crossele_ele24tau30))*1.0", "eleHLTZvtxWeight")
    return weight


lumi_weight = ("41.529 * 1000.0", "lumi")


def DY_base_process_selection(channel):
    return Selection(
            name = "DY_base",
            weights = [
                ("generatorWeight", "generatorWeight"),
                ("puweight", "puweight"),
                ("idWeight_1*idWeight_2","idweight"),
                ("isoWeight_1*isoWeight_2","isoweight"),
                ("trackWeight_1*trackWeight_2","trackweight"),
                triggerweight(channel),
                ("eleTauFakeRateWeight*muTauFakeRateWeight", "leptonTauFakeRateWeight"),
                ("(gen_match_2==1 || gen_match_2==3)*(((abs(eta_1) < 1.46) * 0.88) + ((abs(eta_1) > 1.5588) * 0.51))+!(gen_match_2==1 || gen_match_2==3)", "eletauFakeRateWeightFix"),
                tau_by_iso_id_weight(channel),
                ele_hlt_Z_vtx_weight(channel),
                ("zPtReweightWeight", "zPtReweightWeight"),
                ("prefiringweight", "prefireWeight"),
                lumi_weight
                ]
            )


def TT_process_selection(channel):
    return Selection(
    name = "TT",
    weights = [
        ("generatorWeight", "generatorWeight"),
        ("numberGeneratedEventsWeight", "numberGeneratedEventsWeight"),
        ("crossSectionPerEventWeight", "crossSectionPerEventWeight"),
        ("puweight", "puweight"),
        ("idWeight_1*idWeight_2","idweight"),
        ("isoWeight_1*isoWeight_2","isoweight"),
        ("trackWeight_1*trackWeight_2","trackweight"),
        ("topPtReweightWeight", "topPtReweightWeight"),
        triggerweight(channel),
        ("eleTauFakeRateWeight*muTauFakeRateWeight", "leptonTauFakeRateWeight"),
        tau_by_iso_id_weight(channel),
        ele_hlt_Z_vtx_weight(channel),
        ("prefiringweight", "prefireWeight"),
        lumi_weight
        ]
    )


def VV_process_selection(channel):
    return Selection(
    name = "VV",
    weights = [
        ("generatorWeight", "generatorWeight"),
        ("numberGeneratedEventsWeight", "numberGeneratedEventsWeight"),
        ("puweight", "puweight"),
        ("idWeight_1*idWeight_2","idweight"),
        ("isoWeight_1*isoWeight_2","isoweight"),
        ("trackWeight_1*trackWeight_2","trackweight"),
        triggerweight(channel),
        ("eleTauFakeRateWeight*muTauFakeRateWeight", "leptonTauFakeRateWeight"),
        tau_by_iso_id_weight(channel),
        ele_hlt_Z_vtx_weight(channel),
        ("crossSectionPerEventWeight", "crossSectionPerEventWeight"),
        ("prefiringweight", "prefireWeight"),
        lumi_weight
        ]
    )


def W_process_selection(channel):
    return Selection(
    name = "W",
    weights = [
        ("generatorWeight", "generatorWeight"),
        ("((0.000824363*((npartons <= 0 || npartons >= 5)*1.0 + (npartons == 1)*0.1713 + (npartons == 2)*0.1062 + (npartons == 3)*0.0652 + (npartons == 4)*0.0645)) * (genbosonmass>=0.0) + numberGeneratedEventsWeight * crossSectionPerEventWeight * (genbosonmass<0.0))", "wj_stitching_weight"),
        ("puweight", "puweight"),
        ("idWeight_1*idWeight_2","idweight"),
        ("isoWeight_1*isoWeight_2","isoweight"),
        ("trackWeight_1*trackWeight_2","trackweight"),
        triggerweight(channel),
        ("eleTauFakeRateWeight*muTauFakeRateWeight", "leptonTauFakeRateWeight"),
        tau_by_iso_id_weight(channel),
        ele_hlt_Z_vtx_weight(channel),
        ("prefiringweight", "prefireWeight"),
        lumi_weight
        ]
    )


def HTT_base_process_selection(channel):
    return Selection(
    name = "HTT_base",
    weights = [
        ("generatorWeight", "generatorWeight"),
        ("puweight", "puweight"),
        ("idWeight_1*idWeight_2","idweight"),
        ("isoWeight_1*isoWeight_2","isoweight"),
        ("trackWeight_1*trackWeight_2","trackweight"),
        triggerweight(channel),
        ("eleTauFakeRateWeight*muTauFakeRateWeight", "leptonTauFakeRateWeight"),
        tau_by_iso_id_weight(channel),
        ele_hlt_Z_vtx_weight(channel),
        ("prefiringweight", "prefireWeight"),
        lumi_weight
        ]
    )


def HTT_process_selection(channel):
    HTT_weights = HTT_base_process_selection(channel).weights + [
        ("numberGeneratedEventsWeight", "numberGeneratedEventsWeight")
        ("crossSectionPerEventWeight", "crossSectionPerEventWeight"),
        ]
    return Selection(name = "HTT", weights = HTT_weights)


def HWW_process_selection(channel):
    return Selection(
    name = "HWW",
    weights = [
        ("generatorWeight", "generatorWeight"),
        ("numberGeneratedEventsWeight", "numberGeneratedEventsWeight"),
        ("0.0857883*(abs(numberGeneratedEventsWeight - 2e-06) < 1e-07) + 1.1019558*(abs(numberGeneratedEventsWeight - 2e-06) >= 1e-07)", "crossSectionPerEventWeight"),
        ("puweight", "puweight"),
        ("idWeight_1*idWeight_2","idweight"),
        ("isoWeight_1*isoWeight_2","isoweight"),
        ("trackWeight_1*trackWeight_2","trackweight"),
        triggerweight(channel),
        ("eleTauFakeRateWeight*muTauFakeRateWeight", "leptonTauFakeRateWeight"),
        tau_by_iso_id_weight(channel),
        ele_hlt_Z_vtx_weight(channel),
        ("prefiringweight", "prefireWeight"),
        lumi_weight
        ]
    )



"""Built-on-top processes

List of other processes meant to be put on top of base processes:
    - DY_process_selection
    - DY_nlo_process_selection
    - ZTT_process_selection
    - ZTT_nlo_process_selection
    - ZTT_embedded_process_selection
    - ZL_process_selection
    - ZL_nlo_process_selection
    - ZJ_process_selection
    - ZJ_nlo_process_selection
    - TTT_process_selection
    - TTL_process_selection
    - TTJ_process_selection
    - VVT_process_selection
    - VVJ_process_selection
    - VVL_process_selection
    - VH_process_selection
    - WH_process_selection
    - ZH_process_selection
    - ttH_process_selection
    - ggH125_process_selection
    - qqH125_process_selection
"""


def DY_process_selection(channel):
    DY_process_weights = DY_base_process_selection(channel).weights
    DY_process_weights.append((
        "((genbosonmass >= 50.0)*6.2139e-05*((npartons == 0 || npartons >= 5)*1.0 + (npartons == 1)*0.1743 + (npartons == 2)*0.3556 + (npartons == 3)*0.2273 + (npartons == 4)*0.2104) + (genbosonmass < 50.0)*numberGeneratedEventsWeight*crossSectionPerEventWeight)","z_stitching_weight"))
    return Selection(name = "DY",
                     weights = DY_process_weights)


def DY_nlo_process_selection(channel):
    DY_nlo_process_weights = DY_base_process_selection(channel).weights
    DY_nlo_process_weights.append((
        "((genbosonmass >= 50.0) * 2.8982e-05 + (genbosonmass < 50.0)*numberGeneratedEventsWeight*crossSectionPerEventWeight)","z_stitching_weight"))
    return Selection(name = "DY_nlo",
                     weights = DY_nlo_process_weights)


def ZTT_process_selection(channel):
    tt_cut = __get_ZTT_cut(channel)
    return Selection(name = "ZTT",
                     cuts = [(tt_cut, "ztt_cut")])

def ZTT_nlo_process_selection(channel):
    tt_cut = __get_ZTT_cut(channel)
    return Selection(name = "ZTT_nlo",
                     cuts = [(tt_cut, "ztt_cut")])

def __get_ZTT_cut(channel):
    if "mt" in channel:
        return "gen_match_1==4 && gen_match_2==5"
    elif "et" in channel:
        return "gen_match_1==3 && gen_match_2==5"
    elif "tt" in channel:
        return "gen_match_1==5 && gen_match_2==5"
    elif "em" in channel:
        return "gen_match_1==3 && gen_match_2==4"
    elif "mm" in channel:
        return "gen_match_1==4 && gen_match_2==4"


def ZTT_embedded_process_selection(channel):
    if "mt" in channel:
        ztt_embedded_weights = [
            ("generatorWeight", "simulation_sf"),
            ("muonEffTrgWeight*muonEffIDWeight_1*muonEffIDWeight_2", "scale_factor"),
            ("idWeight_1*(trigger_24_27_Weight_1*(pt_1>25)+((0.81*(pt_1>=21 && pt_1<22) + 0.82*(pt_1>=22 && pt_1<23) + 0.83*(pt_1>=23))*(pt_1<25)))*isoWeight_1", "lepton_sf"),
            ("(pt_1>25)+(pt_1 >= 21 && pt_1<25)*((pt_2>=20 && pt_2<25)*0.12714+(pt_2>=25 && pt_2<30)*0.46930+0.71983*(pt_2>=30 && pt_2<35) + 0.75209*(pt_2>=35 && pt_2<40) + 0.78164*(pt_2>=40 && pt_2<45) + 0.83241*(pt_2>=45 && pt_2<50) + 0.86694*(pt_2>=50 && pt_2<60) + 0.89966*(pt_2>=60 && pt_2<80) + 0.88534*(pt_2>=80 && pt_2<100) + 0.90095*(pt_2>=100 && pt_2<150) + 0.84402*(pt_2>=150 && pt_2<200) + (pt_2>=200))","tau_leg_weight"),
            ("(gen_match_2==5)*0.97+(gen_match_2!=5)", "emb_tau_id"),
            ("gen_match_1==4 && gen_match_2==5","emb_veto"),
            ("embeddedDecayModeWeight", "decayMode_SF")
            ]
    elif "et" in channel:
        ztt_embedded_weights = [
            ("generatorWeight", "simulation_sf"),
            ("muonEffTrgWeight*muonEffIDWeight_1*muonEffIDWeight_2", "scale_factor"),
            ("(pt_1>28)+(pt_1<28)*(crossTriggerDataEfficiencyWeight_tight_MVAv2_2*(abs(eta_1)>=1.5)+((1.29079*(pt_2>=30 && pt_2<35) + 1.06504*(pt_2>=35 && pt_2<40) + 0.93972*(pt_2>=40 && pt_2<45) + 0.91923*(pt_2>=45 && pt_2<50) + 0.89598*(pt_2>=50 && pt_2<60) + 0.90597*(pt_2>=60 && pt_2<80) + 0.88761*(pt_2>=80 && pt_2<100) + 0.90210*(pt_2>=100 && pt_2<150) + 0.84939*(pt_2>=150 && pt_2<200) + (pt_2>=200))*(abs(eta_1)<1.5)))","tau_leg_weight"),
            ("(pt_1>28)+(pt_1<28)*(crossTriggerDataEfficiencyWeight_1*(abs(eta_1)>=1.5)+((0.39*(pt_1>=25 && pt_1<26) + 0.46*(pt_1>=26 && pt_1<27) + 0.48*(pt_1>=27 && pt_1<28))*(abs(eta_1)<1.5)))","lepton_leg_weight"),
            ("idWeight_1*((pt_1>28)*(trigger_27_32_35_Weight_1*(abs(eta_1) < 1.5) + singleTriggerDataEfficiencyWeightKIT_1*(abs(eta_1)>=1.5))+(pt_1<28))*isoWeight_1", "lepton_sf"),
            ("(gen_match_2==5)*0.97+(gen_match_2!=5)", "emb_tau_id"),
            ("gen_match_1==3 && gen_match_2==5","emb_veto"),
            ("embeddedDecayModeWeight", "decayMode_SF")
            ]
    elif "tt" in channel:
        ztt_embedded_weights = [
            ("generatorWeight", "simulation_sf"),
            ("muonEffTrgWeight*muonEffIDWeight_1*muonEffIDWeight_2", "scale_factor"),
            ("(0.18321*(pt_1>=30 && pt_1<35) + 0.53906*(pt_1>=35 && pt_1<40) + 0.63658*(pt_1>=40 && pt_1<45) + 0.73152*(pt_1>=45 && pt_1<50) + 0.79002*(pt_1>=50 && pt_1<60) + 0.84666*(pt_1>=60 && pt_1<80) + 0.84919*(pt_1>=80 && pt_1<100) + 0.86819*(pt_1>=100 && pt_1<150) + 0.88206*(pt_1>=150 && pt_1<200) + (pt_1>=200))","tau1_leg_weight"),
            ("(0.18321*(pt_2>=30 && pt_2<35) + 0.53906*(pt_2>=35 && pt_2<40) + 0.63658*(pt_2>=40 && pt_2<45) + 0.73152*(pt_2>=45 && pt_2<50) + 0.79002*(pt_2>=50 && pt_2<60) + 0.84666*(pt_2>=60 && pt_2<80) + 0.84919*(pt_2>=80 && pt_2<100) + 0.86819*(pt_2>=100 && pt_2<150) + 0.88206*(pt_2>=150 && pt_2<200) + (pt_2>=200))","tau2_leg_weight"),
            ("((gen_match_1==5)*0.97+(gen_match_1!=5))*((gen_match_2==5)*0.97+(gen_match_2!=5))", "emb_tau_id"),
            ("gen_match_1==5 && gen_match_2==5","emb_veto"),
            ("embeddedDecayModeWeight", "decayMode_SF")
            ]
    elif "em" in channel:
        ztt_embedded_weights = [
            ("1.043*generatorWeight", "simulation_sf"),
            ("(gen_match_1==3 && gen_match_2==4)", "emb_gen_match"),
            ("muonEffTrgWeight*muonEffIDWeight_1*muonEffIDWeight_2", "scale_factor"),
            ("0.99*trackWeight_1*trackWeight_2*idWeight_1*isoWeight_1*idWeight_2*looseIsoWeight_2", "idiso_lepton_sf"),
            ("(trigger_23_data_Weight_2*trigger_12_data_Weight_1*(trg_muonelectron_mu23ele12==1)+trigger_23_data_Weight_1*trigger_8_data_Weight_2*(trg_muonelectron_mu8ele23==1) - trigger_23_data_Weight_2*trigger_23_data_Weight_1*(trg_muonelectron_mu8ele23==1 && trg_muonelectron_mu23ele12==1))/(trigger_23_embed_Weight_2*trigger_12_embed_Weight_1*(trg_muonelectron_mu23ele12==1)+trigger_23_embed_Weight_1*trigger_8_embed_Weight_2*(trg_muonelectron_mu8ele23==1) - trigger_23_embed_Weight_2*trigger_23_embed_Weight_1*(trg_muonelectron_mu8ele23==1 && trg_muonelectron_mu23ele12==1))", "trigger_lepton_sf")
            ]

    ztt_embedded_cuts = [("((gen_match_1>2 && gen_match_1<6) && (gen_match_2>2 && gen_match_2<6))", "dy_genuine_tau")]

    return Selection(name = "Embedded",
                     cuts = ztt_embedded_cuts,
                     weights = ztt_embedded_weights)


def ZL_process_selection(channel):
    veto = __get_ZL_cut(channel)
    return Selection(name = "ZL",
                     cuts = [("{} && {}".format(*veto), "dy_emb_and_ff_veto")])

def ZL_nlo_process_selection(channel):
    veto = __get_ZL_cut(channel)
    return Selection(name = "ZL_nlo",
                     cuts = [("{} && {}".format(*veto), "dy_emb_and_ff_veto")])

def __get_ZL_cut(channel):
    if "mt" in channel:
        emb_veto = "!(gen_match_1==4 && gen_match_2==5)"
        ff_veto = "!(gen_match_2 == 6)"
    elif "et" in channel:
        emb_veto = "!(gen_match_1==3 && gen_match_2==5)"
        ff_veto = "!(gen_match_2 == 6)"
    elif "tt" in channel:
        emb_veto = "!(gen_match_1==5 && gen_match_2==5)"
        ff_veto = "!(gen_match_1 == 6 || gen_match_2 == 6)"
    elif "em" in channel:
        emb_veto = "!(gen_match_1==3 && gen_match_2==4)"
        ff_veto = "(1.0)"
    elif "mm" in channel:
        emb_veto = "!(gen_match_1==4 && gen_match_2==4)"
        ff_veto = "(1.0)"
    return (emb_veto, ff_veto)


def ZJ_process_selection(channel):
    veto = __get_ZJ_cut(channel)
    return Selection(name = "ZJ",
                     cuts = [(__get_ZJ_cut(channel), 'dy_fakes')])

def ZJ_nlo_process_selection(channel):
    veto = __get_ZJ_cut(channel)
    return Selection(name = "ZJ_nlo",
                     cuts = [(__get_ZJ_cut(channel), 'dy_fakes')])

def __get_ZJ_cut(channel):
    if "mt" in channel or "et" in channel:
        return "gen_match_2 == 6"
    elif "tt" in channel:
        return "(gen_match_1 == 6 || gen_match_2 == 6)"
    elif "em" in channel:
        return "0 == 1"
    else:
        return ""


def TTT_process_selection(channel):
    if "mt" in channel:
        tt_cut = "gen_match_1==4 && gen_match_2==5"
    elif "et" in channel:
        tt_cut = "gen_match_1==3 && gen_match_2==5"
    elif "tt" in channel:
        tt_cut = "gen_match_1==5 && gen_match_2==5"
    elif "em" in channel:
        tt_cut = "gen_match_1==3 && gen_match_2==4"
    elif "mm" in channel:
        tt_cut = "gen_match_1==4 && gen_match_2==4"
    return Selection(name = "TTT",
                     cuts = [(tt_cut, "ttt_cut")])


def TTL_process_selection(channel):
    if "mt" in channel:
        emb_veto = "!(gen_match_1==4 && gen_match_2==5)"
        ff_veto = "!(gen_match_2 == 6)"
    elif "et" in channel:
        emb_veto = "!(gen_match_1==3 && gen_match_2==5)"
        ff_veto = "!(gen_match_2 == 6)"
    elif "tt" in channel:
        emb_veto = "!(gen_match_1==5 && gen_match_2==5)"
        ff_veto = "!(gen_match_1 == 6 || gen_match_2 == 6)"
    elif "em" in channel:
        emb_veto = "!(gen_match_1==3 && gen_match_2==4)"
        ff_veto = "(1.0)"
    elif "mm" in channel:
        emb_veto = "!(gen_match_1==4 && gen_match_2==4)"
        ff_veto = "(1.0)"
    return Selection(name = "TTL",
                     cuts = [("{} && {}".format(emb_veto,ff_veto), "tt_emb_and_ff_veto")])


def TTJ_process_selection(channel):
    ct = ""
    if "mt" in channel or "et" in channel:
        ct = "(gen_match_2 == 6 && gen_match_2 == 6)"
    elif "tt" in channel:
        ct = "(gen_match_1 == 6 || gen_match_2 == 6)"
    elif "em" in channel:
        ct = "0 == 1"
    return Selection(name = "TTJ",
                     cuts = [(ct, "tt_fakes")])


def VVT_process_selection(channel):
    if "mt" in channel:
        tt_cut = "gen_match_1==4 && gen_match_2==5"
    elif "et" in channel:
        tt_cut = "gen_match_1==3 && gen_match_2==5"
    elif "tt" in channel:
        tt_cut = "gen_match_1==5 && gen_match_2==5"
    elif "em" in channel:
        tt_cut = "gen_match_1==3 && gen_match_2==4"
    elif "mm" in channel:
        tt_cut = "gen_match_1==4 && gen_match_2==4"
    return Selection(name = "VVT",
                     cuts = [(tt_cut, "vvt_cut")])


def VVJ_process_selection(channel):
    ct = ""
    if "mt" in channel or "et" in channel:
        ct = "(gen_match_2 == 6 && gen_match_2 == 6)"
    elif "tt" in channel:
        ct = "(gen_match_1 == 6 || gen_match_2 == 6)"
    elif "em" in channel:
        ct = "0.0 == 1.0"
    return Selection(name = "VVJ",
                     cuts = [(ct, "vv_fakes")])


def VVL_process_selection(channel):
    if "mt" in channel:
        emb_veto = "!(gen_match_1==4 && gen_match_2==5)"
        ff_veto = "!(gen_match_2 == 6)"
    elif "et" in channel:
        emb_veto = "!(gen_match_1==3 && gen_match_2==5)"
        ff_veto = "!(gen_match_2 == 6)"
    elif "tt" in channel:
        emb_veto = "!(gen_match_1==5 && gen_match_2==5)"
        ff_veto = "!(gen_match_1 == 6 || gen_match_2 == 6)"
    elif "em" in channel:
        emb_veto = "!(gen_match_1==3 && gen_match_2==4)"
        ff_veto = "(1.0)"
    elif "mm" in channel:
        emb_veto = "!(gen_match_1==4 && gen_match_2==4)"
        ff_veto = "(1.0)"
    return Selection(name = "VVL",
                     cuts = [("{} && {}".format(emb_veto,ff_veto), "tt_emb_and_ff_veto")])


def VH_process_selection(channel):
    return Selection(name = "VH",
                     cuts = [("(htxs_stage1p1cat>=300)&&(htxs_stage1p1cat<=505)", "htxs_match")])


def WH_process_selection(channel):
    return Selection(name = "WH",
                     cuts = [("(htxs_stage1p1cat>=300)&&(htxs_stage1p1cat<=305)", "htxs_match")])


def ZH_process_selection(channel):
    return Selection(name = "ZH",
                     cuts = [("(htxs_stage1p1cat>=400)&&(htxs_stage1p1cat<=405)", "htxs_match")])


def ttH_process_selection(channel):
    return Selection(name = "ttH",
                     weights = HTT_process_selection(channel).weights)


def ggH125_process_selection(channel):
    ggH125_weights = [
        ("ggh_NNLO_weight", "gghNNLO"),
        ("1.01", "bbh_inclusion_weight"),
        ("((htxs_stage1p1cat==100||htxs_stage1p1cat==102||htxs_stage1p1cat==103)*crossSectionPerEventWeight*8.210e-8+"
            "(htxs_stage1p1cat==101)*2.17e-8+"
            "(htxs_stage1p1cat==104||htxs_stage1p1cat==105)*4.39e-8+"
            "(htxs_stage1p1cat==106)*1.19e-8+"
            "(htxs_stage1p1cat>=107&&htxs_stage1p1cat<=109)*4.91e-8+"
            "(htxs_stage1p1cat>=110&&htxs_stage1p1cat<=113)*7.90e-9"
            ")","ggh_stitching_weight")
        ]
    ggH125_cuts = [("(htxs_stage1p1cat>=100)&&(htxs_stage1p1cat<=113)", "htxs")]
    return Selection(name = "ggH125", weights = ggH125_weights, cuts = ggH125_cuts)


def qqH125_process_selection(channel):
    qqH125_weights = [
        ("(((htxs_stage1p1cat>=200&&htxs_stage1p1cat<=202)||abs(crossSectionPerEventWeight-0.05544)<0.001||abs(crossSectionPerEventWeight-0.052685)<0.001||abs(crossSectionPerEventWeight-0.03342)<0.001)*crossSectionPerEventWeight*numberGeneratedEventsWeight+(abs(crossSectionPerEventWeight-0.05544)>=0.001&&abs(crossSectionPerEventWeight-0.052685)>=0.001&&abs(crossSectionPerEventWeight-0.03342)>=0.001)*("
            "(htxs_stage1p1cat>=203&&htxs_stage1p1cat<=205)*8.70e-9+"
            "(htxs_stage1p1cat==206)*8.61e-9+"
            "(htxs_stage1p1cat>=207&&htxs_stage1p1cat<=210)*1.79e-8"
            "))","qqh_stitching_weight")
        ]
    qqH125_cuts = [("(htxs_stage1p1cat>=200)&&(htxs_stage1p1cat<=210)", "qqH125")]
    return Selection(name = "qqH125", weights = qqH125_weights, cuts = qqH125_cuts)
