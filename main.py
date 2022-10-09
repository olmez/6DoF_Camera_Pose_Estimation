import numpy as np
import os
import cv2 
from pathlib import PurePath, Path


from Camera.camera import Camera
from PoseEstimation.feature_tracker import FeatureTracker


case_study_path = PurePath(Path(__file__).parent, "4D Sight CV Case Study")

if __name__ == "__main__":

    points_2D = np.load(PurePath(case_study_path, "vr2d.npy"))
    points_2D = points_2D.reshape(points_2D.shape[0], points_2D.shape[-1]) 
    points_3D = np.load(PurePath(case_study_path, "vr3d.npy"))
    points_3D = points_3D.reshape(points_3D.shape[0], points_3D.shape[-1])
    image_list = [i for i in os.listdir(case_study_path) if ".png" in i]

    camera = Camera()
    feature_tracker = FeatureTracker()

    for image in image_list:
        camera.SetImage(PurePath(case_study_path, image))
        feature_tracker.Step(image=camera.image, points_2D=points_2D)
        image_with_points = camera.ShowFeaturePointsOnImage(feature_tracker.matched_points, color=(0, 0, 255))
        cv2.imshow('image', image_with_points)
        cv2.waitKey(0)

    cv2.destroyAllWindows()

