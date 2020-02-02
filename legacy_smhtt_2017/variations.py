from ntuple_processor.utils import Cut
from ntuple_processor.utils import Weight

from ntuple_processor.variations import ChangeDataset
from ntuple_processor.variations import ReplaceCut
from ntuple_processor.variations import ReplaceWeight
from ntuple_processor.variations import RemoveCut
from ntuple_processor.variations import RemoveWeight
from ntuple_processor.variations import AddCut
from ntuple_processor.variations import AddWeight

same_sign = ReplaceCut("same_sign", "os", Cut("q_1*q_2>0", "ss"))

prefiring_variations = [
    ReplaceWeight("CMS_prefiring_Run2017Up", "prefireWeight", Weight("prefiringweightup", "prefireWeight")),
    ReplaceWeight("CMS_prefiring_Run2017Down", "prefireWeight", Weight("prefiringweightdown", "prefireWeight")),
]

mc_tau_es_3prong_variations = ChangeDataset("CMS_scale_mc_t_3prong_Run2017", "tauEsThreeProng")

mc_tau_es_1prong_variations = ChangeDataset("CMS_scale_mc_t_1prong_Run2017", "tauEsOneProng")

mc_tau_es_1prong1pizero_variations = ChangeDataset("CMS_scale_mc_t_1prong1pizero_Run2017", "tauEsOneProngOnePiZero")

tau_es_3prong_variations = ChangeDataset("CMS_scale_t_3prong_Run2017", "tauEsThreeProng")

tau_es_1prong_variations = ChangeDataset("CMS_scale_t_1prong_Run2017", "tauEsOneProng")

tau_es_1prong1pizero_variations = ChangeDataset("CMS_scale_t_1prong1pizero_Run2017", "tauEsOneProngOnePiZero")

ele_es_variations = ChangeDataset("CMS_scale_mc_e", "eleScale")

ele_es_variations = ChangeDataset("CMS_reso_mc_e", "eleSmear")

jet_es_variations = [
        ChangeDataset("CMS_scale_j_eta0to3_Run2017", "jecUncEta0to3"),
        ChangeDataset("CMS_scale_j_eta0to5_Run2017", "jecUncEta0to5"),
        ChangeDataset("CMS_scale_j_eta3to5_Run2017", "jecUncEta3to5"),
        ChangeDataset("CMS_scale_j_RelativeBal_Run2017", "jecUncRelativeBal"),
        ChangeDataset("CMS_scale_j_RelativeSample_Run2017", "jecUncRelativeSample")
        ]

