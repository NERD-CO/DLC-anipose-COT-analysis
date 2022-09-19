import deeplabcut

path_config_file = 'C:/Users/madComp/Desktop/MultiPtDBSDLC/VM05/COTask-Maddie-2022-04-22/config.yaml'

deeplabcut.create_training_dataset(path_config_file)

deeplabcut.train_network(path_config_file)