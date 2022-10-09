from pathlib import PurePath
import numpy as np
import cv2 
from .data_structures import FeatureDetectionMode

class FeatureTracker():
    def __init__(self):
        self.mode = FeatureDetectionMode.INITIALIZATION

        self.feature_points_reference_image = np.array([None])
        self.descriptors_reference_image = np.array([None])

        self.feature_points_current_image = np.array([None])
        self.descriptors_current_image = np.array([None])

        self.matched_points = np.array([None])
        self.descriptor_points = np.array([None])

        self.feature_detector = cv2.ORB_create(nfeatures=100000)
        # Define FLANN parameters
        FLANN_INDEX_LSH = 6
        index_params = dict(algorithm = FLANN_INDEX_LSH,
                            table_number = 6,
                            key_size = 12,
                            multi_probe_level = 1)
        search_params = dict(checks = 50)
        self.matcher = cv2.FlannBasedMatcher(index_params, search_params)

        self.reference_image = None


    def Step(self, image, points_2D):
        if self.mode == FeatureDetectionMode.INITIALIZATION:
            self.InitializeFeaturePointsWithGivenPoints(image=image, points=points_2D)
            return True
        self.DetectPointFeature(image=image)
        self.MatchPointFeature(image=image)
        return True

    
    def InitializeFeaturePointsWithGivenPoints(self, image, points: np.array):
        self.feature_points_reference_image, self.descriptors_reference_image = self.feature_detector.compute(image, np.array([cv2.KeyPoint(point[0], point[1], _size=2) for point in points]), None)
        self.matched_points = self.feature_points_reference_image
        self.reference_image = image
        self.mode = FeatureDetectionMode.ACTIVE


    def DetectPointFeature(self, image):
        self.feature_points_current_image = self.feature_detector.detect(image, None)
        self.feature_points_current_image, self.descriptors_current_image = self.feature_detector.compute(image, self.feature_points_current_image, None)


    def MatchPointFeature(self, image):
        matches = self.matcher.knnMatch(self.descriptors_reference_image, self.descriptors_current_image, k=2)

        matched_points = []
        descriptor_points = []
        for m, n in matches:
            matched_points.append(self.feature_points_current_image[m.trainIdx])
            descriptor_points.append(self.descriptors_current_image[m.trainIdx])

        self.matched_points = np.array(matched_points)
        self.descriptor_points = np.array(descriptor_points)
        
        self._SetCurrentsAsRefences()

    
    def _SetCurrentsAsRefences(self):
        self.feature_points_reference_image = self.matched_points
        self.descriptors_reference_image = self.descriptor_points


    def _FindNearest(self, reference_points, current_points):
        current_points = np.asarray(current_points)
        reference_points = np.asarray(reference_points)
        idx = np.linalg.norm(current_points - reference_points, axis=1).argmin()
        return current_points[idx].astype(int)

    