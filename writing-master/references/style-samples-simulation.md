# Master Style Samples: Simulation Chapter

This file stores a second authoritative writing exemplar for `writing-master`.

It is co-equal with `references/style-samples.md`, and the English was revised by the same editor as the preface exemplar.

## Usage

- Treat this sample and `references/style-samples.md` as parallel highest-priority style standards.
- Use this file to learn how the same editor handles explanatory prose, method introduction, chapter-level progression, and technically dense discussion.
- Never reuse its factual content in unrelated writing.
- When a draft involves simulation methods, CFD, DEM, CFD-DEM, or chapter-style technical exposition, consult this sample alongside the preface sample.

## Source note

Expert-revised bilingual chapter sample supplied by the user. The English reflects the same editor behind the preface exemplar, but in a more method-focused and chapter-structured register.

Style cues:
- Tone: formal, explanatory, technically dense, and controlled
- Sentence rhythm: medium-to-long sentences with explicit logical linkage and restrained emphasis
- Logic: clear movement from concept to mechanism, then to modeling choices, limitations, and application context
- Exposition: strong at definition-to-principle progression, method comparison, and chapter-scale instructional flow
- Lexicon: precise simulation terminology with stable field-standard naming
- Rhetoric: serious and non-decorative, with transitions that carry argument rather than ornament

## Cleaned Bilingual Sample

化学工程中，反应器研发的核心目标之一是放大。在工业生产中，从运营效率和经济效益的角度来看，提高单位时间内的产量至关重要，因此工厂设备的规模总是不断增大。以流化催化裂化装置为例，其放大过程通常分为四个阶段：从实验室规模到中试规模的放大倍率通常为5到10倍；从中试规模到示范规模则需要进一步放大20到50倍；最终，从示范规模到商业装置规模的放大倍率可达50到150倍。

In chemical engineering, a central objective of reactor research and development is scale-up. In industrial production, maximizing the output per unit time is essential for operational efficiency and economic viability. Consequently, the size of industrial equipment continues to increase. Taking fluid catalytic cracking (FCC) units as an example, the scale-up process is typically divided into four stages: the transition from laboratory to pilot scale with a scale-up ratio of about 5 to10, from pilot scale to demonstration scale, a further scale-up of 20 to 50 times is required, and finally, from demonstration to full commercial scale , the scale-up factor can reach 50 to 150.

与固定床反应器不同，流化床反应器内的气体和颗粒均处于运动状态。由于颗粒之间以及气体与颗粒之间的复杂相互作用，反应器内会形成不均匀的流动结构，如气泡、颗粒聚团等介观尺度结构。这些介观尺度结构在很大程度上主导了反应器内动量、热量和质量的传递过程以及化学反应的进行。

In contrast to fixed-bed reactors, both the gas and solid particles in fluidized-bed reactors are in continuous motion. Due to complex inter-particle and gas-particle interactions, heterogeneous flow structures, such as bubbles and particle clusters, are formed within the reactor. These meso-scale structures largely govern the transport of momentum, heat, and mass, as well as the progression of chemical reactions in the reactor.

流化床反应器运行时形成的介观尺度结构受到多种因素的显著影响，包括操作条件、床体尺寸、内部构件设计、进料方式和全床的压力平衡等。在设备放大的过程中，这些因素往往会发生显著变化，从而进一步影响反应器内的局部传递过程与反应行为，导致反应器整体性能难以准确预测。这种复杂的多尺度、多因素耦合作用，使得流化床反应器的放大成为化学工程中一项极具挑战性的任务。

The meso-scale structures formed during the operation of fluidized-bed reactors are significantly influenced by a variety of factors, including operating conditions, bed dimensions, internal structural design, feed introduction methods, and the global pressure balance of the bed. During the scale-up process, these factors often undergo substantial changes, which in turn alter local transport processes and reaction behavior within the reactor, thereby making it difficult to accurately predict overall reactor performance. This complex coupling of multiple scales and factors makes the scale-up of fluidized-bed reactors a highly challenging task in chemical engineering.

一百年前，流化床反应器的研发进展主要依赖反复试验，而非系统的理论方法。尽管流化床在工业应用中具备诸多优势，但其开发所需的高额资金和长周期成为普及的重要障碍。从二十世纪四十年代起，学术界和工业界开始对流化床内部的流动特性和放大规律展开研究。从六十年代到九十年代，研究重点逐渐扩展到气泡行为、密相行为、气体分布器设计、颗粒夹带率、夹带分离高度等方面，并运用无量纲分析等方法指导放大过程。同时，研究者们在流化床反应器放大研究中逐步建立了不同类型的模型，最初采用简单模型，后来发展出更加精细的分区模型。

A century ago, advancements in the development of fluidized bed reactors relied primarily on trial-and-error experiments rather than systematic theoretical approaches. Although fluidized beds offer numerous advantages in industrial applications, the prohibitive capital investment and prolonged development cycles constituted significant obstacles to their widespread adoption. Since the 1940s, researchers in academia and industry have investigated the flow characteristics and scale-up principles of fluidized beds. From the 1960s to the 1990s, the research scope gradually expanded to include more details, such as bubble dynamics, dense-phase behavior, gas distributor design, transport disengagement height, and entrainment rate. Dimensionless analysis was also employed to guide the scale-up process. Simultaneously, researchers developed various modeling frameworks for scale-up. Early iterations utilized simplistic models, which later evolved into more refined compartment models.

根据流化床的流动特性，分区模型将流化床中的颗粒与气体混合物按特征划分为不同的"流动相"，并分别捕捉各相内部及相间的流动与传递特性。此类模型基于成熟的反应器模型构建，并结合实验数据，使计算过程简便，且常能获得解析解。由于分区描述方式能够很好地契合流化床的流动特征，同时计算简洁高效，分区模型得到了广泛认可并持续发展。

Based on the flow characteristics of fluidized beds, the compartment model classifies the gas-particle mixture into distinct "flowing phases" according to their features. It captures both the internal flow dynamics within each phase and the interphase transport between them. Built upon established reactor models and integrated with empirical correlations, these models achieve a balance between physical accuracy and computational tractability, often yielding analytical solutions. Because this compartmentalized approach maps effectively to the inherent flow behavior of the bed while remaining computationally efficient and simplistic, compartment models have gained broad recognition and continue to undergo active development.

在较低气速下，两相理论首先被提出来描述传统气固流化床反应器。如第5章所讨论的，当气速超过最小流化速度时，"额外"的气体会聚集成气泡并穿过流化床层，而床层其余部分则被认为保持在最小流化状态。基于这一流动特征，反应器内的流动可分为气泡相和密相。密相通常使用全混流反应器模型进行描述；而气泡相的行为则采用分离式平推流流反应器模型进行描述。两相之间存在质量交换。该模型即为两相流模型，其示意图见图9-1。与此两相流模型类似的还有第4章中介绍的广义尾涡模型。

At relatively low gas velocities, the two-phase theory was introduced to describe conventional gas-solid fluidized bed reactors. As discussed in Chapter 5, when the gas velocity exceeds the minimum fluidization velocity, the "excess" gas coalesces into bubbles that rise through the fluidized bed, while the rest of the bed remains in a minimum fluidization state. Based on this flow characteristic, the flow in the reactor can be divided into a bubble phase and the dense phase. The dense phase is typically modeled as a continuous stirred tank reactor (CSTR), which is a well-mixed system, while the bubble phase is described using a segregated plug-flow reactor model (PFR), reflecting the movement of gas bubbles through the bed. Mass exchange occurs between these two phases. This model is referred to as the two-phase model, shown in Figure 9-1. A similar two-phase flow model is the generalized wake model introduced in Chapter 4.

在较高气速下，环核模型被提出来描述循环流化床反应器。如第6章所讨论的，在循环流化床上行床反应器内的床体被划分为靠近边壁的环区和靠近中轴线的核区。在核区，颗粒含量较低，气体与颗粒以较高速度向上运动。在环区，受壁面摩擦作用影响，颗粒运动速度降低。根据不同的操作条件，颗粒可能缓慢上升或下行，气体则以较低速度与颗粒同向流动，从而导致该区域固含率相对较高。此外，气体和颗粒会在两个区域之间发生相互交换。描述这一现象而发展出的模型被称为环核模型，其示意图见图9-2。

At higher gas velocities, the core-annulus model was introduced to describe circulating fluidized bed reactors. As discussed in Chapter 6, the bed in a circulating fluidized bed riser reactor is divided into an annular region near the wall and a core region near the central axis. In the core region, the particle concentration is low, and both gas and particles move upward at high velocities. In the annular region, particle velocity is reduced due to wall friction. Depending on operating conditions, particles may ascend or descend slowly, while the gas flows in the same direction at a lower velocity, leading to a relatively higher solids concentration. Additionally, gas and particles are exchanged between the two regions. The model developed to describe this phenomenon is known as the core-annulus model, as illustrated in Figure 9-2.

以两相流模型和环核模型为代表的分区模型，在流化床反应器早期研究与设计中发挥了重要的理论作用，为气固两相流动的理解与预测提供了框架。这些模型既支撑了反应器放大设计，也深化了对反应器行为及其底层机理的认识。然而，随着研究的不断深入，分区模型由于没有考虑动态瞬时介观尺度流动结构的变化，限制了其对复杂流动现象的描述能力，从而在一定程度上阻碍了模型的普适性和对流化床的进一步研究。

Compartment models, represented by the two-phase flow model and the core--annulus model, played a vital theoretical role in the early research and design of fluidized-bed reactors, providing a framework for understanding and predicting gas-solid two-phase flow. These models not only underpin reactor scale-up design, but also deepen the understanding of reactor behavior and its underlying mechanisms. However, as research has progressed, the inability of compartment models to account for dynamic and instantaneous changes in meso-scale flow structures has limited their capacity to describe complex flow phenomena. Consequently, this has, to a certain extent, hindered the universality of these models and the further study of fluidized beds.

在二十世纪六十年代，随着电子计算机的兴起，航空航天领域的研究者率先引入数值模拟方法以求解工程问题。随着计算机性能的提升、算法的优化以及新模型的不断发展，数值模拟方法逐步拓展至各类工程场景和系统的研究。到了二十世纪八十年代，该方法自然也被应用于多相流体系中的流态化现象。相比于分区模型，数值模拟方法的最大优势在于能够捕捉反应器从启动到稳态的整个演化过程，精确呈现各时间点的空间状态。

In the 1960s, with the rise of electronic computers, aerospace researchers were the first to introduce numerical simulation methods to solve engineering problems. As computational power increased, algorithms were optimized, and new models were continuously developed, numerical simulation gradually to the study of various engineering scenarios and systems. By the 1980s, these methods were naturally applied to the study of the fluidization phenomena within multiphase systems. Compared to compartment models, the greatest advantage of numerical simulation lies in its ability to capture the entire evolution of a reactor from startup to steady state, providing a detailed and accurate spatial distribution at every time step.

数值模拟方法是一类方法的统称，包括计算流体力学方法（CFD）、离散元方法（DEM）等。这些方法通过更底层的模型动态捕捉流化床中瞬时的局部介观尺度流动结构，能够对反应器内部的流动、传热、传质以及化学反应过程进行更为精确的模拟与预测。与分区模型相比，这些方法具有更强的普适性，不需要针对不同系统或操作条件分别建立独立的模型，并且可以更加自然地拓展应用到诸如传热、传质和复杂反应等领域。通过精确描述和分析多尺度现象，数值模拟方法能够为反应器的设计与放大提供更科学、更可靠的支持。

Numerical simulation methods encompass a range of approaches, such as the computational fluid dynamics (CFD) and discrete element method (DEM). By utilizing more fundamental models to dynamically capture instantaneous local meso-scale flow structures within fluidized beds, these methods enable more precise simulation and prediction of fluid flow, heat transfer, mass transfer, and chemical reaction processes. Compared to compartment models, these methods are more universally applicable, eliminating the need to develop independent models for different systems or operating conditions. Additionally, they naturally extend to fields such as heat transfer, mass transfer, and complex reactions. By accurately describing and analyzing multi-scale phenomena, numerical simulation methods provide more scientific and reliable support for reactor design and scale-up.

经过一个世纪的发展，对流化床反应器放大规律和模型的深入研究，使现代化学工程师能够省去传统设计中至少一个必需的中间放大单元，从而显著缩短开发周期，并大幅降低成本。这种巨大的效率提升正是驱动流化床反应器模型和模拟技术不断优化与创新的核心动力。

Through a century of development, in-depth research into the scaling laws and models of fluidized bed reactors has enabled modern chemical engineers to eliminate at least one essential intermediate scaling step required in traditional design processes. This optimization has not only significantly shortened the development cycle but also substantially reduced costs. This immense improvement in efficiency serves as the driving force behind the continuous optimization and innovation of fluidized bed reactor models and simulation technologies.

本章将依次介绍气相和颗粒相的模拟方法，并简要阐述两相之间的相互作用机制。通过详细讲解数值模拟方法的基本公式与核心原理，全面展示该方法的优势和特点。随后，将系统总结当前主流的多相流模拟方法，并结合实际案例进行分析，帮助读者更直观地理解这些方法的应用场景与效果。

This chapter will sequentially introduce simulation methods for the gas phase and particle phase and explain the interaction mechanisms between them. Through a detailed explanation of the fundamental equations and core principles of numerical simulation methods, the advantages and characteristics of these methods will be comprehensively demonstrated. Subsequently, the chapter will systematically summarize the current mainstream multiphase flow simulation methods and analyze practical case studies to help readers better understand the application scenarios and effectiveness of these approaches.

读完本章后，读者将对数值模拟方法有清晰的基本认识，熟悉流态化模拟的多种技术路径，理解主流模拟方法的实现过程。这将为读者独立开展流态化模拟研究奠定坚实的理论与实践基础。

By the end of this chapter, readers will have gained a clear understanding of numerical simulation methods, become familiar with various technical approaches for fluidization simulations, and understand the implementation processes of mainstream simulation methods. This will establish a solid theoretical and practical foundation for readers to independently conduct research in fluidization.

# 9.1气相模拟方法

# 9.1 Numerical Simulation Methods for the Gas Phase

在流态化系统中，常用的流体相模拟方法是计算流体力学。近年来，适用于多孔介质和复杂边界的格子玻尔兹曼方法（LBM）也越来越多地被用于模拟颗粒间流动的流体。本节将重点介绍当前应用最广泛的计算流体力学方法，并借助该方法带领读者初步了解数值模拟的基本概念与方法。

In fluidized systems, Computational Fluid Dynamics (CFD) is the most commonly used method for simulating gas phases. In recent years, the Lattice Boltzmann Method (LBM), which is particularly well-suited for porous media and complex boundaries, has also been increasingly applied to simulate gas flow between particles. This section will focus on the CFD method and use it to introduce readers to the fundamental concepts and approaches of numerical simulation.

## 9.1.1 计算流体力学方法的基本原理和优势

## 9.1.1 Fundamental Principles and Advantages of the CFD Method

不同于以宏观结构假设为基础的分区模型，计算流体力学方法直接以基本守恒定律为出发点。这些定律源于最基本的物理原理，具有明确的物理基础和普适性。这些物理定律通常用微分方程表达，例如，流体流动时的动量守恒是由Navier-Stokes式（NS方程）描述的。通过代数变形，可以将其表示成牛顿第二定律 的形式：

Unlike compartment models, which are based on macroscopic structural assumptions, CFD takes the fundamental conservation laws as its point of departure. These laws originate from the most basic principles of physics and possess a clear physical foundation and universality within the continuum framework. These laws are typically expressed as differential equations. For example, the conservation of momentum in fluid flow is described using the Navier-Stokes (NS) equations. Through algebraic manipulation, these can be expressed in the form of Newton's second law, :

式左侧表示流体内部所受的压力、内部应力和外力（如重力）之和，即所有作用在流体上的力 ；右侧的流体密度代表单位体积的质量，括号内的项则表示流体的加速度 。无论研究对象如何变化，NS方程的形式始终保持不变。

The left-hand side of the equation represents the sum of all forces acting on the fluid, , including the pressure, internal stresses, and external forces (such as gravity). On the right-hand side, the fluid density corresponds to the mass term, , while the terms in parentheses represent the acceleration of the fluid, . Regardless of the specific system being studied, the form of the NS equations remains invariant.

除了动量守恒定律，计算流体力学方法中还常用到质量守恒定律、能量守恒定律等基本物理定律。这些定律同样可以用微分方程的形式来描述，其方程形式在不同的研究体系中保持一致。这类微分方程通常被称为控制方程。

In addition to the law of momentum conservation, fundamental physical laws such as the conservation of mass and energy are also commonly used in CFD. These laws can also be expressed in the form of differential equations, and their equations maintain consistent forms across different systems. Such differential equations are commonly referred to as governing equations.

这正是前文提到的数值模拟方法普适性的体现：通过基于最基本的守恒定律来描述系统行为，并以此为基础求解不同体系中的流动和传递过程。研究者无需为每种不同的系统单独提出特定方程，而是能够统一应用这些控制方程。

This exemplifies the universality of numerical simulation methods mentioned earlier: by describing system behavior based on the fundamental conservation laws, it serves as the foundation for solving flow and transport processes across different systems. Researchers do not need to propose specific equations for each unique system. Instead, they can uniformly apply these governing equations.

控制方程能够描述研究系统中的质量守恒、动量守恒和能量守恒，但在大多数非理想情况下，难以获得这些方程的解析解。因此，需要借助数值方法进行求解，例如有限差分法、有限元法和有限体积法等。在下一节中，将通过具体实例更直观地理解控制方程的物理含义和计算流体力学的求解方法，从而更高效地应用计算流体力学，并提高对模拟结果的分析和解读能力。

Governing equations can describe mass conservation, momentum conservation, and energy conservation within a studied system. However, in most non-ideal cases, obtaining analytical solutions for these equations is challenging. Therefore, numerical methods such as the finite difference method, finite element method, and finite volume method are employed for solving them. In the following section, specific examples will be used to provide a more intuitive understanding of the physical meaning of governing equations and the solution methods used in the CFD method This will enable more efficient application of CFD and enhance the capacity for the analysis and interpretation of simulation results.

## 9.1.2 控制方程的物理含义和解的含义

## 9.1.2 Physical Significance of Governing Equations and Their Solutions

控制方程可以从更通用的形式出发进行分析，以深入理解其所描述的内容。控制方程的一般形式为：

Governing equations can be interpreted from a more universal form to gain a deeper understanding of their underlying principles. The general form of the governing equations is:

式中从左到右依次包括瞬态项、对流项、扩散项和源项。这一结构可以通过花香的传播过程生动地理解。金秋时节，一个人站在一棵桂花树旁，他用控制方程描述香气的传播（以 表示花香分子的浓度）。

From left to right, the equation terms represent the transient, convection, diffusion, and source components. This structure can be intuitively conceptualized through the process of fragrance dispersion. In the golden autumn, imagine a person standing near an osmanthus tree, using governing equations to describe the spread of the fragrance (denoted as , representing the concentration of fragrance molecules).

桂花树作为香气的源头，不断向周围释放香气分子，这对应源项。随着时间推移，香气分子沿着浓度梯度从高浓度区域（桂花树附近）向低浓度区域（人的鼻子附近）扩散，逐渐让人隐约闻到花香，这体现了扩散项的作用。当一阵风吹过，香气分子随气流迅速传至鼻前，浓郁的香气瞬间扑面而来，这是对流项的体现。而香气体验的变化过程------从闻不到花香，到隐约闻到，再到浓郁的花香，则通过瞬态项记录鼻子附近香气分子浓度随时间的变化。

The osmanthus tree, as the source of the fragrance, continuously releases fragrance molecules into the surrounding area, which corresponds to the source term. Over time, the fragrance molecules diffuse along the concentration gradient from the high-concentration region near the tree to the low-concentration region near the person's nose, allowing the fragrance to be gradually detected---this illustrates the role of the diffusion term. When a breeze blows, the fragrance molecules are rapidly carried by the airflow to the person, resulting in a sudden, intense scent---this demonstrates the convection term. Finally, the evolution of the sensory experience---from the initial absence of scent to a faint aroma and then to a rich fragrance---is captured by the transient term, which records the change in molecular concentration near the nose over time.

通过这些项的综合作用，控制方程完整地描述了香气分子的生成、扩散、流动以及随时间的动态变化，全面反映了香气分子在空间和时间上的行为。同时，该方程也是对香气分子组分守恒的具体描述。

Through the collective effects of these terms, the governing equation provides a comprehensive description of the generation, diffusion, convection, and dynamic changes of fragrance molecules over time, fully reflecting their behavior in both space and time. Furthermore, this equation also serves as a specific formulation of the species conservation for these molecules.

控制方程最终提供的结果是一种以时空为变量的物理量，称为场。例如，以一个房间为研究对象，在房间内任意空间点上，每一时间点都对应一个特定的温度值。将这些空间位置在不同时间点的温度数据汇总，便可得到房间内的温度场，即一组 数据。基于这些数据，可以直观地绘制出任意时间点的温度分布，并随着时间推进，清晰呈现房间内各空间位置温度的动态变化。这便是这个房间的温度场。

The result provided by governing equations is a physical quantity expressed as a function of space and time, known as a field. For example, consider a room as the subject of study. At any spatial point within the room, each point in time corresponds to a specific temperature value. By compiling the temperature data from various spatial positions over different points in time, one can obtain the temperature field of the room, represented as a set of data. Based on these data, the temperature distribution at any given moment can be visually mapped, and as time progresses, the dynamic evolution of temperature across all spatial locations in the room can be clearly depicted. This constitutes the temperature field of the room.

在研究反应器时，人们通常关注其内部的流场、温度场以及组分浓度场等信息。这些场的信息可以全面反映反应器内部在特定时空条件下的物理和化学行为，从而为反应器的设计与优化提供科学依据，显著简化相关过程。

When studying reactors, researchers typically focus on internal data such as the flow field, temperature field, and component concentration field in the reactor. The information from these fields comprehensively reflects the physical and chemical behaviors within the reactor under specific spatial and temporal conditions. This provides a scientific basis for reactor design and optimization, thereby significantly simplifying the related processes.

控制方程用于描述物理场的行为，通过求解不同的控制方程，可得到相应的场分布结果。那么，物理场的计算是如何实现的呢？可以将控制方程所描述的对象理解为一个固定空间位置的"小框"，即研究系统中的一个固定体积。这个体积足够大，可以容纳足够多的分子以表现出稳定的宏观特性；同时又足够小，使得流体在该体积内的性质可以近似为均匀分布。

Governing equations are used to describe the behavior of physical fields. By solving different governing equations, the corresponding field distributions can be obtained. So how then, is the computation of physical fields implemented? The object described by governing equations can be understood as a "small box" at a fixed spatial location, representing a fixed volume within the studied system. This volume is large enough to encompass a sufficient number of molecules to exhibit stable macroscopic properties, yet small enough for the fluid properties within the volume to be approximated as uniformly distributed.

还是以房间内的温度场为例，图9-3（a）中的"小框"可以视为温度计周围的一小块空间，该空间足够小，可以认为其内部的温度是均匀的。当房间内布置足够多的温度计时[见图9-3（b）]，这些温度计所对应的"小框"将覆盖整个房间，从而记录每个位置的温度信息。控制方程中的瞬态项、对流项、扩散项和源项均以这些小块空间内的物理过程为基础进行描述，每个"小框"对应一个控制方程。通过联立并同时求解所有"小框"所对应的控制方程，即可得到整个房间内的温度分布。再通过对时间步的推进求解，即可得到不同时刻下的房间内的温度分布，即温度场。

Using the room temperature field again as an example, the \"small boxes\" in Figure 9-3(a) can be viewed as tiny spatial regions surrounding a thermometer, small enough that the temperature within it can be considered uniform. When a sufficient number of thermometers are distributed throughout the room [see Figure 9-3(b)], the small boxes corresponding to these thermometers collectively cover the entire room, recording the temperature information at every location. The transient term, convection term, diffusion term, and source term in the governing equations are all described based on the physical processes occurring within these small spatial regions, with each small box corresponding to a governing equation. By simultaneously solving the governing equations for all the small boxes, the temperature distribution across the entire room can be determined. Moreover, by advancing the solution through time steps, the temperature distribution within the room at different moments can be obtained, thereby establishing the temperature field.

在宏观尺度上，物理世界在时空中呈现连续性。例如，房间内的温度会随空间位置的变化和时间的推移而连续变化。然而，在上述描述中，房间被划分为一个个小空间，这些小空间之间的物理性质不再连续。这是因为直接求解控制方程的解析解难度较大，而数值算法提供的解是离散的，即由一系列不连续的点组成。相应地，时间上也存在类似的不连续性。然而，当这些间隔足够小时，离散解可以被视为对真实连续场的合理近似。

On a macroscopic scale, the physical variables exhibit continuity in space and time. For example, the temperature within a room varies continuously as spatial position and time change. However, in the aforementioned description, the room is divided into small spaces, and the physical properties between these regions are no longer continuous. This transition occurs because obtaining analytical solutions directly from governing equations is highly difficult, and the solutions provided by numerical algorithms are discrete, consisting of a series of discontinuous points. Correspondingly, a similar discontinuity exists in time. Nevertheless, when these intervals are sufficiently small, the discrete solution can be considered a reasonable approximation of the real continuous field.

因此，温度计的布置越稀疏，得到的温度场的空间分辨率就越低，所需联立的方程数量也随之减少，但计算结果与真实情况的偏差也会增大。相反，为了描述具有高空间分辨率的温度场，需要联立更多的方程，所得结果也更接近真实情况[见图9-3（c）]。

Therefore, the sparser the distribution of thermometers, the lower the spatial resolution of the resulting temperature field. While the number of equations to be solved decreases accordingly, the deviation of the computational results from the actual situation increases. In contrast, to describe a temperature field with high spatial resolution, a larger number of equations need to be solved, yielding results that are closer to the actual situation [see Figure 9-3(c)].

在控制方程的四项中，瞬态项的计算与前一个时间点的状态相关，扩散项和对流项的计算则与相邻空间点的状态相关。当系统的初始状态和空间边界的条件被定义后，通过数值算法求解控制方程，可以按照时间顺序计算出每个时间点对应的整个空间分布。更具体地说，时间点之间的间隔称为时间步，空间的划分称为网格，初始时刻的状态称为初始条件，定义系统边界的条件称为边界条件，而研究的区域则称为计算域。这些构成了计算流体力学方法的基本原理和核心流程。

Among the four terms of the governing equations, the calculation of transient term is related to the state at the previous point in time, while the calculations of the diffusion term and convection term are related to the states of adjacent spatial points. Once the system's initial state of system and spatial boundary conditions are defined, the governing equations can be solved using numerical algorithms to compute the full spatial distribution corresponding to each point in time in chronological order. Specifically, the interval between time points is called a time step, the division of space is called a mesh, the state at the initial time is called the initial condition, the conditions defining the system's boundaries are called boundary conditions, and the region being studied is referred to as the computational domain. These elements constitute the basic principles and core processes of the CFD method.

## 9.1.3 描述气体流场的控制方程

## 9.1.3 Governing Equations for Gas Flow Fields

综上，若要获取反应器内的流场分布，需要将计算域设定为流化床反应器的内部区域，并给出相应的初始条件和边界条件，结合连续性式（质量守恒）与NS式（动量守恒）进行求解：

In summary, to obtain the flow field distribution within the reactor, the computational domain must be defined as the internal region of the fluidized bed reactor, with the corresponding initial and boundary conditions specified. The solution is then obtained by solving the continuity equation (mass conservation) and the NS equations (momentum conservation):

式（9-3）定义了空间划分中每个网格的质量守恒，描述了网格内流体质量随时间的变化（瞬态项）以及流体流入、流出网格的质量（对流项）。式（9-4）则定义了动量守恒，描述了网格内流体动量随时间的变化（瞬态项）、流入和流出流体引起的动量变化、因周围网格中流速差异和流体黏性对本网格内流体产生的动量变化，以及重力对网格内流体的动量影响。

Equation (9-3) defines the mass conservation for each grid in the spatial division, describing the change in fluid mass within the grid over time (transient term) and the mass of fluid entering or exiting the grid (convection term). Equation (9-4) defines momentum conservation, describing the change in fluid momentum within the grid over time (transient term), the momentum change caused by the fluid entering and exiting the grid, the momentum change within the grid due to velocity differences and fluid viscosity in adjacent grids, and the impact of gravity on the fluid's momentum within the grid.

方程中应力张量，，的表达式展开如下：

The expression for the stress tensor, , in the Equation (9-4) is expanded as follows:

黏度项描述了当前网格中的流体由于相邻网格中不同流动速度造成的摩擦力而产生的动量的变化。在应力张量中， 和 分别代表剪切黏度和体积黏度。剪切黏度引起的动量变化可以类比为一种摩擦力，方向为切向，即平行于流体微元的流动方向。例如，设想两个摞在一起的木块一起向同一方向运动。如果其中一个木块的速度大于另一个木块，由于摩擦力的存在，较慢的木块会受到一个向前的力，而较快的木块则会受到相等大小的反向阻力。体积黏度则反映了流体在压缩或膨胀过程中所产生的黏性效应。可以将其想象为用手指按压一块小果冻，果冻对手指的回弹作用类似于体积黏度对体积变化的阻力。虽然这些类比并不十分严谨，但它们有助于理解动量守恒中黏度的作用。

The viscosity term describes the change in momentum of the fluid within the current grid due to the frictional forces caused by different flow velocities across adjacent grids. In the stress tensor, and represent the shear viscosity and bulk viscosity, respectively. The momentum change induced by shear viscosity can be conceptualized as a frictional force oriented tangentially, i.e., parallel to the direction of flow in the fluid element. For example, imagine two stacked wooden blocks moving in the same direction. If one block moves faster than the other, the slower block will experience a forward force due to friction, while the faster block experiences an equal and opposite resistive force. Bulk viscosity, on the other hand, reflects the viscous effects generated when the fluid undergoes compression or expansion. It can be imagined as pressing a finger into a small piece of jelly, where the jelly's resistance to compression is similar to the resistance that bulk viscosity exerts against volume changes. While these analogies are not perfectly accurate, they help in understanding the role of viscosity in momentum conservation.

在计算流体力学中，应力张量通常通过层流模型或不同的湍流模型进行封闭。尽管经过近两百年的发展，如何有效地描述湍流仍然是一个巨大的难题。幸运的是，在工程应用中已有许多简化模型可以针对不同情况加以应用。如果读者对湍流有兴趣，可以参考《Turbulent Flow》一书。

In the CFD method, the stress tensor is typically closed using either laminar models or various turbulence models. Despite nearly two hundred years of development, the effective description of turbulence remains a major challenge. Fortunately, many simplified models have been developed for engineering applications and can be used under different conditions. Readers interested in turbulence may refer to the book "Turbulent Flow."

通过数值方法同时求解质量守恒方程和动量守恒方程，便得到了流化床内未加入颗粒时流体的流场分布。

By simultaneously solving the mass conservation equation and momentum conservation equation simultaneously using numerical methods, the flow field distribution of the fluid in the fluidized bed in the absence of particles can be obtained.

接下来，将颗粒引入系统。

Next, particles are introduced into the system.

# 9.2 颗粒相的模拟方法

# 9.2 Numerical Simulation Method for the Particle Phase

在介绍具体模型之前，有必要回顾欧拉框架和拉格朗日框架两种视角。在研究连续介质时，欧拉框架的模型和方法最为常用。欧拉框架的视角就像是在某一个固定的坐标位置开了一扇窗，人们从窗口去观察流体流动并记录流动的信息。在上一节中，计算流体力学方法与气体流场的描述便是基于欧拉框架的视角。与之相对，拉格朗日框架则是观察者坐在流体微元上，随着流体一起流动并记录流动的信息。

Before introducing specific models, it is necessary to review the two perspectives of the Eulerian framework and the Lagrangian framework. In the study of continuum mechanics, the models and methods under the Eulerian framework are the most commonly used. The Eulerian perspective is akin to opening a window at a fixed coordinate position, through which one observes and records the flow of the fluid. In the previous section, the CFD methods and the description of the gas flow field were based on the Eulerian perspective. In contrast, under the Lagrangian framework, the observer is assumed to sit on a fluid element, moving with the fluid, and recording the flow information.

借用《Fluid Mechanics》中的例子来进一步说明这两种框架的差异：假设正在研究某一城市区域的交通状况。如果作为一名交通工程师，关注点可能集中在市中心某十字路口，观察该固定位置的交通流动，这对应于欧拉框架；而如果作为一名警察，追踪某辆特定车辆的运动情况，则是采用拉格朗日框架。

To further illustrate the difference between these two frameworks, let's borrow an example from "Fluid Mechanics": Suppose the traffic conditions in a city area are being studied. If, as a traffic engineer, the focus is on a fixed intersection in the city center and the observation of traffic flow at that location, this corresponds to the Eulerian framework. On the other hand, if, as a police officer, the focus is on tracking the movement of a specific vehicle, this corresponds to the Lagrangian framework.

在流化床的实验研究中，这两种视角被广泛应用。例如，通过固定位置的探头采集流化床中的压力波动或固含率，属于基于欧拉框架的研究；而通过放入示踪颗粒并使用高速相机追踪其运动，则是采用拉格朗日框架的研究方法。

In experimental studies of fluidized beds, both perspectives are widely employed. For example, collecting pressure fluctuations or solids holdup in a fluidized bed at fixed locations using probes represents an Eulerian approach, whereas introducing tracer particles and tracking their motion with a high-speed camera corresponds to a Lagrangian approach.

在数值模拟中，连续相一般采用欧拉框架进行建模和求解，而离散相则常用拉格朗日框架。然而，流化床中的颗粒虽本质上是离散的，但在流化状态下却呈现出诸多连续介质的特性。因此，对于颗粒相，既可以采用欧拉框架建模，也可以选择拉格朗日框架。不同的建模方法不仅会影响研究思路，还会对最终的模拟结果产生显著影响。

In numerical simulations, the continuous phase is typically modeled and solved using the Eulerian framework, while the discrete phase is often modeled using the Lagrangian framework. However, although particles in a fluidized bed are inherently discrete, they exhibit many characteristics of a continuous medium in the fluidized state. Therefore, the particle phase can be modeled using either the Eulerian or the Lagrangian framework. Different modeling approaches may affect not only the research methodology but also the final simulation results significantly.

## 9.2.1 离散元方法

## 9.2.1 Discrete Element Method

### 离散元方法的控制方程

### Governing equations of the Discrete Element Method

与前文通过欧拉框架建模得到流体的流场不同，离散元方法（DEM）是一种采用拉格朗日框架的建模方法。在模拟颗粒的运动过程中，离散元方法同步求解颗粒的平移和旋转两种运动状态。其描述颗粒平移的控制方程表达如下:

In contrast to the flow field of the fluid obtained through Eulerian framework modeling, the discrete element method (DEM) is a modeling approach developed under the Lagrangian framework. During the simulation of particle motion, the DEM simultaneously solves for both the translational and rotational motion states of particles. The governing equation describing the translation of particles is given as follows:

式（9-6）中，等号左侧表示颗粒的惯性项，即颗粒质量与加速度的乘积；等号右侧则为颗粒所受的所有外力之和。因此，离散元法中用于描述颗粒平移的控制方程本质上体现了牛顿第二定律：

In Equation (9-6), the left side represents the inertial term of the particle, that is, the product of the particle mass and acceleration; the right side represents the sum of all external forces acting on the particle. Therefore, the governing equation used in the DEM to describe particle translation is essentially an expression of Newton's second law:

颗粒所受的外力在式（9-7）中依次为压力梯度力、重力、与流体相的相互作用力、接触力以及非接触力。其中，接触力是颗粒在直接接触或碰撞时产生的作用力；非接触力则是颗粒在未直接接触时可能存在的远程相互作用力，例如静电力、范德华力等。

The external forces acting on the particle in Equation (9-6) are, in order, the pressure gradient force, gravity, the interaction force between the particle and the fluid phase, contact force, and non-contact force. Among these, the contact forces refer to the forces exerted when particles are in direct contact or collide with one another, while non-contact forces are long-range interactions that may exist even when particles are not in direct contact, such as electrostatic forces and van der Waals forces.

描述颗粒旋转运动状态的控制方程如下所示：

The governing equation describing the rotational motion of the particles is as follows:

式中 是由颗粒接触点的切向作用力产生的力矩，它主导颗粒的旋转运动。力矩的大小和方向取决于切向力的强度以及其作用点到颗粒质心的距离。这一力矩直接影响颗粒绕自身质心的角加速度。是颗粒的转动惯量，它与颗粒的质量以及质量分布相关。转动惯量越大，在相同的力矩作用下，颗粒的角加速度就越小，这反映了颗粒对旋转运动的抵抗能力。因此，该控制方程也可以看作是牛顿第二定律在旋转运动中的表达形式。

where is the torque generated by the tangential forces at the particle contact points, which governs the rotational motion of the particle. The magnitude and direction of the torque depend on the intensity of the tangential force and the distance from the point of application to the center of mass of the particle. This torque directly affects the angular acceleration of the particle around its center of mass. The variable is the moment of inertia, which is related to the mass and mass distribution of the particle. The larger the moment of inertia, the smaller the angular acceleration of the particle under the same torque, reflecting the resistance of the particle to rotational motion. Therefore, this governing equation can also be seen as an expression of Newton's second law for rotational motion.

### 拉格朗日追踪

### Lagrangian Tracking

正如本节开头对欧拉视角和拉格朗日视角的回顾，在离散元方法中，算法直接追踪每一个颗粒的状态。因此，无需对计算域进行空间划分，也即不存在网格的概念。而每个颗粒都需要由一组控制方程来描述其行为。因此，系统中颗粒数量越多，所需同时计算的控制方程也就越多。

As reviewed at the beginning of this section regarding the Eulerian and Lagrangian perspectives, in the DEM, the algorithm directly tracks the state of each particle. Therefore, there is no need to partition the computational domain, meaning that there is no concept of a mesh. Instead, each particle is described by a set of governing equations that characterize its behavior. As a result, the more particles there are in the system, the more governing equations need to be solved simultaneously.

### 颗粒碰撞

### Particle Collisions

在了解了颗粒运动的描述和颗粒追踪之后，离散元方法中另一个重要的组成部分是对颗粒碰撞的建模。最常见的碰撞模型包括硬球模型和软球模型。

After understanding the description of particle motion and particle tracking, another important component of the DEM is the modeling of particle collisions. The most common collision models include the hard-sphere model and the soft-sphere model.

硬球模型将颗粒之间的碰撞视为一个瞬时事件，即碰撞在瞬间发生并完成。碰撞前后的状态变化依据动量和动能守恒定律进行计算。这与高中物理中学习的刚性"小木块"碰撞原理类似。硬球模型的计算开销较低，但由于简化程度较高，也存在一些局限性。例如，它只能描述两个"小球"之间的碰撞，无法处理多颗粒间的复杂碰撞；此外，它仅适用于平移碰撞，无法考虑旋转对碰撞行为的影响。因此，硬球模型通常适用于小球较为稀疏的系统，例如模拟气体分子运动等场景。

The hard-sphere model treats collisions between particles as instantaneous events, meaning that the collision occurs and is completed instantaneously. The changes in state before and after the collision are calculated based on the laws of conservation of momentum and energy. This is similar to the principle of rigid "block" collisions learned in high school physics. The hard-sphere model has a relatively low computational cost, but due to its high level of simplification, it also has some limitations. For example, it can only describe collisions between two "spheres" and cannot handle complex collisions among multiple particles. Additionally, it is only applicable to translational collisions and cannot account for the effect of rotation on collision behavior. Therefore, the hard-sphere model is typically suitable for systems with relatively sparse particles, such as simulations of gas molecule motion.

在现实世界中，物体之间的碰撞并非瞬间完成，而是一个伴随着形变的过程。因此，在典型的流化床系统中，颗粒之间的碰撞以及颗粒与壁面的接触通常采用软球模型进行处理。该模型允许颗粒在接触时发生弹性形变，并通过弹簧-阻尼模型模拟整个碰撞过程，来描述颗粒的弹性接触和能量耗散。

In the real world, collisions between objects do not occur instantaneously but rather take place through a process accompanied by deformation. Therefore, in typical fluidized bed systems, collisions between particles and contacts between particles and the wall are usually modeled using the soft-sphere model. This model allows particles to undergo elastic deformation upon contact and simulates the entire collision process using a spring-dashpot model, thereby describing the particle's elastic contact and energy dissipation.

软球模型的数学表达式如下：

The mathematical expression of the soft-sphere model is as follows:

式中表示碰撞过程中颗粒之间的几何重叠长度，即两个颗粒接触时的相互侵入距离。变量和分别为弹簧系数和阻尼系数，它们是弹簧-阻尼器模型的关键参数，用于描述颗粒在接触和分离过程中的弹性恢复力和能量耗散作用。则表示颗粒间的相对碰撞速度，即两个颗粒在当前瞬时速度的差值。碰撞的示意图见图9-6。

where represents the geometric overlap length between particles during a collision, i.e., the mutual penetration distance when two particles come into contact. The variables and are the spring constant and damping coefficient, respectively, which are key parameters of the spring-dashpot model used to describe the elastic recovery force and energy dissipation during the contact and separation of particles. The expression represents the relative collision velocity between particles, i.e., the difference between the instantaneous velocities of two particles at the current moment. A schematic of the collision is shown in Figure 9-6.

从表达式可以看出，颗粒间的几何重叠距离越大，弹性恢复力就越强，从而导致碰撞后颗粒反弹的过程更加剧烈。同时，碰撞速度越高，阻尼系数产生的能量耗散越显著，颗粒间的阻力作用也会更大。

From the expression, the greater the geometric overlap distance between particles, the stronger the elastic recovery force, thereby resulting in a more pronounced rebound process after the collision. Similarly, the higher the collision velocity, the more significant the energy dissipation caused by the damping coefficient, leading to a stronger resistive effect between the particles.

基于上述分析，可以进一步说明离散元方法对仿真时间步长的严格要求。如果时间步长设置得过大，颗粒在单个时间步内可能移动较长距离，导致颗粒间的接触和重叠（几何侵入距离）超出合理的物理范围。这不仅会使碰撞后的反弹速度不符合实际，还可能破坏系统的整体物理真实性。因此，确保时间步长足够小以精确捕捉颗粒间的接触过程，是离散元方法中至关重要的一项准则。

Based on the above analysis, it can be further deduced that the DEM imposes strict requirements on the simulation time step. If the time step is set too large, particles may move a considerable distance within a single time step, causing their contact and overlap (geometric penetration distance) to exceed reasonable physical limits. This can result not only in unrealistic rebound velocities after collisions but also in the loss of overall physical realism in the system. Therefore, ensuring that the time step is sufficiently small to accurately capture the contact process between particles is a critical principle in DEM.

### 离散元方法面临的挑战

### Challenges of DEM

离散元方法在颗粒系统的模拟中面临两大主要挑战。首先，当颗粒数量较大时，模拟需要处理庞大的方程组和海量颗粒信息，对处理器性能和内存容量提出了极高的要求。以一个容量约为400毫升、直径6厘米、高15厘米的水杯为例，若装满粒径约为200微米的细盐，杯中颗粒数量约为50000000（五千万）。要追踪这些颗粒的运动以及它们之间的相互作用，对当前计算机而言已是极大的挑战。如果将此系统扩展到真实流化床规模，颗粒数量可能达到数十亿级，超出现有计算设备和算法的能力范围。

The DEM faces two major challenges in the simulation of particle systems. First, when the number of particles is large, the simulation must handle massive sets of equations and a large volume of particle data, imposing extremely high demands on processor performance and memory capacity. For instance, consider a cup with a capacity of approximately 400 mL, a diameter of 6 cm, and a height of 15 cm. If filled with fine salt particles of about 200 microns in diameter, the number of particles in the cup would be roughly 50 million. Tracking the motion of these particles and their interactions is already a significant challenge for current computing capabilities. If this system is further scaled up to the size of an actual fluidized bed, the number of particles may reach the order of several billion, exceeding the limits of existing computational equipment and algorithms.

另一个挑战则来自时间步长的精度要求。随着颗粒尺寸的减小，颗粒碰撞后重叠的过程变得极其短暂，重叠距离也更小。因此，模拟需要采用更小的时间步长以准确捕捉这些快速变化的细节。若时间步长设置过大，可能导致颗粒错过碰撞，或产生物理上不合理的过度重叠，从而使模拟失真甚至导致数值崩溃。在气固流态化系统中，DEM模拟通常需要时间步长小于10^-5^至10^-6^秒。然而，对于需要数秒乃至几十秒才能达到稳定状态的系统，这意味着模拟过程中需要数百万甚至上亿次的时间步计算，极大地消耗计算资源和时间。

Another challenge arises from the precision requirements for the time step. As particle size decreases, the overlap process following particle collisions becomes extremely brief, and the overlap distance becomes smaller. Consequently, the simulation requires smaller time steps to accurately capture these rapid changes. If the time step is set too large, particles may miss collisions or experience physically unrealistic excessive overlaps, leading to distorted simulations or even numerical instabilities. In gas-solid fluidized systems, DEM simulations typically require time steps smaller than 10^-5^ to 10^-6^ seconds. However, for systems that take several seconds or even tens of seconds to reach a steady state, this translates to millions or even billions of time step calculations, resulting in very high computational cost in terms of both resources and time.

针对这些困难，目前存在两种潜在的解决方案。一种方法是采用粗粒化技术，用一个"颗粒团"代表一定数量的颗粒，从而显著减少颗粒数量并降低计算资源的需求。然而，这种方法需要重新定义颗粒间的相互作用模型，如碰撞和摩擦，并对其准确性进行验证。另一种解决方案是将颗粒追踪和碰撞计算部署在GPU上，而非传统的CPU。GPU拥有大量核心，虽然单个核心的计算能力相对较弱，但其多核并行特性特别适合处理颗粒运动和碰撞的计算任务，从而大幅提升计算速度。

To address these challenges, two potential solutions currently exist. One approach is to use coarse-graining particle techniques, in which a "particle parcel" represents a certain number of particles, thereby significantly reducing the particle count and demand for computational resources. However, this method requires redefining the interaction models between particles, such as collision and friction, and validating their accuracy. Another solution is to perform particle tracking and collision computations on GPUs instead of traditional CPUs. GPUs have numerous cores, and although the computational power of each core is relatively limited, their highly parallel multi-core structure makes them particularly well-suited for handling particle motion and collision calculations, thereby greatly improving computation speed.

综上所述，尽管离散元方法在计算效率和精度上存在显著瓶颈，但通过方法改进与硬件优化，这些问题可以在一定程度上得到缓解。在实际应用中，合理平衡精度与计算成本，并选择最适合的策略，仍是实现高效模拟的关键。

In summary, although the DEM faces significant bottlenecks in computational efficiency and accuracy, these issues can be alleviated to some extent through methodological improvements and hardware optimization. In practical applications, striking an appropriate balance between accuracy and computational cost, and selecting the most suitable strategy, remain critical to achieving efficient simulations.

## 9.2.2 双流体模型

## 9.2.2 Two-Fluid Model

颗粒在流化床中的运动具有独特的特性，这为分析其行为和建立模型提供了不同的视角。流态化是指颗粒或粉末在流体作用下能够像流体一样流动，并展现出某些流体的特性。因此，从理论上将流态化系统中的颗粒相视为流体是一种合理且有效的假设。基于这一假设，双流体模型（TFM）将颗粒相定义为一种连续相，并在欧拉框架下将其作为流体进行求解，为复杂流态化现象的描述提供了另一种途径。

The motion of particles in a fluidized bed exhibits unique characteristics, offering distinct perspectives for analyzing their behavior and developing models. Fluidization refers to the phenomenon in which particles or powders are able to flow like a fluid under the influence of a fluid, exhibiting certain fluid-like properties. Therefore, from a theoretical standpoint, treating the particle phase in a fluidized system as a fluid is a reasonable and effective assumption. Based on this assumption, the two-fluid model (TFM) defines the particle phase as a continuous phase and treats it as a fluid to be solved within the Eulerian framework, providing an alternative approach to describing complex fluidization phenomena.

从模型的角度来看，表面上似乎只需将描述流体的质量守恒方程和动量守恒方程复制一份用于颗粒相，便可完成颗粒流的建模。然而，实际情况远比想象中复杂。在将颗粒群体视为"流体"的过程中，存在诸多关键问题亟待解决。例如，如何在理论与建模层面准确描述颗粒群的流体特性（如黏度、压力等）。此外，流体与颗粒之间的复杂相互作用也是不可忽视的难点，例如曳力的准确处理。这些问题的解决不仅是双流体模型理论发展的核心，更直接决定了模型在实际工程中的应用价值与预测能力。

From a modeling perspective, it might seem that simply duplicating the mass conservation and momentum conservation equations used for fluids and applying them to the particle phase would suffice for modeling particle flow. However, the reality is far more complex. Treating a particle assembly as a "fluid" involves addressing numerous critical issues. For example, how can the "fluid-like" characteristics of the particle assembly, such as viscosity and pressure, be accurately described from both theoretical and modeling perspectives? Furthermore, the complex interactions between the fluid and particles, such as the accurate treatment of drag forces, also pose significant challenges. Addressing these issues is not only central to the theoretical development of the TFM but also directly determines the practical applicability and predictive accuracy of the model in engineering applications.

首先从质量守恒方程开始分析。在双流体模型中，描述质量守恒的连续性方程如下：

First, the analysis begin with the mass conservation equation. In the TFM, the continuity equation describing mass conservation is expressed as follows:

其中， 和 分别表示当前网格中的流体体积分数和颗粒体积分数，在流化床中通常称为空隙率和固含率。类似于单相的连续性方程，式（9-10）及（9-11）中的第一项描述了当前网格内流体质量随时间的变化，第二项表示由于流体进出网格所导致的质量变化。在双流体模型中，由于颗粒相被视为一种流体，因此两相的方程形式完全一致。

where and represent the fluid volume fraction and particle volume fraction in the current cell, respectively, commonly referred to as voidage and solids holdup in fluidized beds. Similar to the one-phase continuity equation, the first term describes the change in fluid mass within the cell over time, while the second term represents the mass changes caused by fluid entering and leaving the cell. In the TFM, since the particle phase is treated as a fluid, the equations for the two phases share the same form.

由于研究体系中存在两个流体相，方程中特别引入体积分数，以描述两相的空间分布并确保质量守恒。尽管连续性方程本身不需要额外的参数设定，但在实际求解过程中，由于多相流系统的复杂性，方程的数值收敛性常常成为一个难点。双流体模型的核心在于动量方程，其分别描述了流体相和颗粒相的运动。

Since the system being studied contains two fluid phases, volume fractions are specifically introduced into the equations to describe the spatial distribution of the two phases and to ensure mass conservation. Although the continuity equation themselves do not require additional parameter settings, achieving numerical convergence of the equations often becomes challenging due to the complexity of multiphase flow systems. The core of the TFM lies in the momentum equations, which describe the motion of the fluid phase and the particle phase, respectively.

流体相与颗粒相的动量方程分别表示为：

The momentum equations for the fluid phase and particle phase are expressed as follows:

动量方程的物理意义从左到右可以分为五个部分：瞬态项、对流项、扩散项（包括压力项和黏性项）、重力项以及相间交换项。前四部分与单相流体动量方程类似，只是专门引入了体积分数以适应双相的描述。由于模拟系统包含两个相，且两相间相互作用复杂，双流体模型特别引入了相间交换项，以表征流化床特有的流动结构。相间交换项由相间交换系数 和滑移速度 组成。滑移速度反映了两相间的相对运动速度，其大小直接决定了两相的相互作用强度。显然，滑移速度越大，两相的动量交换越强。这一部分内容将在后续讨论流体与颗粒相互作用时详细展开。

The physical significance of the momentum equation can be divided into five components from left to right: the transient term, convection term, diffusion term (including pressure and viscous terms), gravity term, and interphase exchange term. The first four components are similar to those in single-phase fluid momentum equations, but volume fractions are specifically introduced to account for the two-phase description. Since the simulated system includes two phases with complex interactions, the TFM introduces the interphase exchange term to represent the unique flow structures in fluidized beds. The interphase exchange term consists of the interphase exchange coefficient and the slip velocity . The slip velocity reflects the relative motion between the two phases, and its magnitude directly determines the strength of the interaction between them. Evidently, the larger the slip velocity, the stronger the momentum exchange between the phases. This topic will be discussed in detail in the subsequent section on fluid-particle interactions.

在双流体模型中，颗粒相被视为流体，因此其动量方程的形式与流体相保持一致。正如前文提到的，在流态化过程中，颗粒的行为与流体相似，展现出许多流体的典型特性，这为将颗粒视为"流体"提供了理论基础。然而，尽管颗粒在某些方面类似于流体，它们本质上并非流体，尤其是在流动过程中，颗粒缺乏一些典型的流体性质，例如连续的压力场和黏度特性。

In the TFM, the particle phase is treated as a fluid, and thus its momentum equation has the same form as that of the fluid phase. As previously mentioned, during fluidization, the behavior of particles resembles that of a fluid, exhibiting many typical fluid characteristics, providing a theoretical basis for treating particles as a "fluid". However, despite these similarities, particles are not inherently fluids. In particular during flow processes where they lack certain typical fluid properties, such as a continuous pressure field and viscosity characteristics.

因此，要继续使用动量守恒方程对颗粒相进行模拟，就必须针对这些差异构建适当的理论和模型，以补充和封闭颗粒相的特性描述。这些模型需要充分考虑颗粒的离散性及其相互作用，既要保留颗粒流动的流体特征，又要准确捕捉颗粒间和两相间的复杂动力学行为。

Therefore, to continue using the momentum conservation equation to model the particle phase, it is necessary to develop appropriate theories and models to address these differences and provide a complete description of the particle phase properties. These models must fully account for the discreteness of particles and their interactions, while preserving the fluid-like characteristics of particle flow and accurately capturing the complex dynamics between particles and between the two phases.

### 颗粒动理学理论

### Kinetic Theory of Granular Flow

颗粒动理学理论（KTGF）是双流体模型中描述颗粒相的核心理论基础，也是实现这一模型的关键。本节将对该理论进行简要介绍，以帮助读者理解颗粒相如何被有效地描述为一种"流体"。

The kinetic theory of granular flow (KTGF) serves as the core theoretical foundation for describing the particle phase in the TFM and is also essential to its implementation. This section will provide a brief introduction to KTGF to help readers understand how the particle phase can be effectively described as a "fluid".

在欧拉框架下，流体的行为通过描述固定空间位置的流体微元内部动量的变化及其与相邻微元之间的动量传递来刻画。而在颗粒相的描述中，控制方程关注的是微元内大量颗粒的整体行为，而非像拉格朗日框架那样逐一追踪每个颗粒的运动轨迹。这种整体描述带来的一个主要挑战是如何有效地定义颗粒相的压力和黏度。

In the Eulerian framework, fluid behavior is characterized by describing the changes in momentum within a fluid element at a fixed spatial location and the momentum transfer between adjacent elements. In contrast, the description of the particle phase focuses on the collective behavior of a large number of particles within a fluid element, rather than individually tracking the motion of each particle as in the Lagrangian framework. A primary challenge of this collective description is how to effectively define the pressure and viscosity of the particle phase.

自二十世纪五十年代以来，研究者们尝试借鉴分子运动论，用微观粒子（原子和分子）的运动特性来推导宏观颗粒流的性质，从而形成了颗粒动理学理论。经过数十年的发展，该理论逐步完善。特别是在1994年，Gidaspow在其著作《Multiphase Flow and Fluidization: Continuum and Kinetic Theory Descriptions》中对颗粒动理学理论进行了系统总结，并推动其在工程实践中的应用，使其能够更精确地定量描述颗粒流动行为，并实现与CFD的耦合计算。

Since the 1950s, researchers have attempted to draw on the kinetic theory of gases, using the motion characteristics of microscopic particles (atoms and molecules) to derive the macroscopic properties of granular flows, thereby establishing the KTGF. Over several decades, this theory has been gradually refined. In particular, in 1994, when Gidaspow provided a systematic summary of KTGF in his book "Multiphase Flow and Fluidization: Continuum and Kinetic Theory Descriptions", which further promoted its application in engineering practice, allowing particle flow behavior to be described more accurately and quantitatively and enabling its coupling with CFD calculations.

在分子运动论中，气体的宏观性质（如温度、压强、黏度等）可以通过微观分子的随机运动行为来解释。例如，气体是由大量做随机运动的分子组成，这些分子对单位面积平面的撞击力宏观上表现为压强。由于分子数量极大且撞击频率极高，压强在宏观尺度上表现得稳定。此外，在考虑两层平行流动的气体时，分子的随机运动会使动量从一层传递到另一层，从而产生摩擦力，这种现象反映了气体的黏性。这种动量的交换过程遵循牛顿黏性定律，并与动量方程中的动量扩散项（黏度项）相对应。气体的黏度实质上是分子热运动带来的近距离相互作用的结果。

In the kinetic theory of gases, the macroscopic properties of a gas (such as temperature, pressure, and viscosity) can be explained by the random motion of microscopic atoms/molecules. For example, a gas consists of a large number of randomly moving molecules, and the force exerted by these molecules on a surface of unit area manifests macroscopically as pressure. Because the number of molecules is extremely large and the collision frequency is very high, the pressure appears stable at the macroscopic scale. Moreover, when considering two parallel layers of gas flow, the random motion of molecules transfers momentum from one layer to the other, generating frictional forces. This phenomenon reflects the viscosity of the gas. This momentum exchange process follows Newton's law of viscosity and corresponds to the momentum diffusion term (viscous term) in the momentum equation. Fundamentally, the viscosity of a gas arises from short-range interactions due to molecular thermal motion.

分子运动论还指出，温度越高，分子热运动越剧烈，分子随机运动速度也越快。温度作为流体中分子随机运动强度的宏观度量，不仅影响流体的压力，还决定其黏度。类比这一理论，研究者发展出颗粒动理学理论，并引入"颗粒温度"这一拟物理量，作为衡量颗粒随机运动剧烈程度的指标。通过颗粒温度，可以进一步推导出颗粒相的压力、黏度以及动能变化的表达式，为颗粒相的宏观描述提供了重要依据。颗粒温度的定义与分子运动论中气体温度的定义类似：

The kinetic theory of gases also points out that the higher the temperature, the more intense the molecular thermal motion and the faster the random motion of molecules. Temperature, as a macroscopic measure of the intensity of random molecular motion in a fluid, affects not only the pressure of the fluid but also its viscosity. Drawing on this theory, researchers developed the KTGF and introduced the concept of "granular temperature" as a quasi-physical quantity to measure the intensity of random particle motion. Granular temperature serves as a key metric for deriving expressions for the pressure, viscosity, and kinetic energy variation of the particle phase, providing a critical basis for the macroscopic description of granular flows. The definition of granular temperature is similar to that of gas temperature in the Kinetic Theory of Gases:

式中， 表示颗粒相对于其平均速度的波动分量，用以反映颗粒的随机运动速度。颗粒温度可以通过求解颗粒温度输运方程获得。基于颗粒温度，可以直接计算颗粒相的压力和应力，从而封闭颗粒相的动量守恒方程。

where, represents the fluctuation component of particle velocity relative to its mean value, which reflects the random motion of particles. The granular temperature can be obtained by solving the granular-temperature transport equation. Based on the granular temperature, the pressure and stress of the particle phase can be directly calculated, thereby closing the momentum conservation equation for the particle phase.

连续性方程与动量方程共同构成了描述流体和颗粒流动的基本框架。在给定适当的初始条件和边界条件后，求解这两组方程便可得到计算域内流体相和颗粒相的流场。换句话说，通过流场的求解，可以获得任意时刻、任意位置处系统内的压力、流体和颗粒的速度向量以及局部的固含率。这一过程正是流态化模拟的核心目标------为深入研究颗粒流动特性及其在工业应用中的行为提供定量化的理论依据。

The continuity equation and momentum equation together form the fundamental framework for describing the flow of the fluid and particles. Given appropriate initial and boundary conditions, solving these two sets of equations yields the flow fields of the fluid phase and particle phase within the computational domain. In other words, by solving the flow field, one can obtain the pressure, the velocity vectors of the fluid and particles, and the local solids holdup at any given time and at any location within the system. This process represents the core objective of fluidization simulations --- namely, to provide quantitative theoretical foundations for in-depth investigations of particle flow characteristics and their behavior in industrial applications.

### 双流体模型的优势与挑战

### Advantages and Challenges of the Two-Fluid Model

正如前文所述，基于颗粒动理学理论的双流体模型无需像离散元方法那样追踪每个颗粒的行为，因此特别适用于模拟颗粒较小、数量较多、表现出宏观统计特征的流态化系统。然而，这一优势同时也引发了两个主要的建模困难。

As previously mentioned, the TFM based on the KTGF does not require tracking the behavior of every individual particle, as does the discrete element method, and is therefore particularly suitable for simulating fluidized systems with small particle in which the particles are small in size, large in number, and exhibit macroscopic statistical characteristics. However, this advantage also gives rise to two major modeling challenges.

首先，颗粒动理学理论通过统计力学推导并计算"颗粒团"的宏观性质，如压力、应力和黏度。然而，在推导过程中，颗粒通常被假设为光滑、刚性、球形，这与实际情况存在一定差距。此外，由于理论基于全局假设推导出的颗粒相性质，模型难以全面考虑颗粒粒径分布、颗粒形貌以及非接触力等因素的影响。

First, the KTGF uses statistical mechanics to derive and calculate the macroscopic properties of particle "clusters", such as pressure, stress, and viscosity. However, during the derivation process, particles are typically assumed to be smooth, rigid, and spherical, which deviates from actual conditions. Additionally, since the theory derives the particle-phase properties on the basis of global assumptions, the model struggles to comprehensively account for factors such as particle size distribution, particle morphology, and non-contact forces.

其次，为捕捉介观尺度的非均匀流动结构，计算时需选用足够小的网格尺寸。早期研究认为，网格尺寸为颗粒直径的10至50倍较为适宜，符合宏观统计特性。然而，近期研究表明，3至10倍颗粒直径的网格尺寸更能精确捕捉非均匀结构；过大的网格会增强局部均匀性，进而高估两相间的相互作用。尽管较小的网格提升了模拟精度，但在大型反应器的三维建模中，这也意味着网格数量显著增加，从而导致计算资源需求的急剧增长。

Second, to capture heterogeneous flow structures at the mesoscale, sufficiently small grid sizes must be selected during computation. Early studies suggested that grid sizes 10 to 50 times the particle diameter were appropriate, as they conformed to macroscopic statistical characteristics. However, recent research indicates that grid sizes 3 to 10 times the particle diameter can more accurately capture heterogeneous structures. Excessively large grids increase local uniformity, which may lead to an overestimation of the interactions between the two phases. Although smaller grids improve simulation accuracy, **t**hey also imply a significant increase in the number of grid cells in the three-dimensional modeling of large reactors, resulting in a sharp increase in the demand for computational resources.

这两点会在很大程度上影响双流体模型的模拟结果，因此建模和计算时需要特别关注并加以考虑。同时，它们也会极大地限制双流体模型的进一步发展和实际应用。

These two factors can significantly affect the simulation results of the TFM, and thus require careful attention and consideration during modeling and computation. At the same time, they also greatly inhibit the further development and practical application of the TFM.

# 9.3 流体与颗粒间的相互作用和耦合方式

# 9.3 Interactions and Coupling Mechanisms between Fluid and Particles

## 9.3.1 相互作用

## 9.3.1 Interactions

前文介绍了颗粒动理学模型和离散元模型在颗粒相处理中的应用，并提及了流体-颗粒体系中气体与颗粒的相互作用。接下来，本节将简要概述流体与颗粒之间的相互作用及其耦合方式。

The previous sections introduced the application of the KTGF and the DEM in the treatment of the particle phase, as well as discussing the interactions between the fluid and particles in fluid-particle systems. This section will briefly outline the interactions between fluid and particles and their coupling mechanisms.

当流体为气体时，颗粒与流体相互作用中占主导地位的是曳力。曳力主要由流体黏性在颗粒表面产生的剪切力构成，其大小受到颗粒形状、尺寸以及流体与颗粒之间相对速度的影响。曳力的方向始终与颗粒相对于流体的运动方向相反。

When the fluid is a gas, the dominant interaction force between particles and the fluid is the drag force. Drag force is primarily composed of the shear force generated by fluid viscosity on the particle surface. Its magnitude is influenced by particle shape, size, and the relative velocity between the fluid and the particles. The direction of the drag force always opposes the direction of particle motion relative to the particles.

此外，当流化床密度较高且整体压力梯度较大时，压力梯度力的作用也尤为重要。在流场不均匀的情况下，颗粒周围流体施加在颗粒表面的压力会存在差异，从而导致压力合力不为零。在流化床中，压力梯度力是驱动颗粒运动和实现颗粒悬浮的重要作用力之一。

Additionally, when the fluidized bed features high density levels and a significant overall pressure gradient, the pressure gradient force becomes particularly important. In an non-uniform flow field, the fluid pressure exerted on the particle surface differs around the particle, resulting in a net pressure force. In fluidized beds, the pressure gradient force is one of the key forces driving particle motion and enabling particle suspension.

当流体为液体时，浮力在颗粒与流体的相互作用中也占有重要地位。浮力的大小主要取决于被排开流体的质量。由于气体的密度通常比颗粒小上千倍，因此在气体与颗粒的体系中，浮力通常可以忽略不计；然而，液体的密度与颗粒接近，在液体与颗粒的体系中，浮力的影响则不可忽视。

When the fluid is a liquid, buoyancy also plays a significant role in the interaction between particles and the fluid. The magnitude of buoyancy primarily depends on the mass of the displaced fluid. Since the density of a gas is typically thousands of times lower than that of particles, buoyancy can usually be neglected in gas-particle systems. However, because the density of a liquid is close to that of the particles, the influence of buoyancy in liquid-particle systems cannot be ignored.

除了曳力、压力梯度力和浮力之外，附加质量力、升力、电磁力以及布朗运动力等相互作用力在特定情境下也可能发挥重要作用，显著影响颗粒与流体的相互作用行为。

In addition to drag force, pressure gradient force, and buoyancy, other interaction forces such as the virtual mass force, lift force, electromagnetic force, and Brownian force may also play important roles under specific conditions, thereby significantly influencing the interaction behavior between particles and the fluid.

## 9.3.2 耦合方式

## 9.3.2 Coupling Methods

在计算中，如果考虑所有可能的相互作用，将浪费大量计算资源。因此，通常根据实际情况保留对系统影响最大的相互作用，而忽略那些影响微乎其微的部分。图9-7展示了不同耦合方式的示意图。

In computations, if all possible interactions are taken into account, a large amount of computational resources will be wasted. Therefore, only the interactions that have the greatest impact on the system are typically retained according to practical conditions, while those with negligible effects are ignored. Figure 9-7 illustrates the different coupling mechanisms.

当颗粒量极少时，颗粒对流体流场的影响可以忽略，此时仅需考虑流体对颗粒的作用，这种耦合方式称为单向耦合。随着颗粒量逐渐增加，其对流场的影响变得显著，不得不加以考虑，此时采用双向耦合。进一步增加颗粒量时，颗粒间的碰撞不可忽视，此时需要同时考虑流体与颗粒之间的相互作用以及颗粒与颗粒之间的相互作用，这种方式被称为四向耦合。

When the particle concentration is very low, their influence on the fluid flow field can be ignored, and only the effect of the fluid on the particles needs to be considered. This coupling method is called one-way coupling. As the number of particles increases, their impact on the flow field becomes significant and must be taken into account. in this case, two-way coupling is adopted. With a further increase in particle quantity, collisions between particles can no longer be ignored. At this stage, both the interactions between the fluid and particles and those between particles themselves must be considered. This method is called four-way coupling.

在流化床反应器，尤其是气固流态化过程中，固含率通常大于0.01。因此，在这种情况下，必须采用四向耦合进行建模计算（见图9-7）。

In fluidized bed reactors, especially during gas-solid fluidization processes, the solids holdup is typically greater than 0.01. Therefore, in such cases, four-way coupling must be used for modeling and computation (refer to Figure 9-7).

通过四向耦合，将计算流体力学与离散元方法相结合的耦合模型（CFD-DEM）能够有效模拟流体和颗粒的两相流动。在该模型中，固体颗粒的运动采用拉格朗日框架进行追踪，而气体流动则在固定的欧拉网格中求解。气体与颗粒之间的相互作用通过动量交换描述，颗粒之间的相互作用则通过碰撞模型以及其他接触力和非接触力模型进行模拟，从而全面捕捉两相流中的复杂行为。

Through four-way coupling, the coupled method combining CFD with the DEM method, known as CFD-DEM, can effectively simulate the two-phase flow of fluids and particles. In this method, the motion of solid particles is tracked using a Lagrangian framework, while the gas flow is solved on a fixed Eulerian grid. The interactions between the gas and particles are described through momentum exchange, while particle interactions are simulated using collision models as well as other contact and non-contact force models, thereby comprehensively capturing the complex behavior of two-phase flows.

在流体与颗粒相互作用的实际计算中，由于气体的控制体积（即网格）的尺寸通常大于单个颗粒------一个控制体积内往往包含多个颗粒，因此曳力、浮力等相互作用力通常通过加权平均的方法进行近似计算。以曳力为例，其计算依赖于封闭模型。曳力封闭模型的建立基于实验数据或高精度数值模拟，用于描述曳力系数与局部固含率、流体与颗粒间的滑移速度等参数之间的关系。

In the practical calculation of fluid-particle interactions, the size of the gas control volume (i.e., the grid) is typically larger than that of a single particle, with one control volume often containing multiple particles. As a result, interaction forces such as drag and buoyancy are generally approximated using a weighted averaging method. Taking drag force as an example, its calculation relies on a drag closure model. The drag closure model is established based on experimental data or high-fidelity numerical simulations and is used to describe the relationship between the drag coefficient and parameters such as local solids holdup and the slip velocity between the fluid and particles.

因此，通过控制体积内的平均固含率和平均滑移速度，可以计算该控制体积内的平均曳力系数，从而求得流体相与颗粒相之间的由于平均曳力引起的动量交换。这种方法在保证计算效率的同时，能够有效捕捉流体与颗粒相互作用的主要特性。

Therefore, by using the average solids holdup and average slip velocity within the control volume, the average drag coefficient for that control volume can be calculated, thereby determining the momentum exchange between the fluid phase and the particle phase caused by the average drag force. This approach can effectively capture the main characteristics of fluid-particle interactions while ensuring computational efficiency.

双流体模型自构建之初便基于四向耦合原理------颗粒间的相互作用通过颗粒动理学方法描述，流体与颗粒间的相互作用则通过动量交换实现。与CFD-DEM方法不同，双流体模型中流体和颗粒均在欧拉网格中求解，并在同一控制体积（网格）内进行计算。由于在双流体模型中流体相和颗粒相都被视为连续介质，因此曳力也以体积平均的形式在控制体积内求解，并同样依赖于封闭模型的描述。

From its inception, the TFM has been based on the principle of four-way coupling---particle-particle interactions are described using the KTGF, while fluid-particle interactions are captured through momentum exchange. Unlike the CFD-DEM method, in the TFM, both the fluid and particle phases are solved on Eulerian grids and computed within the same control volume (grid). Since both the fluid and particle phases are treated as continuous media in the TFM, drag force is also computed in a volume-averaged form within the control volume and relies on closure models for its description.

从上述描述可以看出，无论是双流体模型还是CFD-DEM模型，流体与颗粒间相互作用的计算都依赖于封闭模型。因此，封闭模型与体系的适配程度对数值模拟结果的准确性具有重要影响。此外，控制体积的选择对模拟结果也有显著影响。由于封闭模型计算所采用的参数是控制体积内的平均值，所得的相间相互作用参数同样以平均值形式表示。因此，若控制体积过大，系统将难以准确捕捉非均匀的介观尺度结构；而若控制体积过小，则可能导致封闭模型计算的结果不准确，因为封闭模型的构建通常未考虑控制体积接近或小于单个颗粒尺寸的情况。

From the above description, it is evident that the calculation of fluid-particle interactions in both the TFM and the CFD-DEM model relies on closure models. Therefore, the degree of compatibility between the closure model and the system plays a critical role in the accuracy of numerical simulation results. A detailed summary of different closure models can be found in reference. Furthermore, the selection of the control volume has a significant impact on simulation results. Since the parameters used in closure models are derived as averaged values within the control volume, the resulting interphase interaction parameters are also represented in an averaged form. If the control volume is too large, the system will have difficulty accurately capturing non-uniform meso-scale structures, leading to a loss of critical flow details. Conversely, if the control volume is too small, the accuracy of closure model calculations may be compromised, as most closure models are generally constructed without considering cases in which the control volume approaches or is smaller than the size of an individual particle.

# 9.4 不同尺度下的多相流模型及其特点

# 9.4 Multiphase Flow Models at Different Scales

本章前文重点介绍了两种可用于模拟流态化系统的方法：双流体方法和计算流体力学-离散元方法。这两种方法均需要在欧拉框架下求解其流体相的流场，并依赖封闭模型的支持。然而，在上一节的讨论中提到，由于封闭模型的限制，这两种方法在模拟少量颗粒的微观场景或工业设备的宏观场景时面临一定挑战。但对于捕捉介观尺度的非均匀流动结构而言，这两种方法表现出极大的优势（见图9-8）。

The previous sections of this chapter focused on two methods that can be used to simulate fluidized systems: the TFM and the CFD-DEM method. Both methods require solving the fluid-phase flow field within an Eulerian framework and rely on closure models. However, as discussed in the previous section, due to the limitations of closure models, these methods face certain challenges when simulating micro-scale scenarios involving a small number of particles or macro-scale industrial equipment. Nevertheless, they exhibit significant advantages in capturing heterogeneous flow structures at the meso-scale (see Figure 9-8).

## 9.4.1 微观尺度模型

## 9.4.1 Micro-Scale Model

当缩小控制体积的尺寸至远小于单个颗粒时（小于1/10 ），可以采用直接数值模拟（DNS）结合沉浸边界法（IBM），直接解析流场中的湍流以及颗粒表面的流场与相互作用。也可利用格子玻尔兹曼方法（LBM），基于流体的统计物理特性，模拟其宏观行为。对于颗粒相，可以将颗粒轮廓直接作为计算域的边界，或采用离散元方法（DEM）进行处理。

When the size of the control volume is reduced to far below that of a single particle (less than 1/10 ), direct numerical simulation (DNS) combined with the immersed boundary method (IBM) can be used to directly resolve the turbulence in the flow field, as well as the flow around particle surfaces and their interactions. The lattice Boltzmann method (LBM) can also be utilized to simulate the behavior of the fluid based on its statistical physical properties. For the particle phase, the particle contours can be directly treated as the boundary of the computational domain or resolved using the DEM.

在这套方法框架下，所有的流动与相互作用均通过数值方法精确解析，无需进行平均处理，也不依赖任何经验公式进行封闭。然而，由于计算量极为庞大，这类方法通常仅适用于模拟极小区域及少量颗粒（数量从几个到十几个）。这种微观尺度的模拟非常适合研究颗粒-流体间的相互作用机理及传递过程，从而为开发微观尺度的封闭模型提供基础。例如，Hill和Koch使用LBM模拟了流体穿过球体阵列时，流速与空隙率等因素对流动的影响，并基于此开发了可以用于TFM和CFD-DEM 模拟方法的曳力封闭模型。

Within this methodological framework, all flow phenomena and interactions are accurately resolved using numerical methods, without the need for averaging or relying on empirical closure formulas. However, due to the immense computational demands, such methods are typically limited to simulating very small regions and a small number of particles (ranging from a few to a dozen). These micro-scale simulations are particularly suitable for studying the mechanisms and transfer processes of particle-fluid interactions, providing a foundation for developing micro-scale closure models. For example, Hill and Koch used the LBM to simulate the effects of factors such as flow velocity and voidage on fluid flow through arrays of spheres. Based on this, they developed a drag force closure model applicable to both the TFM and CFD-DEM simulation methods.

## 9.4.2 宏观尺度模型

## 9.4.2 Macro-Scale Model

前文提到，由于TFM和CFD-DEM方法在宏观尺度的工业反应器模拟中难以达到较高的准确性，研究者们针对这一问题展开了深入研究。

As mentioned earlier, because the TFM and CFD-DEM methods have difficulty achieving high accuracy in the simulation of industrial reactors at the macroscopic scale, researchers have carried out extensive studies on this issue.

当采用TFM方法时，为了适应大尺寸的流化床反应器，会采用尺寸过大的控制体积，而过大的控制体积让计算出的流场变得均匀，无法准确捕捉非均匀结构。针对此，研究者们开发了一系列的亚网格模型来补足缺陷。建立亚网格模型的方法通常有半经验方法、能量最小化多尺度方法（EMMS）和滤波方法。亚网格模型能够预测出大尺寸控制体中可能出现的介观尺度非均匀结构，从而给出较为准确的相间相互作用以及传递相关的参数。

When using the TFM method, overly large control volumes are often employed to accommodate large-scale fluidized bed reactors. However, such excessively large control volumes make the calculated flow field overly uniform and unable to accurately capture heterogeneous structures. To address this issue, researchers have developed a series of sub-grid models to compensate for these limitations. Methods for constructing sub-grid models typically include semi-empirical approaches, the energy minimization multi-scale (EMMS) method, and the filtered methods. Sub-grid models can predict meso-scale heterogeneous structures that may arise within large control volumes, providing more accurate parameters for interphase interactions and transport processes.

而采用CFD-DEM方法模拟工业尺寸的流化床反应器时，同时追踪极大量的颗粒是不现实的。研究者们建立了粗粒化（CGP）方法，其通过创建代表多个实际颗粒的"颗粒包"来显著减少模拟中需要追踪的实际数量。这种方法需要重新定义颗粒间的相互作用模型，如碰撞和摩擦，并对其准确性进行验证。

When using the CFD-DEM method to simulate industrial-scale fluidized bed reactors, it is impractical to track an extremely large number of particles simultaneously. To address this, researchers have developed the coarse-graining particle (CGP) method, which significantly reduces the number of particles that need to be tracked in the simulation by creating "particle parcels" that represent multiple actual particles. This approach requires redefining the interaction models between particles, such as collision and friction, and validating their accuracy.

同样采用颗粒包思想的多相颗粒团方法（MP-PIC）结合了欧拉和拉格朗日两种描述框架，用于模拟颗粒相的运动。在该方法中，采用拉格朗日框架来追踪代表颗粒团的运动，同时利用欧拉框架通过平均化的封闭方程来描述颗粒间的相互作用，例如碰撞等。与MP-PIC方法类似的还有稠密离散粒子模型（DDPM），该模型同样采用拉格朗日框架追踪颗粒团，其颗粒团间的相互作用通过基于颗粒动力学理论的相关模型进行计算。

The multiphase particle-in-cell (MP-PIC) method, which likewise adopts the particle parcel concept, combines both Eulerian and Lagrangian frameworks to simulate the motion of the particle phase. In this method, a Lagrangian framework is used to track the motion of parcels representing groups of particles, while a Eulerian framework is employed to describe particle interactions, such as collisions, using averaged closure equations. A similar approach to the MP-PIC is the dense discrete particle model (DDPM), which also uses the Lagrangian framework to track particle parcels, with inter-parcel interactions are calculated through models based on the granular dynamics theory.

通过以上对TFM和CFD-DEM方法的改进，让数值模拟大型实验室尺寸、中试尺寸乃至工业尺寸的流化床反应器成为可能。

These improvements to the TFM and CFD-DEM methods have made it possible to numerically simulate fluidized bed reactors at large laboratory, pilot, and even industrial scales.

# 9.5 模拟实例

# 9.5 Simulation Example

## 9.5.1 二维鼓泡流化床反应器

## 9.5.1 Two-Dimensional Bubbling Fluidized Bed Reactor

该案例展示了利用双流体模型对鼓泡流化床的流场和反应场进行的模拟。图9-9（a）展示了模拟对象------鼓泡流化床装置------的示意图。反应器主体为一个3米高、内径152毫米的圆柱体。气体的主体为空气，从床底通过气体分布器进入床体，并从顶部排出。

This case demonstrates the simulation of the flow field and reaction field in a bubbling fluidized bed using the TFM. Figure 9-9(a) shows a schematic diagram of the simulated system---the bubbling fluidized bed reactor. The reactor body consists of a cylindrical column with a height of 3m and an inner diameter of 152mm. Air serves as the primary gas, entering the bed through a gas distributor at the bottom and exiting from the top.

本实例仅简要展示数值模拟后的流场与反应场的直接结果。在实际研究或工程应用中，应针对具体问题进行深入分析，根据需求和目标精心设计案例，并开展针对性的数据处理与分析，以最终获取所需的结论。

This example only briefly presents the direct results of numerical simulation for the flow and reaction fields. In actual research or engineering applications, in-depth analysis should be carried out for specific problems. Cases should be carefully designed according to relevant requirements and objectives, and targeted data processing and analysis should be conducted in order to obtain the desired conclusions.
