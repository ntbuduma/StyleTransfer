import cv2

vidcap = cv2.VideoCapture("results/video_test_german_transition_logistic_seri.mp4")
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("logistic/l%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1