from __future__ import print_function
import matplotlib.pyplot as plt
#import pystem as ps
from pystem.stemsegmentation import segmentationSTEM
from pyiron_base import PythonTemplateJob
import numpy as np
import time

def plot_individual(image):
    plt.imshow(image)
    plt.xticks([])
    plt.yticks([])    

class pystem_Seg(PythonTemplateJob):
    def __init__(self, project, job_name):
        super(pystem_Seg, self).__init__(project, job_name)
        self._image_path = ''
        self.input['image_path']=''
        self.input['image'] = None
        self._image = None
        self._step = 5
        self._descriptor_name = ''
        self.input['descriptor_name'] = ''
        self.n_patterns = 3
        self.window_x=20
        self.window_y=20
        self.patch_x=20
        self.patch_y=20
        self.seg = None
        self.labels = None

    @property
    def image_path(self):
        return self._image_path
    
    @image_path.setter
    def image_path(self, name):
        self._image_path = name

    @property
    def descriptor_name(self):
        return self._descriptor_name
    
    @descriptor_name.setter
    def descriptor_name(self, name):
        self._descriptor_name = name

    @property
    def image(self):
        return self._image

    def image_load(self):
        self._image = np.load(self._image_path)
    
    def plot_image(self):
        plt.imshow(self._image[:,:],cmap='gray')
        plt.xticks([])
        plt.yticks([])

    def plot_label(self):
        if self.status.finished :
            with self.project_hdf5.open("output/generic") as h5out:
                self.labels = h5out["labels"]
                plt.imshow(self.labels)
                plt.xticks([])
                plt.yticks([])    
        else:
            plt.imshow(self.labels)
            plt.xticks([])
            plt.yticks([])
    
    def run_static(self):
        self.seg = segmentationSTEM( n_patterns=self.n_patterns,
                       window_x=self.window_x,window_y=self.window_y,
                       patch_x=self.patch_x,patch_y=self.patch_y,
                       step=self._step,
                       descriptor_name=self._descriptor_name,
                       #method='direct',
                       upsampling=True)
        
        self.labels = self.seg.perform_clustering(self._image)
        with self.project_hdf5.open("output/generic") as h5out: 
             h5out["labels"] = self.labels
        self.status.finished = True



