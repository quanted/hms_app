"""
HMS Hydrodynamic module content
"""


header = 'HMS: Hydrodynamics'

description = "<p>The movement of water through a surface water system connects excess precipitation to the oceans in " \
              " completing the hydrological cycle. Being able to model this movement allows one to " \
              " predict and trace the flow of water through a hydrologic system. Determining the flow rate through" \
              " a stream segment is a central task of " \
              " surface water hydrology studies looking at erosion, pollution concentrations, and flooding occurrences " \
              " among many things. Flow in a stream network can be described as the product of the cross-sectional area" \
              " of the stream channel and the velocity of water moving through the system." \
              "\[Q=vA_c\]</p>" \
              " <p>The governing equation to simulate the flow of water is the continuity equation. Some more " \
              "complex models use the continuity and the momentum equations. " \
              "<p>The Continuity Equation : \( {\partial Q \over \partial x} + {\partial A_c \over \partial t} = 0\) " \
              "The Momentum Equation: \( S_f=S_o - {\partial y \over\partial x} - {V\partial V \over g\partial x} - " \
              "{\partial V\over g\partial t}\)<p>" \
              "<p>The constant volume flow routing option keeps the same volume of water throughout the system " \
              "The equation used for determining outflow is \(Q_{out}= \sum Q_{in}\) <p>" \
              "<p>The changing volume option allows depth, velocity, volume, and area to change based on user defined " \
              "channel geometries.  <p>" \
              "<p>The kinematic wave option used both the continuity and momentum equations to translate a flood wave " \
              "through a system. The equation to find the outflow at a given time and stream segment is:  \[Q_{i, t+1}" \
              "= {-(Q_{i,t} - Q_{i-1,t+1}) \over \Delta x \\alpha \\beta ({Q_{i,t+1}^*})^{\ beta-1}} \Delta t + Q_{i,t}\]"




unknown_description = '<p>There is nothing for you here!</p>'

constantvolume_description = "<p>Constant volume flow routing is the simplest of the three options presented. Outflow " \
                             " \(Q_{out}\) from a segment is equal to the sum of inflows \(Q_{in}\) to that segment " \
                             " agreeing with the conservation of mass equation. Any change in flow anywhere translates " \
                             " throughout the entire system instantaneously. Volume, velocity, and depth " \
                             " do not change with flow adjustments. By applying the conservation of mass to the " \
                             " channel system you get: </p>" \



changingvolume_description = "<p>For the changing volume routing option, flow is propagated instantaneously as it is " \
                             " with constant volume routing using the continuity equation. " \
                             "  Volume, velocity, area, and depth can vary throughout " \
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
