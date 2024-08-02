#######################################################
# Example python script for
# making slices and projections.
# This is just the same as the
# code in the jupyter notebook,
# copied and pasted into an empty file
########################################################


import yt 



# code for loading in datasets and turning into slices and projections (mass weighted)



yt.enable_parallelism()



#list of fields I'm interested in 

fields = ['density', 'temperature', 'metallicity', 'entropy', 'radial_velocity', 'cooling_time']



#make the timeseries

ts = yt.load("/mnt/research/galaxies-REU/sims/claire_isogal_sims/newCGM_h2sf_no-ramp/DD????/DD????")



#loop through all the snapshots in the sim (make sure to check first and edit this before running it)

for ds in ts.piter():

   

    filename = ds.filename.split('/')[-1]

    

    #make a sphere and cylinder to make slices and projections. Radius may change depending on sim used

    mysphere = ds.sphere([0.5,0.5,0.5], (206,'kpc'))

    myxcylinder = ds.disk([0.5,0.5,0.5], [1,0,0], (206,'kpc'), (206,'kpc'))

    myzcylinder = ds.disk([0.5,0.5,0.5], [0,0,1], (206,'kpc'), (50,'kpc'))



    #loop through all the fields you want

    for field in fields:



        #need to make an x sliceplot of field

        s = yt.SlicePlot(ds, 'x', ('gas', field), data_source=mysphere, center = [0.5,0.5,0.5], width=(412,'kpc'))

        s.annotate_timestamp(text_args={'color':'dimgray'})

        

        #need to set colorbar to stay constant. May need to add or change if have more/different fields

        if field == 'density':

            s.set_zlim(("gas", field), zmin=(1e-31, "g/cm**3"), zmax=(1e-26, "g/cm**3"))

        elif field == 'temperature':

            s.set_zlim(("gas", field), zmin=(1e4, "K"), zmax=(1e7, "K"))

        elif field == 'metallicity':

            s.set_log('metallicity', False)

            s.set_zlim(('gas', field), zmin=(0, 'Zsun'), zmax=(6, 'Zsun'))

        elif field == 'entropy':

            s.set_zlim(("gas", field), zmin=(1e0, "cm**2*keV"), zmax=(1e6, "cm**2*keV"))

            s.set_cmap(('gas', 'entropy'), 'plasma')

        elif field == 'radial_velocity':

            s.set_log('radial_velocity', False)

            s.set_unit('radial_velocity', 'km/s')

            s.set_zlim(("gas", "radial_velocity"), zmin=(-5e2, "km/s"), zmax=(5e2, "km/s"))

            s.set_cmap('radial_velocity', 'coolwarm')

        elif field == 'cooling_time':

            s.set_unit(field, 'Myr')

            s.set_zlim(("gas", field), zmin=(1e0, "Myr"), zmax=(1e9, "Myr"))

        

        #save the slice

        s.save("newCGM_noramp_"+str(field)+"_slice_x_snapshot_"+filename+".png")

        

###########################################

        

        #need to make a z sliceplot of field

        s = yt.SlicePlot(ds, 'z', ('gas', field), data_source=mysphere, center = [0.5,0.5,0.5], width=(412,'kpc'))

        s.annotate_timestamp(text_args={'color':'dimgray'})

        

        #need to set colorbar to stay constant. May need to change if have more/different fields

        if field == 'density':

            s.set_zlim(("gas", field), zmin=(1e-31, "g/cm**3"), zmax=(1e-26, "g/cm**3"))

        elif field == 'temperature':

            s.set_zlim(("gas", field), zmin=(1e4, "K"), zmax=(1e7, "K"))

        elif field == 'metallicity':

            s.set_log('metallicity', False)

            s.set_zlim(('gas', field), zmin=(0, 'Zsun'), zmax=(6, 'Zsun'))

        elif field == 'entropy':

            s.set_zlim(("gas", field), zmin=(1e0, "cm**2*keV"), zmax=(1e6, "cm**2*keV"))

            s.set_cmap(('gas', 'entropy'), 'plasma')

        elif field == 'radial_velocity':

            s.set_log('radial_velocity', False)

            s.set_unit('radial_velocity', 'km/s')

            s.set_zlim(("gas", "radial_velocity"), zmin=(-5e2, "km/s"), zmax=(5e2, "km/s"))

            s.set_cmap('radial_velocity', 'coolwarm')

        elif field == 'cooling_time':

            s.set_unit(field, 'Myr')

            s.set_zlim(("gas", field), zmin=(1e0, "Myr"), zmax=(1e9, "Myr"))

        

        #save the slice

        s.save("newCGM_noramp_"+str(field)+"_slice_z_snapshot_"+filename+".png")

            

#########################################            

               

        #now do the same but with mass weighted projections

        

        

        

        #need to make an x projection of field

        p = yt.ProjectionPlot(ds, 'x', ('gas', field), weight_field=('gas', 'mass'), data_source=myxcylinder,

                              center = [0.5,0.5,0.5], width=(412, 'kpc'))

        p.annotate_timestamp(text_args={'color':'dimgray'})

        

        #need to set colorbar to stay constant. May need to add or change if have more/different fields

        if field == 'density':

            p.set_zlim(("gas", field), zmin=(1e-31, "g/cm**3"), zmax=(1e-26, "g/cm**3"))

        elif field == 'temperature':

            p.set_zlim(("gas", field), zmin=(1e4, "K"), zmax=(1e7, "K"))

        elif field == 'metallicity':

            p.set_log('metallicity', False)

            p.set_zlim(('gas', field), zmin=(0, 'Zsun'), zmax=(6, 'Zsun'))

        elif field == 'entropy':

            p.set_zlim(("gas", field), zmin=(1e0, "cm**2*keV"), zmax=(1e6, "cm**2*keV"))

            p.set_cmap(('gas', 'entropy'), 'plasma')

        elif field == 'radial_velocity':

            p.set_log('radial_velocity', False)

            p.set_unit('radial_velocity', 'km/s')

            p.set_zlim(("gas", "radial_velocity"), zmin=(-5e2, "km/s"), zmax=(5e2, "km/s"))

            p.set_cmap('radial_velocity', 'coolwarm')

        elif field == 'cooling_time':

            p.set_unit(field, 'Myr')

            p.set_zlim(("gas", field), zmin=(1e0, "Myr"), zmax=(1e9, "Myr"))

        

        #save the projection

        p.save("newCGM_noramp_"+str(field)+"_projection_x_snapshot_"+filename+".png")



########################################

    

        #need to make a z projection of field

        p = yt.ProjectionPlot(ds, 'z', ('gas', field), weight_field=('gas', 'mass'), data_source=myzcylinder,

                              center = [0.5,0.5,0.5], width=(412, 'kpc'))

        p.annotate_timestamp(text_args={'color':'dimgray'})

        

        #need to set colorbar to stay constant. May need to change if have more/different fields

        if field == 'density':

            p.set_zlim(("gas", field), zmin=(1e-31, "g/cm**3"), zmax=(1e-26, "g/cm**3"))

        elif field == 'temperature':

            p.set_zlim(("gas", field), zmin=(1e4, "K"), zmax=(1e7, "K"))

        elif field == 'metallicity':

            p.set_log('metallicity', False)

            p.set_zlim(('gas', field), zmin=(0, 'Zsun'), zmax=(6, 'Zsun'))

        elif field == 'entropy':

            p.set_zlim(("gas", field), zmin=(1e0, "cm**2*keV"), zmax=(1e6, "cm**2*keV"))

            p.set_cmap(('gas', 'entropy'), 'plasma')

        elif field == 'radial_velocity':

            p.set_log('radial_velocity', False)

            p.set_unit('radial_velocity', 'km/s')

            p.set_zlim(("gas", "radial_velocity"), zmin=(-5e2, "km/s"), zmax=(5e2, "km/s"))

            p.set_cmap('radial_velocity', 'coolwarm')

        elif field == 'cooling_time':

            p.set_unit(field, 'Myr')

            p.set_zlim(("gas", field), zmin=(1e0, "Myr"), zmax=(1e9, "Myr"))

        

        #save the projection

        p.save("newCGM_noramp_"+str(field)+"_projection_z_snapshot_"+filename+".png")
