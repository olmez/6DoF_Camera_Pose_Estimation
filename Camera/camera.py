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
        self.image = cv2.imread(str(image_path)) #cv2.IMREAD_GRAYSCALE


    def SetFeaturePoints(self, points: np.array):
        self.feature_points = points


    def ShowFeaturePointsOnImage(self):
        for point in self.feature_points:  
            self.image = cv2.circle(self.image, (point[0][0], point[0][1]), radius=4, color=(0, 0, 255), thickness=-1)


    def ResetPose(self):
        self.pose = Camera6DoFPose()      

