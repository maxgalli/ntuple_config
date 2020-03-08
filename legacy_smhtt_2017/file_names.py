"""Database

Dictionaries where the keys are the dataset names and the items
lists containing the names of the files to be fetched.
"""

nominal_files = {
    'data': [
        'SingleMuon_Run2017B_31Mar2018v1_13TeV_MINIAOD',
        'SingleMuon_Run2017C_31Mar2018v1_13TeV_MINIAOD',
        'SingleMuon_Run2017D_31Mar2018v1_13TeV_MINIAOD',
        'SingleMuon_Run2017E_31Mar2018v1_13TeV_MINIAOD',
        'SingleMuon_Run2017F_31Mar2018v1_13TeV_MINIAOD'
        ],
    'DY': [
        'DY2JetsToLLM50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_ext1-v2',
        'DY2JetsToLLM50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_v1',
        'DY3JetsToLLM50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_ext1-v1',
        'DY3JetsToLLM50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_v1',
        'DYJetsToLLM50_RunIIFall17MiniAODv2_PU2017RECOSIMstep_13TeV_MINIAOD_madgraph-pythia8_ext1-v1',
        'DYJetsToLLM50_RunIIFall17MiniAODv2_PU2017RECOSIMstep_13TeV_MINIAOD_madgraph-pythia8_v1',
        'DY1JetsToLLM50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_v1',
        'DY1JetsToLLM50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_ext1-v2',
        'DY4JetsToLLM50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_v2',
        'DYJetsToLLM10to50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_ext1-v2',
        'EWKZ2JetsZToLLM50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_v2',
        'EWKZ2Jets_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_v2'
        ],
    'TT': [
        'TTTo2L2Nu_RunIIFall17MiniAODv2_PU2017newpmx_13TeV_MINIAOD_powheg-pythia8_v1',
        'TTToHadronic_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_powheg-pythia8_v2',
        'TTToSemiLeptonic_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_powheg-pythia8_v1'
        ],
    'VV': [
        'WW_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_pythia8_v2',
        'WZ_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_pythia8_v1',
        'ZZ_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_pythia8_v2',
        'STt-channelantitop4finclusiveDecaysTuneCP5_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_powheg-pythia8_v2',
        'STtWantitop5finclusiveDecaysTuneCP5_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_powheg-pythia8_v2',
        'STtWtop5finclusiveDecaysTuneCP5_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_powheg-pythia8_v2',
        'STt-channeltop4finclusiveDecaysTuneCP5_RunIIFall17MiniAODv2_PU2017newpmx_13TeV_MINIAOD_powheg-pythia8_v1'
        ],
    'W': [
        'W1JetsToLNu_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_v4',
        'W2JetsToLNu_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_v5',
        'W3JetsToLNu_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_v1',
        'W4JetsToLNu_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_v2',
        'WGToLNuG_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_v1',
        'WJetsToLNu_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_ext1-v2',
        'WJetsToLNu_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_v3',
        'EWKWMinus2JetsWToLNuM50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_v2',
        'EWKWPlus2JetsWToLNuM50_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph-pythia8_v2'
        ],
    'ggH': [
        'GluGluHToTauTauHTXSFilterSTXS1p1Bin101M125_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_powheg-pythia8_v2',
        'GluGluHToTauTauHTXSFilterSTXS1p1Bin104to105M125_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_powheg-pythia8_v1',
        'GluGluHToTauTauHTXSFilterSTXS1p1Bin106M125_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_powheg-pythia8_v2',
        'GluGluHToTauTauHTXSFilterSTXS1p1Bin107to109M125_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_powheg-pythia8_v1',
        'GluGluHToTauTauHTXSFilterSTXS1p1Bin110to113M125_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_powheg-pythia8_v2',
        'GluGluHToTauTauM125_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_powheg-pythia8_ext1-v1',
        'GluGluHToTauTauM125_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_powheg-pythia8_v2'
        ],
    'qqH': [
        'VBFHToTauTauHTXSFilterSTXS1p1Bin203to205M125_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_powheg-pythia8_v1',
        'VBFHToTauTauHTXSFilterSTXS1p1Bin206M125_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_powheg-pythia8_v1',
        'VBFHToTauTauHTXSFilterSTXS1p1Bin207to210M125_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_powheg-pythia8_v1',
        'VBFHToTauTauM125_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_powheg-pythia8_v1',
        'WminusHToTauTauM125_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_powheg-pythia8_v1',
        'WplusHToTauTauM125_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_powheg-pythia8_v1',
        'ZHToTauTauM125_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_powheg-pythia8_v1'
        ]
    }
