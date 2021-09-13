def pload_vtk(file_name, input_directory):
    """Read VTK file and returns the variables as 1D vectors"""

    input_directory=input_directory
    file_name = file_name

    reader= vtk.vtkDataSetReader()
    reader.SetFileName(input_directory+file_name)
    reader.ReadAllVectorsOn()
    reader.ReadAllScalarsOn()
    reader.Update()

    data = reader.GetOutput() 
    dens = data.GetCellData().GetArray("rho")
    pres = data.GetCellData().GetArray("prs")
    trac = data.GetCellData().GetArray("tr1")
    vel1 = data.GetCellData().GetArray("vx1")
    vel2 = data.GetCellData().GetArray("vx2")
    vel3 = data.GetCellData().GetArray("vx3")

    rho = np.array(dens)
    prs = np.array(pres)
    tr1 = np.array(trac)
    vx1 = np.array(vel1)
    vx2 = np.array(vel2)
    vx3 = np.array(vel3)

    temp = 1.203E+6*prs*6.724418E-01/rho
    rho = rho*1.115E-26
    vx1 = vx1*1.000E+07
    vx2 = vx2*1.000E+07
    vx3 = vx3*1.000E+07
    
    return rho, prs, tr1, vx1, vx2, vx3, temp
