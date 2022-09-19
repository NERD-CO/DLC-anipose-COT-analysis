import deeplabcut

if __name__ == '__main__':
    path_config_file = 'C:/Users/madComp/Desktop/MultiPtDBSDLC/VM04/COTask-Maddie-2022-07-05/config.yaml'

    deeplabcut.evaluate_network(path_config_file)

    viddir = 'C:/Users/madComp/Desktop/DBS_Videos/VM04_Compressed_Video/VM04/'
    videofile_path = [viddir+'/session001/20210908_VM04_session001_topCam-0000.mp4', 
viddir+'/session002/20210908_VM04_session002_topCam-0000.mp4', 
viddir+'/session003/20210908_VM04_session003_topCam-0000.mp4', 
viddir+'/session004/20210908_VM04_session004_topCam-0000.mp4', 
viddir+'/session005/20210908_VM04_session005_topCam-0000.mp4', 
viddir+'/session006/20210908_VM04_session006_topCam-0000.mp4', 
viddir+'/session001/20210908_VM04_session001_leftCam-0000.mp4', 
viddir+'/session002/20210908_VM04_session002_leftCam-0000.mp4', 
viddir+'/session003/20210908_VM04_session003_leftCam-0000.mp4', 
viddir+'/session004/20210908_VM04_session004_leftCam-0000.mp4', 
viddir+'/session005/20210908_VM04_session005_leftCam-0000.mp4', 
viddir+'/session006/20210908_VM04_session006_leftCam-0000.mp4', 
viddir+'/session001/20210908_VM04_session001_rightCam-0000.mp4', 
viddir+'/session002/20210908_VM04_session002_rightCam-0000.mp4', 
viddir+'/session003/20210908_VM04_session003_rightCam-0000.mp4', 
viddir+'/session004/20210908_VM04_session004_rightCam-0000.mp4', 
viddir+'/session005/20210908_VM04_session005_rightCam-0000.mp4', 
viddir+'/session006/20210908_VM04_session006_rightCam-0000.mp4']

    deeplabcut.analyze_videos(path_config_file, videofile_path, videotype='.mp4', save_as_csv=True)

    deeplabcut.create_labeled_video(path_config_file, videofile_path, videotype='.mp4')

    deeplabcut.plot_trajectories(path_config_file,videofile_path)