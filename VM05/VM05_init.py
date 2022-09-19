import deeplabcut

task = 'COTask'
experimenter = 'Maddie'
viddir = 'C:/Users/madComp/Desktop/DBS_Videos/VM05_Compressed_Video/VM05/'
video = [viddir+'/session001/20211007_VM05_session001_topCam-0000.mp4', 
viddir+'/session002/20211007_VM05_session002_topCam-0000.mp4', 
viddir+'/session003/20211007_VM05_session003_topCam-0000.mp4', 
viddir+'/session004/20211007_VM05_session004_topCam-0000.mp4', 
viddir+'/session005/20211007_VM05_session005_topCam-0000.mp4', 
viddir+'/session006/20211007_VM05_session006_topCam-0000.mp4', 
viddir+'/session007/20211007_VM05_session007_topCam-0000.mp4', 
viddir+'/session008/20211007_VM05_session008_topCam-0000.mp4',
viddir+'/session001/20211007_VM05_session001_leftCam-0000.mp4', 
viddir+'/session002/20211007_VM05_session002_leftCam-0000.mp4', 
viddir+'/session003/20211007_VM05_session003_leftCam-0000.mp4', 
viddir+'/session004/20211007_VM05_session004_leftCam-0000.mp4', 
viddir+'/session005/20211007_VM05_session005_leftCam-0000.mp4', 
viddir+'/session006/20211007_VM05_session006_leftCam-0000.mp4', 
viddir+'/session007/20211007_VM05_session007_leftCam-0000.mp4', 
viddir+'/session008/20211007_VM05_session008_leftCam-0000.mp4',
viddir+'/session001/20211007_VM05_session001_rightCam-0000.mp4', 
viddir+'/session002/20211007_VM05_session002_rightCam-0000.mp4', 
viddir+'/session003/20211007_VM05_session003_rightCam-0000.mp4', 
viddir+'/session004/20211007_VM05_session004_rightCam-0000.mp4', 
viddir+'/session005/20211007_VM05_session005_rightCam-0000.mp4', 
viddir+'/session006/20211007_VM05_session006_rightCam-0000.mp4', 
viddir+'/session007/20211007_VM05_session007_rightCam-0000.mp4', 
viddir+'/session008/20211007_VM05_session008_rightCam-0000.mp4']

print(video)
path_config_file = deeplabcut.create_new_project(task,experimenter,video,copy_videos=True)