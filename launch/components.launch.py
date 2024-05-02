# Enway GmbH - All Rights reserved.
# Proprietary & confidential.

from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode
import launch
import os

def generate_launch_description():
    """Generate launch description with multiple components."""
    config = os.path.join(
        get_package_share_directory('patchworkpp'),
            'config',
            'ground_segmentation.yaml'
        )
    container = ComposableNodeContainer(
            name='patchwork_container',
            namespace='',
            package='rclcpp_components',
            executable='component_container',
            composable_node_descriptions=[
                ComposableNode(
                    package='patchworkpp',
                    plugin='patchworkpp::PatchworkppPointXYZI',
                    name='ground_segmentation',
                    namespace='ground_segmentation',
                    parameters=[{config}]),
            ],
            output='screen',
    )

    return launch.LaunchDescription([container])
