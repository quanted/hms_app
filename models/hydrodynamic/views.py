"""
HMS Hydrodynamic module content
"""


header = 'HMS: Hydrodynamics'
description = "<p>The movement of water through a surface water system connects excess precipitation to downstream" \
              " water bodies, like oceans and lakes. Being able to model this movement allows one to " \
              " predict and trace the flow of water through a hydrologic system. Determining the flow rate through" \
              " a stream segment is a central task of " \
              " surface water hydrology studies looking at erosion, pollution concentrations, and flooding occurrences " \
              " among many things. The governing equation to simulate the flow of water is the continuity equation." \
              " Complex models use the continuity and the momentum equations.</p> " \
              "<p>The Continuity Equation : \( {\partial Q \over \partial x} + {\partial A_c \over \partial t} = 0\) " \
              "The Momentum Equation: \( S_f=S_o - {\partial y \over\partial x} - {v\partial v \over g\partial x} - " \
              "{\partial v\over g\partial t}\)</p>" \
              "<p>The <b>constant volume</b> flow routing option keeps the same volume of water throughout the system" \
              " by using the a mass balance.</p> " \
              "<p>The <b>changing volume</b> option allows depth, velocity, volume, and area to change depending on " \
              "user defined channel geometries.  </p>" \
              "<p>The <b>kinematic wave</b> option used both the continuity and momentum equations to translate a flood wave " \
              "through a system. This is a more complex model with many changing variables.  </p>"\
              '<img src="/static_qed/hms/images/inputs_table.png" alt="Model Input Table" style="">'



unknown_description = '<p>There is nothing for you here!</p>'

constantvolume_description = "<p>Constant volume flow routing is the simplest of the options presented. Outflow " \
                             " \(Q_{out}\) from a segment is equal to the sum of inflows \(Q_{in}\) into that segment " \
                             " agreeing with the conservation of mass equation. Any change in inflows anywhere translates " \
                             " throughout the entire system instantaneously. Volume, velocity, width, and depth " \
                             " do not change with flow adjustments. By applying the conservation of mass to the " \
                             " channel system you get:\[Q_{out}= \sum Q_{in}\] " \
                             " <p>Constant volume routing models can be applied anywhere to study the movement of " \
                             "water through a system because stream characteristics are not needed. " \
                             "<p>The only input needed for the Constant Volume Option is a Boundary Flow (m3/s).</p>" \



changingvolume_description = "<p>For the changing volume routing option, flow is propagated instantaneously as it is " \
                             " with constant volume routing using the continuity equation. " \
                             "  However, in this method volume, velocity, area, and depth change as flow changes. " \
                             "  Using a discharge-water depth relationship; volume, velocity, area," \
                             "  and depth are calculated depending on the geometry of the stream. </p>" \
                             "<p>Changing volume routing methods are useful when the model time step is smaller than the" \
                             " time it takes for a flow wave to move through the system. For example; if the model time" \
                             " step is hourly and the flow wave moves through the system in one day, specific details" \
                             " from more complex models are unnecessary because the volume changes only slightly in" \
                             " the model time step. </p>" \
                             "<p>Inputs for this option include a Boundary flow (m3/s), stream segment length (m)," \
                             " bottom width (m), z-slope of channel geometry, the depth multiplier, and a depth exponent."\



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
                            "\[Q_{i, t+1}= {-(Q_{i,t} - Q_{i-1,t+1}) \over \Delta x \\alpha \\beta ({Q_{i,t+1}^*})^" \
                            "{\ beta-1}} \Delta t + Q_{i,t}\]"\
                            "<p>The complex kinematic wave routing option is useful when detailed information about the" \
                            " stream system is provided and when travel time of flow is important. </p>" \

constantvolume_algorithm_description = "<p>The constant volume option uses the conservation of mass equation to determine" \
                                       " outflow as the sum of inflows. Volume, velocity, width, and depth remain" \
                                       " constant in this model." \
                                       " \[Q_{out}= \sum Q_{in}\] </p>"\
                                       '<img src="/static_qed/hms/images/constant.png" alt="Constant Volume Routing" style="">'

changingvolume_algorithm_description = "<p> Using a discharge-water depth relationship; volume, velocity, area, and" \
                                       " depth are calculated for each change in flow depending on the geometry of" \
                                       " the stream. A rectangle, triangle, and trapezoid shape are options for" \
                                       " channel geometries. A flow-depth regression model based on the " \
                                       " log of empirical observations is needed to solve the power function \(d=yQ^c\)." \
                                       " Where d is depth [m], Q is discharge [m3/s], y and c are constants calculated" \
                                       " by the regression model using observed data. Y and c are used as inputs into" \
                                       " the model as the depth multiplier and exponent. Plotting the log of the equation" \
                                       " gives:\[log (d)=c*\log (Q) + \log (y)\]"\
                                       '<img src="/static_qed/hms/images/flow_regression.png" alt="Depth Flow Regression" style="">'

kinematicwave_algorithm_description = "<p>  This is where the full kinematic wave algorithm will go. \[Q_{i, t+1}" \
                                      "= {-(Q_{i,t} - Q_{i-1,t+1}) \over \Delta x \\alpha \\beta ({Q_{i,t+1}^*})^" \
                                      "{\ beta-1}} \Delta t + Q_{i,t}\]</p> "