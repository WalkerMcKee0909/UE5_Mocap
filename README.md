NOTE: This is a senior project for Aaron Riopelle and Walker McKee. The purpose of this project is to create an AI plugin for Unreal Engine 5 that can record and create animations with a webcam. This is a work in progress and the README will be updated as progress is made. Once our class is over, our progress will be made open source and continued progress will be made at the discretion of Walker or Aaron.

FEB 13, 2024 (Walker):
There are a few parts to this project. There is a mediapipe and openCV aspect, then there will be a script to get the data from the opencv script and translate the bones of a character in UE5 to said locations. In the simplest terms of pseudocode:

for every frame:
  get landmark locations
  for every landmark:
    transform corisponding bone

This is easier said than done, and will be a lot more complicated than this

Below is a diagram of the landmarks found by Mediapipe. We have no intention on using facial tracking as UE5 already has a very good facial animation system so we don't need landmarks 1-10, however we will use landmark 0 to track the head. We will use landmarks 15 and 16 to track the hands, and 17-22 are not needed. Landmarks 28 and 27 will not be used as they are not needed. 

This leaves us with only 15 landmarks to track. As we make progress this number may change, however we think this will provide us with decent animations that can be used as a baseline to be adjusted later by the developer.
<img width="723" alt="pose_landmarks_index" src="https://github.com/WalkerMcKee0909/UE5_Mocap/assets/89943198/642fbdc1-15c8-40f7-88a3-b96d2a444a21">
