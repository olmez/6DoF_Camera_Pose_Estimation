from pathlib import PurePath, Path
import cv2 
import numpy as np


from .data_structures import Camera6DoFPose, CameraIntrinsicParameters


class Camera:
    def __init__(self, config_path = PurePath(Path(__file__).parent, "config")):
        self.intrinsic_parameters = CameraIntrinsicParameters(PurePath(config_path, "intrinsic_parameters.yaml"))
        self.pose = Camera6DoFPose()

        self.image = None
        self.feature_points = None


    def SetImage(self, image_path: PurePath):
        self.image = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)


    def SetFeaturePoints(self, points: np.array):
        self.feature_points = points


    def ShowFeaturePointsOnImage(self, feature_points, color=(0, 0, 255)):
        image_with_points = self.image.copy()
        for point in feature_points:  
            cv2.circle(image_with_points, (int(point.pt[0]), int(point.pt[1])), radius=4, color=color, thickness=-1)
        return image_with_points


    def ResetPose(self):
        self.pose = Camera6DoFPose()      

