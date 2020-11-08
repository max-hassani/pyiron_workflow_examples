# pyiron_workflow_examples
Here, you can find examplary notebooks for pyiron workflows. Pyiron play the role of a workflow manager software, while it runs the simulations/analysis underneath using various simulation/analysis software, such as LAMMMPS, DAMASK, and FEniCS. 
In this repository, you can find following examples:
1. LAMMPS-DAMASK Workflow: Macroscopic mechanical behavior of Cu-Ni alloys   
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/muh-hassani/pyiron_workflow_examples/main)   
In the [`LAMMPS-DAMASK-workflow/Lammps-damask-workflow.ipynb`](https://github.com/muh-hassani/pyiron_workflow_examples/blob/main/LAMMPS-DAMASK-workflow/Lammps-damask-workflow.ipynb) notebook, elastic constants for various concentraitons of Cu and Ni in Cu-Ni alloys were obtained from LAMMPS simulations. Then the elastic constants are fed to DAMASK simulation to determine the macroscopic response of a multi-grain Cu-Ni system under tensile loading.  
Via the following link you can test the LAMMPS-DAMASK-workflow notebook on binder: https://mybinder.org/v2/gh/muh-hassani/pyiron_workflow_examples/main   
2. FEniCS workflow example: A membrane under gauassian-distributed loads    
In the [`FEniCS/PoissonEq/membrane_under_gaussian_load.ipynb`](https://github.com/muh-hassani/pyiron_workflow_examples/blob/fenics/FEniCS/PoissonEq/membrane_under_gaussian_load.ipynb) notebook, the defelection of a circular membrane under various gaussian-distributed loads are studied. FEniCS are used to solve Poisson equation for the defelection of the membrane, while pyiron manages the jobs and the I/O data. The sharpness of the distributed load is varied to study the reponse of the membrane. Finally the deflection of the membrane for various loads are ploted.   
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/muh-hassani/pyiron_workflow_examples/fenics)
