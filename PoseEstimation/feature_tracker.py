from pathlib import PurePath
import numpy as np
import cv2 
from .data_structures import FeatureDetectionMode

class FeatureTracker():
    def __init__(self):
        self.mode = FeatureDetectionMode.INITIALIZATION

        self.feature_points_reference_image = np.array([None])
        self.feature_points_current_image = np.array([None])
        self.matched_feature_points = np.array([])

        self.feature_detector = cv2.FastFeatureDetector_create()

        self.feature_matches = []


    def Step(self, image, points_2D):
        if self.mode == FeatureDetectionMode.INITIALIZATION:
            self.InitializeFeaturePointsWithGivenPoints(points=points_2D)
        self.DetectPointFeature(image=image)
        self.MatchPointFeature()

    
    def InitializeFeaturePointsWithGivenPoints(self, points: np.array):
        self.feature_points_reference_image = np.array([[point[0], point[1]] for point in points])
        self.mode = FeatureDetectionMode.ACTIVE


    def DetectPointFeature(self, image):
        feature_points = self.feature_detector.detect(image, None)
        self.feature_points_current_image = np.array([[point.pt[0], point.pt[1]] for point in feature_points])


    def MatchPointFeature(self):
        matched_points = []
        for point in self.feature_points_reference_image:
            matched_points.append(self._FindNearest(point, self.feature_points_current_image))

        self.matched_feature_points = np.array(matched_points)
        self._SetCurrentsAsRefences(self.matched_feature_points)

    
    def _SetCurrentsAsRefences(self, feature_points):
        self.feature_points_reference_image = feature_points


    def _FindNearest(self, reference_points, current_points):
        current_points = np.asarray(current_points)
        reference_points = np.asarray(reference_points)
        idx = np.linalg.norm(current_points - reference_points, axis=1).argmin()
        return current_points[idx].astype(int)

    