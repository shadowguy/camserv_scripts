
## Initialize the camera client.
from cam_server import CamClient
cam_client = CamClient()

# Print the list of available cameras.
print(cam_client.get_cameras())

# If modifying: Put the name of the camera you want to modify.
#camera_to_modify = "SATOP31-PSCR136"

# Retrieve the camera config.
#camera_config = cam_client.get_camera_config(camera_to_modify)
#print(camera_config)
# Specify the desired camera config.
#camera_config={
#  'name': 'SATOP31-PSCR136',
#  'source': 'SATOP31-PSCR136',
#  'source_type': 'epics',
#  'mirror_x': False,
#  'mirror_y': False,
#  'rotate': 0,
#  
#  'camera_calibration': {
#    'reference_marker': [0, 0, 100, 100],
#    'reference_marker_width': 100.0,
#    'reference_marker_height': 100.0,
#    'angle_horizontal': 0.0,
#    'angle_vertical': 0.0
#  }
#}

# Specify the new camera name.
#new_camera_name = "SATOP31-PSCR136"

# Save the camera configuration.
#cam_client.set_camera_config(new_camera_name, camera_config)
#
## In case you need to, delete the camera config you just added.
# cam_client.cam_client.delete_camera_config(new_camera_name)
print('done')
