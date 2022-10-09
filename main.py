import numpy as np
import os
import cv2 
from pathlib import PurePath, Path


from Camera.camera import Camera
from PoseEstimation.feature_tracker import FeatureTracker
from PoseEstimation.data_structures import FeatureDetectionMode


case_study_path = PurePath(Path(__file__).parent, "4D Sight CV Case Study")

if __name__ == "__main__":

    points_2D = np.load(PurePath(case_study_path, "vr2d.npy"))
    points_3D = np.load(PurePath(case_study_path, "vr3d.npy"))
    image_list = [i for i in os.listdir(case_study_path) if ".png" in i]

    camera = Camera()
    feature_tracker = FeatureTracker()

    for image in image_list:
        camera.SetImage(PurePath(case_study_path, image))
        if feature_tracker.mode == FeatureDetectionMode.INITIALIZATION:
            feature_tracker.InitializeFeaturePointsWithGivenPoints(points=points_2D)
            feature_tracker.DetectPointFeature(img=camera.image)
            feature_tracker.MatchPointFeature()
        camera.SetFeaturePoints(points_2D)
        camera.ShowFeaturePointsOnImage()
        cv2.imshow('image', camera.image)
        cv2.waitKey(0)

    cv2.destroyAllWindows()
    print("OKKEYYY")

