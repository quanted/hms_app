"""
HMS Hydrodynamic module content
"""

header = 'HMS: hydrodynamics'

description = "<p>The movement of water through a surface water system connects excess precipitation to the oceans in " \
              " completing the hydrological cycle. Figure 1 shows the connection from precipitation to surface runoff to " \
              " streamflow inside of a watershed. Surface water systems have great importance because they provide " \
              " drinking water, electricity, and recreation for people. Being able to model this movement allows one to " \
              " predict and trace the flow of water through a hydrologic system. Simulating flow throughout a stream " \
              " network of a watershed, not only at a pour point of a watershed, is essential for studying water quality " \
              " and quantity issues in a stream. Determining the flow rate through a stream segment is a central task of " \
              " surface water hydrology studies looking at erosion, pollution concentrations, and flooding occurrences " \
              " among many things. </p>" \
                ' <img src="http://latex.codecogs.com/gif.latex?1+sin(x)" border="0"/>'


unknown_description = '<p>There is nothing for you here!</p>'

constantvolume_description = "<p>Constant volume flow routing is the simplest of the three options presented. Outflow " \
                             " (Q_out) from a segment is equal to the sum of inflows (Q_in) to that segment agreeing " \
                             " with the conservation of mass equation. Any change in flow anywhere translates " \
                             " throughout the entire system instantaneously (Figure 2a). Volume, velocity, and depth " \
                             " do not change with flow adjustments. By applying the conservation of mass to the " \
                             " channel system you get: </p>" \
                               '<img src="/static_qed/hms/images/constant_volume_temp.png" alt="Constant Flow ' \
                             ' Schematic" style="">'


changingvolume_description = "<p>For the changing volume routing option, flow is propagated instantaneously as it is " \
                             " with constant volume routing using the continuity equation. The difference between the " \
                             " two hydrological methods is how volume, velocity, area, and depth can vary throughout " \
                             " the system in the changing volume routing method. Using a discharge-water depth " \
                             " relationship; volume, velocity, area, and depth are calculated for one of three channel " \
                             " shapes with user-defined geometries. The user chooses between a rectangle, triangle, " \
                             " and trapezoid shape for each stream segment. A flow-depth regression model based on the " \
                             " log of empirical observations is needed to solve the power function below. </p>"



kinematicwave_description = "<p>The kinematic wave routing scheme is the most complex of the routing methods described " \
                            " because it provides a more realistic flow simulation. This hydraulic method adopts the " \
                            " idea that the natural movement of flood waves is governed mostly by the friction and " \
                            " bed slopes. Kinematic wave models assume the pressure term, the convective acceleration, " \
                            " and the local acceleration terms of the momentum equation to be insignificant, thus only " \
                            " gravity and friction forces are used. Unlike the other routing schemes, kinematic waves " \
                            " are not instantaneous; the waves propagate downstream. This routing scheme translates a " \
                            " flood wave through the system with no attenuation of the peak flow. The implementation " \
                            " of the continuity and momentum equations in the kinematic wave routing scheme is " \
                            " represented below. </p>" \
