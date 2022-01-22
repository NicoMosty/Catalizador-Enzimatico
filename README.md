<h1 align="center">Taller 5</h1>
<p align="center">Nicolas Puentes Urrego</p>
<p align="center">Ingenieria Enzimática</p>

---

<h3 align="center">Transferencia simultánea de masa & reacción bioquímica en el soporte esférico</h1>
A continuación se muestra la ecuación diferencial que representa la transferencia simultanea de masa y reacción química dentro del biocatalizador enzimático, donde:

<div align="center"><img style="background: white;" src="svg\BmqQnjNriH.svg"></div>

Para el caso del radio inicial 
<span align="center"><img style="background: white;" src="svg\df5Zwv1KvJ.svg"></span>

<div align="center"><img style="background: white;" src="svg\a3OeoYVWBx.svg"></div>

Para poder hallar la distribución se utiliza la siguiente distribución con tablas, donde: 
<div align="center"><img style="background: white;" src="svg\Screenshot_1.png"></div>

Se puede ver en la tabla que se supone un valor de <span align="center"><img style="background: white;" src="svg\qll8hwB79R.svg"></span> (naranja)y se modifica hasta que el valor en <span align="center"><img style="background: white;" src="svg\24HlDziO7A.svg"></span> sea igual a 1.

Para hacer lo anterior se definen los siguientes invervalos de <span align="center"><img style="background: white;" src="svg\NG6Wf3CbzN.svg"></span> , donde:

<div align="center"><img style="background: white;" src="svg\pRHcd00R4e.svg"></div>

<div align="center"><img style="background: white;" src="svg\ZPrwbSIlio.svg"></div>

Para poder realizar el calculo se definió un <span align="center"><img style="background: white;" src="svg\WrAgk89JJb.svg"></span>

Para calcular lo anterior se realizó un algoritmo en *Python*. El código se
encuentra en el siguiente link:

[Programa en Python (Concentración Sustrato vs Radio)](SvsR.py)

Los resultados se muestran a continuación:

<div align="center"><img style="background: white;" src="Images/Beta-10.0.png"></div>
<div align="center"><img style="background: white;" src="Images/Beta-5.0.png"></div>
<div align="center"><img style="background: white;" src="Images/Beta-1.0.png"></div>
<div align="center"><img style="background: white;" src="Images/Beta-0.5.png"></div>
<div align="center"><img style="background: white;" src="Images/Beta-0.1.png"></div>
<div align="center"><img style="background: white;" src="Images/Beta-0.05.png"></div>
<div align="center"><img style="background: white;" src="Images/Beta-0.01.png"></div>
