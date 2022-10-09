from pathlib import PurePath, Path
from .data_structures import Camera6DoFPose, CameraIntrinsicParameters


class Camera:
    def __init__(self, config_path = PurePath(Path(__file__).parent, "config")):
        self.intrinsic_parameters = CameraIntrinsicParameters(PurePath(config_path, "intrinsic_parameters.yaml"))
        self.pose = Camera6DoFPose()


    def ResetPose(self):
        self.pose = Camera6DoFPose()      

