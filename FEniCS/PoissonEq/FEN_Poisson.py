from __future__ import print_function
import matplotlib.pyplot as plt
import mshr as mshr
import fenics as FEN
from pyiron_base import PythonTemplateJob

class FEN_Poisson(PythonTemplateJob):
    def __init__(self, project, job_name):
        super(FEN_Poisson, self).__init__(project, job_name)
        self.input['a']= ''
        self.input['L'] = ''
        self._a=None
        self._L=None
        self.input['vtk_filename']=project.name+'/output.pvd'
        self._vtk_filename = str(job_name)+'/output.pvd'
        self.input['mesh'] = None
        self._mesh = None
        self._BC = None
        self.input['BC']=None
        self.input['V']=None
        self._V = None
        self._u = None
        self._v = None
        self.input['u']
        self.input['v']
        self._f = None
        self._domain = None


    @property
    def domain(self):
        return self._domain
    @domain.setter
    def domain(self, dmn):
        self._domain = dmn

    @property
    def L(self):
        return self._L  
    @L.setter
    def L(self, expression):
        self.input['L'] = expression
        self._L = expression

    @property
    def mesh(self):
        return self._mesh
    
    @mesh.setter
    def mesh(self, mesh):
        self.input['mesh'] = mesh
        self._mesh = mesh
        
    @property
    def V(self):
        return self._V
    
    @V.setter
    def V(self, vol):
        self.input['V'] = vol
        self._V = vol

    @property
    def u(self):
        return self._u
    
    @u.setter
    def u(self, exp):
        self.input['u'] = exp
        self._u = exp
    
    @property
    def v(self):
        return self._v
    
    @v.setter
    def v(self, exp):
        self.input['v'] = exp
        self._v = exp
    
    @property
    def BC(self):
        return self._BC
    
    @BC.setter
    def BC(self, boundary):
        self.input['BC'] = boundary
        self._BC = boundary

    @property
    def a(self):
        return self._a
    
    @a.setter
    def a(self, expression):
        self.input['a'] = expression
        self._a = expression

    @property
    def vtk_filename(self):
        return self.input['vtk_filename']
    
    @vtk_filename.setter
    def vtk_filename(self, filename):
        self.input['vtk_filename'] = filename
        self._vtk_filename = filename

    def grad(self, arg):
        return FEN.grad(arg)

    def Circle(self,center, rad):
        """
        create a mesh on a circular domain with a radius equal to rad
        """
        return mshr.Circle(center, rad)
    
    def dxProd(self,A):
        """
        it returns the product of A and dx
        """
        return A*FEN.dx


    def generate_mesh(self, typ, order, resolution):
        self._mesh = mshr.generate_mesh(self._domain,resolution)
        self.input['mesh'] = self._mesh
        self._V = FEN.FunctionSpace(self._mesh, typ, order)
        self.input['V'] = self._V
        self._u = FEN.TrialFunction(self._V)
        self._v = FEN.TestFunction(self._V)
        #return self._mesh#mshr.generate_mesh(self._domain,resolution)

    def FunctionSpace(self, typ, order):
        return FEN.FunctionSpace(self._mesh, typ, order)

    def Constant(self, value):
        return FEN.Constant(value)
    

    def DirichletBC(self, expression, boundary):
        return FEN.DirichletBC(self._V, expression, boundary)

    def TrialFunction(self):
        return FEN.TrialFunction(self._V)
    
    def TestFunction(self):
        return FEN.TestFunction(self._V)
    
    def dot(self, arg1, arg2):
        return FEN.dot(arg1, arg2)
    
    def dx(self):
        return FEN.dx
    

    #def define_expression(expression,dictionary):


    def mesh_gen_default(self, intervals, typ='P', order=1):
        """
        creates a square with sides of 1, divided by intervals
        by default the type of the volume associated with the mesh
        is considered to be Lagrangian, with order 1.
        """
        self._mesh = FEN.UnitSquareMesh(intervals,intervals) 
        self.input['mesh'] = self._mesh
        self._V = FEN.FunctionSpace(self._mesh, typ, order)
        self.input['V'] = self._V
        self._u = FEN.TrialFunction(self._V)
        self._v = FEN.TestFunction(self._V)


    def BC_default(self,x,on_boundary):
        """
        return the geometrical boundary 
        """
        return on_boundary


    def write_vtk(self):
        """
        write the output
        """
        vtkfile = FEN.File(self._vtk_filename)
        vtkfile << self._u

    def run_static(self):
        """
        solve a PDE based on 'a=L' using u and v as trial and test function respectively
        u is the desired unknown and L is the known part.
        """
        if self._mesh == None:
            print("Fatal error: no mesh is defined")
        if self._L == None:
            print("Fatal error: the bilinear form is not defined; no L defined")
        if self._a == None:
            print("Fatal error: the linear form is not defined; no a defined")
        if self._V == None:
            print("Fatal error: the volume is not defined; no V defined")
        if self._BC == None:
            print("Fatal error: the BC is not defined")
        self._u = FEN.Function(self._V)
        FEN.solve(self._a == self._L, self._u, self._BC)
        with self.project_hdf5.open("output/generic") as h5out: 
             h5out["u"] = self._u.compute_vertex_values(self._mesh)
        #print(type(self._u.compute_vertex_values(job._mesh)))
        self.write_vtk()
        self.status.finished = True
    
    def plot_u(self):
        FEN.plot(self._u)
        #FEN.plot(self._mesh)
    def plot_mesh(self):
        FEN.plot(self._mesh)
        #FEN.plot(self._mesh)