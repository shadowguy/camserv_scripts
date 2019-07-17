
## Initialize the camera client.
from cam_server import CamClient
cam_client = CamClient()
#
## Specify the desired camera config.
camera_config={'name': 'SARES11-SPEC125-M2', 'mirror_y': False, 'camera_calibration': {'reference_marker_height': 100.0, 'reference_marker_width': 100.0, 'angle_vertical': 0.0, 'reference_marker': [0, 0, 100, 100], 'angle_horizontal': 0.0}, 'source_type': 'epics', 'mirror_x': False, 'source': 'SARES11-SPEC125-M2', 'rotate': 0}

## Specify the new camera name.
#new_camera_name = "SARES11-SPEC125-M2"
#
## Save the camera configuration.
#cam_client.set_camera_config(new_camera_name, camera_config)
#
## In case you need to, delete the camera config you just added.
## cam_client.cam_client.delete_camera_config(new_camera_name)
