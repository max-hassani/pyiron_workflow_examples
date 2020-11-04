#!/usr/bin/env python
# coding: utf-8

import damask
import numpy as np
import h5py

def eval_stress(job_file):
  """
  return the stress as a numpy array
  Parameters
  ----------
  job_file : str
    Name of the job_file
  """
  d = damask.Result(job_file)
  stress_path = d.get_dataset_location('avg_sigma')
  stress = np.zeros(len(stress_path))
  hdf = h5py.File(d.fname)
  for count,path in enumerate(stress_path):
      stress[count] = np.array(hdf[path])
  stress = np.array(stress)/1E6
  return stress

def eval_strain(job_file):
  """
  return the strain as a numpy array

  Parameters
  ----------
  job_file : str
    Name of the job_file
  """
  d = damask.Result(job_file)
  stress_path = d.get_dataset_location('avg_sigma')
  strain = np.zeros(len(stress_path))
  hdf = h5py.File(d.fname)
  for count,path in enumerate(stress_path):
      strain[count] = np.array(hdf[path.split('avg_sigma')[0]     + 'avg_epsilon'])

  return strain  

