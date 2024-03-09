import cv2 as cv
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose



video = cv.VideoCapture("Video.mp4")

# Name window and prevent overflow
cv.namedWindow("Video", cv.WINDOW_NORMAL)
cv.resizeWindow("Video", 1280, 720)

# Create mediapipe instance
# Potential params for pose - (min_detection_confidence=0.5, min_tracking_confidence=0.5)
with mp_pose.Pose() as pose:
    #i = 0
    
    writeFile = open("coordinates.txt", "w")
    
    landmarkNumbers = [0, 11, 12, 13, 14, 15, 16, 23, 24, 25, 26, 29, 30, 31, 32]
    
    while video.isOpened():
        success, capture = video.read()
        
        results = pose.process(capture)
        
        # Pull landmark data
        try:
            landmarks = results.pose_world_landmarks.landmark
            #landmarks = results.pose_landmarks.landmark
            
        # If unable to get data, pass the attempt.
        except:
            pass
        
        """
        Write to file in format x,y,z, -> 15 body parts * 3 coords -> 45 values per line.
        New line after for loop to seperate the frame data.
        
        """
        for item in landmarkNumbers:
        
            #print(f'{landmarks[item].x}, {landmarks[item].y}, {landmarks[item].z}, ')
            writeFile.write(f'{landmarks[item].x},{landmarks[item].y},{landmarks[item].z},')
            
        writeFile.write("\n")  
        
        # Apply landmarks for display
        mp_drawing.draw_landmarks(capture, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        
        cv.imshow("Video", capture)
        
        #Must use q to close window. Closing the window manually is bad.
        if cv.waitKey(10) & 0xFF == ord('q'):
            break

    writeFile.close()
    # Release video source -> eventually release webcam.
    video.release()
    #Destroy the window.
    cv.destroyAllWindows()