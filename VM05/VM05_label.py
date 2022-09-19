import deeplabcut

path_config_file = 'C:/Users/madComp/Desktop/MultiPtDBSDLC/VM05/COTask-Maddie-2022-04-22/config.yaml'

deeplabcut.extract_frames(path_config_file, userfeedback=False)

#%gui wx
deeplabcut.label_frames(path_config_file)

deeplabcut.check_labels(path_config_file)