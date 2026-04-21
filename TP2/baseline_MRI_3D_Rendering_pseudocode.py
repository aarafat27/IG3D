
"""
======================================================================
 Title:                   T1 MRI Head Reconstruction Lab – Pseudocode Template
 Creating Author:         Janan ARSLAN
 Creation Date:           [05-03-2025]
 Latest Modification:     [13-03-2025]
 Modification Author:     Janan ARSLAN
 E-mail:                  janan.arslan@icm-institute.org
 Version:                 1.1pseudo
======================================================================


This is a pseudocode provided to students at Sorbonne Université in the IG3D course.

The objective is to replace TODO items with code that will render a 3D MRI model in Blender.

Complete code will be provided to students via Moodle following all lab submissions.


"""

# This pseudocode is provided as a starting point.

# The following imports are available by default
import bpy
import os
import numpy as np
from mathutils import Vector
import math
import sys
import time

# Clear the scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()


# The following allows you to install packages directly
def install_package(package_name):
    """Install a package using pip if it's not already installed"""
    try:
        __import__(package_name)
        print(f"{package_name} is already installed")
    except ImportError:
        print(f"{package_name} not found, attempting to install...")
        python_exe = sys.executable
        import subprocess
        subprocess.check_call([python_exe, "-m", "pip", "install", package_name])
        print(f"Installed {package_name}")

# Using the above to install tifffile and scikit-image
try:
    install_package("tifffile")
    import tifffile
except Exception as e:
    print(f"Error installing tifffile: {e}")
    print("You may need to manually install tifffile.")

try:
    install_package("scikit-image")
    from skimage import measure
    has_skimage = True
except Exception as e:
    print(f"Error installing scikit-image: {e}")
    has_skimage = False

#####################################################################################################
# Function: import_t1_head(file_path, downsample)
# Purpose: Load the T1 MRI head from a TIFF file into a normalized, downsampled 3D numpy array.
def import_t1_head(file_path, downsample=4):
    # TODO: Verify that file_path exists; if not, raise an error.
    # TODO: Open the TIFF file using "with tifffile.TiffFile(file_path) as tif:".
    # TODO: Determine the number of slices (depth) and get the image dimensions from the first page.
    # TODO: Loop over tif.pages, converting each page to a float32 array.
    # TODO: Optionally, print min/max values for the first and last slices for debugging.
    # TODO: Stack all slices into a 3D numpy array.
    # TODO: Normalize the entire volume using: (volume - min) / (max - min).
    # TODO: If downsample > 1, apply slicing: volume[::downsample, ::downsample, ::downsample].
    # TODO: Print final volume shape and min/max values for verification.
    pass
#####################################################################################################


#####################################################################################################
# Function: create_t1_material(name)
# Purpose: Create a Blender material for T1 MRI visualization.
def create_t1_material(name="T1_Material"):
    # TODO: Create a new material with: mat = bpy.data.materials.new(name=name).
    # TODO: Enable nodes by setting mat.use_nodes = True.
    # TODO: Remove all default nodes from mat.node_tree.nodes.
    # TODO: Add a new Diffuse BSDF node, set its color to (0.9, 0.9, 0.85, 1.0) and roughness to around 0.3.
    # TODO: Add a Material Output node and link the Diffuse BSDF output to the Material Output input.
    pass
#####################################################################################################


#####################################################################################################
# Function: extract_skull_surface_improved(volume_data, threshold, name, smooth_iterations)
# Purpose: Extract the skull surface from the volume data using image processing and marching cubes.
def extract_skull_surface_improved(volume_data, threshold=0.65, name="T1_Skull", smooth_iterations=3):
    # TODO: Print a message indicating the start of skull extraction with the given threshold.
    # TODO: If scikit-image is unavailable, add a placeholder cube (using bpy.ops.mesh.primitive_cube_add) and return it.
    # TODO: Invert the volume data with: inv_data = 1.0 - volume_data.
    # TODO: Apply a Gaussian filter (e.g., scipy.ndimage.gaussian_filter with sigma=0.7) to inv_data.
    # TODO: Create a binary volume by thresholding the smoothed data: binary_data = smoothed_volume > threshold.
    # TODO: Use binary closing with a 3x3x3 structuring element to fill small holes in the binary data.
    # TODO: Run the marching cubes algorithm (measure.marching_cubes) on the processed volume.
    # TODO: If marching cubes fails, create and return a placeholder cube.
    # TODO: Otherwise, create a new Blender mesh from the vertices and faces obtained.
    # TODO: Set smooth shading on the mesh, assign the material from create_t1_material, and center the object (set origin to center of volume).
    # TODO: Optionally, add a Smooth modifier (with iterations=smooth_iterations) and a Solidify modifier.
    pass
#####################################################################################################


#####################################################################################################
# Function: setup_medical_lighting()
# Purpose: Set up a three-point lighting configuration for the scene.
def setup_medical_lighting():
    # TODO: Check if bpy.context.scene.world exists; if not, create a new world and assign it to the scene.
    # TODO: Enable nodes for the world and set the Background node's color to (0, 0, 0, 1).
    # TODO: Add three area lights at locations such as (5, -5, 5), (-5, -5, 3), and (0, 5, 5).
    # TODO: Set the energy for each light (e.g., 500, 200, and 300 respectively).
    # TODO: Set the render engine to 'CYCLES' and attempt to enable GPU rendering, with a fallback to CPU.
    # TODO: Optionally, configure render resolution and sample count.
    pass
#####################################################################################################


#####################################################################################################
# Function: setup_t1_head_cameras()
# Purpose: Create multiple camera views for the T1 MRI head.
def setup_t1_head_cameras():
    # TODO: Create a new empty object named "Target" at (0, 0, 0) and link it to the scene.
    # TODO: Define camera positions for views such as sagittal (7, 0, 0), coronal (0, -7, 0), axial (0, 0, 7), and perspective (5, -5, 5).
    # TODO: For each view, add a camera at the specified location, name it accordingly, and add a TRACK_TO constraint targeting "Target".
    # TODO: Set the perspective camera as the active scene camera.
    pass
#####################################################################################################


#####################################################################################################
# Function: process_t1_head(file_path, output_path, downsample, threshold, absolute_scale)
# Purpose: Process and visualize the T1 MRI head by loading data, extracting the skull, applying modifiers, and rendering images.
def process_t1_head(file_path, output_path, downsample=4, threshold=0.65, absolute_scale=24.0):
    # TODO: Print starting information: file path, output path, threshold, downsample factor, and absolute scale.
    # TODO: Call import_t1_head() with file_path and downsample to load volume_data.
    # TODO: Call extract_skull_surface_improved(volume_data, threshold) to obtain the skull mesh object.
    # TODO: Set the skull object's scale to (absolute_scale, absolute_scale, absolute_scale).
    # TODO: Add a Smooth modifier (e.g., factor 0.5 and iterations 3-5) to enhance surface quality.
    # TODO: Add a Solidify modifier with a thickness (e.g., 0.2) to add volume to the mesh.
    # TODO: Optionally, add a Remesh modifier for a more uniform mesh.
    # TODO: Call setup_medical_lighting() to configure the scene lighting.
    # TODO: Call setup_t1_head_cameras() to create and position the cameras.
    # TODO: Create the output directory if it does not exist.
    # TODO: Loop through each camera view:
    #         - Set the active camera.
    #         - Modify the render output filepath to include the view name.
    #         - Render the image and save it.
    pass
#####################################################################################################


#####################################################################################################
# Execute
if __name__ == "__main__":
    # TODO: Set the file path to the provided T1 MRI file (e.g., "t1-head.tif")
    #       and the output path for saving the rendered images.
    t1_file = "/path/to/t1-head.tif"          # TODO: update with actual path
    output_path = "/path/to/save/t1_head.png"   # TODO: update with actual path
    
    # Print file and output information.
    # Call process_t1_head() with appropriate parameters:
    #   - downsample (e.g., 4),
    #   - threshold for skull extraction (e.g., 0.65),
    #   - absolute_scale for final object scaling (e.g., 24.0).
    # Make note of how the 3D model changes (e.g., your expectations with downsampling vs. what actually happens
    # or how changing threshold, scale can impact the final render). 
    process_t1_head(
        file_path=t1_file,
        output_path=output_path,
        downsample=4,
        threshold=0.65,
        absolute_scale=24.0
    )
#####################################################################################################
