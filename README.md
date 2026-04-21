# IG3D Course Labs
<img width="1920" height="1080" alt="low_poly_helicopter" src="https://github.com/user-attachments/assets/48e57243-0f5e-4857-beee-5dc02833468b" />



This repository contains my laboratory work for the **IG3D course** at **Sorbonne University**. These labs cover different topics in computer graphics and interactive 3D, including ray tracing, materials and shading, low-poly modeling, scene creation, medical 3D reconstruction, rigid body simulation, and fluid simulation.

The goal of this work was to understand both the visual and technical side of 3D graphics. Across the labs, I worked on rendering, object creation, scene design, simulation, and image generation. The projects combine modeling, lighting, shading, geometry processing, and physically based simulation.

<img width="1280" height="900" alt="tp_4" src="https://github.com/user-attachments/assets/53e2d410-d0e6-4044-b238-b165826fd770" />

## Lab Contents

### 1. Ray Tracing
This lab focuses on the basics of **ray tracing**. The main objective was to generate rendered images by tracing rays through a scene and computing intersections with objects.

Main ideas covered in this lab:
- ray generation from the camera
- object intersection
- shadows
- reflections
- anti-aliasing
- final rendered scene generation

This lab gave me a strong introduction to image synthesis and how realistic rendering can be produced from mathematical ray-object interactions.

---

### 2. Objects, Materials, Shading and Colours
This lab focuses on creating 3D objects and improving their appearance using **materials, shading, and colours**. The work explores how the same object can look different depending on the surface properties and rendering settings.
<img width="1127" height="788" alt="Screenshot 2026-02-26 192446" src="https://github.com/user-attachments/assets/d697729e-a587-42d0-a1ab-033f0ce39ef8" />
<img width="963" height="656" alt="Screenshot 2026-02-26 194231" src="https://github.com/user-attachments/assets/a522a154-9f4c-461a-adc9-ab6c932394de" />
<img width="1192" height="786" alt="Screenshot 2026-02-26 192317" src="https://github.com/user-attachments/assets/92d19a4f-9d90-4282-9e18-6985815dff41" />


Main ideas covered in this lab:
- object creation and placement
- color design
- material assignment
- smooth and flat shading
- lighting influence on appearance
- visual improvement of rendered models

This part helped me understand how shading and materials make a simple object look more polished and realistic.

---

### 3. Low Poly Girl
This lab is based on building and rendering a **low poly character model**. The focus is on simple geometry, clean stylized design, and visual presentation.
<img width="1920" height="1080" alt="low_poly_smooth" src="https://github.com/user-attachments/assets/86ed2fd2-a17b-431c-bba8-9f7a74ff32d7" />
Main ideas covered in this lab:
- low poly modeling
- character proportions
- color assignment
- simple stylized geometry
- comparison between flat and smooth appearance

The low poly girl model shows how a small number of polygons can still produce a visually appealing 3D character.

---

### 4. Island Scene
This lab focuses on creating a small **stylized island environment**. The scene includes natural elements and uses simple geometric forms to build a complete composition.

Main ideas covered in this lab:
- scene composition
- terrain and environment modeling
- simple trees, house, and landscape objects
- color harmony
- lighting and final presentation

This lab helped me practice how to combine multiple simple objects into one coherent 3D scene.

---

### 5. MRI 3D Reconstruction
This lab explores **medical 3D visualization** using MRI data in Blender. The objective is to reconstruct a 3D model from volumetric head scan data and generate rendered views. The provided pseudocode template shows a workflow based on TIFF volume import, normalization, marching cubes, smoothing, material creation, lighting and camera setup.
<img width="1280" height="960" alt="t1_head_Cam_Sagittal" src="https://github.com/user-attachments/assets/86a3636d-60d7-4734-895b-9881f4cb9a00" />

Main ideas covered in this lab:
- volumetric data loading
- normalization and downsampling
- threshold-based surface extraction
- marching cubes mesh generation
- smoothing and solidification
- medical lighting and multi-view rendering

This lab connects computer graphics with medical imaging and shows how 3D reconstruction can be built from scan data.

---

### 6. Rigid Body Simulation
This lab focuses on **rigid body dynamics**. I implemented the main components of a rigid body solver, including mass, inertia tensor, force, torque, momentum update, position update, and rotation update. I also extended the lab by adding floor collision, bouncing, damping, and a resting state for the cube. fileciteturn0file1
<img width="679" height="541" alt="Screenshot 2026-04-02 200309" src="https://github.com/user-attachments/assets/68d369d4-554b-4645-af74-fb1f5e2ae509" />

Main ideas covered in this lab:
- rigid body motion
- mass and inertia tensor
- force and torque computation
- linear and angular momentum update
- rotation update
- collision with the floor
- bounce and settling behavior

This lab helped me understand the physics side of animation and how motion can be generated from equations rather than manual keyframing.

---

### 7. SPH Fluid Simulation
This lab focuses on **Smoothed Particle Hydrodynamics (SPH)** for fluid simulation. I implemented the important solver parts such as neighbor search, density computation, pressure, body force, viscosity, and particle update. The final simulation shows fluid falling, deforming, spreading, and creating a splash near the boundary.
<img width="874" height="342" alt="Screenshot 2026-04-16 224953" src="https://github.com/user-attachments/assets/092d0cdb-e166-44de-8b0d-b924c4ec5670" />

Main ideas covered in this lab:
- particle-based fluid simulation
- background grid neighbor search
- density and pressure computation
- gravity and viscosity
- Symplectic Euler integration
- fluid motion and splash behavior

This lab gave me a practical introduction to physically based fluid simulation and particle methods.

---

## What I Learned

Through these labs, I improved my understanding of:

- rendering and ray tracing
- 3D modeling and stylized design
- materials, colours, and shading
- scene composition
- medical 3D reconstruction
- rigid body simulation
- particle-based fluid simulation

Overall, the course helped me connect **visual creation** and **technical computation** in 3D graphics.

---

## Conclusion

These IG3D labs show a broad view of computer graphics, from static rendering to dynamic simulation. Each lab focuses on a different aspect of 3D work and together they form a portfolio of modeling, rendering, reconstruction and simulation tasks. This collection reflects both creative and technical progress during the course. It includes image synthesis, object design, environment creation, medical visualization, rigid motion and fluid behavior, which together represent the main practical themes of IG3D.









