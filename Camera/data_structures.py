from dataclasses import dataclass
from Utils.reader import read_dict_from_yaml


@dataclass
class CameraIntrinsicParameters:
    fx: int
    fy: int
    cx: int
    cy: int


    def __init__(self, intrinsic_parameters):
        dict_intrinsic_parameters = dict()
        dict_intrinsic_parameters = read_dict_from_yaml(intrinsic_parameters)


        if self.type_check(dict_intrinsic_parameters):
            self.fx = dict_intrinsic_parameters["fx"]
            self.fy = dict_intrinsic_parameters["fy"]
            self.cx = dict_intrinsic_parameters["cx"]
            self.cy = dict_intrinsic_parameters["cy"]


    def type_check(self, dict_intrinsic_parameters):
        for value in dict_intrinsic_parameters.values():
            if type(value) != int:
                raise TypeError("Intrinsic parameters yaml file type error!")
        return True


@dataclass
class Camera6DoFPose:
    x: float
    y: float
    z: float
    angle_x: float
    angle_y: float
    angle_z: float

    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.angle_x = 0.0
        self.angle_y = 0.0
        self.angle_z = 0.0
