from ntuple_processor.utils import Cut
from ntuple_processor.utils import Weight

from ntuple_processor.variations import ChangeDataset
from ntuple_processor.variations import ReplaceCut
from ntuple_processor.variations import ReplaceWeight
from ntuple_processor.variations import RemoveCut
from ntuple_processor.variations import RemoveWeight
from ntuple_processor.variations import AddCut
from ntuple_processor.variations import AddWeight
from ntuple_processor.variations import SquareWeight

same_sign = ReplaceCut("same_sign", "os", Cut("q_1*q_2>0", "ss"))

prefiring_variations = [
    ReplaceWeight("CMS_prefiring_Run2017Up", "prefireWeight", Weight("prefiringweightup", "prefireWeight")),
    ReplaceWeight("CMS_prefiring_Run2017Down", "prefireWeight", Weight("prefiringweightdown", "prefireWeight")),
]

mc_tau_es_3prong_variations = [
        ChangeDataset("CMS_scale_mc_t_3prong_Run2017Up", "tauEsThreeProngUp"),
        ChangeDataset("CMS_scale_mc_t_3prong_Run2017Down", "tauEsThreeProngDown")
        ]

mc_tau_es_1prong_variations = [
        ChangeDataset("CMS_scale_mc_t_1prong_Run2017Up", "tauEsOneProngUp"),
        ChangeDataset("CMS_scale_mc_t_1prong_Run2017Down", "tauEsOneProngDown")
        ]

mc_tau_es_1prong1pizero_variations = [
        ChangeDataset("CMS_scale_mc_t_1prong1pizero_Run2017Up", "tauEsOneProngOnePiZeroUp"),
        ChangeDataset("CMS_scale_mc_t_1prong1pizero_Run2017Down", "tauEsOneProngOnePiZeroDown")
        ]

tau_es_3prong_variations = [
        ChangeDataset("CMS_scale_t_3prong_Run2017Up", "tauEsThreeProngUp"),
        ChangeDataset("CMS_scale_t_3prong_Run2017Down", "tauEsThreeProngDown")
        ]

tau_es_1prong_variations = [
        ChangeDataset("CMS_scale_t_1prong_Run2017Up", "tauEsOneProngUp"),
        ChangeDataset("CMS_scale_t_1prong_Run2017Down", "tauEsOneProngDown")
        ]

tau_es_1prong1pizero_variations = [
        ChangeDataset("CMS_scale_t_1prong1pizero_Run2017Up", "tauEsOneProngOnePiZeroUp"),
        ChangeDataset("CMS_scale_t_1prong1pizero_Run2017Down", "tauEsOneProngOnePiZeroDown")
        ]

ele_es_variations = [
        ChangeDataset("CMS_scale_mc_eUp", "eleScaleUp"),
        ChangeDataset("CMS_scale_mc_eDown", "eleScaleDown")
        ]

ele_es_variations = [
        ChangeDataset("CMS_reso_mc_eUp", "eleSmearUp"),
        ChangeDataset("CMS_reso_mc_eDown", "eleSmearDown")
        ]

jet_es_variations = [
        ChangeDataset("CMS_scale_j_eta0to3_Run2017Up", "jecUncEta0to3Up"),
        ChangeDataset("CMS_scale_j_eta0to3_Run2017Down", "jecUncEta0to3Down"),
        ChangeDataset("CMS_scale_j_eta0to5_Run2017Up", "jecUncEta0to5Up"),
        ChangeDataset("CMS_scale_j_eta0to5_Run2017Down", "jecUncEta0to5Down"),
        ChangeDataset("CMS_scale_j_eta3to5_Run2017Up", "jecUncEta3to5Up"),
        ChangeDataset("CMS_scale_j_eta3to5_Run2017Down", "jecUncEta3to5Down"),
        ChangeDataset("CMS_scale_j_RelativeBal_Run2017Up", "jecUncRelativeBalUp"),
        ChangeDataset("CMS_scale_j_RelativeBal_Run2017Down", "jecUncRelativeBalDown"),
        ChangeDataset("CMS_scale_j_RelativeSample_Run2017Up", "jecUncRelativeSampleUp"),
        ChangeDataset("CMS_scale_j_RelativeSample_Run2017Down", "jecUncRelativeSampleDown")
        ]

met_unclustered_variations = [
        ChangeDataset("CMS_scale_met_unclusteredUp", "metUnclusteredEnUp"),
        ChangeDataset("CMS_scale_met_unclusteredDown", "metUnclusteredEnDown")
        ]

recoil_resolution_variations = [
        ChangeDataset("CMS_htt_boson_reso_met_Run2017Up", "metRecoilResolutionUp"),
        ChangeDataset("CMS_htt_boson_reso_met_Run2017Down", "metRecoilResolutionDown")
        ]

recoil_response_variations = [
        ChangeDataset("CMS_htt_boson_scale_met_Run2017Up", "metRecoilResponseUp"),
        ChangeDataset("CMS_htt_boson_scale_met_Run2017Down", "metRecoilResponseDown")
        ]

jet_to_tau_fake_variations = [
        AddWeight("CMS_htt_jetToTauFake_Run2017Up", Weight("max(1.0-pt_2*0.002, 0.6)", "jetToTauFake_weight")),
        AddWeight("CMS_htt_jetToTauFake_Run2017Down", Weight("min(1.0+pt_2*0.002, 1.4)", "jetToTauFake_weight"))
        ]

ele_fake_es_1prong_variations = [
        ChangeDataset("CMS_ZLShape_et_1prong_Run2017Up", "tauEleFakeEsOneProngUp"),
        ChangeDataset("CMS_ZLShape_et_1prong_Run2017Down", "tauEleFakeEsOneProngDown")
        ]

ele_fake_es_1prong1pizero_variations = [
        ChangeDataset("CMS_ZLShape_et_1prong1pizero_Run2017Up", "tauEleFakeEsOneProngPiZerosUp"),
        ChangeDataset("CMS_ZLShape_et_1prong1pizero_Run2017Down", "tauEleFakeEsOneProngPiZerosDown")
        ]

mu_fake_es_1prong_variations = [
        ChangeDataset("CMS_ZLShape_mt_1prong_Run2017Up", "tauMuFakeEsOneProngUp"),
        ChangeDataset("CMS_ZLShape_mt_1prong_Run2017Down", "tauMuFakeEsOneProngDown")
        ]

mu_fake_es_1prong1pizero_variations = [
        ChangeDataset("CMS_ZLShape_mt_1prong1pizero_Run2017Up", "tauMuFakeEsOneProngPiZerosUp"),
        ChangeDataset("CMS_ZLShape_mt_1prong1pizero_Run2017Down", "tauMuFakeEsOneProngPiZerosDown")
        ]

lep_trigger_eff_variations_mt = [
        AddWeight("CMS_eff_trigger_mt_Run2017Up", Weight("(1.0*(pt_1<=25)+1.02*(pt_1>25))", "trg_mt_eff_weight")),
        AddWeight("CMS_eff_trigger_mt_Run2017Down", Weight("(1.0*(pt_1<=25)+0.98*(pt_1>25))", "trg_mt_eff_weight")),
        AddWeight("CMS_eff_xtrigger_mt_Run2017Up", Weight("(1.054*(pt_1<=25)+1.0*(pt_1>25))", "xtrg_mt_eff_weight")),
        AddWeight("CMS_eff_xtrigger_mt_Run2017Down", Weight("(0.946*(pt_1<=25)+1.0*(pt_1>25))", "xtrg_mt_eff_weight"))
        ]

lep_trigger_eff_variations_mt_emb = [
        AddWeight("CMS_eff_trigger_emb_mt_Run2017Up", Weight("(1.0*(pt_1<=25)+1.02*(pt_1>25))", "trg_mt_eff_weight")),
        AddWeight("CMS_eff_trigger_emb_mt_Run2017Down", Weight("(1.0*(pt_1<=25)+0.98*(pt_1>25))", "trg_mt_eff_weight")),
        AddWeight("CMS_eff_xtrigger_emb_mt_Run2017Up", Weight("(1.054*(pt_1<=25)+1.0*(pt_1>25))", "xtrg_mt_eff_weight")),
        AddWeight("CMS_eff_xtrigger_emb_mt_Run2017Down", Weight("(0.946*(pt_1<=25)+1.0*(pt_1>25))", "xtrg_mt_eff_weight"))
        ]

lep_trigger_eff_variations_et = [
        AddWeight("CMS_eff_trigger_et_Run2017Up", Weight("(1.0*(pt_1<=28)+1.02*(pt_1>28))", "trg_et_eff_weight")),
        AddWeight("CMS_eff_trigger_et_Run2017Down", Weight("(1.0*(pt_1<=28)+0.98*(pt_1>28))", "trg_et_eff_weight")),
        AddWeight("CMS_eff_xtrigger_et_Run2017Up", Weight("(1.054*(pt_1<=28)+1.0*(pt_1>28))", "xtrg_et_eff_weight")),
        AddWeight("CMS_eff_xtrigger_et_Run2017Down", Weight("(0.946*(pt_1<=28)+1.0*(pt_1>28))", "xtrg_et_eff_weight"))
        ]

lep_trigger_eff_variations_et_emb = [
        AddWeight("CMS_eff_trigger_emb_et_Run2017Up", Weight("(1.0*(pt_1<=28)+1.02*(pt_1>28))", "trg_et_eff_weight")),
        AddWeight("CMS_eff_trigger_emb_et_Run2017Down", Weight("(1.0*(pt_1<=28)+0.98*(pt_1>28))", "trg_et_eff_weight")),
        AddWeight("CMS_eff_xtrigger_emb_et_Run2017Up", Weight("(1.054*(pt_1<=28)+1.0*(pt_1>28))", "xtrg_et_eff_weight")),
        AddWeight("CMS_eff_xtrigger_emb_et_Run2017Down", Weight("(0.946*(pt_1<=28)+1.0*(pt_1>28))", "xtrg_et_eff_weight"))
        ]

btag_eff_variations = [
        ChangeDataset("CMS_htt_eff_b_Run2017Up", "btagEffUp"),
        ChangeDataset("CMS_htt_eff_b_Run2017Down", "btagEffDown")
        ]

mistag_eff_variations = [
        ChangeDataset("CMS_htt_mistag_b_Run2017Up", "btagMistagUp"),
        ChangeDataset("CMS_htt_mistag_b_Run2017Down", "btagMistagDown")
        ]

emb_tau_es_3prong_variations = [
        ChangeDataset("CMS_scale_emb_t_3prong_Run2017Up", "tauEsThreeProngUp"),
        ChangeDataset("CMS_scale_emb_t_3prong_Run2017Down", "tauEsThreeProngDown")
        ]

emb_tau_es_1prong_variations = [
        ChangeDataset("CMS_scale_emb_t_1prong_Run2017Up", "tauEsOneProngUp"),
        ChangeDataset("CMS_scale_emb_t_1prong_Run2017Down", "tauEsOneProngDown")
        ]

emb_tau_es_1prong1pizero_variations = [
        ChangeDataset("CMS_scale_emb_t_1prong1pizero_Run2017Up", "tauEsOneProngOnePiZeroUp"),
        ChangeDataset("CMS_scale_emb_t_1prong1pizero_Run2017Down", "tauEsOneProngOnePiZeroDown")
        ]

ggh_variations = []
for unc in [
        "THU_ggH_Mig01", "THU_ggH_Mig12", "THU_ggH_Mu", "THU_ggH_PT120",
        "THU_ggH_PT60", "THU_ggH_Res", "THU_ggH_VBF2j", "THU_ggH_VBF3j",
        "THU_ggH_qmtop"]:
    ggh_variations.append(AddWeight(unc + "Up", Weight("({})".format(unc), "{}_weight".format(unc))))
    ggh_variations.append(AddWeight(unc + "Down", Weight("(1.0/{})".format(unc), "{}_weight".format(unc))))

zpt_variations = [
        SquareWeight("CMS_htt_dyShape_Run2017Up", "zPtReweightWeight"),
        RemoveWeight("CMS_htt_dyShape_Run2017Down", "zPtReweightWeight")
        ]

top_pt_variations = [
        SquareWeight("CMS_htt_ttbarShapeUp", "topPtReweightWeight"),
        RemoveWeight("CMS_htt_ttbarShapeDown", "topPtReweightWeight")
        ]

